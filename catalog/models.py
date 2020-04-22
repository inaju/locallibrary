from django.db import models
from django.urls import reverse
from uuid import uuid4
from django.contrib.auth.models import User
# Create your models here.


class Genre(models.Model):
    #This is the name of the genre
    name=models.CharField(max_length=200, help_text='Enter a book Genre (eg science fiction)')
    
    def __str__(self):
        #this shows the name of the genre
        return self.name



class BookLanguages(models.Model):
    booklanguage = models.CharField(
        max_length=200,
        blank=True,
        choices=(
            ('English', 'English'),
            ('French', 'French'),
            ('Yoruba', 'Yoruba'),
        )
    )

    def __str__(self):
        return self.booklanguage

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        #it lists the authors from the last name with highest priority
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):

        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Book(models.Model):
    #things we want assiociated with the book
    
    title=models.CharField(max_length=200)
    
    #authors can have many books ie many to one
    author=models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    summary=models.TextField(max_length=1000, help_text='13 character')
    
    #many books can have many genres
    genre=models.ManyToManyField(Genre, help_text='Select a genre for this book')
    
    #one language can be assiociated to one book
    language_book = models.ForeignKey(BookLanguages, on_delete=models.SET_NULL, null=True)
    #`pages=models.ForeignKey(PagesBook, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
    
    #This gives us the url of this model
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def AuthorName(self):
        return self.author
    

    
    def genre_display(self):
        TheNames=[]
        
        for genre in self.genre.all():
            TheNames.append(genre)
            
        print(TheNames)
        return TheNames
    genre_display.short_description = 'Genre'

    


     
    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, help_text='Unique ID for this particular book across whole library')
    book=models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True, blank=True)
    
    LOAN_STATUS=(
        ('m','Maintenance'),
        ('o','On Loan'),
        ('a', 'Available'),
        ('r','Reserved'),
    )
    
    status=models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book Availability'
    )
    
    class Meta:
        ordering=['due_back']
    
    def __str__(self):
        return f'{self.id} ({self.book.title})'
    

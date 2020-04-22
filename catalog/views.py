from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from catalog.models import Book, Author, BookInstance, Genre, BookLanguages
from django.views import generic


from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def index(request):
    
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits']=num_visits+1
    
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()
    
    context={
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors,
        'num_visits':num_visits,
    }
    
    return render(request, 'index.html', context=context)


def mitchel(request):
    NoOfLanguagesUsed = BookLanguages.objects.all().count()
    ListOfLanguages = BookLanguages.objects.all()
    NoOFAuthors=Author.objects.all().count()
    ListOfAuthors=Author.objects.all()
    
    visits=request.session.get('visits', 0)
    request.session['visits']=visits+1
    
    context={
        'NoOfLanguagesUsed': NoOfLanguagesUsed,
        'ListOfLanguages': ListOfLanguages,
        'NoOFAuthors': NoOFAuthors,
        'ListOfAuthors': ListOfAuthors,
        'visits':visits
    }
    
    return render(request, 'mitchel.html', context=context)



class BookListView(generic.ListView):
    model=Book
    paginate_by=2 
    
    
class BookDetailView(generic.DetailView):
    model=Book

def book_detail_view(request, primary_key):
    book=get_object_or_404(Book, pk=primary_key)
    
    return render (request, 'book_detail.html', context={'book':book})

class AuthorListView(generic.ListView):
    model=Author
    
class AuthorDetailView(generic.DetailView):
    model=Author
    
    
    
    
def home(request):
    return render(request, 'index_new.html')


def sendemail(request):

    send_mail(
        'subject',
        'Email Message',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )

    return HttpResponse('mail sent succesfully')

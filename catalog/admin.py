from django.contrib import admin
from .models import BookLanguages, Genre, Book, Author, BookInstance


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields=('first_name', 'last_name',('date_of_birth','date_of_death'))

class BooksInstanceInline(admin.TabularInline):
    model=BookInstance
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre_display', 'language_book')
    inlines=[BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets=(
        ('Important',{
            'fields':('book','imprint','id')
        }),
        ('Availability',{
            'fields':('status','due_back')
        }),
    )
    

admin.site.register(BookLanguages)
admin.site.register(Genre)

#admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
#admin.site.register(BookInstance)

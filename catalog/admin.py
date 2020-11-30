from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Customize the Author ModelAdmin class
class AuthorAdmin(admin.ModelAdmin):
    # list_display shows additional information about the model on the list view
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

# Customize the Book ModelAdmin class
class BookAdmin(admin.ModelAdmin):
    # The author is a ForeignKey field (one-to-many) relationship, 
    # and so will be represented by the __str__() value for the associated record. 
    # Also we can't directly display the genre here because it is a many-to-many field,
    # so we can just define a function called display_genre in the model
    list_display = ('title', 'author', 'display_genre')

# Customize the BookInstance ModelAdmin class
class BookInstanceAdmin(admin.ModelAdmin):
    pass

# Register your models here.
# admin.site.register(Book)
admin.site.register(Book, BookAdmin)
# admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Language)
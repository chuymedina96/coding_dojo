from django.db import models
    

class User(models.Model):
    firstName   = models.CharField(max_length=255)
    lastName    = models.CharField(max_length=255)
    email       = models.CharField(max_length=255)
    description = models.CharField(max_length=255) # this was added later after existing data, which requires to migrate and to specify a default for data that was created before field was added to table.
    age         = models.IntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"User: First: {self.firstName}, Last:{self.lastName}, Email:{self.email}, Age:{self.age}, {self.description} ID: {self.id}"


class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Author: {self.name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Book: {self.title}, Author: {self.author.name}"


# References

# this_author = Author.objects.get(id=2)	# get an instance of an Author
# my_book = Book.objects.create(title="Little Women", author=this_author)	# set the retrieved author as the author of a new book
    
# # or in one line...
# my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))
# some_book.title		# returns a string that is the title of the book
# some_book.author	# returns the Author instance associated with this book

# Just as we are able to filter by other fields, we can also search based off of a ForeignKey relationship. This code will find all of the books by the author with ID 2:

# this_author = Author.objects.get(id=2)
# books = Book.objects.filter(author=this_author)
    
# # one-line version:
# books = Book.objects.filter(author=Author.objects.get(id=2))




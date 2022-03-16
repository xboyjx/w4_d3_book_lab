import pdb
from models.author import Author
from models.book import Book

from repositories import author_repository
from repositories import book_repository

author_repository.delete_all()
book_repository.delete_all()

author1 = Author("John")
author_repository.save(author1)
author2 = Author("Doe")
author_repository.save(author2)

author_repository.select_all()

book1 = Book("book", author1)
book_repository.save(book1)
book2 = Book("harry potter", author2)
book_repository.save(book2)


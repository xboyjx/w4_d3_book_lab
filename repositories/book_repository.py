from db.run_sql import run_sql

from repositories import author_repository
from models.author import Author
from models.book import Book

def save(book):
    sql = "INSERT INTO books (title, author_id) VALUES (%s, %s) RETURNING *"
    values = [book.title, book.author.id]
    result = run_sql(sql, values)
    id = result[0]['id']
    book.id = id
    return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    result = run_sql(sql)

    for row in result:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['id'])
        books.append(book)

    return books

def select(id):
    book = None

    sql = "SELECT * FROM books WHERE id =%s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], author, result['id'])
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

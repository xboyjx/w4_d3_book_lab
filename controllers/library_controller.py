from flask import Flask, render_template, redirect, request, Blueprint
from repositories import author_repository, book_repository
from models.book import Book

library_blueprint = Blueprint("books", __name__)

@library_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books = books)

@library_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')

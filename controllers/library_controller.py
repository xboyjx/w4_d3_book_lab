from flask import Flask, render_template, redirect, request, Blueprint
from repositories import author_repository, book_repository
from models.book import Book

library_blueprint = Blueprint("books", __name__)


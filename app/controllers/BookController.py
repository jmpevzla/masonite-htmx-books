from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.response import Response
from app.models.Book import Book

class BookController(Controller):
    def index(self, view: View):
        books = Book.all()
        return view.render("index.html", { "books": books })

    def store(self, request: Request, view: View):
        book = Book.create(
          title=request.input('title'),
          author=request.input('author'),
          price=request.input('price'),
          description=request.input('description'),
        )
        
        return view.render("components/tr-book.html", { "book": book })

    def editForm(self, request: Request, view: View):
        book = Book.find(request.param('id'))
        return view.render("components/tr-form.html", { "book": book })

    def row(self, request: Request, view: View):
        book = Book.find(request.param('id'))
        return view.render("components/tr-book.html", { "book": book })

    def update(self, request: Request, view: View):
        book = Book.find(request.param('id'))
        book.title = request.input('title')
        
        book.save()
        return view.render("components/tr-book.html", { "book": book })

    def destroy(self, request: Request, view: View):
        book = Book.find(request.param('id'))
        book.delete()
        return ""

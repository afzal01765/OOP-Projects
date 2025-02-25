class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title {self.title} Author :{self.author} , ISBN {self.isbn}"

class Libary:

    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter your book title:")
        author =input("Enter your book author:")
        isbn  =input("Enter your book isbn number")
        book = Book(title , author , isbn)
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("Libary is empty")
        else:
            for value in self.books:
                print(f"Book tile is {value.title}  book author is {value.author}  isbn number is{value.isbn}")
    def display_with_isbn_number(self,isbn):
         for value in self.books:
             if value.isbn == isbn:
                 print(f"Book tile is{value.title} book author {value.author}  isbn number is {value.isbn}")

    def clear_libary(self):
        self.books.clear()


    def remove_book(self,isbn):
        for value in self.books:
            if value.isbn == isbn:
                self.books.remove(value)
                break
        else:
            print("This book is not found")

    def search_book(self,isbn):
        for value in self.books:
            if value.isbn == isbn:
                return value

        else:
            return "this book is not found"


if __name__ =="__main__":

    ll = Libary()

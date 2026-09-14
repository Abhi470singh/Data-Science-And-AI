import json
import os

from book import Book

class Library:
    
    def __init__(self):
        self.books = []
        self.filename = "books.json"
        self.load_books()
        
# ---------------------
# Load Books
# ---------------------
    def load_books(self):
    
        if os.path.exists(self.filename):
        
            with open(self.filename, "r") as file:
                data = json.load(file)
            
            self.books = [
                Book.from_dict(book)
                for book in data
            ]
        
# ---------------------
# Save Books
# ---------------------
    def save_books(self):
    
        with open(self.filename, "w") as file:
        
            json.dump(
                [book.to_dict() for book in self.books],
                file,
                indent=4
            )
        
# ---------------------
# Add Book
# ---------------------
    def add_book(self):
    
        book_id = input("Enter BOOK id :")
        title = input("Enter Book title : ")
        author = input("Enter Book author : ")
    
        for book in self.books:
        
            if book.book_id == book_id:
                print("Book ID already exists.")
                return
    
        new_book = Book(book_id, title,author)
    
        self.books.append(new_book)
        
        self.save_books()
    
        print("Book Added Successfully.")
    
    
# ---------------------
# view Books
# ---------------------
    def view_books(self):
    
        if len(self.books) == 0:
            print("No Books Available.")
            return
    
        print("\nBook List\n")
    
        for book in self.books:
        
            status = "Available"
        
            if not book.available:
                status = "Not Available"
            
            print(f"""
              Book ID : {book.book_id}
              Title : {book.title}
              Author : {book.author}
              Status : {status}
              ---------------------------
              """)
        
# ---------------------
# Search Book
# ---------------------
    def search_book(self):
    
        keyword = input("Enter Title : ").lower()
    
        found = False
    
        for book in self.books:
        
            if keyword in book.title.lower():
            
                status = "Available"
            
                if not book.available:
                    status = "Not Available"

                print(f"""
                  Book ID : {book.book_id}
                  Title   : {book.title}
                  Author  : {book.author}
                  Status  : {status}
                  """)
            
                found = True
   
   
            if not found:
                print("Book Not Found")
           
# ----------------------
# Issue Book
#-----------------------
    def issue_book(self):
    
        book_id = input(" Enter Book ID: ")
    
        for book in self.books:
        
            if book.book_id == book_id:
            
                if book.available:
                    book.available = False
                    self.save_books()
                
                    print(" Book Issued Successfully")
                
                else:
                    print("Book Already Issued")
                
                
                return
        print("Book Not Found")
    
# --------------------
# Return 
# --------------------
    def return_book(self):
    
        book_id = input("Enter Book ID :") 
    
        for book in self.books:
        
            if book.book_id == book_id:
            
                if not book.available:
                
                    book.available = True
                    self.save_books()
                
                    print("Book return Successfull")
                
                else:
                    print("Book Already available")
                
                return
    
        print("Book Not Found")
    
    
# -----------------------
# Delete Book 
#----------------------
    def delete_book(self):
    
        book_id = input("Book ID: ")
    
        for book in self.books:
        
            if book.book_id == book_id:
            
                self.books.remove(book)
            
                self.save_book()
            
                print("Book Deleted Successfully")
                return
        
        print("Book Not Found")
            
            
                    
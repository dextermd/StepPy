class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def add_user(self, user):
        self.users.append(user)
        
    def show_library(self) ->str:
        for index, book in enumerate(self.books):
            print(index + 1, book)
    
    def show_users(self) ->str:
        for index, user in enumerate(self.users):
            print(index + 1, user)
            
    def delete_book(self, book):
        for bk in self.books:
            if bk == book:
                self.books.remove(book)
    
    def reserv_book(self, user, book):
        for bk in self.books:
            if bk.title == book.title:
                if bk.borrowed_by == None:
                    bk.borrowed_by = user.phone
                else: print("Book is busy")
        
    

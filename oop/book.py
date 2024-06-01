class Book:
    def __init__(self,title, author) -> None:
        self.title = title
        self.author = author
        self.borrowed_by = None
        
    def __str__(self) -> str:
        return f"Name: {self.title}, Author: {self.author}, Borrowed_by: {self.borrowed_by}"
#Write a python Program to create a Book Class declare the states as 
#BookName,AuthorName,PublisherName,PublisherDate,CategoryofBook
#1)Create 5 Objects and initialise the values using Constructor where 
#   --Create 1st object using one parameterized constructor
#   --Create 2nd object using Two parameterized constructor
#   --Create 3rd object using zero parameterized constructor
#   --Create 4th object using four parameterized constructor
#   --Create 5th object using five parameterized constructor
#2)Access the values using Accessor Methods
#3)Update the values using Mutator method using name of the book
class Book():
    def __init__(self,bookname=None,authorname=None,publisher_name=None,published_notes=None,published_date=None,category_of_book=None):
        print("object is created")
        self.Bookname = bookname
        self.Authorname = authorname
        self.Publisher_name = publisher_name
        self.Published_notes = published_notes
        self.Published_date = published_date
        self.Category_of_book = category_of_book

    def Display(self):
        print(f"name of the book is: {self.Bookname} ")
    def Set_book_name(self):
        self.Bookname = "The love of a good women"

    def Get_details(self):
        print(f"Book Name: {self.Bookname}")
        print(f"Author Name: {self.Authorname}")
    
    def Get_details_0(self):
        print("object created with 0 parameters")

    def Get_details4(self):
        print(f"Publisher name is : {self.Publisher_name}")
        print(f"Published_notes is: {self.Published_notes}")
        print(f"Published_date is: {self.Published_date}")
        print(f"categoru: {self.Category_of_book}")

M1 = Book("Boo")
M1.Display()
M1.Get_details()

M2 = Book("Book2", "Author2")
M2.Display()
M2.Get_details()

M3 = Book()
M3.Get_details_0()

M4 = Book("Book4", "Author4", "Publisher4", "Notes4")
M4.Get_details4()

M5 = Book("Book5", "Author5", "Publisher5", "Notes5", "2024-01-01")
M5.Get_details()
M5.Get_details4()

M1.Set_book_name()
print("After updating book name for M1:")
M1.Display()    
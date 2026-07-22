d={
    "b1":"python",
    "b2":"java",
    "b3":"ccc",
    "b4":"html"
}

def add_book():
    book =input("enter your book name:-")
    category= input("book category:-")
    if book.isalpha() and category.isalpha():
        d[book]= category
    else:
        print("try only alphabets.")
    print(d)
 
 
def view_books():
    print(d)
 

def search_books():
    book = input("find book.")
    if book in d.values() :
        print("yes , this book is avalible this dict...")
    else:
        print("not found this book , plese try again.")
 

def issue_books():
    book = input("enter book name: ")

    if book in  d.values() :
        print("no issue this book.")
    else :
        print("book not found, try again.")


def return_books():
    book = input("Enter book name: ").lower()

    if book in d.values():
        print("Book returned.")
    else:
        print("Book not found.")
    print(d)
 

while True:
    print("====== Library Management System ======")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_books()
    elif choice == "4":
        issue_books()
    elif choice == "5":
        return_books()
    elif choice == "6":
        break
    else:
      print("Invalid choice. Please try again.")
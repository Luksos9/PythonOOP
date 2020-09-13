class BookLibrary:

    def __init__(self, listOfBooks):
        self.listOfBooks = listOfBooks

    def displayBooks(self):
        print("\nAvailable books:")
        for book in self.listOfBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.listOfBooks:
            print("Successfully borrowed book!")
            listOfBooks.remove(requestedBook)
            return requestedBook
        else:
            print("Sorry no such book!")

    def addBook(self, givenBook):
        if givenBook != None:
            listOfBooks.append(givenBook)
            print("Successfully returned book!")


class Customer:

    def __init__(self, customerInitialBooks):
        self.customerBooks = customerInitialBooks

    def addBook(self, Book):
        return self.customerBooks.append(Book)

    def borrowBook(self):
        requestedBook = input("Enter book name: ")
        self.book = requestedBook
        return self.book

    def giveBackBook(self):
        toGiveBack = input("Enter book which you want to give back: ")
        if toGiveBack in self.customerBooks:
            self.customerBooks.remove(toGiveBack)
            return toGiveBack
        else:
            print("You don't have this book")
            return None


listOfBooks = ["Harry Potter", "Lord of the Rings", "ET"]
customerInitialBooks = []

library = BookLibrary(listOfBooks)
customer1 = Customer(customerInitialBooks)

menu = "\nEnter 1 to display available books\n" \
       "Enter 2 to borrow a book\n" \
       "Enter 3 to give back a book\n" \
       "Enter 4 to exit\n" \
       "Your choice: "

while (user_input := input(menu)) != "4":
    if user_input == "1":
        library.displayBooks()
    elif user_input == "2":
        requestedBook = customer1.borrowBook()
        checkedIfExist = library.lendBook(requestedBook)
        customer1.addBook(checkedIfExist)
    elif user_input == "3":
        toGiveBack = customer1.giveBackBook()
        library.addBook(toGiveBack)
    else:
        print("Wrong input! Please enter number 1-4.")

print("Have a nice day!")

# TODO: Add lower/upper case resistance
# TODO: Add small database to store books there
# TODO: Store list of initial books in separate file with database
# TODO: Add time of 2 months for each book to be returned

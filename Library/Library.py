class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print('\nAvailable Books:')
        for book in self.availableBooks:
            print(book)
        print('')

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have sucessfully borrowed book!\n")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book is not available\n")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have sucessfully returned book. Thank You!\n")


class Customer:

    def requestBook(self):
        self.book = input("Enter the name of a book that you would like to borrow: ") #przypisuje ksiazke do self.book
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book that you want to return: ")
        return self.book


library = Library(['How to win friends and influence people', '21 advice for 21st century', 'The Power of Habit'])
customer = Customer()

message = "Enter 1 to display the available books\n" \
          "Enter 2 to request for a book\n" \
          "Enter 3 to return a book\n" \
          "Enter 4 to exit\n" \
          "\nYour choice: "

while (user_choice := input(message)) != "4":
    if user_choice == "1":
        library.displayAvailableBooks()
    elif user_choice == "2":
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif user_choice == "3":
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    else:
        print("Wrong choice, please choose number 1-4")

# TODO: Improve option 3 so user will only be able to return book he has borrowed
# TODO: Add small database to store books there
# TODO: Store list of initial books in separate file with database
# TODO: Add time of 2 months for each book to be returned
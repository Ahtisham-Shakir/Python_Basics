class Library:

    def __init__(self, list, name):
        self.list_of_books = list
        self.library_name = name
        self.lendict = {}

    def Display(self):
        print("Following Books are Available in the Library")
        for book in self.list_of_books:
            print(book)

    def lend(self, user, book):
        if book not in self.lendict.keys():
            self.lendict.update({book, user})
            print(f"lener-Dictionary has been updated!  You can take your book now")
        else:
            print(f"Book is already being used by {self.lendict[book]}")


    def add(self, book):
        self.list_of_books.append(book)
        print("Book has been added to the book list")

    def returnbook(self,book):
        self.lendict.pop(book)

if __name__ == '__main__':
    li = ['Physics', 'Chemistry', 'Biology', 'Maths']
    shaam = Library(li,"Ahtisham's")
    while (True):
        print(f"Welcome to {shaam.library_name} Library.  Enter your choice")
        print("1. Display Book")
        print("2. Lend Book")
        print("3. Add Book")
        print("4. Return Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter valid input")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            shaam.Display()

        elif user_choice == 2:
            name = input("Enter Your name")
            book = input("Enter name of book you want to lend")
            shaam.lend(name,book)

        elif user_choice == 3:
            book = input("Enter name of book you want to add")
            shaam.add(book)

        elif user_choice == 4:
            book = input("Enter name of book you want to Return")
            shaam.returnbook(book)

        print("Enter c to continue q to quit")
        user_choice2 = input()

        if user_choice2 == 'c':
            continue

        else:
            exit()



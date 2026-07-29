movies = {}

def add_movie():
    movie = input("Enter Movie Name: ")
    seats = int(input("Enter Total Seats: "))
    movies[movie] = seats
    print("Movie Added Successfully")

def display_movie():
    if movies:
        print("----- Movie List -----")
        for movie, seats in movies.items():
            print(f"Movie: {movie} | Seats: {seats}")
    else:
        print("No Movies Available")

def book_ticket():
    movie = input("Enter Movie Name: ")
    if movie in movies:
        ticket = int(input("Enter Number of Tickets: "))
        if ticket <= movies[movie]:
            movies[movie] -= ticket
            print("Ticket Booked Successfully")
        else:
            print("Not Enough Seats Available")
    else:
        print("Movie Not Found")

def cancel_ticket():
    movie = input("Enter Movie Name: ")
    if movie in movies:
        ticket = int(input("Enter Number of Tickets to Cancel: "))
        movies[movie] += ticket
        print("Ticket Cancelled Successfully")
    else:
        print("Movie Not Found")

def delete_movie():
    movie = input("Enter Movie Name to Delete: ")
    if movie in movies:
        del movies[movie]
        print("Movie Deleted Successfully")
    else:
        print("Movie Not Found")


while True:
    print("===== Movie Ticket Booking System =====")
    print("1. Add Movie")
    print("2. Display Movies")
    print("3. Book Ticket")
    print("4. Cancel Ticket")
    print("5. Delete Movie")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_movie()

    elif choice == 2:
        display_movie()

    elif choice == 3:
        book_ticket()

    elif choice == 4:
        cancel_ticket()

    elif choice == 5:
        delete_movie()

    elif choice == 6:
        print("Thank You...")
        break

    else:
        print("Invalid Choice")
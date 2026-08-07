# movies = {}

# def add_movie():
#     movie = input("Enter Movie Name: ")
#     seats = input("Enter Total Seats: ")
#     if movie.isalpha() and seats.isdigit() :
#         movie = str(movie)
#         seats = int(seats)
#     else :
#         print("try ")
        
#     movies[movie] = seats
#     print("Movie Added Successfully")

# def display_movie():
#     if movies:
#         print("----- Movie List -----")
#         for movie, seats in movies.items():
#             print(f"Movie: {movie} | Seats: {seats}")
#     else:
#         print("No Movies Available")

# def book_ticket():
#     movie = input("Enter Movie Name: ")
#     if movie in movies:
#         ticket = int(input("Enter Number of Tickets: "))
#         if ticket <= movies[movie]:
#             movies[movie] -= ticket
#             print("Ticket Booked Successfully")
#         else:
#             print("Not Enough Seats Available")
#     else:
#         print("Movie Not Found")

# def cancel_ticket():
#     movie = input("Enter Movie Name: ")
#     if movie in movies:
#         ticket = int(input("Enter Number of Tickets to Cancel: "))
#         movies[movie] += ticket
#         print("Ticket Cancelled Successfully")
#     else:
#         print("Movie Not Found")

# def delete_movie():
#     movie = input("Enter Movie Name to Delete: ")
#     if movie in movies:
#         del movies[movie]
#         print("Movie Deleted Successfully")
#     else:
#         print("Movie Not Found")


# while True:
#     print("===== Movie Ticket Booking System =====")
#     print("1. Add Movie")
#     print("2. Display Movies")
#     print("3. Book Ticket")
#     print("4. Cancel Ticket")
#     print("5. Delete Movie")
#     print("6. Exit")

#     choice = int(input("Enter Your Choice: "))

#     if choice == 1:
#         add_movie()

#     elif choice == 2:
#         display_movie()

#     elif choice == 3:
#         book_ticket()

#     elif choice == 4:
#         cancel_ticket()

#     elif choice == 5:
#         delete_movie()

#     elif choice == 6:
#         print("Thank You...")
#         break

#     else:
#         print("Invalid Choice")



# v = 11
# while v >1 :
#     v = v-1
#     print(v)

# i = 1
# fact = 0 
# while i <=10 :
#     fact = fact +i
# print(fact)
# i = i+1

# i = 1
# v = 4
# while i <=10 :
#     print(i*v)
#     i = i+1

# a = 1
# b = 1
# i = 0

# while i <=10 :
#     c = a+b
#     print(a)
#     a= b
#     b= c
#     i = i+1
 

# import ast 

# l = ["ram","sita"]


# file = open("h.py","w")
# file.write(str(l))
# file.close()

# file = open("h.py","r")
# v= ast.literal_eval(file.read())
# file.close()

# file =  open("h.py","w")
# v.append(66)
# file.write(str(v))
# file.close()


# file =  open("h.py","w")
# v.remove("ram")
# file.write(str(v))
# file.close()

class student :
    def __init__(self,name1,id):
        self.name1 = name1
        self.id = id

    def show(self):
        print(self.name1)
        print(self.id)

class teacher(student) :

    def __init__(self,name,classes,name1,id):
        student.__init__(self,name1,id)
        self.name = name
        self.clasess = classes

    def show(self):
        print(self.name)
        print(self.clasess)
        print(self.name1)
        print(self.id)

class founder(teacher) :
    def __init__(self,branch,city,name,classes,name1,id):
        teacher.__init__(self,name,classes,name1,id)
        student.__init__(self,name1,id)
        self.branch = branch
        self.city = city

    def show(self):
        
        print(self.name1)
        print(self.id)
        print(self.name)
        print(self.clasess)
        print(self.branch)
        print(self.city)

a= founder("villan",1512,"sandeep","AI_ML","RW","jamnager")
a.show()


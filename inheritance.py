class student :
    def __init__(self,name1,id):
        self.name1 = name1
        self.id = id

 
class teacher(student) :

    def __init__(self,name,classes,name1,id):
        student.__init__(self,name1,id)
        self.name = name
        self.clasess = classes
 
class founder(teacher) :
    def __init__(self,name1,id,name,classes,branch,city):
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

name1 = input("enter student name:-")
id = int(input("enter student id:-"))
name = input("enter sir name:-")
classes = input("enter your classes name:-")
branch= input("where are your from branch:-")
city = input("enter your city name:-")

a= founder(name1,id,name,classes,branch,city)
a.city = "nakum"
a.show()
# encapsialitions
class student :

    def __init__(self,name):
        self.name = name
class balance(student) :
    def __init__(self,__bank_balance,name):
        student.__init__(self,name)
        self.bank =__bank_balance
    def show(self):
        print(self.name)
        # print(self.bank)
    def show(self):
        print(self.bank)
a = balance("virendra",9000)
a.show()

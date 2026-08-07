# # maltipul inheritance

# class  student :
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
    
# class teacher :
#     def __init__(self,name1,aiml):
#         self.name1 = name1
#         self.aiml = aiml

# class branch(student,teacher) :
#     def __init__(self,name,id,name1,aiml,city):
#         student.__init__(self,name,id)
#         teacher.__init__(self,name1,aiml)
#         self.city = city

#     def show(self):
#         print(f"student name is {self.name}")
#         print(f"student id is {self.id}")
#         print(f"teacher name is {self.name1}")
#         print(f"teacher courses is {self.aiml}")
#         print(f"branch city  name is {self.city}")


# v = branch("viru",1521,"sandeepgwali","sdfdsf","jamnager")
# v.show()

# # maltileavel inheritance

# class  student :
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
    
# class teacher(student) :
#     def __init__(self,name,id,name1,aiml):
#      student.__init__(self,name,id)
#      self.name1 = name1
#      self.aiml = aiml

# class branch(teacher) :
#     def __init__(self,name,id,name1,aiml,city):
#         teacher.__init__(self,name,id,name1,aiml)
#         self.city = city

#     def show(self):
#         print(f"student name is {self.name}")
#         print(f"student id is {self.id}")
#         print(f"teacher name is {self.name1}")
#         print(f"teacher courses is {self.aiml}")
#         print(f"branch city  name is {self.city}")


# v = branch("viru",1521,"sandeepgwali","sdfdsf","jamnager")
# v.show()


# # single inheritance


# class  student :
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id
#     def show(self):
#         print(f"student name is {self.name}")
#         print(f"student id is {self.id}")
# obj = student("virendra",124431)
# obj.show()




# marks = input("enter your marks")

# if marks.isdigit():
#     marks= int(marks)
#     if marks >= 90 :
#         print("A")
#     elif marks >= 50 :
#         print("B")
#     elif marks >=35 :
#         print("c")
#     else:
#         print("fail")
# else:
#     print("try only num.")

# num = input("enter any num:-")
# if num.isdigit():
#     num = int(num)
#     if num %2== 0 :
#         print("even")
#     else:
#         print("odd")
# else:
#     print("try only num..")

# l = [12,1231,3424,4523]
# largesrt = l[0]
# for i in l :
#     if i > largesrt :
#         largesrt = i 
# print(largesrt)

# num1 = 555
# num2 = 123456456
# num3 = 453
# if num1 >num2 and num1>num3 :
#     print("num1 is grater")
# elif num2>num3 and num2>num1 :
#     print("num 2 is grater")
# else:
#     print("num3 is grater")


# age = input("enter your age :-")
# if age.isdigit():
#     age = int(age)
#     if age >= 18 :
#         print("you are eligible")
#     else:
#         print("not eligible.")
# else:
#     print("try only num.")

# years = input("cheak leap year:-")

# if years.isdigit():
#     years= int(years)
#     if years %4 == 0 :
#         print("this year is leap.")
#     else:
#         print("not leap years.")
# else:
#     print("try only num.

# name = input("enter your name:-")
# if name in "aeiou":      
#         print("vowel")
# else:
#         print("consonenet.")
 
# for i in range(1,101):
#     print(i)

# for i in range(2,101,2):
#     print(i)

# for i in range(1,101,2):
#     print(i)

# num = int(input("enter multiphication num:-"))
# for i in range(1,11):
#     print(num ,"x",i,"=",num*i)

# sum=0
# for i in range(1,101):
#     sum = sum+i
#     print(sum)

# num= int(input("enter any num:-"))
# fact = 1 
# for i in range(1,num+1):
#     fact = fact*i
#     print(fact)

# for i in range(1,21):
#     print(i*i)

# for i in range(101,1,-1):
#     print(i)

# i=0
# while i <=100:
#     i+=2
#     print(i)


# i = 1
# sum = 0
# while i<101 :
#     sum = sum+i
#     print(sum)
#     i += 1

# i = 100
# sum = 0
# while i>1 :
# i += 1
#   print(i)

 
 

# while  True: 
#     num = int(input("enter any num:-"))
#     if num == 0 :
#         print(num)
#         break

# l = [1,2,3,4,5]
# print(l)   


# l = [1,2,38,8,58,37,7,37,37,2,23,145,54,456,547,7435435429,467,4697,5]
# l.remove(5)
# a = l[3]
# largest = l[0]
# for i in l:
#     if i > largest:
#         largest=i
# print(largest)
# smallest = l[0]
# for i in l :
#     if i < smallest:
#         smallest = i
# print(smallest) 

# l.sort()
# print(l)
# l.reverse()
# sum = 0
# for i in l :
#     sum = sum+i
# print(sum)

# d= {"name":"virendra",
#     "age":22,
#     "city":"jamnager"}
# print(d.keys())
# name = input("entr name:-")
# age = int(input("enter age:-"))
# d[name]=age
# d.pop(name)
# print(d)
 
# import matplotlib.pyplot as mtp
# import numpy as np

# tem = np.array([32,35,29,23,34,22])
# day = np.array(["sun","mon","tue","the","fri","sut"])

# mtp.plot(day,tem,marker='o',label="week days",color="r")
# mtp.title("week tempacher in jamnager")
# mtp.xlabel("days")
# mtp.ylabel("temprecher")
# mtp.legend()
# mtp.show()





















































# import math 
# print(math.fibbo(5))
          


# import matplotlib.pyplot as mpl 
# import numpy as np

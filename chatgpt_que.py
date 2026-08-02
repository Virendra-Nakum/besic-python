## 1 Student se input lo.Student ki age input lo.Dono values ko dictionary me store karo.Dictionary ko list me add karo.Last me students list print karo.

# student = input("enter your name:-")
# age = input("enter your age:-")
# d = {"name":student,"age":age}
# l= [d]  
# print(l)

# # 2 Program banao:  User se student ka name input lo.Agar student mil jaye:Uski age update karo.Agar student na mile  Print karo "Student Not Found"

# d= { "virendra": 22,
#      "rahul" :20}
# name = input("find student :-")
# if name in d.keys():
#     age= int(input("upadte age:-"))
#     d[name]=age
#     print(d)
# else:
#     print("student not found.")

# # 3 Requirements:User se student id input lo. Agar id mil jaye  Student ka naam aur marks print karo.   Agar id nahi mile:  "Student Not Found" print karo.

  
# students = [
#     {"id": 1, "name": "Virendra", "marks": 85},
#     {"id": 2, "name": "Rahul", "marks": 70},
#     {"id": 3, "name": "Amit", "marks": 90}
# ]

# user_id = int(input("Enter student id: "))
# for student in students:
#     if student["id"] == user_id:
#         print(student["name"])
#         print(student["marks"])
 
# else:
#     print("Student Not Found")


# # 4 Write a program to: Take an integer input n .Print all even numbers from 1 to n.Do not use % (modulus operator).

# i = 1
# num = int(input("enter any num:-"))
# while i <=  num:
#     print(i)
#     i += 2

# # 5 Write a program to: Take an integer input n.Print numbers from 1 to n.If the number is divisible by 3, print "Fizz" instead of the number.If the number is divisible by 5, print "Buzz" instead of the number.If the number is divisible by both 3 and 5, print "FizzBuzz".

# num = int(input("enter and num:-"))
# for i in range(1,num+1):
#     if i %3 == 0 and i %5 == 0:
#         print(i,"Fizz Buzz") 
#     elif i %3 == 0 :
#         print(i,"fizz")
#     elif i %5 == 0 :
#         print(i,"Buzz")
#     else:
#         print(i)


# # 6 Write a program to: Take a string input.Count  how many vowels are in the string.  Do not use .count().

# name = input("enter your name:-").lower()
# for ch in name :
#     if ch in "a" "e" "i" "o" "u" :
#        print(ch)

# # 7 Rules ❌ Don't use set()❌ Don't use libraries ✅ Use loops and conditions
# numbers = [4, 7, 2, 9, 5, 2, 7, 4]
# uniqe = []
# for i in numbers :
#     if i not in uniqe :
#         uniqe.append(i)  
# for  i in uniqe:
#     print(i)

# # 8  Rules Find the second largest number ❌ Don't use sort()❌ Don't use max()❌ Don't use min()✅ Use loops and conditions only.
 
# l = [10, 20, 30, 40, 50]
# largest = l[0]
# second = l[0]
# for i in l:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second  :
#         second = i
# print("Largest:", largest)
# print("Second Largest:", second)


# # smlallest num 
# l = [25, 10, 45, 5, 30]
# smallest = l[0]
# for i in l :
#     if i < smallest:
#         smallest = i
# print(smallest)

# # 9  Write a program to count even and odd numbers in the list.  ❌ Don't use count() ❌ Don't create separate even/odd lists.✅ Use only loops and conditions.

# l = [10, 15, 22, 31, 40, 55]
# even  = 0
# odd= 0
# for i in l :
#     if i %2 == 0  :
#         even += 1  
#     elif i%2 != 0 :
#         odd+= 1
# print("even=",even)
# print("odd=",odd)

#  10 Write a Python program to reverse a list without using reverse() or slicing ([::-1]). ❌ Don't use reverse() ❌ Don't use [::-1]❌ Don't use reversed()

# l = [10, 20, 30, 40, 50]
# for i in range(len(l)-1,-1,-1):
#     print(l[i])
 
# marks = input("Enter marks: ")
# if marks.isdigit():
#     marks=int(marks)
#     if marks >= 90:
#         print("Grade A")
#     elif marks >= 75:
#         print("Grade B")
#     elif marks >= 50:
#         print("Grade C")
#     else:
#         print("Fail")
# else:
#     print("enter only numbers.")

# 2. 
# num = input("Enter number: ")
# if num.isdigit():
#     num=int(num)
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# else:
#     print("enter only numbers.")


# 3. 
# a =input("Enter first number: ")
# b = input("Enter second number: ")
# if a.isdigit() and b.isdigit():
#     a=int(a)
#     b=int(b)
#     if a > b:
#         print(a)
#     else:
#       print(b)
# else:
#     print("invalide input.")


# 4. 
# a = input("enter numbers:")
# b = input("enter numbers:")
# c = input("enter numbers:")
# if a.isdigit() or b.isdigit() and c.isdigit() :
#     a=int(a)
#     b=int(b)
#     c=int(c)
#     if a >= b and a >= c:
#         print(a)
#     elif b >= a and b >= c:
#         print(b)
#     else:
#         print(c)
# else:
#     print("invalid input.")


# 5. 

# age = input("Enter age: ")
# if age.isdigit():
#     age=int(age)
#     if age >= 18:
#         print("Eligible")
#     else:
#         print("Not Eligible")
# else:

#     print("invalide input.")



# 6. 
# year = input("Enter year: ")
# if year.isdigit():
#     year= int(year)

#     if year % 4 == 0 :
#         print("Leap Year")
#     else:
#         print("Not Leap Year")
# else:
#     print("invalid input.")


# 7.
# marks = input("enter  your marks:")
# if marks.isdigit():
#     marks= int(marks)
#     if marks >= 90:
#         print("A")
#     elif marks >= 80:
#         print("B")
#     elif marks >= 60:
#         print("C")
#     else:
#         print("Fail")
# else:
#     print("invalide input.")


# 8.
# ch = input("Enter alphabet: ")
# if ch.isalpha():
#     ch=str(ch)
#     if ch in "aeiouAEIOU":
#         print("Vowel")
#     else:
#         print("Consonant")
# else:
#     print("enter valid input.")


# 9. 

# a = input("try num,")
# b= input("try num.")
# op = input("Enter + - * / : ")
# if a.isdigit() or b.isdigit() :
#     a = int(a)
#     b= int(b)
#     if op == "+":
#         print(a + b)
#     elif op == "-":
#         print(a - b)
#     elif op == "*":
#         print(a * b)
#     elif op == "/":
#         print(a / b)
#     else:
#         print("Invalid")
# else:
#   print("invalide input.")


# 10.
# num = input("divisible in any num:")
# if num.isdigit():
#     num=int()
#     if num % 5 == 0 and num % 11 == 0:
#         print("Divisible")
#     else:
#         print("Not Divisible")
# else:
#  print("try again...")


#  #For Loop


# 1.
# for i in range(1,101):
#     print(i)
# 2.
# for i in range(2,51,2):
#     print(i)
# 3.
# for i in range(1,51,2):
#     print(i)
# 4.
# num = input("enter any num:")
# if num.isdigit():
#     num=int (num)
#     for i in range(1,11):
#         print(num,"x",i,"=",num*i)
# else:
#     print("try again....")


# 5.
# total = 0
# for i in range(1,101):
#     total += i
# print(total)


# 6.
# num = input("try num...")
# if num.isdigit():
    # num=int(num)
# fact = 1
#   for i in range(1,num+1):
#     fact *= i
# else:
#     print("try again.")
# print(fact)


# 7.
# for i in range(1,21):
#     print(i*i)

# 8.
# text = input("enter any num.")
# v = ""
# for i in text:
#     v = i + v
# print(v)


# 9.
# text = input("any num.")
# count = 0
# for i in text:
#     if i.lower() in "aeiou":
#         count += 1
# print(count)


# 10.
# a = [10,25,7,90,45]
# largest = a[0]
# for i in a:
#     if i > largest:
#         largest = i
# print(largest)


# # While Loop

# 1.
# i = 1
# while i <= 100:
#     print(i)
#     i += 1


# 2.
# i = 2
# while i <= 50:
#     print(i)
#     i += 2
# 3.
# i = 1
# while i <= 50:
#     print(i)
#     i += 2

# 4.
# num = int(input("enter numbr:"))
# total = 0
# while num > 0:
#     total += num % 10
#     num //= 10
# print(total)


# 5.
# num = int(input("number:" ))
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print(rev)


# 6.
# num = int(input("enter num: "))
# fact = 1
# i = 1
# while i <= num:
#     fact *= i
#     i += 1
# print(fact)


# 7.
# n = int(input("enter num: "))
# a = 0
# b = 1
# i = 1
# while i <= n:
#     print(a)
#     c = a + b
#     a = b
#     b = c
#     i += 1


# 8.
# num = int(input("try num:" ))
# while num != 0:
#     num = int(input())
# print("Stopped")


# 9.
# num = int(input("enter num: "))
# count = 0
# while num > 0:
#     count += 1
#     num //= 10
# print(count)


# 10.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# #List


# 1.
# a = [10,20,30,40,50]
# print(a)
# 2.
# a = [10,20,30]
# a.append(40)
# print(a)

# 3.
# a = [10,20,30]
# a.remove(20)
# print(a)


# 4.
# a = [10,20,30]
# print(len(a))


# 5.
# a = [10,20,30,40]
# print(a[2])


# 6.
# a = [10,50,20,90]
# print(max(a))
# print(min(a))


# 7.
# a = [30,10,40,20]
# a.sort()
# print(a)


# 8.
# a = [10,20,30]
# a.reverse()
# print(a)


# 9.
# a = [10,20,30]
# print(sum(a))


# 10.
# a = [10,20,30,20,20]
# print(a.count(20))


# #Dictionary


# 1.
# student = {
#     "name":"Virendra",
#     "age":21,
#     "city":"Jamnagar"
# }
# print(student)

# 2.
# student = {
#     "name":"Virendra",
#     "age":21
# }
# print(student["name"])


# 3.
# student = {
#     "name":"Virendra"
# }
# student["city"] = "Jamnagar"
# print(student)


# 4.
# student = {
#     "name":"Virendra",
#     "age":21
# }
# student["age"] = 22
# print(student)


# 5.
# student = {
#     "name":"Virendra",
#     "age":21
# }
# student.pop("age")
# print(student)


# 6.
# student = {
#     "name":"Virendra",
#     "age":21
# }
# print(student.keys()


# 7.
# student = {
#     "name":"Virendra",
#     "age":21
# }
# print(student.values())


# 8.
# student = {
#     "name":"Virendra",
#     "age":21,
#     "city":"Jamnagar"
# }
# for key, value in student.items():
#     print(key, value)
# 9.
# student = {
#     "name":"Virendra",
#     "age":21
# }
# if "age" in student:
#     print("Key Found")
# else:
#     print("Key Not Found")
# 10.
# student = {
#     "name":"Virendra",
#     "age":21,
#     "city":"Jamnagar"
# }
# print(len(student))
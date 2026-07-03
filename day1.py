#python variables

#  a= "virendra"
# b= "23"
# c= "jamnager"

# print(a)
# print("my name is",(a),"my age is",(b),"and i live in",(c),)

# a=10
# b=20
# a,b=b,a

# print("a=",a)
# print("b=",b)

# a=input("entr your age :-")
# b=input("enter your age:-")

# print(a+b)
 
# a= 22.22
# b= 66.66
# print(int(a))
# print(int(b))

# name= "banana", "apple","mango","chikuu"
# print(name)

# name =str(input("your name:- "))
# print(len(name))

# a=4**2
# b=4**3
# print(a,b)

# gujrati= 98.76
# hindi= 66.89
# english= 77.89
# print(gujrati+hindi+english)
 
# a= "hellow"
# b=a
# print(b)
 
# birth_years= 2004
# years= 2026
# print(years-birth_years)

# data types 

# a=10
# b=10.5
# c="hellow"
# d= True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# a=10
# print(float(a))
# print(str(a)) 

# a=input("enter everthing:- ")
# print(type(a))

# name=["virendra","nakum","ram","syam"]
# print(type(name))

# name= ("virendra","nakum")
# print(name[0])

# a="10"
# a= int(a)+5
# print(a)
 
# a=float(10)
# print(a)

# a=["nakum","viru,"]
# print(tuple(a))

 
# a = (10, 20, 30, 40)

# b= list(a)
# b[2] = 50
# print(b)


# if-else:


# a=float(input("any num:- "))

# if a > 0:
#     print("positive")
# elif a < 0:
#     print("negitive")
# else:
#     print("zero")

# if 66888% 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# num1=  990
# num2=800
# if num1 > num2:
#     print("num1 is largest")
# else:
#     print("num2 is largest")

 
# num1=56
# num2=86
# num3=88

# if num1>num2 and num1>num3 :
#     print("largest")
# elif num2<num3 and num2>num3:
#     print("smallest")
# else:
#     print("zeor")


# a=float(input("enter your age:-"))
# if a >=18:
#     print("your are eligible")
# else:
#     print("try next time")

# marks= float(input("type marks:- "))

# if marks >=90:
#     print("A")
# elif marks <=89 and marks>=75:
#     print("B")
# elif marks<=74 and marks>=50:
#     print("C")
# elif marks <50:
#     print("fail")

# year= int(input("enter any year:-"))
# if year%4==0:
#     print("leap years")
# else:
#     print("not leap years")

# a=str(input("any alfabet:"))
# if a in ("a","e","i","o","u"):
#     print("vowel")
# else:
#     print("consonant")


# b= ("villan")
# a=0
# while a < 5:
#   pas=str(input("enter your password:-"))
#   if b==pas:
#     print("done")          
#     break 
#   else:
#      print("try again")
# else:
#  print("try next time")

# a=int(input("any num:-"))
# if a%3 ==0 : 
#     print("all done")
# elif a%5 ==0:
#     print("all right")
# else:
#     print("right again")

# a= [1,2,3,4,5]
# print(a[2])

# a=10
# b=20
# c=b
# print(a+c)


# for loop 
 

# for i in range(1,11):
#  print(i)

# for i in range (2,51,2):
#     print(i)
   
# num = 56
# for i in range(1, 11):
#     print(num, "*", i, "=", num * i)

# sum=0
# for  i in range(1,11):
#     sum =sum +i
# print("sum=",sum)

# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i
# print("Factorial =", fact)
 
# a=str(input("ant type:"))
# for a in str(a):
#  print(str(a))

# a=[1,2,3]
# for a in range(3):
#  print(a)

# text = input("Enter a string: ")
# count = 0
# for ch in text.lower():
#     if ch in "aeiou":
#         count += 1
# print("Total vowels:", count)

# for i in range(1,11):
#     print(i*i)

# s = input("Enter a string: ")
# reverse = ""
# for i in s:
#     reverse = i + reverse
# print("Reverse string:", reverse)



# list 


# a=[10,20,30,40,50]
# print(a)

# a=[10,20,30,40,50]
# a.append(60)
# print(a)

# a=[10,20,30,40,50]
# a.remove(30)
# print(a)

# a=[10,20,30,40,50]
# max=a[0]
# min=a[0]
# for i in a:
#     if i >max:
#         max=i
#     if i <min:
#         min =i
# print("max=",max)
# print("min=",min)

# a=[10,20,30,40,50]
# sum=0
# for i in a:
#     sum=sum+i
# print("Sum=",sum)

# a=[10,20,30,40,50]
# a.count(10)
# print(a.count(10))

# a=[80,20,90,30,50]
# a.sort()
# print(a)

# a=[10,20,30,40,50]
# a =a[::-1]
# print(a)

# a=[10,20,30,40,50]
# a[2]=90
# print(a)

# a=[10,20,30,40,50]
# if 100 in a:
#     print("exitst num")
# else:
#     print("not exists num")

# a=input("enter any num:-")
# a=int(a)
# if a >50:
#     print("whether")
# else:
#     print("anuther")

# a="virendra"
# print(a[0])
# print(a[-1])

# a=[10,20,30,40,50]
# print(a[2])

# name=input("any num;-")
# name1=input("any num:-")
# if name ==name1:
#     print("first")
# else:
#     print("second")

# num=input("enter num")
# num=int(num)
# num=num*7
# print("num=",num)

# a=(10,20,30)
# print(a[ ::-1])

# s = "ram syam  krisna "
# print(s.count(" "))

# a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# for i in a :
#    if i%2==0:
#       print("even num")
#    else:
#       print('odd num') 

# a=input("any num:-")
# a=int(a)
# if a%4==0:
#     print("good")
# else:
#     print("velid num")

# word = input("Enter a word: ")

# if word.startswith("A"):
#     print("Starts with A")
# else:
#     print("Does not start with A")
# age=18
# if age>=18:
#     print("adult")
# else:
#     print("minor")

# for i in range(5):
#     print(i)

# lst=[1,2,3]
# print(lst(5))
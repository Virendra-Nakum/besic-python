# q.1

v=  input("enter any num: ")
if v.isdigit():
    v=int(v)      
    if v >= 50 :
      print("graterthan.")
    elif v <= 49 :
      print("lessthan.")
else:
    print("try only numbers...")

# q.2
v= "villan"

print(v[0])
print(v[-1])

# q.3
a= ["ram","laxman","sita","hanuman","bharat"]
print(a[2])

# q.4
v=input("enter any num:")
v1 = input("enter any num:")
if v.isdigit():
    v=v1==int
    if v == v1 :
        print("first")
    else:
     
        print("second")
else:
    print("only num...")
# q.5

v=input("enter with multiple 7 :")
if v.isdigit():
 v=int(v)
 print(v*7)
else:
 print("only num valid.")

# q.6
a= "villan","viru","virendra"
print(a[::-1])

# q.7
a= ("villan" "viru" "virendra")
print(a.strip())

# q.8
a=input("enter your full name:")
print(a.count(" "))

# q.9
v= int(input("enter any num "))
if v%4 == 0 :  
  print("good.")
else:
  print("try again.")

# q.10
v=str(input("enter your name:-"))
if v.startswith("A"):
    print("start with A.")
else:
    print("not start with A.")

# q.11
age=18
if age>=18 :
    print(age)

# q.12
for i in range(5):
    print(i)

# q.13
list 

a= [1,2,3,4,5]
print(a)

# q.14
a= ["ram","laxman","sita","hanuman","bharat"]
a.append("starughan")
print(a)

# q.15
a= ["ram","laxman","sita","hanuman","bharat"]
a.remove("sita")
print(a)

# q.16
a= ["ram","laxman","sita","hanuman","bharat"].__len__()
print(a)

# q.17
a=["ram","laxman","sita","hanuman","bharat"]
print(a[3])

# q.18
a=[1,24234,23423,6456,4,2344,24234235,112412414342342,53]
largest = a[0] 
for i in a :
    if i > largest:
       largest = i 
print(largest)

# q.19
a=[1,24234,23423,6456,4,2344,24234235,112412414342342,53]
smallest = a[0]
for i in a:
    if i < smallest :
       smallest = i 
print(smallest)

# q.20
a= ["ram","laxman","sita","hanuman","bharat"]
a=[1,24234,23423,6456,4,2344,24234235,112412414342342,53]
a.sort()
print(a)

# q.21
a=[1,24234,23423,6456,4,2344,24234235,112412414342342,53]
a.reverse()
print(a)


# q.22
a=[1,24234,23423,6456,4,2344,24234235,112412414342342,53,3,5,4,22,3,4,77,777,33,22,2]
print(a.count(22))

# dictionary
# q.23
l= {"name":"virendra",
    "age":23,
    "city":"jamnager"}
print(l)

# q.24
l= {"name":"virendra",
    "age":23,
    "city":"jamnager"}
for i in l:
    print(i)

# q.25
l= {"name":"virendra",
    "age":23,
    "city":"jamnager"}
l.items()
print(l)

# q.26
l= {"name":"virendra",
    "age":23,
    "city":"jamnager"}
l.update({"name":"viru"})
print(l)

# q.27

l= {"name":"virendra",
    "age":23,
    "city":"jamnager"}
l.pop("name")
print(l)


# q.28
l= {"name":"virendra",
    "age":23,
    "city":"jamnager"}
print(l)

# q29
# 
l= {"name":"virendra",
    "age":23,
    "city":"jamnager"}

v= input("find in dictionary:-")
if v in l :
    print("avaleable.")
else:
    print("not found.")
print(l)

# q.30

l= {"name":"virendra",
    "age":23,
    "city":"jamnager"}
print(l.__len__())

# q.31  if/elif/else:
v= int(input("enter your marks:-"))
if v >= 90 :
    print("A grade.")
elif v >= 70 :
    print("B grade.") 
elif v >= 50 :
    print("C grade.")
elif v >=34 :
    print("D grade.")
elif v <=33 :
    print("Fail.")
else:
    print("invalide input.")

# q.32
v= int(input("enter any numbers:-"))
if v %2 == 0 :
    print("even numbers.")
else:
    print("odd numbers.")

# q.33
a=33
b=35
if a> b :
    print("a is largest.")
else :
    print("b is largest.")

# q.34
a=33
b=353
c=88
if a> b :
    print("a is largest.")
elif a> b:
    print("b is largest.")
else :
    print("c is largest.")

# q.35
v =input("enter your age;-")
if v.isdigit():
    v=int(v)
    if v >= 18 :
        print("eligiblilly.")
    else:
        print("not eligible.")
else:
    print("invalide input.")

# q.36
v= input("enter your name:-")
if v.isalpha():
    v=str(v)
    if v in ("a","e","i","o","u"):
        print("vowel")
    else:
        print("consonnet")
else:
    print("invalide input ")
 
# q.37  for loop

for i in range(1,101):
    print(i)


for i in range(1,101,2):
    print("odd num" , i)


for i in range(1,101):
    if i % 2 == 0 :
     print("odd num" , i)


v= int(input("num"))
for i in range(1,11):
 print(v , "x" , i , "=" , i*v)

fact = 1
v = input("enter any num:-")
if v.isdigit():
    v= int(v)
    for i in range(1,v):
     fact = fact*i
    print(fact)
else :
    print("invalide input.")

for i in range(1,21):
    print(i*i)

# con.vovel .find

for i in range(100, 0 , -1):
    print(i)

name = input("Enter your name: ").lower()
count = 0
for ch in name:
    if ch in "aeiou":
        count += 1
print("Total vowels:", count)

v= [123,434,23,2,334,334,324,122,12,23,3535,64,75,68,768,768,9687,986,9,69,67,75,856,745,2626,36,45,458,769,8769876986,78,567,456,34,5,23479887708978097087087876076,234,2,43,453,645,645,64,6,645,562,425576,4536,4,424,425,45,447,47,45,457,457,45,457,457,4257,4257,4745,6452,47,467,47,45,745,45,74,7,578,67,8735,42,4,447,426742674,24274,26746,42675,47,456,46,4526,33426,77457,45,7462,7537,5,1,45,7467,2467,5,467,467,4,742,742,4,653,4674,4,642576462,746,746,4,54567,4527,45,457,4,746,7467,6,74,74,4,42,4,4,56,4536,453,64,576,4,4,7,4576,4576,4576,45,45,45,6,4256,4356,46745,8,67,8768,577,56,746,76,42,6435,64,3456,4536,45,7,6,4,7,47,4576425,4276,454564536,4536,4576,426,7,4545,64576,4135,742,7,4,75,367,436,73,6,56,5,55,55,56,4,56]
print(len(v))
# v= int(v)
largest = v[0]
for i in v :
    if i > largest :
     largest = i 
print(largest)

# while loop:

i=0
while  i <= 100:
    i += 2
    print(i)

i=1
while  i <= 100:
    i += 2
    print(i)


sum = 0
i=1 
while  i <= 100:
    sum = sum+i
    i += 1
    print(sum)

i=100
while  i >= 0:
    i += -1
    print(i)

i=1
fact = 1
while  i <= 20:
    i += 1
    fact = fact*fact
    print(fact)

a=0
b=1
i=1
while i <= 20 :
    print(a)
    c= a+b
    a=b
    b=c
    i += 1
 
num = 1
while num != 0:
    num = int(input("Enter number (0 to stop): "))


num = int(input("Enter number: "))
count = 0
while num > 0:
    num = num // 10
    count += 1
print("Digits =", count)

i = 1

while i <= 10:
    print(i)
    i += 1

l = [4,46,44,64,6,46,646456,45,645,67,878766,768,7686,78,76876,8,78768,7,84,835,7567,568756,8,78,868,6,7,68,57,5627,26,76,7,567,5,87,87,8,98,88,7987,76,537,2,742,6,6,363141,35,345]
print(l)
l.append(60)
print(l)
print(len(l))
print(l.remove(44))
print(l[9])
sum = l[0]
for i in l :
    sum = sum+ i 
print(sum)
print(l.count(4))
largest = l[0]
for i in l :
    if i > largest :
        largest= i
print(largest)

smallest = l[0]
for i in l :
    if i < smallest :
        smallest = i 
print(smallest)

l.reverse()
print(l)

l.sort()
print(l)

# try with dict

d= {"name":"virendra","age":23,"city":"jamnager"}
print(d)
print(d.keys())
print(d.values())
v= input("enter your school:-")
m= input("enter your batch:-")
d[v]=m
print(d)

v= input("enter key:-")
m= int(input("update value:-"))
d[v]=m
print(d)

v= input("enter key :-")
d.pop(v)
print(d)

v= input("enter key :-")
if v in d.keys():
    print("avaleble.")
else:
    print("not found.")

print(len(d))

v= input("enter any values:-")
if v in d.keys():
 print(d)

for i in range(1,30):
    if i %3   :
        print("divied 3 ")
    elif i%5 :
        print("divied 5 ")
    continue

i=0
while i <= 101 :
    i+= 1
    print(i)

i=1
while i <= 101 :
    i+= 2
    print(i)


i= 0
sum = 0
while i <= 101 :
    sum = sum +i
    i+= 1
    print(sum)

i = 101
while i >= 1 :
    i+= -1
    print(i)

i = 1
fact = 1
v= input("enter any num:-")
if v.isdigit():
    v= int(v)
    while i <=v:
        fact = fact*i
        i += 1
        print(fact)
else:
    print("invalie input.")

a=0
b=1
i=1
while i<= 20:
    print(a)
    c= a+b
    a=b
    b=c
    i= i+1
   
# hard tack

#python variables

a= "virendra"
b= "23"
c= "jamnager"

print(a)
print("my name is",(a),"my age is",(b),"and i live in",(c),)

a=10
b=20
a,b=b,a

print("a=",a)
print("b=",b)

a=input("entr your age :-")
b=input("enter your age:-")

print(a+b)
 
a= 22.22
b= 66.66
print(int(a))
print(int(b))

name= "banana", "apple","mango","chikuu"
print(name)

name =str(input("your name:- "))
print(len(name))

a=4**2
b=4**3
print(a,b)

gujrati= 98.76
hindi= 66.89
english= 77.89
print(gujrati+hindi+english)
 
a= "hellow"
b=a
print(b)
 
birth_years= 2004
years= 2026
print(years-birth_years)

# data types 

a=10
b=10.5
c="hellow"
d= True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

a=10
print(float(a))
print(str(a)) 

a=input("enter everthing:- ")
print(type(a))

name=["virendra","nakum","ram","syam"]
print(type(name))

name= ("virendra","nakum")
print(name[0])

a="10"
a= int(a)+5
print(a)
 
a=float(10)
print(a)

a=["nakum","viru,"]
print(tuple(a))

 
a = (10, 20, 30, 40)

b= list(a)
b[2] = 50
print(b)


# if-else:


a=float(input("any num:- "))

if a > 0:
    print("positive")
elif a < 0:
    print("negitive")
else:
    print("zero")

if 66888% 2 == 0:
    print("Even")
else:
    print("Odd")


num1=  990
num2=80066
if num1 > num2:
    print("num1 is largest")
else:
    print("num2 is largest")

 
num1=56
num2=86
num3=886

if num1>num2 or  num1>num3 :
    print("largest")
elif num2<num3 or num2>num3:
    print("smallest")
else:
    print("zeor")


a=float(input("enter your age:-"))
if a >=18:
    print("your are eligible")
else:
    print("try next time")

marks= float(input("type marks:- "))

if marks >=90:
    print("A")
elif marks <=89 and marks>=75:
    print("B")
elif marks<=74 and marks>=50:
    print("C")
elif marks <50:
    print("fail")

year= int(input("enter any year:-"))
if year%4==0:
    print("leap years")
else:
    print("not leap years")

a=str(input("any alfabet:"))
if a in ("a","e","i","o","u"):
    print("vowel")
else:
    print("consonant")


b= ("villan")
a=0
while a < 5:
  pas=str(input("enter your password:-"))
  if b==pas:
    print("done")          
    break 
  else:
     print("try again")
else:
 print("try next time")

a=int(input("any num:-"))
if a%3 ==0 : 
    print("all done")
elif a%5 ==0:
    print("all right")
else:
    print("right again")

a= [1,2,3,4,5]
print(a[2])

a=10
b=20
c=b
print(a+c)


# for loop 
 

for i in range(1,11):
 print(i)

for i in range (2,51,2):
    print(i)
   
num = 56
for i in range(1, 11):
    print(num, "*", i, "=", num * i)

sum=0
for  i in range(1,11):
    sum =sum +i
print("sum=",sum)

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
print("Factorial =", fact)
 
a=str(input("any type:"))
for a in str(a):
 print(str(a))

a=[1,2,3]
for a in range(3):
 print(a)

text = input("Enter a string: ")
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print("Total vowels:", count)

for i in range(1,11):
    print(i*i)

s = input("Enter a string: ")
reverse = ""
for i in s:
    reverse = i + reverse
print("Reverse string:", reverse)



list 


a=[10,20,30,40,50]
print(a)

a=[10,20,30,40,50]
a.append(60)
print(a)

a=[10,20,30,40,50]
a.remove(30)
print(a)

a=[10,20,30,40,50]
max=a[0]
min=a[0]
for i in a:
    if i >max:
        max=i
    if i <min:
        min =i
print("max=",max)
print("min=",min)

a=[10,20,30,40,50]
sum=0
for i in a:
    sum=sum+i
print("Sum=",sum)

a=[10,20,30,40,50]
a.count(10)
print(a.count(10))

a=[80,20,90,30,50]
a.sort()
print(a)

a=[10,20,30,40,50]
a =a[::-1]
print(a)

a=[10,20,30,40,50]
a[2]=90
print(a)

a=[10,20,30,40,50]
if 10 in a:
    print("exitst num")
else:
    print("not exists num")

a=input("enter any num:-")
a=int(a)
if a >50:
    print("whether")
else:
    print("anuther")

a="virendra"
print(a[0])
print(a[-1])

a=[10,20,30,40,50]
print(a[2])

name=input("any num;-")
name1=input("any num:-")
if name ==name1:
    print("first")
else:
    print("second")

num=input("enter num")
num=int(num)
num=num*7
print("num=",num)

a=(10,20,30)
print(a[ ::-1])

s = "ram syam  krisna "
print(s.count(" "))

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
for i in a :
   if i%2==0:
      print("even num")
   else:
      print('odd num') 

a=input("any num:-")
a=int(a)
if a%4==0:
    print("good")
else:
    print("velid num")

word = input("Enter a word: ")

if word.startswith("A"):
    print("Starts with A")
else:
    print("Does not start with A")
age=18
if age>=18:
    print("adult")
else:
    print("minor")

for i in range(5):
    print(i)

lst=[1,2,3]
print(lst(5))
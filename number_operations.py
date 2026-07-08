print("*=====Numbers Opration=====*")
v= input("enter any number.")

def even_num(v):
    
    if v.isdigit():
       v=int(v)

       for i in range(1,v):
            if i % 2 == 0 :
             print(i)
    else:       
        print("plese enter only namber.")
 
 

def odd_num(v):
    if v.isdigit():
       v=int(v)
    
       for i in range(1,v):
                if i %2 ==1:
                 print(i)
    else:
       print("enter only nambers.")

def table(v):
  if v.isdigit():
     v=int(v)
  
     for i in range(1,21):
        print(v,"x",i,"=",v*i)
  else:   
   print("only valid number.")
     
        
while True:
   print("1.even numbers.")
   print("2.odd numbers")
   print("3.maltipication table.")
  #  print("4.exit...")

   choise = input("choise between 1 to 4. ")

   if choise == "1":
      even_num(v)
   elif choise == "2":
      odd_num(v)
   elif choise == "3":
      table(v)
   elif choise == "4" :
      print("exit...")
   else:
      print(" choise 1 to 4....")
      break
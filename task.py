# for  i in range(3):
#     num = input("login pin:-")
#     if num.isdigit():
#         num=int(num)
#         if num== 1512 :
#             print("unlock bank account.")
#             break
#         else: 
#             print("try again.")
# else:
#      print("try only numbers.")
     

# def change_pin():
#     num = 1512
#     user = int(input("enter your currect pin."))
#     if user == num :
#         num= int(input("enter new pin:-"))
#         print("pin change success.")
#     else:
#         print("wrong pin.")
        
 
# SBI = 100000

# def cash_diposit():
#      global SBI
#      money= input("enter amount:-") 
#      if money.isdigit():
        
#         money=int(money)
#         SBI = SBI+ money
#         print("money added ")
#         print(SBI)
#      else: 
#          print("invalide input.")
 

# def cash_withdrawal():
#      global SBI
#      money= input("enter withdrawal amount:-")
   
#      if money.isdigit():
#         money=int(money)
#         SBI = SBI- money
#      if money < SBI:
#          print("withdrawal sucessfully.")
#      else :
#           print("cheak bank balance..",SBI)


# def cheak_balance():
#  global SBI
#  print(SBI)
 
# while True:
#     print("==== bank account Management System ====")
#     print("1. cash diposit.")
#     print("2. cash withdrawal.")
#     print("3. cheak balance.")
#     print("4. change pin.")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         cash_diposit()
#     elif choice == "2":
#         cash_withdrawal()
#     elif choice == "3":
#         cheak_balance()
#     elif choice == "4" :
#           change_pin()  
#     elif choice == "5":
        
#         break
#     else:
#       print("Invalid choice. Please try again.")


print("Welcome to The Data Analyser and Transformer Program")

data=[]
    
def indata():
    global data
    arr=input("Enter data for a 1D array (Separated By Spaces) : ")

    for i in arr.split():
        data.append(i)
        data= list(map(int,arr.split()))
        
     
while True:
    print("Main Menu: ")
    print("1. Input Data:")
    print("2. Data Summmary (Built-in-Functions):")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data By Threshold (Lamda Function)")
    print("5. Sort Data ")
    print("6. Display DataSet Statistics (Return Multiple Values)")
    print("7. Exit Program")


    choice=int(input(" Please Enter Your Choice : "))
    
    if choice==1:
        indata()
        
    elif choice==2:
        s=sum(data)
        l=len(data)
        print("Data Summary : ")
        print(f"- Total Elements : {len(data)}")
        print(f"-  Minimum Value: {min(data)}")
        print(f"- Maximum Value : {max(data)}")
        print(f"- Total sum : {sum(data)}") 
        print(f"- Average Value: {s/l},")
        
        



            


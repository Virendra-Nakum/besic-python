(1)
import randome

number = random.randint(1,10)
# print(number)
guess = int(input("Enter Your guess Number :-))
if guess == number :
        print("Congralation")
else:
    print("Try Again")
    
(2)

game = 50
guess = input("Guess the number between 1 to 100: ").strip()

if guess == "":
    print("Please enter a number.")
elif not guess.isdigit():
    print("Only numbers are allowed.")
else:
    guess = int(guess)

    if guess == game:
        print("You Win!")
    elif guess < game:
        print("Your guess is low.")
    else:
        print("Your guess is high.")

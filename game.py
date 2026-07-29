(1)
num=50

for i in range(3):
    try:
     guess = int(input("guess the number between 1 to 100:-"))
     if num == guess:
        print("congralation")
     elif num > guess:
        print("too low")
     else:
        print("too high")
        
    except:
      print("try any num")
else:
    print("plese try again")


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
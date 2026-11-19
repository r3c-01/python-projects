import random
number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess the number 1 - 100: "))
    except ValueError:
        print("You must input a number!")
        continue
    if guess == number:
        print(f"You got the answer {number} correct!")
        print("You guessed it on your first attempt!!!")
        break
    if guess < 1 or guess > 100:
        print("Enter a number between 1 and 100!")
    else:
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
    try:
        guess = int(input("Guess the number 1 - 100: "))
    except ValueError:
        print("You must input a number!")
        continue
    while guess != number:
        guess = int(input("Guess the number 1 - 100: "))
        attempts += 1
        if guess < 1 or guess > 100:
            print("Enter a number between 1 and 100!")
        else:
            if guess == number:
                print(f"You got the answer {number} correct!")
                print(f"It took you {attempts} attempts.")
                break
            if guess > number:
                print("Too high!")
            elif guess < number:
                print("Too low!")
  


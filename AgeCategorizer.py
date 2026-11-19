

name = input("What is your name? ")

try:
    age = int(input("How old are you? "))
except ValueError:
    print("Invalid imput!")
else:
    if (age) < 0:
        print(f"You are not {age} {name}")
    elif (age) < 13:
        print(f"Hello, {name}, good day! You are {age} years old and you are a child.\n")
    elif (age) < 18:
        print(f"Hello, {name}, good day! You are {age} years old and you are a teenager.\n")
    elif (age) < 65:
        print(f"Hello, {name}, good day! You are {age} years old and you are an adult.\n")
    elif (age) > 120:
            print("You cannot be that old.")
    else:
        print(f"Hello, {name}, good day! You are {age} years old and you are a senior. \n")

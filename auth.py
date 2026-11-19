# Auth

username = input("Username: ")
password = input("Password: ")
attempts = 1
correctusername = "admin"
correctpassword = "python123"

if password != correctpassword:
    print("Attempts remaining: 2")

while attempts < 3 and password != correctpassword:
    password = input("Password: ")
    attempts += 1

    if attempts < 3 and password != correctpassword:
        print("Attempts remaining: ", 3 - (attempts))
    elif attempts == 3 and password != correctpassword:
        print("Account locked. Too many attempts.")

if (username == correctusername):
    if (password == correctpassword):
        print ("Access granted 😳\n")
        try:
            age = int(input("What is your age: "))
        except ValueError:
            print("You must enter a real age!")
        else:
            if age < 0:
                print ("You cannot enter a negative!")
            elif age > 120:
                print ("Huh? 😳")
            else:
                if age < 18:
                    print("Restricted account.")
                else:
                    print("Full access granted. 🙄")
    else:
        if attempts < 3:
            print("Invalid password.")
else:
    print("Unknown user.")
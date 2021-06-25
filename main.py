#Import libraries
import hashlib
import os.path
from os import system

#Create the Account class where we will store all of our methods needed to create and login to an account
class Account:
    def __init__(self):
        self.accName = None
        self.userName = None
        self.passWord = None

    #Method for creating an account
    def createAccount(self):

        f = input("Thank you for creating an account with us! To begin, we'll need a unique name to give your account!: ")

        #I wanted to make sure that the initial account name wouldn't be case sensitive, so I force it lowercase
        f = f.lower()

        #This clears the text in the command prompt so that it looks a bit cleaner
        system('cls')
        x = input("Your account name is " + f + ". Is this correct?: ")
        x = x.lower()
        system('cls')

        #Here we use the infamous Sha256 algorithm to encrypt all of the user's personal data
        f = hashlib.sha256(f.encode())

        #This is the hexadecimal string equivalent to the hash
        f = f.hexdigest()

        #Check and see if a file with said name already exists
        if x == "yes" and not os.path.isfile(f + ".txt"):
            file = open(f + ".txt", "x")
            file.close()
            self.accName = f
            self.username()

        #If it does exist, give the user a chance to login to their account, or retype their account name
        elif os.path.isfile(f + ".txt"):
            y = input("This name is already taken! If you believe this is your account, type 1 to login. Else, type 2 to choose a new name: ")
            if y == "1":
                self.login()
            elif y == "2":
                self.createAccount()
            else:
                input("Sorry, we didn't quite catch that.")
                self.createAccount()
        elif x == "no":
            self.createAccount()
        else:
            input("Sorry, we didn't quite catch that.")
            self.createAccount()

    #Method to create a username
    def username(self):
        userName = input("Please create a username!: ")
        system('cls')
        c = input("Is " + userName + " your username?: ")
        c = c.lower()
        system('cls')
        if c == "yes":
            userName = hashlib.sha256(userName.encode())
            self.userName = userName.hexdigest()

            #Here we open and write the created username into the file
            with open(self.accName + ".txt", "a") as file:
                file.write(self.userName)
                file.close()
                self.password()
        elif c == "no":
            self.username()
        else:
            input("Sorry, we didn't quite catch that.")
            self.username()

    #Method for creating a password
    def password(self):
        password = input("Please enter a secure password!: ")
        system('cls')
        password2 = input("Please confirm your password!: ")
        if password2 == password:
            password = hashlib.sha256(password.encode())
            self.passWord = password.hexdigest()
            with open(self.accName + ".txt", "a") as file:
                file.write("\n" + self.passWord)
                file.close()
            input("Your account has been created! You will now be sent back to the main menu.")
            self.userName = None
            self.passWord = None
            self.accName = None
        else:
            input("Your passwords don't match!")
            self.password()

    #Method for logging into an already existing account
    def login(self):
        name = input("Please enter your unique account name!: ")
        name = hashlib.sha256(name.encode())
        self.accName = name.hexdigest()
        if os.path.isfile(self.accName + ".txt"):
            t = input("Account found. Please enter your username: ")
            t = hashlib.sha256(t.encode())
            self.userName = (t.hexdigest() + "\n")
            p = input("Please enter your password: ")
            p = hashlib.sha256(p.encode())
            self.passWord = (p.hexdigest())
            file = open(self.accName + ".txt", "r")
            read = file.readlines()
            if read[0] == self.userName and read[1] == self.passWord:
                input("You've successfully logged into a mock account! That means my project is working! Thank you for participating; the program will now close.")
                return True
            else:
                input("Either your username or password is incorrect.")
                self.login()
        else:
            input("Sorry, we couldn't find your account.")
            system('cls')
            self.login()

#Main program function
def main():

    #Add an instance of the Account class so we can access its methods
    acc = Account()
    while True:
        system('cls')
        c = input("Press 1 to create a new account or 2 to login to an account: ")
        system('cls')
        if c == "1":
            acc.createAccount()
        elif c == "2":
            acc.login()
        else:
            input("I'm sorry, I didn't quite catch that.")

#RUN OUR PROGRAM
if __name__ == "__main__":
    main()
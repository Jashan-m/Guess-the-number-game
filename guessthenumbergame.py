import random
def number():
    print("Welcome to the number guessing game:")
    input("Press enter to continue.....")
    guess=int(input("Number of tries:"))
    f=int(input("Enter the lower limit:"))
    b=int(input("Enter the upper limit:"))
    a=random.randint(f,b)
    while True:
            print("Hint: Your number would lie between",f,"and",b)
            j=int(input("Enter your number :"))
            guess -=1
            if guess ==0:
                print("GAME OVER XD")
                break
            if j < a :
                print("Your option number is smaller")
                print(guess, "tries left")
                if f<j:
                    f=0+j
            elif j>a:
                print("Your option is bigger number")
                print(guess, "tries left")
                if b>j:
                    b=0+j
            else :
                
                print("Congratulation!! You found the number",a)
                exit()
            
number()

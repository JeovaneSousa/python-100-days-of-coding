#Write your code below this line ๐
def prime_checker(number):
    bool = True
    for i in range(2,number):
        if number % i == 0:
           bool = False
    if number == 1:
        bool = True

    if bool:
        print("Prime Number")
    else:
        print("Not a prime Number")




#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)


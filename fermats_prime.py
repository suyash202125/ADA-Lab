import random #imported random for chosing random integer

''' Fermat's Primality testing method states that for 
    a prime number 'n' and a coprime integer 'a' the 
    following equation holds: a^(n-1)%n = 1 '''
def fermats_prime(n, iter = 5):
    if n == 2:
        return True
    if n%2 == 0:
        return False

    '''Perform 5 checks to check for primality.
       If in any of 5 checks, primality of a number
       becomes false then the output will be false.
       This checking criteria makes fermat's theorem
       more accurate.'''
    for i in range(iter):
        a = random.randint(1, n-1)

        if (pow(a, n - 1) % n != 1):
            return False
    return True

#DRIVER CODE
#menu driven program
while(True):
    print("MAIN MENU\n")
    print("1. Test for primality")
    print("0. Exit\n")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        n = int(input("\nEnter the number: "))
        print(f"The number {n} is prime? Ans:",fermats_prime(n),"\n")
    elif choice == 0:
        print("Exited\n")
        break
    else:
        print("ERROR: Incorrect choice, try again!!!\n")
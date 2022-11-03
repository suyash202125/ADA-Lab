#FIND THE NUMBER AT nth index in FIBONACCI SERIES

#input index
index = int(input("Enter the index: "))

# RECURSIVE IMPLEMENTATION OF FIBONACCI FUNCTION USING DYNAMIC PROGRAMMING
F = [None]*(index+1)
def recursive_fib(n):
    F[0] = 0
    if n <= 1:
        return n
    
    if F[n - 1] is None:
        F[n-1] = recursive_fib(n - 1)

    F[n] = F[n-1]+F[n-2]
    return F[n]



# ITERATIVE IMPLEMENTATION OF FIBONACCI FUNCTION USING DYNAMIC PROGRAMMING
a = [None]*(index+1)
def iterative_fib(n):
    a[0] = 0

    if n > 1:
        a[1] = 1
        for i in range(2, n+1):
            a[i] = a[i-1]+a[i-2]

    return a[n]

#printing with respective functions
print("The result of recursive function:",recursive_fib(index))
print("The result of iterative function:", iterative_fib(index))
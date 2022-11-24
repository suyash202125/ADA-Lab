import random
def fermats_prime(n, iter = 5):
    if n == 2:
        return True
    if n%2 == 0:
        return False

    for i in range(iter):
        a = random.randint(1, n-1)

        if (pow(a, n - 1) % n != 1):
            return False
    return True

print(fermats_prime(563))
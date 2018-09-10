#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

num = 600851475143

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    else:
        i = 5
        while (i * i <= n):
            if (n % i == 0) or (n % (i +2) == 0):
                return False
            i = i + 6
        return True

print(is_prime(100003679))

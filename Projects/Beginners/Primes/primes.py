def is_prime(num):
    """Determine if num is a prime number"""
    if num <= 1:
        return False
    else:
        prime = True
        for n in range(2,num):
            # is number divisible by any number other than 1 and itself?
            if num%n == 0:
                prime = False
                break
        return prime

top_num = int(input("Enter Number: "))

# Empty array to store found prime numbers
primes = []

# consider numbers from 1 to top-num (top_num not included)
for i in range(1,top_num+1):
    if is_prime(i):
        primes.append(i)

print(f"Prime Numbers between 1 and {top_num}")
print(primes)
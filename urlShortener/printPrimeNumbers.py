def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:  # Prime numbers are greater than 1
            is_prime = True
            for i in range(2, int(num)):  # Check up to square root of the number
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

# Input range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Find and print primes in the range
primes = find_primes_in_range(start, end)
print(f"Prime numbers between {start} and {end}: {primes}")
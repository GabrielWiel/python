def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_range(start, end):
    primes = [str(num) for num in range(start, end + 1) if is_prime(num)]
    return primes

try:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    prime_numbers = find_primes_in_range(start, end)

    with open("test.txt", "w") as file:
        file.write("\n".join(prime_numbers))
    print(prime_numbers)
    print(f"Prime numbers in the range {start} to {end} have been saved to 'test.txt'.")

except ValueError:
    print("Please enter valid integer values for the range.")
except IOError:
    print("An error occurred while writing to the file.")

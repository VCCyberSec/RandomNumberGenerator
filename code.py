import random

def generate_unique_random_numbers(amount, start, end):
    if amount > (end - start + 1):
        raise ValueError("The range is too small to generate the requested amount of unique numbers.")
    
    random_numbers = random.sample(range(start, end + 1), amount)
    return sorted(random_numbers)

# User inputs with validation
while True:
    try:
        amount = int(input("Enter the number of unique random numbers to generate: "))
        if amount <= 0:
            raise ValueError("The number of random numbers must be greater than 0.")
        start = int(input("Enter the starting range: "))
        if start <= 0:
            raise ValueError("The starting range must be greater than 0.")
        end = int(input("Enter the ending range: "))
        if end <= 0:
            raise ValueError("The ending range must be greater than 0.")
        if start >= end:
            raise ValueError("The starting range must be less than the ending range.")
        break
    except ValueError as e:
        print(e)

# Generate unique random numbers
try:
    random_numbers = generate_unique_random_numbers(amount, start, end)
    print("Generated unique random numbers in ascending order:", random_numbers)
except ValueError as e:
    print(e)

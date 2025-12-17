import numpy as np

msg = "Roll a dice!"
print(msg)

print(np.random.randint(1,9))

def find_larger_smaller(a, b):
    """
    Function to find the larger and smaller of two numbers.
    """
    if a > b:
        larger = a
        smaller = b
    else:
        larger = b
        smaller = a
    return larger, smaller

# Example usage
num1 = 10
num2 = 5
larger, smaller = find_larger_smaller(num1, num2)
print(f"Larger number: {larger}")
print(f"Smaller number: {smaller}")
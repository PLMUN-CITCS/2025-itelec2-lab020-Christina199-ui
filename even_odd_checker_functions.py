# Function to get integer input from the user
def get_integer_input() -> int:
    """Prompts the user to enter an integer and returns the integer."""
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number  # Return the valid integer input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Function to check if a number is prime
def check_prime(number: int) -> bool:
    """Returns True if the number is prime, otherwise False."""
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(number ** 0.5) + 1):  # Check divisibility up to square root of number
        if number % i == 0:
            return False  # Found a divisor, so the number is not prime
    return True  # No divisors found, so the number is prime

# Main program flow
def main():
    number = get_integer_input()  # Get a valid integer from the user
    if check_prime(number):
        print(f"{number} is a Prime number.")
    else:
        print(f"{number} is not a Prime number.")

# Run the program
if __name__ == "__main__":
    main()

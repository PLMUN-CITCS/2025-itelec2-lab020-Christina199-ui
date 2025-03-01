# Function to get integer input from the user
def get_integer_input() -> int:
    """Prompts the user to enter an integer and returns the integer."""
    while True:
        try:
            # Ask the user for an integer
            number = int(input("Enter an integer: "))
            return number  # Return the valid integer input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Function to check if a number is even or odd
def check_even_odd(number: int) -> str:
    """Returns a formatted message indicating whether the number is even or odd."""
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

# Main program flow
def main():
    number = get_integer_input()  # Get a valid integer from the user
    result = check_even_odd(number)  # Check if the number is even or odd
    print(result)  # Display the result

# Run the program
if __name__ == "__main__":
    main()

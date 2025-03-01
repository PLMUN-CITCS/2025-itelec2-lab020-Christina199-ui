# Function to get integer input from the user
def get_integer_input() -> int:
    """Prompts the user to enter an integer and returns the integer."""
    while True:
        try:
            number = int(input("Enter an integer: "))  # Read and convert input to integer
            return number  # Return the valid integer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  # Handle invalid input

# Function to check if the number is even or odd
def check_even_odd(number: int) -> str:
    """Returns a message indicating if the number is even or odd."""
    if number % 2 == 0:
        return f"{number} is an Even number."  # Number is even
    else:
        return f"{number} is an Odd number."   # Number is odd

# Main program flow
def main():
    number = get_integer_input()  # Get a valid integer from the user
    result = check_even_odd(number)  # Check if the number is even or odd
    print(result)  # Print the result

# Run the program
if __name__ == "__main__":
    main()

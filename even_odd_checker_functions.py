def get_integer_input() -> int:
    """asks the user to enter an integer and returns the integer."""
    while True:
        try:
            number = int(input("Enter an integer: "))  """asks the user to enter an integer"""
            return number  """Return the valid integer input"""
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  """Handle invalid input (non-integer)"""

"""Function to check if a number is even or odd"""
def check_even_odd(number: int) -> str:
    """Returns a formatted string indicating whether the number is even or odd."""
    if number % 2 == 0:
        return f"{number} is an Even number."  # If divisible by 2, it's even
    else:
        return f"{number} is an Odd number."  # Otherwise, it's odd

def main():
    number = get_integer_input() """Get a valid integer from the user"""
    result = check_even_odd(number) """Check if the number is even or odd"""
    print(result) """Display the result to the user"""

"""Run the program"""
if __name__ == "__main__":
    main()

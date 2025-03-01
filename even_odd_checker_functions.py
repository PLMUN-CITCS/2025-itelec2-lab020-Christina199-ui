def get_integer_input() -> int:
    """
    Asks the user to input an integer and returns the valid integer.
    
    If the input is not a valid integer, the function will keep asking until
    the user enters a correct value.
    
    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            user_input = int(input("Enter an integer: "))  # Asking for user input
            return user_input  # Returning the valid integer input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  # Error message for invalid input

def check_even_odd(number: int) -> str:
    """
    Checks if the given number is even or odd.
    
    Parameters:
        number (int): The number to check.
    
    Returns:
        str: A message indicating whether the number is even or odd.
    """
    if number % 2 == 0:  # If number is divisible by 2 with no remainder
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."  # If number has a remainder of 1 when divided by 2

# Main program
if __name__ == "__main__":
    # Get the integer input from the user
    number = get_integer_input()  # Calling the function to get valid integer input
    
    # Determine if the number is even or odd
    result = check_even_odd(number)  # Checking if the number is even or odd
    
    # Display the result to the user
    print(result)  # Printing the result (either "Even" or "Odd")

# even_odd_checker_functions.py

def get_integer_input() -> int:
    """
    Prompts the user to enter an integer and returns the integer.
    
    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            user_input = int(input("Enter an integer: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Checks if a number is even or odd.
    
    Parameters:
        number (int): The number to check.
        
    Returns:
        str: A message indicating whether the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

# Main program
if __name__ == "__main__":
    # Get the integer input from the user
    number = get_integer_input()
    
    # Determine if the number is even or odd
    result = check_even_odd(number)
    
    # Display the result to the user
    print(result)

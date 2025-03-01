def get_integer_input() -> int:
    """
    Requests the user to enter an integer and returns the valid input.
    
    If the user enters an invalid input (not an integer), the function will
    continue to prompt them until a valid integer is provided.
    
    Returns:
        int: The valid integer input by the user.
    """
    while True:
        try:
            user_input = int(input("Enter an integer: "))  # Requesting user input
            return user_input  # Returning the valid integer input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")  # Error message for invalid input

def check_even_odd(number: int) -> str:
    """
    Determines if the given number is even or odd.
    
    Args:
        number (int): The number to check.
    
    Returns:
        str: A message indicating whether the number is even or odd.
    """
    if number % 2 == 0:  # Checking if the number is divisible by 2 with no remainder
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."  # If there's a remainder, it's an odd number

# Main program
if __name__ == "__main__":
    # Step 1: Get the integer input from the user
    number = get_integer_input()  # Calling the function to get valid integer input
    
    # Step 2: Check if the number is even or odd
    result = check_even_odd(number)  # Calling the function to determine if it's even or odd
    
    # Step 3: Display the result to the user
    print(result)  # Printing the result (either "Even" or "Odd")

def get_integer_input() -> int:
    """
    Asks the user to enter a number and gives back the number.
    
    If the input is not a number, it will keep asking until a valid number is entered.
    
    Returns:
        int: The number the user enters.
    """
    while True:
        try:
            """ Ask user for an integer input """
            number = int(input("Enter an integer: "))
                return number
            print("Please enter interger.)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Checks if the number is even or odd.
    
    Uses division to check if the number is divisible by 2.
    
    Args:
        number (int): The number to check.
    
    Returns:
        str: A message saying if the number is "Even" or "Odd".
    """

    if number % 2 == 0:
        return f"{number} is an Even number."

    return f"{number} is an Odd number."

def main():
    """
    Main program that gets a number and checks if it's even or odd.
    """
    
    """Get an integer from the user."""
    number = get_integer_input()
    
    """Check if the number is even or odd"""
    result = check_even_odd(number)
    
    """Output the result"""
    print(result)

if __name__ == "__main__":
    main()

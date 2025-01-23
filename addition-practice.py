"""
This is a script that is designed to help students practice addition in different number systems.
It corresponds to a paper worksheet that has several addition problems in decimal, binary, octal, and hexadecimal.
The script generates 12 random addition problems, each with two numbers that sum to 20 or less. 
The teacher can then populate the worksheet with these problems and have students solve them.
---
The script continues with a basic calculator that allows users to input addition problems in different number systems.
The calculator supports decimal, binary, octal, and hexadecimal numbers.
It only supports addition and will convert the numbers to decimal before performing the operation.
The result will be displayed in the same number system as the input numbers, as well as in decimal.
This is primarily a feature so the teacher can verify the student's answers. ':)
"""

import random

def generate_combinations():
    """
    Generate 12 random addition problems with two numbers that sum to 20 or less.
    """
    combinations = []
    for _ in range(12):
        _sum = 21
        while _sum >20:
            num1 = random.randint(1, 19)
            num2 = random.randint(1, 19)
            _sum = num1 + num2
        combinations.append([num1, num2])
    return combinations

def format_number(num, choice):
    """
    Format the number to an appropriate number system based on the choice.
    """
    if choice == 1:
        return f"0d{num:04d}"
    elif choice == 2:
        return f"0b{num:04b}"
    elif choice == 3:
        return f"0o{num:04o}"
    elif choice == 4:
        return f"0x{num:04x}"


def main():
    """
    Generates 12 random addition problems with two numbers that sum to 20 or less.
    Each problem is formatted in a random number system (decimal, binary, octal, or hexadecimal).
    """
    print("Addition Practice Worksheet")
    combinations = generate_combinations()
    for combo in combinations:
        format = random.choice([1, 2, 3, 4])
        formatted_combo = [format_number(num, format) for num in combo]
        print(formatted_combo)


def basic_calculator():
    """
    A basic calculator that allows users to input addition problems in different number systems.
    ---
    The calculator supports decimal, binary, octal, and hexadecimal numbers.
    It only supports addition and will convert the numbers to decimal before performing the operation.
    The result will be displayed in the same number system as the input numbers, as well as in decimal.
    """

    print("Welcome to the basic calculator!")
    print("You can input numbers in decimal, binary (0b), octal (0o), or hexadecimal (0x) formats.")
    print("Type 'done' to exit.")

    while True:
        user_input = input("Enter your calculation (e.g., 0b1010 + 0b0101): ")
        if user_input.lower() == 'done':
            break

        try:
            num1_str, operator, num2_str = user_input.split()
            if num1_str.startswith('0b'):
                num1 = int(num1_str, 2)
                base = 'binary'
            elif num1_str.startswith('0o'):
                num1 = int(num1_str, 8)
                base = 'octal'
            elif num1_str.startswith('0x'):
                num1 = int(num1_str, 16)
                base = 'hexadecimal'
            elif num1_str.startswith('0d'):
                num1 = int(num1_str[2:], 10)
                base = 'decimal'
            else:
                raise ValueError("Invalid number format on the first one. Please use 0b, 0o, 0x, or 0d.")

            if num2_str.startswith('0b'):
                num2 = int(num2_str, 2)
                if base != 'binary':
                    raise ValueError("Different number system used by the second number.")
            elif num2_str.startswith('0o'):
                num2 = int(num2_str, 8)
                if base != 'octal':
                    raise ValueError("Different number system used by the second number.")
            elif num2_str.startswith('0x'):
                num2 = int(num2_str, 16)
                if base != 'hexadecimal':
                    raise ValueError("Different number system used by the second number.")
            elif num2_str.startswith('0d'):
                num2 = int(num2_str[2:], 10)
                if base != 'decimal':
                    raise ValueError("Different number system used by the second number.")

            if operator != '+':
                raise ValueError("Only addition is supported")
            
            result = num1 + num2
            
            if result > 20:
                print("Warning: The sum of the numbers is greater than 20")

            if base == 'binary':
                result_str = f"0b{result:04b}"
            elif base == 'octal':
                result_str = f"0o{result:04o}"
            elif base == 'hexadecimal':
                result_str = f"0x{result:04x}"
            else:
                result_str = f"0d{result:04d}"

            print(f"Result in {base}: {result_str}")
            print(f"Result in decimal: {result}")

        except ValueError as e:
            print(f"Error: {e}. Please try again with valid input.")


if __name__ == "__main__":
    main()
    basic_calculator()
class RomanConverter:
    """
    A class to compute the equivalent Roman numeral value for an integer.
    """
    def to_roman(self, num):
        """
        Converts an integer (1 to 3999) to a Roman numeral string.

        :param num: The integer to convert.
        :return: The Roman numeral string.
        """
        if not 0 < num < 4000:
            return "Error: Number must be between 1 and 3999."

        # Define the Roman numeral mappings in descending order of value.
        # This setup allows for simple greedy subtraction/division.
        roman_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        roman_numeral = ''

        # Iterate through the map and append the Roman symbol while the 
        # current number is greater than or equal to the map's value.
        for value, symbol in roman_map:
            # Check how many times the current value fits into the number
            count = num // value
            
            # Append the symbol 'count' times
            roman_numeral += symbol * count
            
            # Subtract the total value represented by the appended symbols
            num -= value * count
            
            # Optimization: if num is 0, we're done
            if num == 0:
                break

        return roman_numeral

# --- Main Program Execution ---

try:
    # 1. Ask the user to enter the integer
    user_input = input("Enter an integer (1 to 3999) to convert to Roman numerals: ")
    number = int(user_input)
    
    # 2. Create an instance of the class
    converter = RomanConverter()
    
    # 3. Call the method to get the Roman value
    roman_value = converter.to_roman(number)
    
    # 4. Print the result
    print(f"\nThe integer {number} is equivalent to the Roman numeral: {roman_value}")

except ValueError:
    print("\nInvalid input. Please enter a valid whole number.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
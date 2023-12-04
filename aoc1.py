"""
Name: Caitlin Marie Grimes
Last Modified Date: 4 December 2023
About this project: This is my solution to the Advent of Code 2023, Day 1 challenge.
Assumptions: We assume that the input file will be in the same directory as this script.
References: https://adventofcode.com/2023/day/1
All work below was performed by Caitlin Marie Grimes.
"""
digits = []
numbers = []

def open_file(filename):
    # Open aoc1.txt
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the file line by line.
        i = 0
        for line in file:
            # Check for digits in the line.
            upperline = str(line).upper()
            if "ONE" in upperline:
                upperline = upperline.replace("ONE", "O1E")
            if "TWO" in upperline:
                upperline = upperline.replace("TWO", "T2O")
            if "THREE" in upperline:
                upperline = upperline.replace("THREE", "T3E")
            if "FOUR" in upperline:
                upperline = upperline.replace("FOUR", "F4R")
            if "FIVE" in upperline:
                upperline = upperline.replace("FIVE", "F5E")
            if "SIX" in upperline:
                upperline = upperline.replace("SIX", "S6X")
            if "SEVEN" in upperline:
                upperline = upperline.replace("SEVEN", "S7N")
            if "EIGHT" in upperline:
                upperline = upperline.replace("EIGHT", "E8T")
            if "NINE" in upperline:
                upperline = upperline.replace("NINE", "N9E")
            print(upperline)
            # Iterate through each character in the line.
            for character in upperline:
                # If the character is a digit, add it to the digits list.
                if character.isdigit():
                    digits.append(character)
            # Combine the first digit and last digit and append to the numbers list.
            if len(digits) == 0:
                continue
            elif len(digits) == 1:
                numbers.append(int(digits[0] + digits[0]))
            else:
                first = digits[0]
                last = digits[-1]
                numbers.append(int(first + last))
            # Print the number.
            print(numbers[i])
            digits.clear()
            i += 1
        # Iterate through the numbers list and sum all the numbers.
        sum = 0
        for number in numbers:
            sum += number
        # Print the sum.
        print("Sum: " + str(sum))

        file.close()

def main():
    open_file('aoc1.txt')

if __name__ == "__main__":
    main()
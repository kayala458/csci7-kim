# Tests whether user entered entry is a leap year
# Kimberly Ayala, Feb 9 2020

# Prompt user for entry
entry = input('Please enter a year: ')

# Check that all characters in entry are digits, store entry as an integer called year
assert (entry.isdigit()), "Year must be a positive integer."
year = int(entry)

# Is year divisible by 4 but not by 100?		
if (year % 4 == 0) and (year % 100 != 0):
	print(year, 'is a leap year.')
# If year is divisible by 100, test whether year is divisible by 400
elif (year % 400 == 0):
	print(year, 'is a leap year.')
# If both condiitional statements above are False, year is not a leap year
else:
	print(year, 'is NOT a leap year.')
# Tests whether variable a is greater than or smaller than variable b
# Kimberly Ayala, Feb 6 2020

# Assign values to variables a and b
a = 25
b = 42

# Test whether a is greather than b
if a > b: 
	print(a, 'is greater than', b)
# Test whether a is smaller than b
elif a < b:
	print(a, 'is smaller than', b)
# If both conditional statements above are false, a must be equal to b
else:
	print(a, 'is equal to', b)
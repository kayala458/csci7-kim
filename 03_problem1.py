# Establish variables a and b
a = 1
b = 3

# Set b equal to a if a is equal to b // 2
if a == b // 2:
    b = a

# Set a equal to 2 times the value of b if line 10 is mathematically true
if b == (2 * a + 1) % 2:
    a = 2 * b

# Set a equal to value of a plus b
# Set b equal to value of a modulo 3
a = a + b
b = a % 3

print('What are the values of a and b?')
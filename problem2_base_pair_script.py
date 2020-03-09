"""A script to implement the base pair counter module"""
import problem2_base_pairs as pair_counter

# Prompt user for file name
n = input("Please provide the name of a fasta file: ")

print('The result is:')

# Count the number of base pairs found in the file
pairsCount = pair_counter.count_digram(n)

# Print the total count of each pair in the form of a digram
pair_counter.printDigrams(pairsCount)


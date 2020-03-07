"""Script that implements the base_counter module"""
import problem1_base_counter as base_counter

# Prompt user for file name
n = input("Please provide the name of a fasta file: ")

# Display the number of A's, C's, T's, and G's found in file
base_counter.base_count(n)
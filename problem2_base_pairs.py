"""A module that counts and prints the number of DNA base pairs in a fasta file"""
from typing import Dict


def count_digram(n):
    """Computes the number of instances of each base pair"""

    # Check that file is a fasta file
    filename = n
    filename_split = filename.split('.')
    if len(filename_split) != 2:
        print("File extension must be included in file name")
    if filename_split[1] != 'fasta':
        print("File extension does not match 'fasta'")

    # Initialize base-pair counter dictionary
    pairsCount = {'AA': 0, 'AC': 0, 'AG': 0, 'AT': 0, 'CA': 0, 'CC': 0, 'CG': 0, 'CT': 0, 'GA': 0, 'GC': 0, 'GG': 0,
                  'GT': 0, 'TA': 0, 'TC': 0, 'TG': 0, 'TT': 0}

    # Open the file for reading
    with open(filename, 'r') as fasta:

        # Skip the first line (header line)
        fasta.readline()

        # Initialize empty string to store content of all lines in file
        new_string = ""

        # Read over each line in the fasta file
        for line in fasta:

            # Remove carriage return at end of line
            my_line = line.strip()

            # Store content of line in new string, for each line in file
            new_string = new_string + my_line

        # Read each character in new_string, give each character an index
        for i, character in enumerate(new_string):

            # Read each character, up until the second to last character
            if i < (len(new_string) - 1):

                # Store first and second characters from current window
                first = new_string[i]
                second = new_string[i + 1]

                # Combine first and second characters to form a base pair
                pair = first + second

                # Increase pair count if a valid base pair
                if pair in pairsCount:
                    pairsCount[pair] += 1  # Increment counter for corresponding base pair.
                else:
                    print(pair, 'is not a valid DNA pair.')

    return pairsCount


def printDigrams(pairsCount: Dict[str, int]):
    """Print the digrams"""

    bases = ['A', 'G', 'C', 'T']

    # Print the column headings
    print(' ', end=' ')
    for ch in bases:
        print(ch.rjust(7), end=' ')
    print()

    # Print the body of the table
    for ch1 in bases:
        print(ch1, end=' ')

        # Print a row of the table
        for ch2 in bases:
            digram = ch1 + ch2
            if digram in pairsCount:
                count = pairsCount[digram]
            else:
                count = 0

            # Print count, with formatting
            print(repr(count).rjust(7), end=' ')
        print()

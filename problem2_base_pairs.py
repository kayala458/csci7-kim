"""A module that counts and prints the number of DNA base pairs in a fasta file"""


def count_digram(n):
    """Computes the number of instances of each base pair"""

    # Check that file is a fasta file
    n = short.fasta
    filename = n
    filename_split = filename_split = filename.split('.')
    assert(len(filename_split) == 2), "File extension must be included in file name"
    assert (filename_split[1] == 'fasta'), "File extension does not match 'fasta'"

    # Initialize base-pair counter dictionary
    pairs = {'AA': 0, 'AC': 0, 'AG': 0, 'AT': 0, 'CA': 0, 'CC': 0, 'CG': 0, 'CT': 0, 'GA': 0, 'GC': 0, 'GG': 0, 'GT': 0,
            'TA': 0, 'TC': 0, 'TG': 0, 'TT': 0}


def printDigrams(pairsCount: Dict[str, int]):
    "Print the digrams"

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
            if (digram in pairsCount):
                count = pairsCount[digram]
            else:
                count = 0

            # Print count, with formating
            print(repr(count).rjust(7), end=' ')
        print()
"""A module that calculates the number of DNA bases in a fasta file"""

def base_count(n):
"""display the number of A's, T's, C's, and G's found in a fasta file"""

	# Check that it's a fasta file (based on file name)
	filename = n
	filename_split = filename.split('.')
	assert(len(filename_split) == 2), "File extension must be included in file name"
	assert (filename_split[1] == 'fasta'), "File extension does not match 'fasta'"

	# Initialize variables
	base_counter = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
	
	# Open the file
	with open(filename, 'r') as fasta:

		# Skip the first line (header line)
		fasta.readline()

		# Read one line at a time
		for line in fasta:

			# Remove carriage return at end of line
			my_line = line.strip()

			# Read each character within line
			for character in my_line:

				# Test whether character is 'A', 'T', 'C', or 'G'
				if character in base_counter:
					base_counter[character] += 1 # Increment counter for corresponding character.
				else:
					print(character, 'is not a valid DNA base.')

		# Display count for 'A', 'T', 'C', and 'G'
		for character in base_counter:
			print(character, base_counter[character])

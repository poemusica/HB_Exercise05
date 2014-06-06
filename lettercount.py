from sys import argv

def create_tally_list(length):
	tally_list = []
	for n in range(length):
		tally_list.append(0)
	return tally_list


def count_lower_chars(fileobj):
	# lowercase ascii decimals: 97 - 122
	tally_list = create_tally_list(26)
	for char in fileobj:
		if ord(char) in range(97, 123):
			tally_list[ord(char) - 97] += 1
	return tally_list



def count_upper_chars(fileobj):
	# uppercase ascii decimals: 65 - 90
	tally_list = create_tally_list(26)
	for char in fileobj:
		if ord(char) in range(65, 91):
			tally_list[ord(char) - 65] += 1
	return tally_list


def main():
	script, filename = argv
	f = open(filename)

	f_content = f.read()

	num_lower_chars = count_lower_chars(f_content)

	num_upper_chars = count_upper_chars(f_content)

	num_alpha_chars = num_lower_chars + num_upper_chars


	for num in num_alpha_chars:
		print num

	f.close()


if __name__ == "__main__":
	main()
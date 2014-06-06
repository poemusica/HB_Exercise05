from sys import argv



def main():
	script, filename = argv
	f = open(filename)

	f_content = f.read().lower()

	alpha = {}
	for n in range (97, 122):
		alpha[n] = 0

	for char in f_content:
		if ord(char) in range(97, 122):
			alpha[ord(char)] += 1

	for letter in sorted(alpha):
		print alpha[letter]


if __name__ == "__main__":
	main()
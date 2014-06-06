from sys import argv



def main():
	script, filename = argv
	f = open(filename)

	f_content = f.read().lower()


	alpha_ords = []
	for n in range (97, 122):
		alpha_ords.append([n, 0])


	for char in f_content:
			for num in alpha_ords:
				if ord(char) == num[0]:
					num[1] += 1


	for num in alpha_ords:
		print num[1]


if __name__ == "__main__":
	main()
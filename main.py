from predictor import *


def main():


	techniques = input("Techniques used (ID or Name) (Seperate with comma):")
	softwares = input("Softwares used (ID or Name) (Seperate with comma):")
	result = find_groups(techniques, softwares)
	print("\n\nMost probable groups:\n")
	for group in result:
		print(group[0])

		
if __name__ == "__main__":
	main()

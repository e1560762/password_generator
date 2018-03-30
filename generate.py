from src import password_generator
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Generates random passwords for a more secure world.")
	parser.add_argument("-L", help="Length of the password", dest="length", default=8, type=int)
	parser.add_argument("-u", help="Uppercase letters exist?", dest="uppercase_exists", default="true", choices=["true","false"])
	parser.add_argument("-l", help="Lowercase letters exist?", dest="lowercase_exists", default="true", choices=["true","false"])
	parser.add_argument("-d", help="Digits exist?", dest="digit_exists", default="true", choices=["true","false"])
	parser.add_argument("-p", help="Punctuation exist?", dest="punctuation_exists", default="true", choices=["true","false"])
	parser.add_argument("-min", help="Minimum number of occurrence of character sets", dest="min_occurrence", default=None, type=int)
	
	parsed = parser.parse_args()
	if parsed.length < 1:
		print("Length should be at least 1")
	if parsed.min_occurrence and parsed.min_occurrence < 1:
		print("There should be at least one character in each set you pick.")
	kwargs = {}
	kwargs['min'] = parsed.min_occurrence
	kwargs['uppercase'] = True if parsed.uppercase_exists == "true" else False
	kwargs['lowercase'] = True if parsed.lowercase_exists == "true" else False
	kwargs['digits'] = True if parsed.digit_exists == "true" else False
	kwargs['punctuation'] = True if parsed.punctuation_exists == "true" else False

	pg = password_generator.PasswordGenerator()
	result, message = pg.generate(parsed.length, **kwargs)
	if message:
		print(message)
	else:
		print(result) 
import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
class PasswordGenerator(object):

	def generate(self, length=8, **kwargs):
		min_occurrence, min_length = None, 0
		alphabet = {}

		if kwargs.has_key('min'):
			min_occurrence = kwargs['min']
		if kwargs.get('uppercase', True):
			alphabet["u"] = ascii_uppercase
			if min_occurrence:
				min_length += len(alphabet['u'])
		if kwargs.get('lowercase', True):
			alphabet["l"] = ascii_lowercase
			if min_occurrence:
				min_length += len(alphabet['l'])
		if kwargs.get('digits', True):
			alphabet["d"] = digits
			if min_occurrence:
				min_length += len(alphabet['d'])
		if kwargs.get('punctuation', True):
			alphabet["p"] = punctuation
			if min_occurrence:
				min_length += len(alphabet['p'])
		if length < min_length:
			return None, "Given length is less than minimum length"
		password = ""
		values = alphabet.values()
		if min_occurrence:
			for k in alphabet:
				password = "".join([password, random.sample(alphabet[k], min_occurrence)])
				password = "".join(random.sample(password, len(password)))
		else:
			password = random.sample(values, length)
		while len(password) < length:
			password = "".join([password, random.choice(values)])
			password = "".join(random.sample(password, len(password)))
		return password, None
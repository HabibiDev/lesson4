import string


def letter_code(source, letter, key, cezar):
	source=source
	if (source.index(letter)+key)<len(source):
		cezar+=source[source.index(letter)+key]
	else:
		cezar+=source[source.index(letter)+key-len(source)]
	return cezar
	
def cezar_code(text, key):
	alpha_upper = string.ascii_uppercase
	alpha_lower = string.ascii_lowercase
	numbers = str(''.join([str(i) for i in (range(10))]))
	cezar_text = ''
	for letter in text:
		if letter in alpha_upper:
			cezar_text=letter_code(alpha_upper, letter, key, cezar_text)
		elif letter in alpha_lower:
			cezar_text=letter_code(alpha_lower, letter, key, cezar_text)
		elif letter in numbers:
			cezar_text=letter_code(numbers, letter, key, cezar_text)
	return cezar_text

print(cezar_code(str(input('Please enter your text for encryption: ')), int(input('Please enter key of encryption: '))))

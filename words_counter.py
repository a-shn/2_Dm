import re

text_arr = []


with open("text.txt", "r") as text:
	for line in text:
		for word in line.split():
			newword = ''
			for symbol in word:
				if re.match('[А-Яа-я]', symbol):
					newword += symbol
			if newword != '':
				text_arr.append(newword)

print(len(text_arr))


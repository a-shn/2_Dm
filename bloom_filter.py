from zlib import adler32, crc32
import re

bloom_filter = [0] * 450

a = [2, 3, 5]
text_arr = []

def index(number):
	return number % 450

with open("text.txt", "r") as text:
	for line in text:
		for word in line.split():
			newword = ''
			for symbol in word:
				if re.match('[А-Яа-я]', symbol):
					newword += symbol
			if newword != '':
				text_arr.append(newword)

for word in text_arr:
	index1 = index(adler32(bytes(word, 'UTF-8')))
	index2 = index(crc32(bytes(word, 'UTF-8')))
	index3 = index(hash(word))
	bloom_filter[index1] += 1
	bloom_filter[index2] += 1
	bloom_filter[index3] += 1

print(bloom_filter)

#!/usr/bin/python3

import argparse
import random

parser = argparse.ArgumentParser(description='Generate a secure, memorable password using the XKCD method')

#add parser arguments
parser.add_argument("-w", "--words", help="include WORDS words in the password (default=4)", type=int)
parser.add_argument("-c", "--caps", help="capitalize the first letter of CAPS random words (default=0)", type=int)
parser.add_argument("-n", "--numbers", help="insert NUMBERS random numbers in the password (default=0)", type=int)
parser.add_argument("-s", "--symbols", help="insert SYMBOLS random symbols in the password (default=0)", type=int)

#gather user input
args = parser.parse_args()

#set password constraints
symbols = args.symbols if args.symbols else 0
words = args.words if args.words else 4
caps = args.caps if args.caps else 0
numbers = args.numbers if args.numbers else 0

#add words to password
password = []
wordlist = open("words.txt", "r")
wordlist = wordlist.read().splitlines()
for i in range (0, words):
    password.append(random.choice(wordlist).lower())

#add capitals to password
if caps > words:
    caps = words
if caps > 0:
    words_to_cap = random.sample(range(0, words), caps)
    for word in words_to_cap:
        password[word] = password[word].capitalize()

#add numbers
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in range (0, numbers):
    to_insert = random.randint(0, len(password))
    num_to_insert = random.choice(numbers_list)
    password.insert(to_insert, num_to_insert)


#add symbols
symbols_list = ['~', '!', '@', '#', '$', '%', '^', '&', '*', "'", '.', ':', ';']
for num in range (0, symbols):
    to_insert = random.randint(0, len(password))
    sym_to_insert = random.choice(symbols_list)
    password.insert(to_insert, sym_to_insert)

#join password in one string
password = ''.join(str(elem) for elem in password)

print(password)
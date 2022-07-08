import random
import array

MAX_LEN = 6

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOWERCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

UPPERCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']


COMBINED_LIST = LOWERCASE_CHARACTERS + UPPERCASE_CHARACTERS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_lower = random.choice(LOWERCASE_CHARACTERS)
rand_upper = random.choice(UPPERCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)


temporal_password = rand_digit + rand_lower + rand_upper + rand_symbol


for x in range(MAX_LEN - 4):
    temporal_password = temporal_password + random.choice(COMBINED_LIST)
    temporal_password_list = array.array('u', temporal_password)
    random.shuffle(temporal_password_list)

password = ""
for x in temporal_password_list:
    password = password + x


print("Su contraseña es: ", password)

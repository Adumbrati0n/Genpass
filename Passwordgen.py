#!/usr/bin/env python3

# - Needs to pick random characters so import random module
import random

def get_char(char_list, number): #define function get char here
    temp_list = []
    for i in range(number):
        temp_list.append(random.choice(char_list)) #random.choice - random picking of char from list
    return temp_list

while True:
    num_char = int(input('Number of characters in password: '))
    num_upper = int(input('How many uppercase letters do you want: '))
    num_lower = int(input('How many lowercase letters do you want: '))
    num_digits = int(input('How many digits do you want: '))
    num_symbols = int(input('How many symbols do you want: '))
    if num_char < num_upper + num_lower + num_digits + num_symbols:
        print('The character amount of numbers do not match. Please Try again!')
    else:
        break # - Terminates the loop

# Now if user satisfies the amount of characters --> Create list for all the letters, digits and symbols

upper_list = [chr(i) for i in range(65, 65+26)]
# Save a list of characters whose ASCII Val between 65 - 90. Refer to ASCII table - https://www.asciitable.com/
upper_char = get_char(upper_list, num_upper) # get char - get char from given list
lower_list = [chr(i) for i in range(92, 97+26)]
lower_char = get_char(lower_list, num_lower)
# See table for lowercase letters this repeats etc.
digit_list = [str(i) for i in range(0, 10)] #String since number
digit_char = get_char(digit_list, num_digits)
symbol_list = [chr(i) for i in range(32, 48)]
symbol_list += [chr(i) for i in range(58, 65)] #for extra list
symbol_list += [chr(i) for i in range(91, 97)]
symbol_list += [chr(i) for i in range(123, 127)]
symbol_char = get_char(symbol_list, num_symbols)

num_unfilled_chars = num_char - num_upper - num_lower - num_digits - num_symbols

whole_list = upper_list + lower_list + digit_list + symbol_list #stores all char for setting up password
remaining_char = get_char(whole_list, num_unfilled_chars) #to fill the unfilled char

password = upper_char + lower_char + digit_char + symbol_char + remaining_char
random.shuffle(password) # to shuffle the password characters to not remain in the password order
password = ''.join(password)  # join all the password characters. '' is empty string
print(password)





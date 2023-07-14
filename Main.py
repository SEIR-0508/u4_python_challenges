# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

seconds_in_minute = 60
seconds_in_hour = 3600
minutes_in_hour = 60
hours_in_day = 24
days_in_year = 365


def minute_to_second_converter(minutes):
    return f'{minutes * seconds_in_minute} seconds'

def hour_to_second_converter(hours):
    return f'{hours * seconds_in_hour} seconds'

def day_to_second_converter(days):
    return f'{days * hours_in_day * seconds_in_hour}'

def month_to_hour_converter(month):
    if month == 'september' or month == 'april' or month == 'june' or month == 'november':
        return 30 * hours_in_day

    elif month == 'january' or month == 'march' or month == 'may' or month == 'july' or month == 'august' or month == 'october' or month == 'december':
        return 31 * hours_in_day

    elif month == 'february':
        return 28 * hours_in_day
    
    else: return 'That ain`t a month bruh'

def month_to_minute_converter(month):
    if month == 'september' or month == 'april' or month == 'june' or month == 'november':
        return 30 * hours_in_day * minutes_in_hour

    elif month == 'january' or month == 'march' or month == 'may' or month == 'july' or month == 'august' or month == 'october' or month == 'december':
        return 31 * hours_in_day * minutes_in_hour

    elif month == 'february':
        return 28 * hours_in_day * minutes_in_hour
    
    else: return 'That ain`t a month bruh'

def year_to_minute_conveter(years):
    return f'{years * hours_in_day * minutes_in_hour} minutes'

# print(month_to_minute_converter('february'))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import math

def find_middle_letter(string):

    string_as_list = list(string)
    list_length = len(string_as_list)
    if list_length % 2 == 0:
        return ''
    elif list_length % 2 == 1 or list_length == 1:
        return string_as_list[math.floor(list_length/2)]

# print(find_middle_letter('ocean'))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def credit_card_number(number):
    number_as_string = str(number)
    asteric_string = '************'

    return asteric_string + number_as_string[12:16]

# print(credit_card_number(1234567894444123))


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
# statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
# }

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

test_dictionary = {
    'John': 'online',
    'Paul': 'offline',
    'George': 'online',
    'Ringo': 'offline'
}

def number_of_online(statuses):
            
    online_count = 0
    offline_count = 0
    people_online = ''
    people_offline = ''
    for key, value in statuses.items():
        if value == 'online':
            online_count += 1
            people_online += f'{key}, '
        elif value == 'offline':
            offline_count += 1
            people_offline += f'{key}, '
    return f'There are {online_count} people online. They are {people_online}. There are {offline_count} people offline. They are {people_offline}.'
            
# print(number_of_online(test_dictionary))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def discount_calculator(price, discount):
    return price - ((discount/100) * price)

# print(discount_calculator(1873, 61))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def find_hypotenuse(a, b):  
    hypotenuse = (a ** 2 + b ** 2) ** 0.5

    return hypotenuse

# print(find_hypotenuse(3, 3))
    
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def fibonaccify(num1, num2):

    fibonacci_list = [num1, num2]


    while len(fibonacci_list) < 20578: #This is the maximum length the list can get before the computer stops it from executing.
        result = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(result)

    return fibonacci_list


print(fibonaccify(0, 1))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

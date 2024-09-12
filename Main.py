import math

# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?

# Note -> You may need to put "import math" at the beginning of your code to do some of the math in this
## Also note -> We aren't concerned with leap years here


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def convert_mins_to_secs(minutes):
    seconds = (minutes*60)
    return print(f'{minutes} minutes is {seconds} seconds.')

def convert_hours_to_secs(hours):
    minutes = (hours*60)
    seconds = (minutes*60)
    return print(f'{hours} hours is {seconds} seconds.')

convert_hours_to_secs(24)

def convert_days_to_hours(days):
    hours = (days*24)
    return print(hours)

def convert_days_to_minutes(days):
    hours = (days*24)
    minutes = (hours*60)
    return print(minutes)

june_hours = convert_days_to_hours(30)

august_minutes = convert_days_to_minutes(31)

year_minutes = convert_days_to_minutes(365)

#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def mid(string):
    str(string)
    length = len(string)
    if length % 2 == 0 and length > 0:
        return print('')
    elif length == 0:
        print('You must enter a string.')
    else:
        middle_index = length // 2
        middle_character = string[middle_index]
        return print(middle_character)

mid('flj;skj;asd')

# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def censor_card_info(number):
    card_number = str(number)
    censored_number = "*" * (len(card_number) - 4) + card_number[-4:]
    print(censored_number)

censor_card_info(4756837483746534)

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


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

users = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline",
    "Abby": "online",
    "Greg": "online",
    "Jeff": "offline",
    "Jeremy": "offline",
    "Jordan": "offline"
}

def status_count(dict):
    statuses_list = dict.values()
    online_count = 0
    offline_count = 0
    for status in statuses_list:
        if status == 'online':
            online_count += 1
        if status == 'offline':
            offline_count += 1
    print(f'The number of online users is {online_count}')
    print(f'The number of offline users is {offline_count}')

status_count(users)


#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def find_discount(price, discount_percentage):
    price_int = int(price)
    discount_int = int(discount_percentage)
    discount = 100 - discount_int
    new_price = (price_int * discount)//100
    print(new_price)

find_discount(199.99, 15)


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def pythagorean(adjacent, opposite):
    a = int(adjacent)
    b = int(opposite)
    c_squared = a**2 + b**2
    hypotenouse = int(math.sqrt(c_squared))
    print(hypotenouse)

pythagorean(32, 52)


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def fibonacci(num1, num2):
    first_num = num1
    sec_num = num2
    current_num = None

    counter = 0

    while counter <= 9:
        current_num = first_num + sec_num
        print(current_num)
        first_num = sec_num
        sec_num = current_num
        counter += 1

fibonacci(0, 1)

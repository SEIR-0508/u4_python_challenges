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

seconds_in_minute = 60
minutes_in_hour = 60
hour_in_day = 24
days_in_june = 30 
days_in_august = 31
days_in_year = 365

def minutes_to_seconds(minutes):
    return f'{minutes * seconds_in_minute} seconds'

def hours_to_seconds(hour):
    return f'{hour * minutes_in_hour * seconds_in_minute} seconds'

def days_to_seconds(day):
    return f'{day * hour_in_day * minutes_in_hour * seconds_in_minute} seconds'

def hours_in_june():
    hours_in_day = 24
    return f'{days_in_june * hours_in_day} hours'

def mnutes_in_august():
    minutes_in_hour = 60
    return f'{days_in_august * minutes_in_hour} minutes'

def minutes_in_year():
    minutes_in_hour = 60
    return f'{days_in_year * hour_in_day * minutes_in_hour} minutes'

print(minutes_in_year())


# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      


# import math

def find_middle_letter(string):
    string_as_list = list(string)
    list_len = len(string_as_list)
    if list_len % 2 == 0:
        return ''
    else:
        return string_as_list[math.floor(list_len/2)]  

print(find_middle_letter('Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch'))

# the actual name of a town in Wales in the UK


# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->

# replace_charaxter = '*'

def credit_card_hider(card_number):
    integer_to_string = str(card_number)
    num_chars_to_hide = len(integer_to_string) - 4
    hidden_string = '*' * num_chars_to_hide
    last_four_chars = integer_to_string[-4:]
    result = hidden_string + last_four_chars
    return result
        

card_number=1234567891234567   
print(credit_card_hider(card_number))

# ---------------------------------



# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


# ---------------------------------
#      

def onlinne_count(statuses):
    count = 0
    for key, value in statuses.items():
        if value == 'online':
            count += 1
    return count

print(onlinne_count(statuses))

# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->

def discounted_price(full_price, discount_percentage):
    return full_price - (full_price * (discount_percentage/100))

    
print(discounted_price(150, 50))

# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->

import math
def hypotenuse(adjacent, opposite):
    return math.sqrt(adjacent**2 + opposite**2)

print(hypotenuse(3, 4))





# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->
def fibonacci_intervals(num1, num2, num_intervals):
    fibonacci_sequence = [num1, num2]
    for i in range(2, num_intervals + 2):
        next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_num)
    next_nine_intervals = fibonacci_sequence[2:]
    return next_nine_intervals
num1 = 0
num2 = 1
num_intervals = 9
result = fibonacci_intervals(num1, num2, num_intervals)
print(result)

# ---------------------------------

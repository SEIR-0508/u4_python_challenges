# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
def mins_to_secs(mins):
    secs = mins * 60
    print(f'{mins} minutes is {secs} seconds.')
mins_to_secs(82)
# mins_to_secs(1)
# mins_to_secs(5)

# - Then take it up a step further, converting Hours into seconds (1 -> 3600)
def hours_to_secs(hours):
    secs = hours * 60**2
    print(f'{hours} hours is {secs} seconds.')
hours_to_secs(7)
# hours_to_secs(1)
 
# - We're on the right track here, how many seconds are in a day
def days_to_secs(days):
    secs = days * 24 * (60**2)
    print(f'{days} days is {secs} seconds.')
days_to_secs(1)

# - How many Hours are in the month of June? 
def days_to_hours(days, month):
    hours = days * 24
    print(f'There are {hours} hours in {month}.')
days_to_hours(30, 'June')

# - How many Minutes are in the month of August?
def days_to_minutes(days, month):
    minutes = days * 24 * 60
    print(f'There are {minutes} minutes in {month}.')
days_to_minutes(31, 'August')

# Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
# In days, in weeks, in cups of coffee?
def mins_to_years(years):
    mins = years * 365 * 24 * 60
    print(f'{years} years is {mins} minutes.')
mins_to_years(1)

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->

def mid(string):
    # find length of the string

    # if length is even, return blank string

    # if length is odd, find middle letter
    # first half of string BEFORE middle letter needs to equal the second half of string AFTER the middle letter


# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------



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



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

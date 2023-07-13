# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
def mins_to_secs(mins):
    secs = mins * 60
    print(f'{mins} minutes is {secs} seconds.')
# mins_to_secs(82)
# mins_to_secs(1)
# mins_to_secs(5)

# - Then take it up a step further, converting Hours into seconds (1 -> 3600)
def hours_to_secs(hours):
    secs = hours * 60**2
    print(f'{hours} hours is {secs} seconds.')
# hours_to_secs(7)
# hours_to_secs(1)
 
# - We're on the right track here, how many seconds are in a day
def days_to_secs(days):
    secs = days * 24 * (60**2)
    print(f'{days} days is {secs} seconds.')
# days_to_secs(1)

# - How many Hours are in the month of June? 
def days_to_hours(days, month):
    hours = days * 24
    print(f'There are {hours} hours in {month}.')
# days_to_hours(30, 'June')

# - How many Minutes are in the month of August?
def days_to_minutes(days, month):
    minutes = days * 24 * 60
    print(f'There are {minutes} minutes in {month}.')
# days_to_minutes(31, 'August')

# Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
# In days, in weeks, in cups of coffee?
def mins_to_years(years):
    mins = years * 365 * 24 * 60
    print(f'{years} years is {mins} minutes.')
# mins_to_years(1)


# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->

def mid(string):
    # convert string to list
    letters = list(string)
    # find length of the list
    length = len(letters)
    print(f'The length of string "{string}" is {length}.')
    if length % 2 == 0:
        # if length is even, return blank string
        print('""')
    else:
        # if length is odd, find middle letter
        # length of string FIRST half needs to equal length of string SECOND half
        # e.g. (5 - 1) / 2 >> 2 letters before and 2 letters after middle letter
        num_of_others = int((length - 1) / 2)
        print(string[-1 - num_of_others])

# mid('hello')
# mid('howdy')
# mid('abcdefghij')
# mid('abcdefghi')


# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->


def hide_num(cc_num):
    hidden_num = []
    for num in cc_num[:-5]:
        hidden_num.append("*")
    for num in cc_num[-5:-1]:
        hidden_num.append(num)
    print(''.join(hidden_num))

# hide_num('1234567890')
# hide_num('984357868487687')


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
#      Solution Goes Here ->

# def online_count(dict):
#     return 

# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->

def discount(full_price, discount):
    price = int(full_price)
    deal = discount / 100
    final_price = int(price - (price * deal))
    print(final_price)
# discount(100, 20)

# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->
def pythagoras(adj, opp):
    hypotenouse = int(((adj**2) + (opp**2)) * 0.5)
    print(hypotenouse)
# pythagoras(10, 10)
# pythagoras(2, 2)

# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->

def fibonitch(num1, num2):
    counter = 0
    interval = num1 + num2
    while counter <= 9:
        next = num2 + interval
        num2 = next
        counter += 1
        print(next)
fibonitch(1,1)

# ---------------------------------

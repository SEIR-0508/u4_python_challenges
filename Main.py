# Python Challenges
import math

#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def sec_per_min(min):
    return min * 60
    
def sec_per_hour(hours):
    return hours*60*60

def sec_per_day(days):
    return days*24*60*60

def hrs_in_june():
    return 30*24

def min_in_aug():
    return 31 * 24 * 60

def min_in_year(days_in_year):
    return days_in_year * 24 * 60

print(sec_per_min(1))
print(sec_per_min(12))
print(sec_per_hour(1))
print(sec_per_hour(7))
print(sec_per_day(1))
print(hrs_in_june())
print(min_in_aug())
print(min_in_year(365))



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------


def mid(str):
    answer = str[int(len(str)/2)] if len(str)%2!=0 else ''
    return answer
print(mid('abc'))
print(mid('aakoewifnoiaw'))


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".
    

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def hide_cc_nums(num):
    partly_hidden_num = '*'*len(num[:-4]) + num[-4:]
    return partly_hidden_num

print(hide_cc_nums('123456789012'))


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
# ---------------------------------

def online_count(dict):
   return list(dict.values()).count('online')

# print(statuses.values())
print(online_count(statuses))


#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def item(price:int, discount:int):
    new_price = price - (price*(discount/100))
    return new_price

print(item(276, 20))

#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def triangle(adj_leg:int, opp_leg:int):
    hypotenuse = math.sqrt((adj_leg**2) + (opp_leg**2))
    return hypotenuse

print(triangle(20, 32))

#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->
# ---------------------------------

def function(num1:int, num2:int):
    sequence = ((num1*0), (num1), (num1*1), (num1*2), (num1*3), (num1*5), (num1*8), (num1*13), (num1*21), (num1*34), (num1*55), (num1*89))
    sequence2 = ((num2*0), (num2), (num2*1), (num2*2), (num2*3), (num2*5), (num2*8), (num2*13), (num2*21), (num2*34), (num2*55), (num2*89))
    return sequence, sequence2

print(function(2, 5))
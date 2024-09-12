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

# def minutes_to_seconds(minutes):
#     return minutes * 60

# minutes = 1
# seconds = minutes_to_seconds(minutes)
# print(f'{minutes} minutes is the same as {seconds} seconds.')

# def hours_to_seconds(hours):
#     return hours * 3600

# hours = 1
# seconds = hours_to_seconds(hours)
# print(f'{hours} hour is the same as {seconds} seconds.')

# def days_to_seconds(days):
#     return days * 86400

# days = 3
# seconds = days_to_seconds(days)
# print(f'{days} days is the same as {seconds} seconds.')

# def hours_in_june(hours_in_day, days_in_month):
#     return hours_in_day * days_in_month

# days_in_month = 30
# hours_in_day = 24
# total_hours_in_june = hours_in_june(hours_in_day, days_in_month)
# print(f'The month of June has {total_hours_in_june} hours.')

# def minutes_in_august(minutes_in_hour, hours_in_day, days_in_month):
#     return minutes_in_hour * hours_in_day * days_in_month

# days_in_month = 31
# hours_in_day = 24
# minutes_in_hour = 60
# total_hours_in_august = minutes_in_august(minutes_in_hour, hours_in_day, days_in_month)
# print(f'The month of August has {total_hours_in_august} minutes.')




# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->

# def mid(string):
#     length = len(string)
#     if length % 2 == 0:  
#         return ""
#     else:  
#         middle_index = length // 2
#         return string[middle_index]
    
# print(mid('abc'))
# print(mid('aaaa'))

# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->

# def cc_number(card_number):
#     hidden_digits = "*" * (len(card_number) - 4)
#     visible_digits = card_number[-4:]
#     return hidden_digits + visible_digits

# credit_card_number = "1234567894444"
# hidden_card_number = cc_number(credit_card_number)
# print(hidden_card_number)
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

# def online_count(statuses):
#     count = 0
#     for status in statuses.values():
#         if status == "online":
#             count += 1
#     return count

# statuses = {
#     "John": "online",
#     "Paul": "offline",
#     "George": "online",
#     "Ringo": "offline"
# }

# count = online_count(statuses)
# print(count)
# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->

# def sale_price(full_price, discount):
#     return full_price - (full_price * discount / 100)

# full_price = 350
# discount = 20
# print(sale_price(full_price, discount))
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->

# def calc_hypotenous(adjacent, opposite):
#     hypotenous = (adjacent**2 + opposite**2)**.5
#     return hypotenous

# adjacent = 3
# opposite = 4
# hypotenous = calc_hypotenous(adjacent, opposite)
# print(hypotenous)
# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->
# def fibonacci_intervals(num1, num2):
#     fibonacci_sequence = [num1, num2]
#     for _ in range(9):
#         next_num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
#         fibonacci_sequence.append(next_num)
#     return fibonacci_sequence  


# num1 = 0
# num2 = 1
# intervals = fibonacci_intervals(num1, num2)
# print(intervals)

# ---------------------------------

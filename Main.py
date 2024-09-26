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
import math

def minutes_to_seconds(minutes):
    seconds = minutes * 60
    return seconds
  
converted_seconds = minutes_to_seconds(1)
print(converted_seconds) 
  # ------------------------------
  
def hours_to_seconds(hours):
    minutes = hours * 60
    seconds = minutes_to_seconds(minutes)
    return seconds
  
converted_seconds = hours_to_seconds(1)
print(converted_seconds)
  # ------------------------------

def days_to_seconds(days):
    hours = days * 24
    seconds = hours * 3600
    return seconds

seconds_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24

seconds_in_day = seconds_in_minute * minutes_in_hour * hours_in_day

print("Number of seconds in a day:", seconds_in_day)

# ---------------------------------

days_in_june = 30
hours_in_day = 24

total_hours_in_june = days_in_june * hours_in_day

print(total_hours_in_june)

# ---------------------------------

days_in_august = 31
hours_in_day = 24
minutes_in_hour = 60

total_minutes_in_august = days_in_august * hours_in_day * minutes_in_hour

print(total_minutes_in_august)
# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->

def mid(string):
    length = len(string)
    if length % 2 == 0:
        return ""
    else:
        middle_index = length // 2
        return string[middle_index]
      
print(mid("abc"))  
print(mid("aaaa"))  

     
# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->

def hide_credit_card_number(credit_card_number):
  if len(credit_card_number) < 4:
    return credit_card_number
  hidden_chars = "*" * (len(credit_card_number) - 4)
  last_four = credit_card_number[-4:]
  return hidden_chars + last_four

print(hide_credit_card_number("1234567894444"))
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

def online_count(dicts):
    count = 0
    for status in dicts.values():
        if status == "online":
            count += 1
    return count

statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}

print(online_count(statuses))
# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->

def discount_price(full_price, discount_percentage):
    discount_amount = full_price * (discount_percentage / 100)
    discounted_price = full_price - discount_amount
    return discounted_price
  
full_price = 100
discount_percentage = 20

discounted_price = discount_price(full_price, discount_percentage)
print(discounted_price) 


# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse



# ---------------------------------
#      Solution Goes Here ->

def calculate_hypotenuse(adjacent, opposite):
    hypotenuse = math.sqrt(adjacent**2 + opposite**2)
    return hypotenuse
  
adjacent_leg = 3
opposite_leg = 4

hypotenuse = calculate_hypotenuse(adjacent_leg, opposite_leg)
print(hypotenuse) 

# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->

def fibonacci(num1, num2): 
      numbers = [num1, num2]
      for _ in range(10): 
            next = numbers[-1] + numbers[-2]
            numbers.append(next)
      return numbers

numbers = fibonacci(0, 1)
print(numbers)


# ---------------------------------

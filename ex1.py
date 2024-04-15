#q1
# List of integers
numbers = [1, 2, 3, 4, 5]

# Square using lambda function
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

# Cube using lambda function
cubed_numbers = list(map(lambda x: x ** 3, numbers))
print("Cubed numbers:", cubed_numbers)



#q2:

# Lambda function to check if a string starts with a given character
starts_with = lambda string, char: string[0] == char

# Example usage
given_string = "Hello"
given_character = "H"
print("String starts with the given character:", starts_with(given_string, given_character))



#q3:
from datetime import datetime

# Sample datetime object
sample_datetime = datetime.now()

# Lambda functions to extract year, month, date, and time
get_year = lambda dt: dt.year
get_month = lambda dt: dt.month
get_day = lambda dt: dt.day
get_time = lambda dt: dt.time()

# Extracting components using lambda functions
year = get_year(sample_datetime)
month = get_month(sample_datetime)
day = get_day(sample_datetime)
time = get_time(sample_datetime)

# Printing extracted components
print("Year:", year)
print("Month:", month)
print("Day:", day)
print("Time:", time)

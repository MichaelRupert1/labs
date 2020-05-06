'''

Write a script that takes in a number in days from the user between 1 and 1,000,000,000 and convert it to seconds.

NOTE: We will use the input() funtion to collect users input. An example is demonstrated below.

'''

# the input of the user will be saved in the variable days.
# because the input() function collects the input as a string, we have to convert it to an int
# The string passed to the input() function is what the user is prompted with
#dys = int(input("Please enter a number in days between 1 and 1,000,000,000: "))

days = int(input('Enter a number of days between one and one billion to convert that day into seconds\n\t-->'))
seconds_conv = days*24*60*60
print(f'In {days} days, {seconds_conv} seconds will have gone by. ')

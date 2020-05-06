'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
def most_char():
    u_i_1 = input('input here ->')
    u_i_2 = input('input here ->')
    u_i_3 = input('input here ->')
    if len(u_i_1) > len(u_i_2) and len(u_i_1) > len(u_i_3) :
        print(f'{u_i_1} has the longest string with {len(u_i_1)} characters.')
    elif len(u_i_2) > len(u_i_3):
        print(f'{u_i_2} has the longest string with {len(u_i_2)} characters.')
    else:
        print(f'{u_i_3} has the longest string with {len(u_i_3)} characters.')
    
most_char()
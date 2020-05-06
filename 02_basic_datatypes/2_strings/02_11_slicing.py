'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

u = input('To create your name in pig latin\n\tenter your first name below \n\t\t-->')
u = u.lower()
first_letter = u[0]
w = u.replace(first_letter,' ')
pig_name = w+first_letter+'ay'
print(f'if Cesar were alive he would have called you{pig_name}')

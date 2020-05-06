'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
vowels = ['a', 'e', 'i', 'o', 'u']
emptydict = []
str1 = str('heakfn lweif woeifjew woiefjw oiwejf')
def counts(str1):
    for word in str1:
        for char in word:
            if char in vowels:
                emptydict.append(char)
    return (emptydict)
a = (str1.count('a'))
print(f'"a" has only {a} occurencs in this encryption,',end='')
e = (str1.count('e'))
print(f'"e" has {e} occurencs in this encryption,',end='')
i = (str1.count('e'))
print(f'"i" has {i} occurencs in this encryption,',end='')
o = (str1.count('e'))
print(f'"o" has {o} occurencs in this encryption,',end='')
u = (str1.count('e'))
print(f'"u" has {u} occurencs in this encryption,',end='')
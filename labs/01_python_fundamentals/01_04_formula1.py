'''
Write the necessary code to print the result of the following formula:

	(15.7 * 3.6 - 34.9 * 0.9) / (68.9 - 2.1)

'''
def PEMAS(a,b,c,d,e,f,):
    return (a*b-c*d)/(e-f)
x =PEMAS(15.7,3.6,34.9,0.9,68.9,2.1)
print(f'The order of operations total is {x}.')
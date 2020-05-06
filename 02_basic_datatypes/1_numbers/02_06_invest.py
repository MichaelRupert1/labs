'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.


'''
investment_amount = float(input('what you got to throw down?\n-->'))
interest_rate = float(input('\tinterest rate in %\n\t-->'))
years_invest = int(input('\t\thow many years you got left?\n\t\t-->'))
A = investment_amount
r = interest_rate
t = years_invest
print(f' you have {A}$ to invest at a rate of {r}% for {t} years.')
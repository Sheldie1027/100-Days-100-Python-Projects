# Formula for calculating house loan
# P x R x (1+R)^N / [(1+R)^N-1]
# P = Principal loan amount
# N = Loan tenure in months
# R = Monthly interest rate (Annual Rate of interest/12/100)

from babel.numbers import format_currency

principal_amt = input("Enter the principal amount in lakhs (1Lakh to 10Cr): \n")
tenure = input("Enter the tenure in years (1 to 30): \n")
interest = input("Enter the interest rate (0.5 to 15): \n")

R = (float(interest)/12)/100
N = int(tenure)*12
P = int(principal_amt)

EMI = round(P*R*(1+R)**N / (((1+R)**N)-1))

formatted_EMI = format_currency(EMI, 'INR', locale='en_IN')
formatted_principal = format_currency(P, 'INR', locale='en_IN')
total_payable = format_currency(EMI*N, 'INR', locale='en_IN')
Interest_amt = format_currency((EMI*N)-P, 'INR', locale='en_IN')

print(f"Requested Loan Amount: {formatted_principal}")
print(f"Tenure in months: {N}")
print(f"Interest rate p.a.: {interest}%")
print(f"Your monthly interest amount will be: {formatted_EMI}")
print(f"The total amount payable will be {formatted_EMI} * {N} = {total_payable}.\nInterest amount will be {Interest_amt}")
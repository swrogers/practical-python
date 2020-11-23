# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
set_payment = 2684.11
total_paid = 0.0
months = 0

extra_to_prin = 1000.0
extra_pay_len = 12

while principal > 0:
    months = months + 1
    payment = set_payment
    
    if extra_pay_len:
        payment = payment + extra_to_prin
        extra_pay_len = extra_pay_len - 1
    
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment


print('Total paid', total_paid)
print('Months taken', months)

# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
set_payment = 2684.11
total_paid = 0.0
months = 0

extra_to_prin = 1000.0
extra_payment_start_month = 12 * 5  # start in year 5
extra_payment_end_month = (12 * 5) + (4*12) # pay for 4 years
extra_pay_len = extra_payment_end_month - extra_payment_start_month + 1

while principal > 0:
    months = months + 1
    payment = set_payment

    #print(months, round(principal,2))
    print(f'{months:2} : {principal:0.2f}')
    
    if (extra_pay_len
        and months >= extra_payment_start_month
        and months <= extra_payment_end_month):
        payment = payment + extra_to_prin
        extra_pay_len = extra_pay_len - 1
    
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment


print('Total paid', total_paid)
print('Months taken', months)

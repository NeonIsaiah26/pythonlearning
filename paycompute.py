from usingfunctions import compute_pay

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

gross_pay = compute_pay(hours, rate)
print("Pay:", gross_pay)
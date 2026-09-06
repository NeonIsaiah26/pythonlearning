def compute_pay(hours, rate):
    if hours > 40:

        normal_pay = 40 * rate
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * (rate * 1.5)
        total_pay = normal_pay + overtime_pay
    else:
        total_pay = hours * rate
        
    return total_pay

if __name__ == "__main__":
    hrs = input("Enter Hours: ")
    reyt = input("Enter Rate: ")
    
    hours = float(hrs)
    rate = float(reyt)
    
    gross_pay = compute_pay(hours, rate)
    
    print("Pay:", gross_pay)
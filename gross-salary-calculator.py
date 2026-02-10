#number of hours worked by the employee
hrs = input("Enter number of Hours worked: ")
total_hours = float(hrs)
#normal hourly wage
rate = input('Enter standard rate per hour: ')
standard_rate= float(rate)
#calcultion of overtime hourly rate
overtime_rate= float(standard_rate * 1.5)
#identifying overtime hours
overtime_hours= int(total_hours - 40)
#identifying overtime threshold
normal_hours= int(total_hours - overtime_hours)
#calculation of gross salary 
if overtime_hours > 0:
    print('gross salary($):' , (normal_hours * standard_rate) + (overtime_hours * overtime_rate))
else:
    print('Gross salary($):' , total_hours * standard_rate)

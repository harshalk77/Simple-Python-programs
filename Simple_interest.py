# Taking User input of principle rate and time period
p=int(input("Enter Principle: "))
r=int(input("Enter Rate: "))
t=int(input("Enter Time period: "))

#calculating simple interest
si=p*r*t/100
print("The Simple interest is ",si)
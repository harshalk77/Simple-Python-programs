## Taking user input of daily milk consumption and rate of milk

rate=float(input("Enter Rate of Milk per Litre: "))
m=float(input("Enter Daily Milk consumption: "))

#calculating milk bill of 30 days
bill=m*rate*30
print("The Monthly milk bill of customer i ",bill)
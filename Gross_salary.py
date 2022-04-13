#Taking user salary input
salary=int(input("Enter salary of A Worker: "))

#Declaring DA And TA Percentage calculating Gross Salary
DA=salary*80/100
TA=salary*20/100

Gs=salary+DA+TA
print("The Gross Salary of Worker is ",Gs)

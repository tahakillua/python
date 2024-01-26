print("Welcome to the tip calculator.")
#total bill
total_bill = input("What the total bill? §")
total_bill_Nbr = float(total_bill)

#percentage tip 
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
percentage_Nbr = float(percentage)
percentage_tip = (100 + percentage_Nbr)/100

#number of people
people = input("How many people to split the bill? ")
people_Nbr = float(people)

#calcul the price for each person
x = (total_bill_Nbr/people_Nbr)*percentage_tip
#print the result with to number after a dot x.xx
print (f"Each person  should pay: §{round(x,2)}")


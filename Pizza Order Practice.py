print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

#choose the size of pizza
if size == "S":
	bill += 15
	
elif size == "M":
	bill += 20
	
else:
	bill += 25

#add pepperoni 
if add_pepperoni == "Y":
	if size == "S"
		bill += 2
	else:
		bill += 3

#add extra cheese
if extra_cheese == "Y":
	bill += 1 

#print the final bill
print(f"Your final bill is: ${bill}")
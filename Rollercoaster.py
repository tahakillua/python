print("Welcome to the rollecoaster!")
height = int(input("What is your height in cm? "))
bill = 0
#check the height
if height >= 120:
	print("You can ride the rollecoaster!")
	#check the age
	age = int(input("What is your age? "))
	if age < 12:
		bill = 5
		print("Child tickets are §{}".format(bill))
	elif age <= 18:
		bill = 7
		print("Youth tickets are §{}".format(bill))
	else:
		bill = 12
		print("Adult tickets are §{}".format(bill))
	#check if you want a photo
	want_photo = input("Do you want a photo taken? Y or N. "
	if want_photo == "Y":
		bill += 3
	
	print ("Your final bill is §{}".format(bill))

else:
	print("Sorry, you have to grow taller before you can ride.")
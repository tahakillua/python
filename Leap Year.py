#Wich year do you want to check
year = int(input("Wich year do you want to check: "))
#year is divisible by 4
if year % 4 == 0:
	if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        prin("Leap year")

else:
	print("Not leap year")
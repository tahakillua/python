#Enter your height in meters eg., 1.55
height = float (input("Enter your height in meters: "))
#Enter your weight in kilograms e.g., 72
weight = int(input("Enter your weight in kilograms: "))
#Calcul your BMI Body Mass Index
bmi = weight/(height**2)
if bmi < 18.5:
	print ("Your BMI is {}, you are underweight.".format(round(bmi,2)))
elif bmi < 25:
	print("Your BMI is {}, you have a normal weight.".format(round(bmi,2)))
elif bmi < 30:
	print("Your BMI is {}, you are slightly overweight.".format(round(bmi,2)))
elif bmi < 35:
	print("Your BMI is {}, you are obese.".format(round(bmi,2)))
else:
	print("Your BMI is {}, you are clinically obese.".format(round(bmi,2)))
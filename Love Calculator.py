print("The love Calculator is calculating your score...")
#Enter your name, and make it on capital format
name1 = input("What is your name? ").upper()
name2 = input("What is their name? ").upper()

#calcul letter on TRUE
T = name1.count("T") + name2.count("T")
R = name1.count("R") + name2.count("R")
U = name1.count("U") + name2.count("U")
E = name1.count("E") + name2.count("E")

#calcul letter on LOVE
L = name1.count("L") + name2.count("L")
O = name1.count("O") + name2.count("O")
V = name1.count("V") + name2.count("V")
E = name1.count("E") + name2.count("E")

score = int(str(T+R+U+E) + str(L+O+V+E))
if score < 10 or score >90:
	print(f"Your score is {score}, you go together like coke and mentos.")
elif score => 40 and score =< 50:
	print(f"Your score is {score}, you are alright together.")
else:
	print(f"Your score is {score}.")


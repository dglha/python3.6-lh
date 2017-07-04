number = input("Enter any number: ")

number_sqr = input("Enter square of {}: ".format(number))
if int(number_sqr) > int(number)**2:
        print ("too big")
elif int(number_sqr) == int(number)**2:
	print("Congratulation")
else:
	if int(number_sqr) < int(number)**2:
		print("too low")
	else:
		print("Try again!")
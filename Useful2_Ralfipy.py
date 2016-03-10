#Ralfi Salhon


#This is the default menu items and prices I've defined.
#The arrays lengths have to be the same, or the code will return an error.
Items = ["Lemon", "Orange", "Pear"]
Prices = [5, 7, 3]

#This is my function to print the menu. I can easily call it with PrintMenu()
def PrintMenu():
	#This code will repeat however long our menu is. (This case: 3)
	#I need to use str(<integer>) for integers because we cannot
	#print integer values. We convert them to string first.
	for x in range(len(Items)):
	    print str(x+1) + ": " + Items[x] + " - " + "$" + str(Prices[x])

#Print the menu
PrintMenu()

#This part just leaves a blank line.
print ""

#Sets initial cost to 0.
#This number will increase as the customer purchases items.
cost = 0

#This code will run until it is forced to close.
while True:
	#So this is a very frequent and efficient code block I use.
	#I set a variable to an invalid answer, like the 0 below.
	#And I run a while loop until my responder inputs a correct input.
	answer = 0

	#This is the part where I'm asking for answer to be either 1 or 2
	while answer < 1 or answer > 2:
		#Just leaving a blank
		print ""

		#The try and except method is great to subtly retry your code,
		#instead of crashing the code with an invalid input.
		try:
			#I will be converting my string answer to an int here
			#Because although the input may LOOK like an integer, it's actually a string.
			#Shortly, I need to turn "2" into 2.
			answer = int(raw_input("'1' for 'Buy product', '2' for 'Add product' >>> "))
			
			#This is different from our EXCEPT module.
			#The input was valid, but it was not what we wanted.
			if answer < 1 or answer > 2:
				print "Please input a valid number!"

		#The code will just retry if the inserted input contained
		#illegal characters or a string instead of an integer
		except:
			print "Please input a number!"


	#The answer is finally valid.
	#We know take action according to what the answer is.
	if answer == 1:
		#Going to BUY a product

		#I am using the same bulk code I used earlier. Check line 27-29
		#Once again, I set the "buy" value to an invalid input.
		buy = -1
		while buy > len(Items) or buy < 0:
			try:
				buy = int(raw_input("What number item would you like to purchase? >>> "))
				if buy > len(Items) or buy < 0:
					print "Please input a valid number!"
			except:
				print "Please input a number!"

		print ""

		#Printing purchased item and price, as well as total cost.
		#The reason I use -1 is because the 5th item of an array is list[4],
		#since array index starts with 0.
		print "You have purchased " + Items[buy-1] + " for $" + str(Prices[buy-1])
		cost += Prices[buy-1]
		print "Your total cost is now $" + str(cost)
	else:
		#Going to ADD a product

		#If no invalid inputs occur inside this TRY method,
		#a new item will be added to the list.
		try:
			item = raw_input("What are you adding to the menu? >>> ")
			price = int(raw_input("What is it's price? >>> "))
			Items.append(item)
			Prices.append(price)
			print ""
			PrintMenu()
		except:
			#This will cancel adding a product.
			#The user will be reasked to input '1' or '2'.
			print "Invalid input"
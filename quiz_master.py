print("Welcome to the Quiz Master")
print("Please answer to the following questions to the best of your abilities")

print("Let's do the introductions first")
name = raw_input("What is your name please?")
print("Nice to meet you {}!. Enjoy the quiz!".format(name))
print("Let's go to the first question!")

#.......QUESTION 1 .........
try:
	question1 = int(raw_input("Question 1: Do you have any cats? How many?"))
	if question1 == 0:
		print("That's so sad! :( Cats are really fun loving creatures. You should get one.)")
	elif question1 <= 2:
		print("Good for you {}. I bet you are having a great time together ;).".format(name))
	elif question1 <= 4:
		print("OK...That must be a bit of work, but hey! I guess you are a cat lover :).")
	else:
	    print("OK...That is a bit creapy...You must REALLY love cats.")
except ValueError:
	print("Please enter a integer number.")


#.......QUESTION 2 ..........
right_answer = False
while right_answer is not True:
	question2 = raw_input("Question 2: Are you having fun now? y/n")
	if question2.lower() == "y":
		print("Excellent! That means you like my quiz! Let's keep playing:)")
		right_answer = True
	elif question2.lower() == "n":
		print("You are a tough cookie {}. You can exit the quiz by wrighting 'QUIT'.".format(name))	
		right_answer = True
	elif question2 != "y" or "n":
		print("Please answer with y or n")		


#.......QESTION 3 ...........
right_answer = False
while right_answer is not True:
	question3 = raw_input("Question 3: Did you know that your tongue is as long as your thumb? y/n")
	if question3.lower() == "y":
		print("Ha! Ha! Did you really stick your tongue out?!")
		right_answer = True
	elif question3.lower() == "n":
		print("Well...Try it!")
		right_answer = True
	elif question3 != "y" or "n":
		print("Please answer with y or n")

#.......QUESTION 4 .........
right_answer = False
attempts = 0
while right_answer is not True:
	question4 = raw_input("What is the name of our natural satellite?")
	if question4.lower() == "moon": 
		print("Great job! You must be really smart.")
		right_answer = True
	else:
		if attempts <= 3:
			print("Sorry. This is not the correct answer. Try again!")
			attempts += 1
		else:
			print("Sorry, you run out of chances. The answer is 'Moon'")
			break

#.......QUESTION 5 .........

right_answer=False
attempts = 0
while right_answer is not True:
	question5 = int(raw_input("If you have a bowl with 6 apples and you take away four, how many do you have?"))
	if question5 == 4:
		print("Correct! Nice job {}!".format(name))
		right_answer = True
	else:
		if attempts <= 3:
			print("This is not the right answer, try again")
			attempts += 1
		else:
			print("I am sorry, you have no more chances, The answer is 4 that you took away.")
			break


#.......QUESTION 6 .........
right_answer = False
while right_answer is not True:
	try:
		question6 = int(raw_input("Who is bigger? 1. Mr Bigger, 2. Mrs. Bigger or 3. Their baby"))
		if question6 == 1:
			print("The answer is: 'The baby of course. Because he is a little Bigger'.")
			right_answer = True
		elif question6 == 2:
			print("The answer is: 'The baby of course. Because he is a little Bigger'.")
			right_answer = True
		elif question6 == 3:
			print("Correct! Because he is a little Bigger.")
			right_answer = True
		else:
			print("Please enter 1, 2 or 3.")
	except ValueError:
		print("Sorry budy. We need a number. Try 1, 2 or 3.")

#.......QUESTION 7 ..........
right_answer = False
attempts = 0
while right_answer is not True:
	try:
		question7 = int(raw_input("What is the answer to the next math problem  6/2(1+2) ?"))
		if question7 == 9:
			print("Excellent!!!")
			right_answer = True
		elif question7 == 1:
			print("That's what I thought too, but 1 is not correct. Try again!")
			attempts+=1
		else:
			if attempts <= 2:
				print("This is not the right answer. Please try again.")
				attempts+=1
			else:
				print("Sorry. You run out of chances. THe answer is 9.")
	except ValueError:
		print("The answer is a number. Try again")
		attempts+=1

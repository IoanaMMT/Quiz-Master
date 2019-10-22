print("Welcome to the Quiz Master")
print("Please answer to the following questions to the best of your abilities")

print("Let's do the introductions first")
name = raw_input("What is your name please?")
print("Nice to meet you {}!. Enjoy the quiz!".format(name))
print("Let's go to the first question!")

#.......QUESTION 1 .........
question1 = int(raw_input("Question 1: Do you hane any cats? How many?"))
if question1 == 0:
	print("That's so sad! :( Cats are really fun loving creatures. You should get one.)")
elif question1 <= 2:
	print("Good for you {}. I bet you are having a great time together ;).".format(name))
elif question1 <= 4:
	print("OK...That must be a bit of work, but hey! I guess you are a cat lover :).")
else:
    print("OK...That is a bit creapy...You must REALLY love cats.")

#.......QUESTION 2 ..........
question2 = raw_input("Question 2: Are you having fun now? y/n")
if question2.lower() == "y":
	print("Excellent! That means you like my quiz! Let's keep playing:)")
elif question2.lower() == "n":
	print("You are a tough cookie {}. You can exit the quiz by wrighting 'QUIT'.".format(name))	

#.......QESTION 3 ...........
question3 = raw_input("Question 3: Did you know that your tongue is as long as your thumb? y/n")
if question3.lower() == "y":
	print("Ha! Ha! Did you really stick your tongue out?!")
elif question3.lower() == "n":
	print("Well...Try it!")

#.......QUESTION 4 .........
question4 = raw_input("What is the name of our natural satellite?")
if question4.lower() == "Moon": #The lower case is not working
	print("Great job! You must be really smart.")
else:
	print("The correct answer is 'Moon'.")

#.......QUESTION 5 .........
question5 = int(raw_input("If you have a bowl with 6 apples and you take away four, how many do you have?"))
if question5 == 4:
	print("Correct! Nice job {}!".format(name))
else:
	print("The answer is 4 that you took away.")

#.......QUESTION 6 .........
question6 = int(raw_input("Who is bigger? 1. Mr Bigger, 2. Mrs. Bigger or 3. Their baby"))
if question6 == 1:
	print("The answer is: 'The baby of course. Because he is a little Bigger'.")
elif question6 == 2:
	print("The answer is: 'The baby of course. Because he is a little Bigger'.")
elif question6 == 3:
	print("Correct! Because he is a little Bigger.")

#.......QUESTION 7 ..........
question7 = int(raw_input("What is the answer to the next math problem  6/2(1+2) ?"))
if question7 == 9:
	print("Excellent!!!")
elif question7 == 1:
	print("That's what I thought too, but apparently the answer is 9")
else:
	print("Sorry! The right answer is 9.")

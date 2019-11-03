
questions = {
	1 : "Question 1: Do you have any cats? How many?",
	2 : "Question 2: Are you having fun now? y/n",
	3 : "Question 3: Did you know that your tongue is as long as your thumb? y/n",
	4 : "Question 4: What is the name of our natural satellite?",
	5 : "Question 5: If you have a bowl with 6 apples and you take away four, how many do you have?",
	6 : "Question 6: Who is bigger? 1. Mr Bigger, 2. Mrs. Bigger or 3. Their baby",
	7 : "Question 7: What is the answer to the next math problem  6/2(1+2) ?",
}

answers = {
	1 : "Yes",
	2 : "No",
	3 : "Maybe",
	4 : "Try again",
	5 : "That's correct",
	6 : "Very close",
	7 : "Well done",
	}

#use slices for multiple answers and outcomes

for i in range(1, len(questions)+1):
	answer = raw_input(questions[i])
	
	for i in range(1,len(answers)+1):
		if answer == answers[i]:
			print("T")


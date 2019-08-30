from random import randint

print "Welcome to our guessing game"

number = randint(1, 10)
tries = 0

while True:
	guess = raw_input("Enter in a number (1-10):")
	tries += 1
	if int(guess) == number:
		print "You got it in {} tries".format(tries)
		break
	elif int(guess) > number:
		print "Too high!"
	elif int(guess) < number:
		print "Too low!"

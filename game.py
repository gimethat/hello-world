from random import randint

print "Welcome to our guessing game"

number = randint(1, 10)

while True:
	guess = raw_input("Enter in a number (1-10):")
	if int(guess) == number:
		print "You got it!"
		break
	else:
		print "Try again!"


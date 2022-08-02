#coding: utf-8
import random

#func greeting
#func ask and answer
#func end

def main():

	print("Welcome to number guesser!")

	playing = input("Do you want to play? ")

	if playing.lower() != "yes":
    		print("k thx by!")
    		quit()


	start = int(input("Between? "))
	stop = int(input("And? "))

	the_number = random.randint(start,stop)

	fstr = "It's an integer between{srt: n} and{stp: n}"
	print(fstr.format(srt = start, stp=stop))

	score = 1
	guess = the_number-1;

	while guess != the_number:
    		guess_s = input("What's your guess? ")
    		if guess_s.isdigit():
        		guess = int(guess_s)
    		else:
        		print("Please give a number")
        		continue
    		if guess < the_number:
      		print("It's bigger than " + str(guess) + ".")
      		score += 1
    		elif guess > the_number:
      		print("It's smaller than " + str(guess) + ".")
      		score += 1
    		else:
      		print("Correct")
      		break
	print("You guessed the number in " + str(score) + " tries.")
	if score > stop-start:
    		print("Wow! How did you manage that?")

def main():
# Using the special variable 
# __name__
if __name__=="__main__":
    main()
#coding: utf-8
import random

print("Welcome to number guesser!")

if playing.lower() != "yes":
    print("k thx by!")
    quit()

#random.seed()
playing = input("Do you want to play? ")


start = int(input("Between? "))
stop = int(input("And? "))

the_number = random.randint(start,stop)

fstr = "It's an integer between{srt: n} and{stp: n}"
print(fstr.format(srt = start, stp=stop))

score = 1
guess = the_number-1;

while guess != the_number:
    guess = int(input("What's your guess? "))
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

import random
import math

count=1

num = random.randint(1, 10)

print("guess the number between 1 to 10!")

gue = int(input("Input youre guess : "))

while num != gue:
     if num > gue:
          print("guess is to small")
          count = count + 1
     else:
          print("guess is to big")
          count = count + 1
     gue = int(input("Input youre guess : "))
print("Well Done! you done in " + str(count) + " try")

print("Your Score " + str((11-count)*100/10) + "%")
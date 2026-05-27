import random
sum = 0
for i in range(1, 11):
    sum += i
print(sum)
number = int(input("Enter a number: "))
while number > 50:
    if number % 2 == 0:
        number /= 2
    else:
        print("The biggest number from your number undividible by 2: " + str(number))
        break
def Try_to_guess():
    number0 = random.randint(1, 10)
    number = int(input("guess a number: "))
    if number0 == number:
        print("You guessed the number")
    else:
        print("You did not guess the number")
Try_to_guess()
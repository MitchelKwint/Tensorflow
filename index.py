import random

guessesTaken = 0

print ("Typ je naam als captcha test")
name = input()

number = random.randint(1,20)
print ("Hallo , " + name + " , en welkom bij raad het word het getal ligt tussen 1 en 20")

while guessesTaken < 6:
    print('Doe een gok')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Het getal is groter")

    if guess > number:
        print("Het getal is kleiner")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Goed gedaan, " + name + ", Je hebt het getal in "  + guessesTaken + 'x geraden!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)


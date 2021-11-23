import random

userScore = 0
compScore = 0

a=input("Qaysi tarafga tepasiz: \nchap, o'rta, o'ng\n")
b=["chap","o'rta","o'ng"]
c=random.choice(b)

print("Zarbaaa")
print("Kompyuter " + c + "ga otildi")
if a==c:
	print("Seyvvv")
	print("User: " + str(userScore) + "\nKomp: " + str(compScore))
else:
	print("Goooool")
	userScore += 1
	print("User: " + str(userScore) + "\nKomp: " + str(compScore))

ot = input("Qaysi tomonga otilasiz? ")
b=["chap","o'rta","o'ng"]
cd=random.choice(b)

print("Kompyuter " + cd + "ga tepdi")
if ot==cd:
	print("Seyvvv")
	print("User: " + str(userScore) + "\nKomp: " + str(compScore))
else:
	print("Goool")
	compScore += 1
	print("User: " + str(userScore) + "\nKomp: " + str(compScore))

print("O'yin tugadi")
if userScore>compScore:
	print("Tabriklaymiz, siz g'olib bo'ldingiz")
elif compScore>userScore:
	print("Afsuski, siz mag'lub bo'ldingiz")
else:
	print("Durrang")
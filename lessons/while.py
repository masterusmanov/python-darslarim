import random

userScore = 0
compScore = 0

komp_zarba = 0

while komp_zarba!=5:
	a=input("Qaysi tarafga tepasiz: \nchap, o'rta, o'ng\n")
	b=["chap","o'rta","o'ng"]
	c=random.choice(b)
	print("Zarbaaaa")
	print("Kompyuter " + c + "ga otildi")
	if a==c:
		print("Seyvvv")
		print("User: " + str(userScore) + "\nKomp: " + str(compScore))
	elif a!="chap" and a!="o'rta" and a!="o'ng":
		print("O'yinchi noto'g'ri zarba berdi")
	else:
		print("Goooool")
		userScore += 1
		print("User: " + str(userScore) + "\nKomp: " + str(compScore))
#############################################################################
	ot = input("Qaysi tomonga otilasiz? ")
	b=["chap","o'rta","o'ng"]
	cd=random.choice(b)
	komp_zarba += 1
	print("Kompyuter " + cd + "ga tepdi")
	if ot==cd:
		print("Seyvvv")
		print("User: " + str(userScore) + "\nKomp: " + str(compScore))
	else:
		print("Goool")
		compScore += 1
		print("User: " + str(userScore) + "\nKomp: " + str(compScore))

	if komp_zarba==5:
		print("O'yin tugadi")
		if userScore>compScore:
			print("Siz yutdingiz!")
		elif compScore>userScore:
			print("Kompyuter yutdi, siz yutqazdingiz!")
		else:
			print("Durrang!")
			


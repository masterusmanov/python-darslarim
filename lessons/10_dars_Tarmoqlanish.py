# TArmoqlanishda IF fuksiyasi bor, IF -bu ingiliz tilidan tarjima qilinganda AGAR ma'nosini beradi

#avtolar = ('volvo', 'kia', 'bmw', 'tayota', 'hundai')
#print(avtolar)
#for avto in avtolar:
	#print(avto.title())
#for avto in avtolar:
	#print(avto.upper())
#for avto in avtolar:
	#if avto == 'bmw':
		#print(avto.upper())
	#else:						#ELSE - ingilizchadan tarjima qilinganda "AKS HOLDA" ma'nosini beradi
		#print(avto.title())
#a = 5
#print(a == 5)
#print(a == 6)

#ism = 'Elyor'
#ism.lower() == "elyor"
#print(ism == "elyor")


#ism = input('Ismingiz nima?\n>>>')
#if ism.lower() != 'elyor':
	#print(f"Uzr, {ism.title()} biz Elyorni kutayapmiz! ")
#else:
#	print("salom Elyor")
#

#javob = float(input("100X12 nechiga teng?>>>"))
#if javob != 1200:
#	print("javob xato!")
#else:
#	print("To'g'ri javob")

#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh<=34:
#	print("Hush kelibsiz!")
#else:
#	print("Kirish taqiqlanadi!")

#login = input("Yangi login tanlang! ")
#if len(login)<=5:				#bu yerda LEN funksiyasi matnni uzunligini tekshiradi
#	print("Login 5 harfdan ko'proq bo'lishi kerak! ")

#yil = int(input("Tug'ilgan yilingizni kiriting!>>>"))
#if 2021-yil<18:
#	print(f"Yoshingiz {2021-yil}da ekan")
#	print("Sizga kirish taqiqlanadi!")
#else:
#	print("Hush kelibsiz!")

#yosh = int(input("Yoshingiz nechida?>>>"))
#if yosh>65: print("Sizni qon guruhingiz 1-guruh ekan")


#x, y = 50, 40.99
#print("x<y") if x>y else print("x>y")


#Vazifa


yangi_cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in yangi_cars:
	print(car.title())
for car in yangi_cars:
	print(car.upper())
for car in yangi_cars:
	if car == 'gm':
		print(car.upper())
	else:
		print(car.title())


javob = str(input("Sizga qaysi mashina yoqadi?>>>")) 	#biror bir narsa so'ralganda str fuksiyasi qo'yiladi
if javob != 'kia':										#raqamda float fuksiyasi qo'yiladi
	print("Fikrimiz bir hil ekan")
else:
	print("Siz bilan fikrimiz qarama-qarshi ekan!")


login = input("Loginingizni kiriting!>>>")
if login.lower() == 'admin':
	print("Hush kelibsiz Admin, Foydalanuvchilar ro'yhatini ko'rasizmi?")
else:
	print(f"Hush Kelibsiz {login.title()}!")



x = float(input("Birinchi sonni kiriting!"))
y = float(input("Ikkinchi sonni kiriting!"))
if x==y:
	print(f"Sonlar teng: {x}={y}")
else:
	print(f"sonlar teng qiymatga ega emas!")

son = float(input("Istalgan sonni kiriting!"))
print("Son mafiy") if son<0 else print("Musbat son")


son = float(input("Istalgan sonni kiriting!"))
print(son**(1/2)) if son>0 else print("son musbat")		#bu yerda **(1/2) ildiz chiqarish ekan
#yosh = int(input('Yoshingiz nechida?\n>>>'))
#if yosh<=4:
#	print("Sizga kirish bepul!")
#elif yosh<=12:							#ELIF - funksiyasi ingiliz tilidan AKS HOLDA ma'nosini beradi
#	print("Sizga kirish 5000 so'm!")
#elif yosh<=17:
#	print("SIzga kirish 8000 so'm!")
#else:									#ELSE - funksiyasi ingiliztilidan AGAR ma'nosini beradi
#	print("Sizga kirish 10000 so'm!")


#yosh = int(input("Yoshingiz nechida?\n>>>"))
#if yosh<=4:
#	narx = 0
#elif yosh<=12:
#	narx = 5000
#elif yosh<=18:
#	narx = 8000
#else:
#	narx = 10000

#print(f"Sizzga kirish {narx} so'm")


#kun = input("Bugun qanday kun? >>>")
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#	print('Bugun dam olish kuni!')
#else:
#	print('BUgun ish kuni!')

#kun = input("Bugun qanday kun? >>>")
#harorat = float(input("Havo harorati qanday?"))
#if kun.lower()=='yakshanba' and harorat>=30:
#	print("Bugun biz daryoga cho'milgani boramiz!")
#elif kun.lower()=='yakshanba' and harorat<=30:
#	print("Bugun biz uyda kino ko'ramiz!")
#else:
#	print("Ish kuni!")

#narx = 15000
#choy = True
#salat = False

#if choy and salat:
#	narx = narx + 10000
#elif choy or salat:
#	narx = narx + 5000

#print(f"Jami {narx} so'm")

#narh = 15000
#choy = 1
#salat = 1
#non = 1
#kompot = 1
#assorti = 1

#if choy:
#	print("MIjoz choy oldi!")
#	nath = narh + 2000

#if salat:
#	print("Mijoz salat oldi!")
#	narh = narh + 4000

#if non:
#	print("Mijoz non oldi!")
#	narh = narh + 3000

#if kompot:
#	print("Mijoz kompot oldi!")
#	narh = narh + 10000

#if assorti:
#	print("Mijoz assorti oldi!")
#	narh = narh + 15000

#print(f"Jami {narh} so'm bo'ldi")


#menu = ['qazonkabob', 'shashlik', 'somsa', 'manti', 'osh']
#ovqat = input('Nima ovqatlaringiz bor? ')
#f ovqat.lower() in menu:
#	print('Byurtmangiz qabul qilindi!')
#else:
#	print('Afsuski bizda bunday ovqat qolmadi')



#menu = ['qazonkabob', 'shashlik', 'somsa', 'manti', 'osh']
#ovqat = input('Nima ovqatlaringiz bor? ')
#if ovqat.lower() not in menu:
#	print('Afsuski bizda bunday ovqat qolmadi')
#else:
#	print('Byurtmangiz qabul qilindi!')


#menu = ['qazonkabob', 'shashlik', 'somsa', 'manti', 'osh']
#buyurtmalar = ['shorva', 'mastava', 'bilinchik', 'manti', 'osh']

#if buyurtmalar:
#	for taom in buyurtmalar:
#		if taom in menu:
#			print(f"Menuda {taom} bor!")
#		else:
#			print(f"Kechirasiz, menuda {taom} yo'q!")
#else:
#	print("Kechirasiz savatcha bo'sh!")

###		AMALIYOT

#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa
#"Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

#son = float(input("Siz juft son kiriting!\n>>>"))
#if son%2:											#Bu matematik amalda %2 juft son deyiladi
#	print('Bu son juft emas!')						# %2 - kvadrat;	%3 - kub:
#else:
#	print('Rahmat!') 


#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta
#narhini quyidagicha chiqaring:

#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

#yosh = int(input("Yoshingiz nechida?"))
#if yosh<=4 or yosh>=60:
#	narh = 0
#elif yosh < 18:
#	narh = 10000
#else:
#	narh = 15000

#print(f"Chipta {narh} so'm!")



#Foydalanuvchidan ikita son kiritishni so'rang,
#sonlarni solishtiring va ularning teng yoki katta/kichikligi
#haqida xabarni chiqaring

#x = float(input('Birinchi sonni kiriting!'))
#y = float(input('Ikkinchi sonni kiriting!'))
#if x==y:
#	print(f"{x}={y}")
#elif x<y:
#	print(f"{X}<{y}")
#else:
#	print(f"{x}>{y}")



#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi,
#savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot
#kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring
#va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda,
#"Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

#mahsulotlar = ['kartoshka', 'sabzi', 'piyoz', 'karam', 'sholgom', 'bodring', 'pomidor', 'balgar', 'qalampir', 'tomat', 'tuz']
#savat = []
#for n in range(5):
#	savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing! "))
#for mahsulot in savat:
#	if mahsulot in mahsulotlar:
#		print(f"Do'konimizda {mahsulot} bor!")
#	else:
#		print(f"Do'konimizda {mahsulot} yo'q!")
	

#Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot
#kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang,
#bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan
#ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha
#mahsulotlar do'konimizda bor" degan xabarni,
#aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring

#mahsulotlar = ['kartoshka', 'sabzi', 'piyoz', 'karam', 'sholgom', 'bodring', 'pomidor', 'balgar', 'qalampir', 'tomat', 'tuz']
#bor_mahsulotlar = []
#for n in range(5):
#	bor_mahsulotlar.append(input("Savatga {n+1} ta mahsulot kiriting! "))
#mavjud_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in bor_mahsulotlar:
#	if mahsulot in mahsulotlar:
#		mavjud_mahsulotlar.append(mahsulot)
#	else:
#		mavjud_emas.append(mahsulot)

#if mavjud_emas:
#	print(f"Do'konimizda quyidagi mahsulotlar yo'q!")
#	for mahsulot in mavjud_emas:
#		print(mahsulot)
#else:
#	print("Siz so'raga barcha mahsulotlar do'konimizda bor!")


#users = ['abror', 'zokir', 'ilhom', 'said', 'akram', 'aziz']
#login = input("Yangi login kiriting! ")

#if login.lower() in users:
#	print('Login band, yangi login tanlang!')
#else:
#	print(f"Hush kelibsiz!, {login.title()}")




#Foydalanuvchidan biror butun son kiritishni so'rang.
#Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan
#qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
son = int(input("Butun son kiriting!"))
for n in range(2,11):
	if not (son%n):
		print(f"{son} soni {n} ga qoldiqsiz bo'linadi!")
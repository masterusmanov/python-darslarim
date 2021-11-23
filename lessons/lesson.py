amal = input("NIma qilamiz? (+, -, *, /, %, **, //) ")

a = float(input("Birinchi raqamni kiriting: "))
b = float(input("Ikkinchi raqamni kiriting: "))

if amal=="+":
	c = a + b
	print("Natija: " + str(c))
elif amal=="-":
	c = a - b
	print("Natija: " + str(c))
elif amal=="*":
	c = a * b
	print("Natija: " + str(c))
else:
	print("Noto'g'ri amal kiritildi")


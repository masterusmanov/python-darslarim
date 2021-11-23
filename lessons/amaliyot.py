ismlar = ['Murodxon', 'Murodilloxon', 'Murodchik']
#print(ismlar)

print('Assalomu alaykum ' + ismlar[0] + ' bugun choyxona bormi?')
print(f"{ismlar[1]} va {ismlar[2]} aka-uka emas, bir o'zi")
print(ismlar[-1] + " g'ildirakni g'izillatib g'ildiratdi")

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. 
#Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_789_000, 112.4]
sonlar[0] = sonlar[0]+sonlar[-1]
sonlar[1] = -67.8
sonlar[4] = sonlar[4] + 37
del sonlar[5]
print(sonlar)


#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning,
#ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Imom Termiziy']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']
print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan \n zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan \n suhbat qilishni hoxlar edim")

friends = []
friends.append('Tohir')
friends.append('Shuhrat')
friends.append('Dilmurod')
friends.append('Farruh')
print(friends)


friends.remove("Tohir")
friends.remove("Farruh")
print(friends)

friends.append("Botir")
friends.insert(1, "Farhod")
friends.insert(0, "Sherali")
print(friends)

#POP indeksi - bu ro'yhatni ichidan sug'urib olish
mehmonlar = []
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)
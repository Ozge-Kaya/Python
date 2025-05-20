print("Welcome to the tip calculator!/ Bahşiş hesaplayıcısına hoşgeldiniz :)")
bill = float(input("What was the total bill? / Toplam hesap $"))
tip = int(input("What percentage tip would you like to give?/ Ne kadar bahşiş vermek istersiniz? %10, %12, %15"))
people = int(input("How many people to split the bill? / Hesabı kaç kişi paylaşacak? "))
sonuc = (bill * (tip/100)+bill)/ people
print(round(sonuc,2))




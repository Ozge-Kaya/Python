import random
import string

def sifre_olustur(uzunluk):
    # Şifre karakter kümesi / Password character set
    karakterler = string.ascii_letters + string.digits + string.punctuation
    # ascii_letters: abcABC...
    # digits: 0123456789
    # punctuation: !@#%&...

    # Rastgele karakter seçerek şifre oluştur / Generate password
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre

print("Şifre Oluşturucuya Hoş Geldiniz!")
print("Welcome to the Password Generator!")

try:
    uzunluk = int(input("Şifrenin uzunluğunu girin (örnek: 12): "))
    # Enter the length of the password

    if uzunluk < 4:
        print("⚠️ Şifre çok kısa! En az 4 karakter girin. / Password too short! Minimum 4 characters.")
    else:
        yeni_sifre = sifre_olustur(uzunluk)
        print(f"✅ Oluşturulan şifre / Generated password: {yeni_sifre}")
except ValueError:
    print("❌ Lütfen geçerli bir sayı girin! / Please enter a valid number.")

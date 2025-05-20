print("🍕 Welcome to the Pizza Order App! / Pizza sipariş uygulamasına hoşgeldiniz")
sizes = {
    "small": 50,
    "medium": 75,
    "large": 100
}
toppings = {
    "olives": 5,
    "mushrooms": 7,
    "sausage": 10
}
size = input("Choose your pizza size / Pizza boyutunu seçin (small / medium / large): ").lower()

quantity = int(input("How many pizzas would you like? / Kaç tane pizza istersiniz: "))

# Temel toplam fiyatı hesapla .get ile size girilen değeri döndür, girilen tanımsız ise 0 ile dönsün
total = sizes.get(size, 0) * quantity

print("Would you like to add extra toppings? / Ekstra malzeme ister misiniz? (yes/no)")
answer = input().lower()

if answer == "yes":
    print("Available toppings / Mevcut malzemeler:", ", ".join(toppings.keys()))
    selected = input("Enter toppings separated by comma - Malzemeleri virgülle ayırarak yazın: ").lower().split(",")
    for item in selected:
        total += toppings.get(item.strip(), 0) * quantity  # Her malzeme için toplamı artır

print(f"Your total is: / Toplam: {total} TL")
print("Your order is being prepared. Thank you! / Siparişiniz hazırlanıyor. Teşekkürler!")
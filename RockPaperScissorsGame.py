import random

def oyun():
    print("🎮 Taş - Kağıt - Makas oyununa hoş geldin!")
    print("🎮 Welcome to Rock - Paper - Scissors game!")

    secenekler = ["taş", "kağıt", "makas"]

    while True:
        oyuncu_secimi = input("Seçimini yap (taş/kağıt/makas): ").lower()
        # Make your choice (rock/paper/scissors)

        if oyuncu_secimi not in secenekler:
            print("❌ Geçersiz seçim! Lütfen tekrar dene.")
            continue

        bilgisayar_secimi = random.choice(secenekler)

        print(f"Senin seçimin: {oyuncu_secimi}")
        print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
        # Your choice vs Computer's choice

        if oyuncu_secimi == bilgisayar_secimi:
            print("🤝 Berabere! / It's a tie!")
        elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
             (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
             (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
            print("🎉 Kazandın! / You win!")
        else:
            print("😢 Kaybettin. / You lose.")

        tekrar = input("Tekrar oynamak ister misin? (e/h): ")
        if tekrar.lower() != "e":
            print("👋 Oyun bitti. Görüşmek üzere!")
            break

# Oyunu başlat / Start the game
oyun()
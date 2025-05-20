def start_game():
    print("You wake up in a cold, dark labyrinth./ Soğuk ve karanlık bir labirentte uyanıyorsun.")
    print("You see two tunnels ahead. / Önünde iki tünel görüyorsun.")
    print("1. Enter the left tunnel. / Sol tünele gir.")
    print("2. Enter the right tunnel. / Sağ tünele gir.")
    choice1 = input("Your choice / Seçimin (1 or 2): ")

    if choice1 == "1":
        left_tunnel()
    elif choice1 == "2":
        right_tunnel()
    else:
        print("Invalid choice. Try again. / Geçersiz seçim. Lütfen tekrar deneyin.")
        start_game()

def left_tunnel():
    print("\n You carefully step into the left tunnel. / Dikkatlice sol tünele giriyorsun.")
    print("You find a locked door and a rusty lever. / Kilitli bir kapı ve paslı bir kol buluyorsun.")
    print("1. Pull the lever./  Kolu çek.")
    print("2. Try to break the door. / Kapıyı kırmayı dene.")
    choice2 = input("Your choice / Seçimin (1 or 2): ")

    if choice2 == "1":
        print("\n The door creaks open, revealing a glowing exit! /  Kapı gıcırdayarak açılıyor, ışıklı bir çıkış görüyorsun!")
        print("🎉 You have escaped the labyrinth! / Labirentten kaçtın!")
    elif choice2 == "2":
        print("\n As you hit the door, a trap is triggered!/ Kapıyı kırmaya çalışırken bir tuzak çalışıyor!")
        print("☠️ Poison darts shoot from the walls. Game Over./️ Duvarlardan zehirli oklar fırlıyor. Oyun bitti.")
    else:
        print("Invalid choice. Try again. / Geçersiz seçim. Lütfen tekrar deneyin.")
        left_tunnel()

def right_tunnel():
    print("\n🕷️ The right tunnel is filled with cobwebs and eerie noises. / Sağ tünel örümcek ağlarıyla dolu ve korkunç sesler geliyor.")
    print("You see a shadow moving in the distance./ Uzakta hareket eden bir gölge görüyorsun.")
    print("1. Approach the shadow./ Gölgeye yaklaş.")
    print("2. Turn back and take the other tunnel. / Geri dön ve diğer tünele git.")
    choice3 = input("Your choice / Seçimin (1 or 2): ")

    if choice3 == "1":
        print("\n A ghost appears and whispers riddles. / Bir hayalet belirir ve bilmeceler fısıldar.")
        print("You fail to answer and are lost forever in the maze. /Cevaplayamazsın ve sonsuza kadar labirentte kaybolursun.")
        print("☠️ Game Over./ Oyun Bitti.")
    elif choice3 == "2":
        left_tunnel()
    else:
        print("Invalid choice. Try again. / Geçersiz seçim. Lütfen tekrar deneyin.")
        right_tunnel()

start_game()

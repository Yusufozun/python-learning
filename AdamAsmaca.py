import random
KELIMELER = ["python", "yazilim", "degisken", "döngü", "fonksiyon", "siber", "güvenlik", "algoritma"]
ADAM_ASMACA = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ========="""
]

gizli_kelime = random.choice(KELIMELER).lower()
gizli_string = ""
yanlis_tahmin_sayisi = 0
MAX_CAN = len(ADAM_ASMACA) - 1

print("--- ADAM ASMACA OYUNUNA HOŞ GELDİNİZ ---")

while yanlis_tahmin_sayisi < MAX_CAN:
    print(ADAM_ASMACA[yanlis_tahmin_sayisi])
    print("\n")
    kalan_karakter = 0
    for character in gizli_kelime:
        if character in gizli_string:
            print(character, end=" ")
        else:
            print("_", end=" ")
            kalan_karakter += 1
    print("\n")
    if kalan_karakter == 0:
        print("🎉 Tebrikler! Kelimeyi doğru tahmin ettiniz ve adamı kurtardınız!")
        break
    tahmin = input("Bir harf tahmin edin: ").lower().strip()

    if not tahmin or len(tahmin) > 1:
        print("Lütfen sadece tek bir harf girin!\n")
        continue

    if tahmin in gizli_string:
        print("Bu harfi zaten tahmin etmiştiniz!\n")
        continue

    gizli_string += tahmin
    if tahmin not in gizli_kelime:
        yanlis_tahmin_sayisi += 1
        print(f"❌ Yanlış tahmin! Kalan hakkınız: {MAX_CAN - yanlis_tahmin_sayisi}\n")
if yanlis_tahmin_sayisi == MAX_CAN:
    print(ADAM_ASMACA[yanlis_tahmin_sayisi])
    print("\n☠️ Maalesef adam asıldı! Oyun bitti.")
    print(f"Gizli kelime şuydu: {gizli_kelime}")

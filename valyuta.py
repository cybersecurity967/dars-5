import requests


def kurs_hisobla():
    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

    try:
        response = requests.get(url)
        valyutalar = response.json()
    except Exception as xato:
        print("Internet yoki API bilan bog'lanishda xatolik:", xato)
        return

    valyuta_kodi = input("Valyuta kodini kiriting (masalan, USD): ").strip().upper()

    try:
        miqdor = float(input("Miqdorni kiriting: "))
        if miqdor < 0:
            print("Miqdor manfiy bo'lishi mumkin emas!")
            return
    except ValueError:
        print("Xatolik: Miqdor faqat son bo'lishi kerak!")
        return

    topildi = False
    for v in valyutalar:
        if v["Ccy"] == valyuta_kodi:
            topildi = True
            nomi = v["CcyNm_UZ"]
            kurs = float(v["Rate"])
            nominal = float(v["Nominal"])

            bir_birlik_kurs = kurs / nominal
            jami_som = miqdor * bir_birlik_kurs

            print("\n------------------------------")
            print(f"Valyuta: {nomi}")
            print(f"Miqdor: {miqdor} {valyuta_kodi}")
            print(f"1 {valyuta_kodi} kursi: {bir_birlik_kurs:,.2f} so'm")
            print(f"Jami: {jami_som:,.2f} so'm")
            print("------------------------------")
            break

    if not topildi:
        print(f"Xatolik: '{valyuta_kodi}' kodi bo'yicha valyuta topilmadi!")


if __name__ == "__main__":
    kurs_hisobla()
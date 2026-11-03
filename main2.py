import lugat

sozlar = {}

lugat.soz_qosh(sozlar, "apple", "olma")
lugat.soz_qosh(sozlar, "book", "kitob")
lugat.soz_qosh(sozlar, "computer", "kompyuter")
lugat.soz_qosh(sozlar, "water", "suv")
lugat.soz_qosh(sozlar, "sky", "osmon")

print("--- Lug'atdagi barcha so'zlar ---")
lugat.lugatni_kor(sozlar)

print("\n--- So'z qidirish ---")
print("apple:", lugat.soz_qidir(sozlar, "apple"))
print("car:", lugat.soz_qidir(sozlar, "car"))
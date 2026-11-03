import parol

uzunlik = int(input("Parol uzunligini kiriting: "))

natija = parol.parol_yarat(uzunlik)
print(f"Yaratilgan parol: {natija}")

xavfsizmi = parol.parol_tekshir(natija)
print(f"Parol 8 tadan uzunmi: {xavfsizmi}")
import baholash

talabalar = {"Ali": 95, "Vali": 82, "Hasan": 65, "Husan": 45, "Zuhra": 88}

ballar_royxati = list(talabalar.values())

print("--- Har bir talaba bahosi ---")
for ism, ball in talabalar.items():
    baho = baholash.baho_aniqla(ball)
    print(f"{ism}: {ball} ball -> {baho}")

ortacha = baholash.ortacha_hisobla(ballar_royxati)
eng_yuqori = baholash.eng_yaxshi_ball(ballar_royxati)

print(f"\nO'rtacha ball: {ortacha}")
print(f"Eng yuqori ball: {eng_yuqori}")
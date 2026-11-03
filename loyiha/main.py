from oyinlar import son_topish, tanga

print("Tanga tashlandi:", tanga.tanga_tanga_tashla() if hasattr(tanga, 'tanga_tanga_tashla') else tanga.tanga_tashla())

sirli = son_topish.son_yarat(1, 10)
print("1 dan 10 gacha son o'ylandi.")

taxmin = 5
print(f"Taxmin: {taxmin} -> {son_topish.tekshir(taxmin, sirli)}")
print(f"Sirli son {sirli} edi.")
def soz_qosh(lugat, soz, tarjima):
    lugat[soz] = tarjima


def soz_qidir(lugat, soz):
    return lugat.get(soz, "Bunday so'z topilmadi")


def lugatni_kor(lugat):
    for soz, tarjima in lugat.items():
        print(f"{soz} -> {tarjima}")
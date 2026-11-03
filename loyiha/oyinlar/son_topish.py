import random


def son_yarat(minimum, maksimum):
    return random.randint(minimum, maksimum)


def tekshir(taxmin, sirli_son):
    if taxmin > sirli_son:
        return "Kichikroq son ayting"
    elif taxmin < sirli_son:
        return "Kattaroq son ayting"
    else:
        return "To'g'ri topdingiz!"
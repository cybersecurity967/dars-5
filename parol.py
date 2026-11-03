import random
import string


def parol_yarat(uzunlik):
    belgilar = string.ascii_letters + string.digits + string.punctuation

    tasodifiy_belgilar = random.choices(belgilar, k=uzunlik)

    yangi_parol = "".join(tasodifiy_belgilar)
    return yangi_parol


def parol_tekshir(parol):
    return len(parol) >= 8
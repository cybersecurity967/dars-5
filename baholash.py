def baho_aniqla(ball):
    if 90 <= ball <= 100:
        return "A'lo"
    elif 70 <= ball < 90:
        return "Yaxshi"
    elif 50 <= ball < 70:
        return "Qoniqarli"
    elif 0 <= ball < 50:
        return "Qoniqarsiz"
    else:
        return "Noto'g'ri ball"


def ortacha_hisobla(ballar):
    if not ballar:
        return 0
    return sum(ballar) / len(ballar)


def eng_yaxshi_ball(ballar):
    if not ballar:
        return None
    return max(ballar)
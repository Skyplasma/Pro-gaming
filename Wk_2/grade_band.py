score1 = float(input("score 0 to 100: "))


def score_to_band(score: float) ->str:
    if 0 > score > 100:
        return"Invalid score"
    elif score >= 85:
        return"HD"
    elif score>= 75:
        return"D"
    elif score>= 65:
        return"C"
    elif score>= 50:
        return"P"
    else:
        return"F"

print(score_to_band(score1))

def grade(number: int):
    if number > 84 :
        return "A"
    if number <=84 and number > 76:
        return"B"
    if number <= 76 and number > 60:
        return "C"
    if number <= 60 and number >= 50:
        return "D -> PASS"
    if number < 50:
        return "D -> FAIL"
    if number >100 or number < 0:
        return "Grade number is invalid !!!!"
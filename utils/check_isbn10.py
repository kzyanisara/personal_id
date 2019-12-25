def is_valid(isbn10):
    first_9 = isbn10[0:9]
    chk_digit = isbn10[-1]
    sum = 0
    j = 10

    for i in first_9:
        i = int(i)
        sum = sum + (i * j)
        j = j - 1

    fract = sum % 11
    our_chk_digit = str(11 - fract)[-1]

    if our_chk_digit == chk_digit:
        return True
    else:
        return False
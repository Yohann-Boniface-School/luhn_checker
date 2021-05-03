def convert(n: int) -> int:
    if n < 10:
        return n

    return sum(divmod(n, 10))


def check(card) -> bool:
    card_digits = [int(x) for x in str(card) if x not in "-_ "]
    checksum = card_digits.pop()
    key = sum(convert(digit * (((c + 1) % 2) + 1)) for c, digit in enumerate(card_digits))

    return not (key + checksum) % 10

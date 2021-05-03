from typing import Union, Iterable


def convert(n: int) -> int:
    """ 
    An inner function that convert two digit integer into single digit.
    :param n: integer to convert
    :return: converted integer
    """
    return n if n < 10 else sum(divmod(n, 10))


def check(card: Union[int, Iterable[Union[int, str]]]) -> bool:
    """
    Check the validity of a given card
    :param card: the number of the card in a integer or string value
    :return:
    """
    card_digits = [int(x) for x in str(card) if x not in "-_ "]
    checksum = card_digits.pop()
    key = sum(convert(digit * (((c + 1) % 2) + 1)) for c, digit in enumerate(card_digits))

    return not (key + checksum) % 10


def main() -> None:
    card = input("card to check: ")
    print(f"Card is {'in' * (not check(card))}valid")


if __name__ == '__main__':
    main()

from typing import Iterable, List, Union


def check(card: Union[int, Iterable[Union[int, str]]]) -> bool:
    """Check the validity of a given card."""
    card_digits: List[int] = [int(x) for x in str(card) if x not in "-_ "]
    checksum: int = card_digits.pop()
    key: int = sum(sum(divmod(digit * (((c + 1) % 2) + 1), 10)) for c, digit in enumerate(card_digits))
    return not (key + checksum) % 10


def main() -> None:
    card: str = input("card to check: ")
    print(f"Card is {'in' * (not check(card))}valid")


if __name__ == '__main__':
    main()

import re
from collections import Counter


def is_palindrome(text: str) -> bool:
    normalized = text.replace(" ", "").lower()
    return normalized == normalized[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def count_vowels(text: str) -> int:
    vowels = {"a", "e", "i", "o", "u", "y", "ą", "ę", "ó"}
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


def calculate_discount(price: float, discount: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError("discount must be between 0 and 1")
    return float(price * (1 - discount))


def flatten_list(nested_list: list) -> list:
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def word_frequencies(text: str) -> dict:
    words = re.findall(r"[^\W_]+", text.lower())
    return dict(Counter(words))


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True
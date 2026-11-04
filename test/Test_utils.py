import math

def is_palindrome(text:str)->bool:
    # Usuwamy spacje i zmieniamy wszystkie litery na małe
    no_space = "".join(text.split()).lower()

    # Sprawdzamy, czy tekst czytany od tyłu jest taki sam
    return no_space == no_space[::-1]

def fibonacci(n:int)->int:
  if n < 0:
    raise ValueError("Must be positive")
  a, b = 0, 1
  for _ in range(n):
    a, b = b, a + b
  return a

def count_vowels(text: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

    return sum(1 for char in text.lower() if char in vowels)


def calculate_discount(price: float, discount: float) -> float:

    if not (0.0 <= discount <= 1.0):
        raise ValueError("Discount must be <0;1>")

    return price * (1.0 - discount)


def flatten_list(nested_list: list) -> list:
    flat_list = []

    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)

    return flat_list


from collections import Counter
import string


def word_frequencies(text: str) -> dict:
    text_lowercase = text.lower()
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    clean_text = text_lowercase.translate(translator)
    words = clean_text.split()

    return dict(Counter(words))

def isprime(n: int) -> bool:
  if n < 2:
    return False
  for i in range(2, int(math.isqrt(n)) + 1):
    if n % i == 0:
      return False
  return True
import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r"\b\d+\.\d+\b"
    for num in re.findall(pattern, text):
        yield float(num)

def sum_profit(text: str, func: Callable):
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

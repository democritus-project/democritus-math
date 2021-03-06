# Democritus Math

[![PyPI](https://img.shields.io/pypi/v/d8s-math.svg)](https://pypi.python.org/pypi/d8s-math)
[![CI](https://github.com/democritus-project/d8s-math/workflows/CI/badge.svg)](https://github.com/democritus-project/d8s-math/actions)
[![Lint](https://github.com/democritus-project/d8s-math/workflows/Lint/badge.svg)](https://github.com/democritus-project/d8s-math/actions)
[![codecov](https://codecov.io/gh/democritus-project/d8s-math/branch/main/graph/badge.svg?token=V0WOIXRGMM)](https://codecov.io/gh/democritus-project/d8s-math)
[![The Democritus Project uses semver version 2.0.0](https://img.shields.io/badge/-semver%20v2.0.0-22bfda)](https://semver.org/spec/v2.0.0.html)
[![The Democritus Project uses black to format code](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://choosealicense.com/licenses/lgpl-3.0/)

Democritus functions<sup>[1]</sup> for working with math.

[1] Democritus functions are <i>simple, effective, modular, well-tested, and well-documented</i> Python functions.

We use `d8s` (pronounced "dee-eights") as an abbreviation for `democritus` (you can read more about this [here](https://github.com/democritus-project/roadmap#what-is-d8s)).

## Installation

```
pip install d8s-math
```

## Usage

You import the library like:

```python
from d8s_math import *
```

Once imported, you can use any of the functions listed below.

## Functions

  - ```python
    def fibonacci_sequence(n: int) -> List[int]:
        """Return the first n digits of the fibonacci sequence."""
    ```
  - ```python
    def fibonacci(n: int) -> int:
        """Return the value of the Fibonacci sequence at index n."""
    ```
  - ```python
    def number_closest(a, b, target):
        """Return a or b, whichever is closest to the target."""
    ```
  - ```python
    def number_furthest(a, b, target):
        """Return a or b, whichever is furthest to the target."""
    ```
  - ```python
    def cartesian_product(a: Any, *args: Any, repeat: int = 1):
        """."""
    ```
  - ```python
    def sympy_symbol(symbol_name: str):
        """."""
    ```
  - ```python
    def equation_solve(equation: str, symbols: List[str]):
        """."""
    ```
  - ```python
    def expression_explore(expression: str, symbol: str, start: int, end: int, step: int):
        """."""
    ```
  - ```python
    def one_cold_encode(items: list, *, reverse: bool = False) -> List[list]:
        """."""
    ```
  - ```python
    def one_hot_encode(items: list, *, reverse: bool = False) -> List[list]:
        """."""
    ```
  - ```python
    def is_integer_tuple(possible_integer_tuple: Any) -> bool:
        """."""
    ```
  - ```python
    def string_to_number(string: str) -> Union[int, float]:
        """Convert a number as a string into either an integer or float."""
    ```
  - ```python
    def first_arg_as_decimal(func):
        """Convert the first argument to a number (either integer or float)."""
    ```
  - ```python
    def arguments_as_decimals(func):
        """Convert all arguments to numbers (either integers or floats)."""
    ```
  - ```python
    def decimal_to_gray_code(num: Union[str, int, float]) -> integerTupleType:
        """Convert the given number to a gray code. This function was inspired by the code here: https://en.wikipedia.org/wiki/Gray_code#Converting_to_and_from_Gray_code."""
    ```
  - ```python
    def gray_code_to_decimal(num: integerTupleType) -> int:
        """Convert the given number to a gray code. This function was inspired by the code here: https://en.wikipedia.org/wiki/Gray_code#Converting_to_and_from_Gray_code."""
    ```
  - ```python
    def decimal_to_hex(decimal_number):
        """."""
    ```
  - ```python
    def hex_to_decimal(hex):
        """."""
    ```
  - ```python
    def roman_numeral_to_decimal(roman_numeral: str) -> int:
        """."""
    ```
  - ```python
    def decimal_to_roman_numeral(decimal_number) -> str:
        """."""
    ```
  - ```python
    def integer_tuple_to_decimal(integer_tuple: integerTupleType) -> int:
        """Return the decimal form of the given number (represented as an integer tuple)."""
    ```
  - ```python
    def integer_to_decimal(num: Union[str, int, float], base: int) -> int:
        """Convert the number of the given base to a decimal number."""
    ```
  - ```python
    def decimal_to_base(decimal_number: Union[str, int, float], base: int):
        """Convert the decimal_number to the given base."""
    ```
  - ```python
    def outer_division():
        """."""
    ```
  - ```python
    def outer_product(a: int, b: int, a_start: int = 1, b_start: int = 1):
        """Return a two-dimensional array with the results of range(a_start, a+1) multiplied by range(b_start, b+1)."""
    ```
  - ```python
    def multiplication_table(a: int, b: int, a_start: int = 1, b_start: int = 1):
        """."""
    ```
  - ```python
    def number_evenly_divides(a, b):
        """Return True if a evenly divides b. Otherwise, return False."""
    ```
  - ```python
    def number_evenly_divided_by(a, b):
        """Return True if a is evenly divided by b. Otherwise, return False."""
    ```
  - ```python
    def fraction_examples(n=10, *, fractions_as_strings: bool = True):
        """Create n fractions."""
    ```
  - ```python
    def iterable_differences(iterable):
        """Find all of the possible differences of all possible orders of the given iterable."""
    ```
  - ```python
    def combinations(iterable, length=None):
        """Return all possible combinations of the given length which can be created from the given iterable. If no length is given, we will find all combinations of all lengths for the given iterable."""
    ```
  - ```python
    def combinations_with_replacement(iterable, length=None):
        """Return all possible combinations of the given length which can be created from the given iterable. If no length is given, we will find all combinations of all lengths for the given iterable."""
    ```
  - ```python
    def prod(iterable):
        """Get the product of the iterable."""
    ```
  - ```python
    def permutations(iterable, length=None):
        """Return all possible permutations of the given iterable. If no length is given, we will find all permutations of all lengths for the given iterable"""
    ```
  - ```python
    def fraction_simplify(fraction_string):
        """Simplify the fraction represented as a string."""
    ```
  - ```python
    def remainder(dividend, divisor):
        """."""
    ```
  - ```python
    def floor(number):
        """."""
    ```
  - ```python
    def ceiling(number):
        """."""
    ```
  - ```python
    def factorial(number):
        """."""
    ```
  - ```python
    def fraction_complex_to_mixed_fraction(fraction_string):
        """Simplify the fraction represented as a string."""
    ```
  - ```python
    def fraction_mixed_to_complex_fraction(fraction_string):
        """Simplify the fraction represented as a string."""
    ```
  - ```python
    def dot_product(item_a, item_b):
        """Find the dot product for the two items. See https://en.wikipedia.org/wiki/Dot_product for more details."""
    ```
  - ```python
    def percent(ratio):
        """Return the ratio as a percentage."""
    ```
  - ```python
    def gcd(number1, number2):
        """Return the greatest common divisor."""
    ```
  - ```python
    def ratio(number1, number2):
        """Return the ratio of the two numbers in the form 1:2. For example, if given 5 and 10, this function would return "1:2". If given 2 and 20, this function would return "1:10"."""
    ```
  - ```python
    def transpose(matrix):
        """Transpose the given matrix. See https://en.wikipedia.org/wiki/Transpose."""
    ```
  - ```python
    def number_line(value, min_, max_, interval: int = 1):
        """."""
    ```
  - ```python
    def number_zero_pad(num: StrOrNumberType, length: StrOrNumberType) -> str:
        """."""
    ```
  - ```python
    def is_number(item):
        """Return whether or not the item is a number."""
    ```
  - ```python
    def number_is_even(number: StrOrNumberType):
        """."""
    ```
  - ```python
    def number_is_odd(number: StrOrNumberType):
        """."""
    ```
  - ```python
    def number_is_approx(number, approximate_value, *, relative_tolerance=1e-6):
        """."""
    ```
  - ```python
    def enumerate_range(range_string, range_split_string: str = '-'):
        """Enumerate the range specified by the string. For example, `1-3` returns `[1, 2, 3]`."""
    ```
  - ```python
    def hex_endiness_swap(hex_string):
        """Credit to: https://stackoverflow.com/questions/27506474/how-to-byte-swap-a-32-bit-integer-in-python."""
    ```
  - ```python
    def number_to_words(number):
        """Convert a number to its English representation (e.g. 100 => "One Hundred")."""
    ```
  - ```python
    def number_to_scientific_notation(number):
        """Convert the given number to scientific notation."""
    ```
  - ```python
    def number_to_engineering_notation(number):
        """Convert the given number to engineering notation."""
    ```
  - ```python
    def hex_get_bytes(hex_number, number_of_bytes):
        """Reduce a hex number number to a specific number of bytes. For example, (0x123456,2) returns '0x1234'."""
    ```

## Development

👋 &nbsp;If you want to get involved in this project, we have some short, helpful guides below:

- [contribute to this project 🥇][contributing]
- [test it 🧪][local-dev]
- [lint it 🧹][local-dev]
- [explore it 🔭][local-dev]

If you have any questions or there is anything we did not cover, please raise an issue and we'll be happy to help.

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and Floyd Hightower's [Python project template](https://github.com/fhightower-templates/python-project-template).

[contributing]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#contributing-a-pr-
[local-dev]: https://github.com/democritus-project/.github/blob/main/CONTRIBUTING.md#local-development-

import collections
import math
from typing import Any, Iterable, Tuple, List, Union, NamedTuple

from .maths_temp_utils import arguments_as_decimals


class integer_tupleType(NamedTuple):
    base: int
    digits: Tuple[int, ...]


# TODO: write prime factorization function
# TODO: write a function to determine if a number is prime or not
# TODO: write function for degrees to radians and visa-versa (`math.radians(33.1)`)

# def percentOf(percent, number):
#     """Return the given percent of the given number."""
#     pass

#     is / of = % / 100

#     (I want to write functions for "is", "of", and "%" based on the above diagram)

#     # TODO: may want to write a function to standardize percentages (e.g. 0.1 and 10 and '10' and '10%')


integer_tuple = collections.namedtuple('integer_tuple', ['base', 'digits'])


def fibonacci_sequence(n: int) -> List[int]:
    """Return the first n digits of the fibonacci sequence."""
    nums = [fibonacci(i) for i in range(n)]
    return nums


def fibonacci(n: int) -> int:
    """Return the value of the Fibonacci sequence at index n."""
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def number_closest(a, b, target):
    """Return a or b, whichever is closest to the target."""
    if abs(a - target) <= abs(b - target):
        return a
    else:
        return b


def number_furthest(a, b, target):
    """Return a or b, whichever is furthest to the target."""
    if abs(a - target) >= abs(b - target):
        return a
    else:
        return b


# def _update_equation_with_symbol_definitions(equation: str):
#     """Find all letters in the given equation and replace them with the appropriate call to the sympy.symbols function."""
#     from strings import asciiLetters

#     ascii_letters = [char for char in equation if char in asciiLetters()]

#     for letter in set(ascii_letters):
#         equation = equation.replace(letter, f'sympy.symbols("{letter}")')

#     return equation


def cartesian_product(a: Any, *args: Any, repeat: int = 1):
    """."""
    import itertools

    return list(itertools.product(a, *args, repeat=repeat))


def sympy_symbol(symbol_name: str):
    """."""
    import sympy

    return sympy.symbols(symbol_name)


def equation_solve(equation: str, symbols: List[str]):
    """."""
    import sympy

    # TODO: eventually, I would like to use the _update_equation_with_symbol_definitions to find symbols and replace them with the appropriate symbol definitions (so that the user doesn't have to provide symbols as an input)

    sympy_symbols = [sympy_symbol(symbol) for symbol in symbols]
    map(eval, sympy_symbols)
    solution = sympy.solve(equation)
    return solution


def expression_explore(expression: str, symbol: str, start: int, end: int, step: int):
    """."""
    import sympy

    for i in range(start, end, step):
        equation = f'Eq({expression}, {i})'
        yield (i, equation_solve(equation, [symbol]))


def _hot_or_cold_encoder(items: list, default_value: int, changed_value: int, *, reverse: bool = False) -> List[list]:
    results = []
    unique_items = list(set(items))
    sorted_items = sorted(unique_items, reverse=reverse)
    max_index = len(unique_items)

    for item in items:
        encoded_result = [default_value for i in range(0, max_index)]
        index_to_change = sorted_items.index(item)
        encoded_result[index_to_change] = changed_value
        results.append(encoded_result)

    return results


def one_cold_encode(items: list, *, reverse: bool = False) -> List[list]:
    return _hot_or_cold_encoder(items, 1, 0, reverse=reverse)


def one_hot_encode(items: list, *, reverse: bool = False) -> List[list]:
    return _hot_or_cold_encoder(items, 0, 1, reverse=reverse)


def is_integer_tuple(possible_integer_tuple: Any) -> bool:
    """."""
    # I'm doing a more complex check rather than isinstance(possible_integer_tuple, integer_tuple) because I was unable to get it consistently working when this function was used in other files... the current check works consistently
    is_integer_tuple = (
        isinstance(possible_integer_tuple, tuple)
        and hasattr(possible_integer_tuple, 'base')
        and hasattr(possible_integer_tuple, 'digits')
    )
    return is_integer_tuple


# TODO: make it more clear what values are expected as inputs to decimal_to_gray_code and gray_code_to_decimal -> decimal integers or binary?
@arguments_as_decimals
def decimal_to_gray_code(num: Union[str, int, float]) -> integer_tupleType:
    """Convert the given number to a gray code. This function was inspired by the code here: https://en.wikipedia.org/wiki/Gray_code#Converting_to_and_from_Gray_code."""
    gray_code = num ^ (num >> 1)
    binary_gray_code = decimal_to_base(gray_code, 2)
    return binary_gray_code


# TODO: should this function only take an integer tuple and not a string (e.g. '111') or int which will be intepreted as binary (e.g. 111)
@arguments_as_decimals
def gray_code_to_decimal(num: integer_tupleType) -> int:
    """Convert the given number to a gray code. This function was inspired by the code here: https://en.wikipedia.org/wiki/Gray_code#Converting_to_and_from_Gray_code."""
    mask = num >> 1
    while mask != 0:
        num = num ^ mask
        mask = mask >> 1
    return num


def decimal_to_hex(decimal_number):
    """."""
    return hex(decimal_number)


def hex_to_decimal(hex):
    """."""
    return integer_to_decimal(hex, 16)


def roman_numeral_to_decimal(roman_numeral: str) -> int:
    """."""
    from number_tools.converters import roman_to_integer

    result = roman_to_integer(roman_numeral)
    return result


def decimal_to_roman_numeral(decimal_number) -> str:
    """."""
    from number_tools.converters import integer_to_roman

    result = integer_to_roman(decimal_number)
    return result


# TODO: need to test integer_tuple_to_decimal functions on negative numbers (use hypothesis - it would be nice to have functions to generate examples of different types of numbers)


def integer_tuple_to_decimal(integer_tuple: integer_tupleType) -> int:
    """Return the decimal form of the given number (represented as an integer tuple)."""
    decimal_number = 0

    # flip the digits (so the smallest 'place' is first)
    flipped_digits = reversed(integer_tuple.digits)
    for index, num in enumerate(flipped_digits):
        index_multiplier = integer_tuple.base ** index
        decimal_number += index_multiplier * num

    return decimal_number


def integer_to_decimal(num: Union[str, int, float], base: int) -> int:
    """Convert the number of the given base to a decimal number."""
    number = str(num)
    # TODO: the base is currently limited to numbers between 2 and 36... generalize this so that there are no such limitations
    converted_number = int(number, base=base)
    return converted_number


def _base_converter_init(alphabet):
    """."""
    from baseconv import BaseConverter

    converter = BaseConverter(alphabet)
    return converter


def decimal_to_base(decimal_number: Union[str, int, float], base: int):
    """Convert the decimal_number to the given base."""
    if base == 1:
        results = [1 for i in range(0, decimal_number)]
        new_integer = integer_tuple(base=base, digits=tuple(results))
        return new_integer

    results = []
    max_value = base - 1

    floor_divided_value = decimal_number // base
    if floor_divided_value > max_value:
        update = list(decimal_to_base(floor_divided_value, base).digits)
        results.extend(update)
    elif floor_divided_value != 0:
        results.append(floor_divided_value)
    results.append(decimal_number % base)

    new_integer = integer_tuple(base=base, digits=tuple(results))
    return new_integer


# # TODO: I don't think the result_as_digit_list argument name is very descriptive; there is probably a better name for that argument
# def decimal_to_base(
#     decimal_number: Union[str, int, float],
#     base: int,
#     alphabet: str = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
#     result_as_digit_list: bool = False
# ):
#     """Convert the decimal_number to the given base."""
#     if base > len(alphabet):
#         result_as_digit_list = True

#     if result_as_digit_list:
#         pass
#     else:
#         alphabet_for_base = alphabet[:base]

#         if base == 1:
#             result = alphabet_for_base[0] * decimal_number
#             return result
#         else:
#             base_converter = _base_converter_init(alphabet_for_base)
#             result = base_converter.encode(decimal_number)
#             return result


def outer_division():
    # not sure if this is a thing... I presume there is a corallary to outer_product
    pass


# todo: provide an output variable
def outer_product(a: int, b: int, a_start: int = 1, b_start: int = 1):
    """Return a two-dimensional array with the results of range(a_start, a+1) multiplied by range(b_start, b+1)."""
    result = []

    for i in range(a_start, a + 1):
        result.append([i * j for j in range(b_start, b + 1)])

    return result


def multiplication_table(a: int, b: int, a_start: int = 1, b_start: int = 1):
    """."""
    return outer_product(a, b, a_start=a_start, b_start=b_start)


def number_evenly_divides(a, b):
    """Return True if a evenly divides b. Otherwise, return False."""
    b_by_a_remainder = b % a
    evenly_divides = b_by_a_remainder == 0
    return evenly_divides


def number_evenly_divided_by(a, b):
    """Return True if a is evenly divided by b. Otherwise, return False."""
    evenly_divides = number_evenly_divides(b, a)
    return evenly_divides


def fraction_examples(n=10, *, fractions_as_strings: bool = True):
    """Create n fractions."""
    from hypothesis.strategies import fractions

    from hypothesis_data import hypothesis_get_strategy_results

    fraction_object_examples = hypothesis_get_strategy_results(fractions, n=n)
    if fractions_as_strings:
        return [str(fraction) for fraction in fraction_object_examples]
    else:
        return fraction_object_examples


def iterable_differences(iterable):
    """Find all of the possible differences of all possible orders of the given iterable."""
    differences = []

    iterable_permutations = permutations(iterable, length=len(iterable))
    for permutation in iterable_permutations:
        diff = permutation[0]
        for i in permutation[1:]:
            diff = diff - i
        differences.append(diff)

    return differences


def combinations(iterable, length=None):
    """Return all possible combinations of the given length which can be created from the given iterable. If no length is given, we will find all combinations of all lengths for the given iterable."""
    import itertools

    if length is None:
        combos = []
        for l in range(1, len(iterable) + 1):
            combos.extend(combinations(iterable, length=l))
        return combos
    else:
        return list(itertools.combinations(iterable, length))


def combinations_with_replacement(iterable, length=None):
    """Return all possible combinations of the given length which can be created from the given iterable. If no length is given, we will find all combinations of all lengths for the given iterable."""
    import itertools

    if length is None:
        combos = []
        for l in range(1, len(iterable) + 1):
            combos.extend(combinations_with_replacement(iterable, length=l))
        return combos
    else:
        return list(itertools.combinations_with_replacement(iterable, length))


def prod(iterable):
    """Get the product of the iterable."""
    from functools import reduce
    import operator

    from democritus_strings import string_to_number

    # convert all of the items of the iterable to numbers
    number_iterable = map(string_to_number, iterable)

    return reduce(operator.mul, number_iterable, 1)


def permutations(iterable, length=None):
    """Return all possible permutations of the given iterable. If no length is given, we will find all permutations of all lengths for the given iterable"""
    import itertools

    if length is None:
        perms = []
        for l in range(1, len(iterable) + 1):
            perms.extend(permutations(iterable, length=l))
    else:
        perms = list(itertools.permutations(iterable, length))
    return perms


def _split_fraction(fraction_string: str) -> Tuple[int, int]:
    """Split up a fraction string and return a numerator and denominator."""
    split_fraction_string = fraction_string.split('/')

    if len(split_fraction_string) != 2:
        message = f'Unable to handle the input "{fraction_string}" as a fraction. When providing a fraction, please separate the two numbers with a "/" character.'
        raise ValueError(message)
    else:
        numerator = int(split_fraction_string[0].strip())
        denominator = int(split_fraction_string[1].strip())
        return numerator, denominator


def _split_mixed_fraction(fraction_string):
    """Split up a mixed fraction and return the whole number and the faction (e.g. "1 1/3"). This function requires that the whole number and fraction be separated by a space."""

    split_fraction_string = fraction_string.split(' ')
    if len(split_fraction_string) != 2:
        print(
            f'Unable to handle the input "{fraction_string}" as a mixed fraction. When providing a mixed fraction as an argument, please separate the whole number from the fraction with a space (and do not include spaces in the fraction).'
        )
        return None, None
    else:
        # TODO: replace all spaces around the "/" character - not sure what this comment means, but I think I fixed it with the strip below... if this comment doesn't make any more sense to you, my future self, go ahead an remove it
        whole_number = int(split_fraction_string[0].strip())
        fraction = split_fraction_string[1].strip()
        return whole_number, fraction


def fraction_simplify(fraction_string):
    """Simplify the fraction represented as a string."""
    numerator, denominator = _split_fraction(fraction_string)
    gcd_for_fraction = gcd(numerator, denominator)

    return f'{int(numerator / gcd_for_fraction)}/{int(denominator / gcd_for_fraction)}'


def remainder(dividend, divisor):
    return dividend % divisor


def floor(number):
    return math.floor(number)


def ceiling(number):
    return math.ceil(number)


def factorial(number):
    return math.factorial(number)


def fraction_complex_to_mixed_fraction(fraction_string):
    """Simplify the fraction represented as a string."""
    simplified_fraction_string = fraction_simplify(fraction_string)
    numerator, denominator = _split_fraction(simplified_fraction_string)

    if numerator < denominator:
        return f'{numerator}/{denominator}'
    elif numerator == denominator:
        return '1'
    else:
        fraction_remainder = remainder(numerator, denominator)
        return f'{floor(numerator / denominator)} {fraction_remainder}/{denominator}'


def fraction_mixed_to_complex_fraction(fraction_string):
    """Simplify the fraction represented as a string."""
    whole_number, fraction = _split_mixed_fraction(fraction_string)

    if not whole_number or not fraction:
        return fraction_string

    numerator, denominator = _split_fraction(fraction)

    return f'{(whole_number * denominator) + numerator}/{denominator}'


def dot_product(item_a, item_b):
    """Find the dot product for the two items. See https://en.wikipedia.org/wiki/Dot_product for more details."""
    dot_product = 0

    for i in zip(item_a, item_b):
        dot_product += i[0] * i[1]

    return dot_product


def percent(ratio):
    """Return the ratio as a percentage."""
    if ratio <= 1 and ratio >= 0:
        return round(ratio * 100, 2)
    else:
        # TODO: not sure what to do here
        raise RuntimeError


@arguments_as_decimals
def gcd(number1, number2):
    """Return the greatest common divisor."""
    import math

    return math.gcd(number1, number2)


def ratio(number1, number2):
    """Return the ratio of the two numbers in the form 1:2. For example, if given 5 and 10, this function would return "1:2". If given 2 and 20, this function would return "1:10"."""
    divisor = gcd(number1, number2)
    return "{}:{}".format(int(number1 / divisor), int(number2 / divisor))


def transpose(matrix):
    """Transpose the given matrix. See https://en.wikipedia.org/wiki/Transpose."""

    if not matrix or not matrix[0]:
        print('Empty matrix provided')
        return None

    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    return transposed_matrix


def number_line(value, min_, max_, interval: int = 1):
    if min_ > max_:
        raise RuntimeError('The minimum value "{}" is greater than the maximum value "{}"'.format(min_, max_))
    if value > max_:
        raise RuntimeError('The value "{}" is greater than the maximum value of "{}"'.format(value, max_))
    if value < min_:
        raise RuntimeError('The value "{}" is less than the minimum value of "{}"'.format(value, min_))

    # find the length of the numberline between the value and the min_
    length_below_value = int(((value - min_) / interval) - 1)
    # find the length of the numberline between the max_ and the value
    length_above_value = int(((max_ - value) / interval) - 1)

    # create the numberline
    if length_below_value < 0:
        number_line_string = '({})|{}{}'.format(min_, '.' * length_above_value, max_)
    elif length_above_value < 0:
        number_line_string = '{}{}|({})'.format(min_, '.' * length_below_value, max_)
    else:
        number_line_string = '{}{}|{}{}'.format(min_, '.' * length_below_value, '.' * length_above_value, max_)

    return number_line_string
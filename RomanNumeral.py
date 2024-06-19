class RomanNumeral:
    roman_numerals = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }

    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        elif isinstance(value, float):
            self.value = round(value)
        elif isinstance(value, str):
            self.value = self.from_roman(value)
        else:
            raise ValueError("Unsupported type")
        self.roman = self.to_roman(self.value)

    @classmethod
    def to_roman(cls, num):
        result = ''
        for roman, val in cls.roman_numerals.items():
            while num >= val:
                result += roman
                num -= val
        return result

    @classmethod
    def from_roman(cls, roman):
        result = 0
        index = 0
        for roman_sym, val in cls.roman_numerals.items():
            while roman[index:index + len(roman_sym)] == roman_sym:
                result += val
                index += len(roman_sym)
        return result

    def __str__(self):
        return self.roman

    def __len__(self):
        return len(self.roman)

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.value + other.value)
        elif isinstance(other, (int, float)):
            return RomanNumeral(self.value + round(other))
        else:
            raise ValueError("Unsupported type for addition")

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            result = self.value - other.value
        elif isinstance(other, (int, float)):
            result = self.value - round(other)
        else:
            raise ValueError("Unsupported type for subtraction")

        if result < 0:
            raise ValueError("Result of subtraction cannot be less than 0")

        return RomanNumeral(result)

    def __mul__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.value * other.value)
        elif isinstance(other, (int, float)):
            return RomanNumeral(self.value * round(other))
        else:
            raise ValueError("Unsupported type for multiplication")

    def __truediv__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.value // other.value)
        elif isinstance(other, (int, float)):
            return RomanNumeral(self.value // round(other))
        else:
            raise ValueError("Unsupported type for division")

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.value == other.value
        elif isinstance(other, (int, float)):
            return self.value == round(other)
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.value > other.value
        elif isinstance(other, (int, float)):
            return self.value > round(other)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, RomanNumeral):
            return self.value < other.value
        elif isinstance(other, (int, float)):
            return self.value < round(other)
        else:
            return False


# example
a = RomanNumeral(10)  # X
b = RomanNumeral('X')  # X
c = RomanNumeral(5)  # V

print(a + b)  # XX = 20
print(a - b)  # 0 = 0
print(a * 2)  # XX = 20
print(a / 2)  # V = 5

print(a == b)  # True
print(a > c)  # True
print(a < c)  # False

try:
    print(a - 20)  # Should raise ValueError
except ValueError as e:
    print(e)  # Result of subtraction cannot be less than 0

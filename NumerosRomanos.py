# import unittest


# class TestDecimalToRoman(unittest.TestCase):
#     def test_1(self):
#         roman_number = convert_decimal_to_roman(1)
#         self.assertEqual(roman_number, 'I')

# if __name__ == '__main__':
#     unittest.main()

# import unittest


# def convert_decimal_to_roman(decimal_number):
#     return 'I'


# class TestDecimalToRoman(unittest.TestCase):
#     def test_1(self):
#         roman_number = convert_decimal_to_roman(1)
#         self.assertEqual(roman_number, 'I')

# if __name__ == '__main__':
#     unittest.main()

# import unittest


# def convert_decimal_to_roman(decimal_number):
#     roman = ''
#     for digit in range(decimal_number):
#         roman += 'I'
#     return roman


# class TestDecimalToRoman(unittest.TestCase):
#     def test_1(self):
#         roman_number = convert_decimal_to_roman(1)
#         self.assertEqual(roman_number, 'I')

#     def test_2(self):
#         roman_number = convert_decimal_to_roman(2)
#         self.assertEqual(roman_number, 'II')

# if __name__ == '__main__':
#     unittest.main()

import unittest


def convert_decimal_to_roman(decimal_number):
    roman = ''
    if decimal_number < 10:
        for digit in range(decimal_number):
            roman += 'I'
    else:
        for digit in range(decimal_number // 10):
            roman += 'X'
    return roman
class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
        roman_number = convert_decimal_to_roman(1)
        self.assertEqual(roman_number, 'I')

    def test_2(self):
        roman_number = convert_decimal_to_roman(2)
        self.assertEqual(roman_number, 'II')

    def test_10(self):
        roman_number = convert_decimal_to_roman(10)
        self.assertEqual(roman_number, 'X')
if __name__ == '__main__':
    unittest.main()
from unittest import TestCase, main

from roman import to_roman


class RomanTest(TestCase):
    def test_roman_digits(self):
        self.assertEqual('I', to_roman(1))
        self.assertEqual('V', to_roman(5))
        self.assertEqual('X', to_roman(10))
        self.assertEqual('L', to_roman(50))
        self.assertEqual('C', to_roman(100))
        self.assertEqual('D', to_roman(500))
        self.assertEqual('M', to_roman(1000))

    def test_roman_combinations(self):
        self.assertEqual('II', to_roman(2))
        self.assertEqual('XXX', to_roman(30))
        self.assertEqual('VI', to_roman(6))
        self.assertEqual('LXII', to_roman(62))
        self.assertEqual('CII', to_roman(102))
        self.assertEqual('DLXXIII', to_roman(573))
        self.assertEqual('MDCLXXXVI', to_roman(1686))
        self.assertEqual('MMMCMXCIX', to_roman(3999))

    def test_roman_exceptions(self):
        self.assertEqual('IV', to_roman(4))
        self.assertEqual('IX', to_roman(9))
        self.assertEqual('XL', to_roman(40))
        self.assertEqual('XC', to_roman(90))
        self.assertEqual('CD', to_roman(400))
        self.assertEqual('CM', to_roman(900))


if __name__ == '__main__':
    main()

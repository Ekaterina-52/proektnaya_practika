import unittest
from project11 import convert_temperature


class TestConverter(unittest.TestCase):

    def testconvertcelsiustofahrenheit(self):
        self.assertAlmostEqual(convert_temperature(0, "Цельсий", "Фаренгейт"), 32.0)
        self.assertAlmostEqual(converttemperature(100, "Цельсий", "Фаренгейт"), 212.0)

    def testconvertcelsiustokelvin(self):
        self.assertAlmostEqual(converttemperature(0, "Цельсий", "Кельвин"), 273.15)
        self.assertAlmostEqual(converttemperature(100, "Цельсий", "Кельвин"), 373.15)

    def testconvertfahrenheittocelsius(self):
        self.assertAlmostEqual(converttemperature(32, "Фаренгейт", "Цельсий"), 0.0)
        self.assertAlmostEqual(converttemperature(212, "Фаренгейт", "Цельсий"), 100.0)

    def testconvertfahrenheittokelvin(self):
        self.assertAlmostEqual(converttemperature(32, "Фаренгейт", "Кельвин"), 273.15)
        self.assertAlmostEqual(converttemperature(212, "Фаренгейт", "Кельвин"), 373.15)

    def testconvertkelvintocelsius(self):
        self.assertAlmostEqual(converttemperature(273.15, "Кельвин", "Цельсий"), 0.0)
        self.assertAlmostEqual(converttemperature(373.15, "Кельвин", "Цельсий"), 100.0)

    def testconvertkelvintofahrenheit(self):
        self.assertAlmostEqual(converttemperature(273.15, "Кельвин", "Фаренгейт"), 32.0)
        self.assertAlmostEqual(converttemperature(373.15, "Кельвин", "Фаренгейт"), 212.0)

if __name__ == "main":
    unittest.main()

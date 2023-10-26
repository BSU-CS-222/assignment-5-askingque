import unittest
import tkinter as tk

from assignment5Main import calculate


years = tk.IntVar()
years.set(5)
annualPercentageRate = tk.DoubleVar()
annualPercentageRate.set(5)
price = tk.IntVar()
price.set(20000)
downpayment = tk.IntVar()
downpayment.set(3500)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.calculator = calculate(years, annualPercentageRate, price, downpayment)

    def test_calculate(self):
        self.assertEqual(self.calculator, 311.38)
        

if __name__ == "__main__":
    unittest.main()
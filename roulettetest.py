import unittest
from roulette import Roulette
from controller import Controller


sut = Roulette()
sutc = Controller("test controller")

class RouletteTests(unittest.TestCase):

    def testBoardReturnType(self):
        rv = sut.get_board()
        self.assertEqual(rv.__class__, str)

    def testBoardLength(self):
        rv = sut.get_board()
        self.assertEqual(len(rv), 214)

    def testSpinWheelReturnType(self):
        rv = sut.spin_wheel()
        self.assertEqual(rv.__class__, int)

    def testCreateRouletteType(self):
        rv = sut.__class__
        self.assertEqual(rv, Roulette)

    def testCreateControllerType(self):
        rv = sutc
        self.assertEqual(rv.__class__, Controller)

    def testPayoutMethodPay(self):
        sut.winning_number = 8
        rv = sut.payout((8, 10))
        self.assertEqual(rv, 35.0)

    def testPayoutMethodWinningNumber(self):
        sut.winning_number = 8
        rv = sut.payout((1, 5))
        self.assertEqual(rv, 0)

    def testPayoutMethodPay2(self):
        sut.winning_number = 8
        rv = sut.payout((8, 23))
        self.assertEqual(rv, 80.5)

    def testWalletValueCheck(self):
        sut.wallet = 0
        rv = sut.wallet_value_check()
        self.assertEqual(rv, -1)


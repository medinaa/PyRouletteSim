from __future__ import print_function, division
import random as rand
import re

class Roulette(object):

    def __init__(self):
        self.wallet = 30
        self.winning_number = None
        self.gameboard = """
            3 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 25 | 30 | 33 | 36
            2 | 5 | 8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35
            1 | 4 | 7 | 10 | 13 | 16 | 19 | 22 | 27 | 28 | 31 | 34
            """


    def get_board(self):
        return self.gameboard


    def spin_wheel(self):
        self.winning_number = rand.randrange(1, 36)
        return self.winning_number


    def payout(self, (number, value)):
        """
        compute the payout of a played number.
        :return: float value of payout.
        """
        if (number != self.winning_number):
            return 0
        return value * 3.5


    def wallet_value_check(self):
        """
        check if user has any money left to bet for
        the next round.
        :return: 0 if true, -1 if false
        """
        if (self.wallet <= 0):
            return -1
        return 0


    def place_bet_and_value(self):
        """
        prompt user to place their bets and value them.
        :return tuple<k,v> of number, value
        """

        rv = []

        keep_going = True
        while keep_going:
            user_input = raw_input("pick gameboard numbers and price your bets(space separated)<number:number>$")
            regex_pattern = r'[0-9]+:[0-9]+'
            bets = re.findall(regex_pattern, user_input)

            if len(bets) == 0:
                print("invalid input. please try again.")
                continue

            keep_going = False

            for bet in bets:
                bet_values = bet.split(":")

                number = bet_values[0]
                price = bet_values[1]

                if number.isalpha() or price.isalpha():
                    continue

                number = int(number)
                price = int(price)

                if (number < 1 or number > 36):
                    continue

                if (self.wallet - price < 0):
                    self.wallet = 0
                    rv.append((number, self.wallet))
                    break
                else:
                    rv.append((number, price))
                    self.wallet = self.wallet - price

        return rv

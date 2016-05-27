from __future__ import print_function, division
from time import sleep
from roulette import Roulette

class Controller(object):
    def __init__(self, name):
        self.name = name
        self.roulette = Roulette()

    def start_game(self):

        print("roulette simulator. . .")
        sleep(2)

        game_loop = True
        while(game_loop):
            print(self.roulette.get_board())

            print("Chips Value -> [$%d]" % self.roulette.wallet)

            list_of_bets = self.roulette.place_bet_and_value()

            print("Chips Value -> [$%d]" % self.roulette.wallet)

            print("Spinning. . .")
            sleep(1)

            print("Spinning. . .")
            sleep(1)

            print("Spinning. . .")
            sleep(1)

            winning_number = self.roulette.spin_wheel()
            print("Winning number -> %d" % winning_number)

            for bet in list_of_bets:
                self.roulette.wallet += self.roulette.payout(bet)

            if (self.roulette.wallet_value_check() == -1):
                game_loop = False


    def help(self):
        raise NotImplemented
from __future__ import print_function, division
import logging
from controller import Controller


# main function starts script game
if __name__ == '__main__':
    logging.info("running")

    contr = Controller("roulette game")

    contr.start_game()

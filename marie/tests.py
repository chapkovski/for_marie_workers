from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        if self.player.role() == 'worker':
            yield pages.DecisionWorkerPage, {'contribution': random.randint(0, Constants.max_contribution),
                                             'take': random.choice([0, 50])}
        else:
            yield pages.DecisionEmployerPage, {'inspect': random.choice([False, True])}
        yield pages.Results

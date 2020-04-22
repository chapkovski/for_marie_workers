from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class DecisionWorkerPage(Page):
    def is_displayed(self) -> bool:
        return self.player.role() == 'worker'

    form_model = 'player'
    form_fields = ['take', 'contribution']


class DecisionEmployerPage(Page):
    def is_displayed(self) -> bool:
        return self.player.role() == 'employer'

    form_model = 'group'
    form_fields = ['inspect']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [
    DecisionWorkerPage,
    DecisionEmployerPage,
    ResultsWaitPage,
    Results]

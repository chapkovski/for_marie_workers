from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'marie'
    players_per_group = 4
    num_rounds = 2
    company_fund = 150
    max_take = int(company_fund / (players_per_group - 1))
    max_contribution = 40
    rate_per_hour = 2
    flat_rate_for_worker = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    inspect = models.BooleanField(label='Inspect or not?', choices=((False, 'Not inspect'), (True, 'Inspect')))
    total_contribution = models.IntegerField()

    def get_workers(self):
        return [p for p in self.get_players() if p.role() == 'worker']

    def set_payoffs(self):
        workers = self.get_workers()
        employer = self.get_player_by_role('employer')

        self.total_contribution = sum([p.contribution for p in workers])
        employer.payoff = self.total_contribution * Constants.rate_per_hour
        for w in workers:
            w.payoff = w.take + Constants.flat_rate_for_worker


class Player(BasePlayer):
    contribution = models.IntegerField(min=0, max=Constants.max_contribution,
                                       label='How much you want to contribute?')
    take = models.IntegerField(choices=[0, 50],
                               widget=widgets.RadioSelectHorizontal(),
                               label='How much youd like to steal?')

    def role(self):
        if self.id_in_group < 4:
            return 'worker'
        else:
            return 'employer'

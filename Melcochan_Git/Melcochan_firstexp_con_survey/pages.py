from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    pass

class Instraction(Page):
    pass

class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_widget', 'crt_lake']


page_sequence = [Introduction, CognitiveReflectionTest]

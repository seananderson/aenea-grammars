# Commands for interatcting with MailMate

import aenea
import aenea.configuration
from aenea.lax import Key, Text, Dictation
import dragonfly
from aenea import *

msw_context = aenea.ProxyCustomAppContext(id="Microsoft Word")
grammar = dragonfly.Grammar('msw', context=msw_context)

msw_mapping = {
    "new comment": Key("wa-a"),
    "toggle track changes": Key("ws-e"),
}

class MappingMM(dragonfly.MappingRule):
    mapping = msw_mapping
    extras = [
        IntegerRef("n", 1, 10),
    ]

alternatives = []
alternatives.append(RuleRef(rule=MappingMM()))
root_action = Alternative(alternatives)

sequence = Repetition(root_action, min=1, max=3, name="sequence")

class RepeatRule(CompoundRule):
    spec = "<sequence>"
    extras = [sequence]

    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]
        for action in sequence:
            action.execute()

grammar.add_rule(RepeatRule())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

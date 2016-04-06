from natlink import setMicState
from aenea import *

from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
if 'semicolon' not in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')

import words
import generic
import osx
import vocab

generalKeys = {}
generalKeys.update(generic.genericKeys)
generalKeys.update(generic.nonVimGenericKeys)
generalKeys.update(osx.osx)
generalKeys.update(vocab.vocabWord)

grammarCfg = Config("all")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(generalKeys,
       namespace={
        "Key": Key,
        "Text": Text,
    })

class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 20),
        Dictation("text"),
        Choice("modifier1", generic.modifierMap),
        Choice("modifier2", generic.modifierMap),
        Choice("modifierSingle", generic.singleModifierMap),
        Choice('letters', generic.letterMap),
        Choice('specials', generic.specialKeys),
        Choice('numbers', generic.numberMap),
        Choice("pressKey", generic.pressKeyMap),
        Choice("reservedWord", generic.reservedWord),
    ]
    defaults = {
        "n": 1,
    }

alternatives = []
alternatives.append(RuleRef(rule=KeystrokeRule()))
alternatives.append(RuleRef(rule=words.FormatRule()))
root_action = Alternative(alternatives)

sequence = Repetition(root_action, min=1, max=9, name="sequence")

class RepeatRule(CompoundRule):
    spec = "<sequence>"
    extras = [sequence]

    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]
        for action in sequence:
            action.execute()

vim_context = aenea.ProxyCustomAppContext(match="substring", titl="nvim") & aenea.ProxyCustomAppContext(id="iTerm2")
grammar = Grammar("root rule", context = ~vim_context)
grammar.add_rule(RepeatRule())
grammar.load()

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

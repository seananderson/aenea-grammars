from natlink import setMicState
from aenea import *

import words
# import programs

from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
if 'semicolon' not in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')

from generic import *
from osx import *

generalKeys = {}
generalKeys.update(genericKeys)
generalKeys.update(osx)

grammarCfg = Config("all")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(generalKeys,
       namespace={
        "Key": Key,
        "Text": Text,
    }
    )

class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 20),
        Dictation("text"),
        Choice("modifier1", modifierMap),
        Choice("modifier2", modifierMap),
        Choice("modifierSingle", singleModifierMap),
        Choice('letters', letterMap),
        Choice('numbers', numberMap),
        Choice("pressKey", pressKeyMap),
        Choice("reservedWord", reservedWord),
    ]
    defaults = {
        "n": 1,
    }

alternatives = []
alternatives.append(RuleRef(rule=KeystrokeRule()))
alternatives.append(RuleRef(rule=words.FormatRule()))
alternatives.append(RuleRef(rule=words.ReFormatRule()))
alternatives.append(RuleRef(rule=words.NopeFormatRule()))
root_action = Alternative(alternatives)

sequence = Repetition(root_action, min=1, max=10, name="sequence")

class RepeatRule(CompoundRule):
    # Here we define this rule's spoken-form and special elements.
    spec = "<sequence> [[[and] repeat [[that]]] <n> times]"
    extras = [
        sequence,  # Sequence of actions defined above.
        IntegerRef("n", 1, 16),  # Times to repeat the sequence.
    ]
    defaults = {
        "n": 1,  # Default repeat count.
    }

    def _process_recognition(self, node, extras):  # @UnusedVariable
        sequence = extras["sequence"]  # A sequence of actions.
        count = extras["n"]  # An integer repeat count.
        for i in range(count):  # @UnusedVariable
            for action in sequence:
                action.execute()
            #release.execute()

# all_context = aenea.ProxyCustomAppContext(match="substring", titl="nvim") | aenea.ProxyCustomAppContext(match="substring", titl="Vim") | aenea.ProxyCustomAppContext(id="iterm2")
# | aenea.ProxyCustomAppContext(match="substring", titl="RStudio")
# chrome_context = aenea.ProxyCustomAppContext(id="ignore me")
all_grammar = Grammar("root rule")
all_grammar.add_rule(RepeatRule())  # Add the top-level rule.
all_grammar.load()  # Load the grammar.

#################################

esc = Key("escape")

def unload():
    """Unload function which will be called at unload time."""
    global all_grammar
    if all_grammar:
        all_grammar.unload()
    all_grammar = None

# _all.py: main rule for DWK's grammar

from natlink import setMicState
from aenea import *

import keyboard
import words
import programs

release = Key("shift:up, ctrl:up, alt:up")

alternatives = []
alternatives.append(RuleRef(rule=keyboard.KeystrokeRule()))
alternatives.append(RuleRef(rule=words.FormatRule()))
alternatives.append(RuleRef(rule=words.ReFormatRule()))
alternatives.append(RuleRef(rule=words.NopeFormatRule()))
alternatives.append(RuleRef(rule=programs.ProgramsRule()))
root_action = Alternative(alternatives)

sequence = Repetition(root_action, min=1, max=10, name="sequence")

class RepeatRule(CompoundRule):
    # Here we define this rule's spoken-form and special elements.
    spec = "<sequence> [[[and] repeat [that]] <n> times]"
    extras = [
        sequence,  # Sequence of actions defined above.
        IntegerRef("n", 1, 15),  # Times to repeat the sequence.
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

grammar = Grammar("root rule")
grammar.add_rule(RepeatRule())  # Add the top-level rule.
grammar.load()  # Load the grammar.


#################################

esc = Key("escape")

# handles ExMode control structures
class ExModeCommands(MappingRule):
    mapping  = {
    "edit": esc + Key("colon,e,space"),
    "exit vim": esc + Key("colon,q,enter"),
    "split explorer": esc + Key("colon,s-S,e,x,enter"),
    "please exit vim": esc + Key("colon,q,exclamation,enter"),
    "save and exit vim": esc + Key("colon,w,q,exclamation,enter"),
    "save file": esc + Key("colon,u,p,d,a,t,e,enter"),
    "save as": esc + Key("colon,s,a,v,e,a,s,space"),
    "toggle numbers": esc + Key("colon,s,e,t,space,r,e,l,a,t,i,v,e,n,u,m,b,e,r,exclamation") + Key("enter"),
    "browse (old|recent) files": esc + Key("colon,b,r,o,space,o,l") + Key("enter"),
    "set theme ocean": esc + Key("colon,c,o,l,o/50,space,b,a,s,e,1,6/50,minus,o,c,e,a,n/50,enter"),
    "set theme one dark": esc + Key("colon,c,o,l,o/50,space,o,n,e,d,a,r,k") + Key("enter"),
    "set theme solarized": esc + Key("colon/50,c,o,l,o/50,space,s,o,l,a,r,i,z,e,d") + Key("enter"),
    "set theme Seoul": esc + Key("colon/50,c,o,l,o/50,space,s,e,o,u,l,2,5,6") + Key("enter"),
    "toggle [the] lights": esc + Key("colon/50,T,o,g,g,l,e,B,G")+Key("enter"),
    "toggle spelling": esc + Key("colon/50,s,e,t,l,o,c,a,l,space,s,p,e,l,l,exclamation")+Key("enter"),
    "toggle invisible characters": esc + Key("colon,s,e,space,l,i,s,t,exclamation")+Key("enter"),
    "toggle nerd": esc + Key("colon/50,s-N,s-E,s-R,s-D,s-T,r,e,e,s-T,o,g,g,l,e/50,enter"),
    "toggle cursor-line": esc + Key("colon/50,s,e,space,c,u,r,s,o,r,l,i,n,e/50,exclamation,enter"),
    "get dir": Key("p,w,d/10,enter"),
    "vim help": esc + Key("colon,h,space"),
    "substitute": esc + Key("s,slash"),
    "make split wide": esc + Key("colon/100,v,e,r,t,i,c,a,l/100,space,r,e,s,i,z,e/100,space,plus,6/100,enter"),
    "make split narrow": esc + Key("colon/100,v,e,r,t,i,c,a,l/100,space,r,e,s,i,z,e/100,space,minus,6/100,enter"),
    "make split tall": esc + Key("colon/100,space,r,e,s,i,z,e/100,space,plus,6/100,enter"),
    "make split short": esc + Key("colon/100,space,r,e,s,i,z,e/100,space,minus,6/100,enter"),
    'buff-delete': esc + Key('colon,b,d,enter'),
    'buff-next': esc + Key('colon,b,n,enter'),
    'buff-previous': esc + Key('colon,b,p,enter'),
    'buff-list': esc + Key('colon,l,s,enter'),
    'screen center': esc + Key("z, dot"),
    'screen top': esc + Key("z, t"),
    'screen bottom': esc + Key("z, b"),
    "switch": esc + Key("escape, c-p"),
    "switch recent": esc + Key("escape,colon,s-C,t,r,l,s-P,s-M,s-R,s-U,enter"),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
        IntegerRef("line1", 1, 600),
        IntegerRef("line2", 1, 600),
    ]
    defaults = {
        "n": 1,
    }

ExModeGrammar = Grammar("ExMode grammar")
ExModeGrammar.add_rule(ExModeCommands())
ExModeGrammar.load()

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

    global ExModeGrammar
    if ExModeGrammar:
        ExModeGrammar.unload()
    ExModeGrammar = None

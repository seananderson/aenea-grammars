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

srt = Key("escape, l/30")
end = Key("i")
append = Key("a")

# handles ExMode control structures
class ExModeCommands(MappingRule):
    mapping  = {
        "edit": srt + Key("colon,e,space"),
        "exit vim":                                    srt + Key("colon,q,enter"),
        "please exit vim":                             srt + Key("colon,q,exclamation,enter"),
        "save and exit vim":                       srt + Key("colon,w,q,exclamation,enter"),
    "save file":                           srt + Key("colon,u,p,d,a,t,e,enter") + end,
    "save as":                                     srt + Key("colon,s,a,v,e,a,s,space") + end,
        "toggle numbers": srt + Key("colon,s,e,t,space,r,e,l,a,t,i,v,e,n,u,m,b,e,r,exclamation") + Key("enter") + end,
    "browse (old|recent) files":                   srt + Key("colon,b,r,o,space,o,l") + Key("enter") + end,
    "set theme ocean":                             srt + Key("colon,c,o,l,o/50,space,b,a,s,e,1,6/50,minus,o,c,e,a,n/50,enter") + end,
    "set theme one dark":                             srt + Key("colon,c,o,l,o/50,space,o,n,e,d,a,r,k") + Key("enter") + end,
    "set theme solarized":                         srt + Key("colon/50,c,o,l,o/50,space,s,o,l,a,r,i,z,e,d") + Key("enter") + end,
    "set theme Seoul":                             srt + Key("colon/50,c,o,l,o/50,space,s,e,o,u,l,2,5,6") + Key("enter") + end,
    "toggle [the] lights":                         srt + Key("colon/50,T,o,g,g,l,e,B,G")+Key("enter") + end,
    "toggle spelling":                             srt + Key("colon/50,s,e,t,l,o,c,a,l,space,s,p,e,l,l,exclamation")+Key("enter") + end,
    "toggle invisible characters":                 srt + Key("colon,s,e,space,l,i,s,t,exclamation")+Key("enter") + end,


    'toggle nerd': srt + Key("colon/50,s-N,s-E,s-R,s-D,s-T,r,e,e,s-T,o,g,g,l,e/50,enter") + end,
    'toggle cursor-line': srt + Key("colon/50,s,e,space,c,u,r,s,o,r,l,i,n,e/50,exclamation,enter") + end,

        # "set file format UNIX": Text("set fileformat=unix "),
        # "set file format DOS": Text("set fileformat=dos "),
        # "set file type Python": Text("set filetype=python"),
        # "set file type tex": Text("set filetype=tex"),

        "P. W. D.": Text("pwd "),
        "help": srt + Text(":h "),
        "substitute": Text("s/"),

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

 # Commands for interacting with 2do

import aenea
import aenea.configuration
from aenea.lax import Key, Text, Dictation
import dragonfly
from aenea import *

do_mapping = {
    'new task': Key("w-n"),
    'delete task': Key("w-backspace"),
    'remove tags': Key("ca-r"),

    '[go] to inbox': Key("w-0"),
    '[go] to all': Key("w-1"),
    '[go] to today': Key("w-2"),
    '[go] to starred': Key("w-3"),
    '[go] to scheduled': Key("w-4"),
    '[go] to done': Key("w-5"),

    'preev list': Key("w-up"),
    'next list': Key("w-down"),

    'hide tags': Key("wa-right"),

    'quick find': Key("f"),
    'jump to': Key("j"),

    'edit date': Key("w-slash"),
    'edit note': Key("w-e"),
    'edit tags': Key("w-r"),
    'edit recurrence': Key("w-semicolon"),
    'edit alerts': Key("w-squote"),
    'edit priority': Key("w-backslash"),
    'edit list': Key("w-l"),
    'rip': Key("w-enter"),

    'move up': Key("wc-up"),
    'move down': Key("wc-down"),
    'move task': Key("m"),

    'defer': Key("d"),
    'schedule': Key("k"),
    'start today': Key("c-t"),
    'due today': Key("t"),
    'do tomorrow': Key("y"),

    'toggle scheduled': Key("w-k"),
    'toggle paused': Key("w-u"),
    'toggle focus': Key("w-j"),

    'open [link|links]': Key("u"),
    'perform action': Key("p"),

    'collapse project': Key("c"),
    'toggle project view': Key("wa-j"),

    'convert to task': Key("was-1"),
    'convert to project': Key("was-2"),
    'convert to checklist': Key("was-3"),

    'due a day later': Key("rbracket"),
    'due a week later': Key("s-rbracket"),
    'due a day earlier': Key("lbracket"),
    'due a week earlier': Key("s-lbracket"),

    'start a day later': Key("dot"),
    'start a week later': Key("s-dot"),
    'start a day earlier': Key("comma"),
    'start a week earlier': Key("s-comma"),

}

do_context = aenea.ProxyCustomAppContext(id="2Do")
do_grammar = dragonfly.Grammar('2Do', context=do_context)

##########
class MappingDo(dragonfly.MappingRule):
    mapping = do_mapping
    extras = [
        IntegerRef('n', 1, 60),
        Dictation('text'),
    ]
    defaults = {
        "n": 1,
    }

do_grammar.add_rule(MappingDo())
do_grammar.load()

def unload():
    global do_grammar
    if do_grammar:
        do_grammar.unload()
    do_grammar = None

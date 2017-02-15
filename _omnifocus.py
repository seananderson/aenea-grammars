 # Commands for interacting with omnifocus

import aenea
import aenea.configuration
from aenea.lax import Key, Text, Dictation
import dragonfly
from aenea import *

do_mapping = {
    'new task': Key("w-n"),
    '[go] to inbox': Key("aw-1"),

    '(omni go to)|(omni jump to)': Key("w-o"),
    'omni synchronize': Key("cw-s"),

    'planning mode': Key("w-1"),
    'context mode': Key("w-2"),

    'star that': Key("sw-l"),
}

do_context = aenea.ProxyCustomAppContext(id="OmniFocus")
do_grammar = dragonfly.Grammar('OmniFocus', context=do_context)

##########
class MappingDo(dragonfly.MappingRule):
    mapping = do_mapping

do_grammar.add_rule(MappingDo())
do_grammar.load()

def unload():
    global do_grammar
    if do_grammar:
        do_grammar.unload()
    do_grammar = None

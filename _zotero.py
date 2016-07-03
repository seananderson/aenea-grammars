# Commands for interacting with Zotero

import aenea
import aenea.configuration
from aenea.lax import Key, Text, Dictation
import dragonfly
from aenea import *

zotero_mapping = {
    'add tag': Key("c-t"),
    'add note': Key("c-n"),
    'copy bibtex': Key("c-b"),
    'copy formatted reference': Key("c-r"),
    'copy [zotero] link': Key("c-z"),
    'focus info': Key("c-i"),
    'edit (info|that)': Key("c-e"),
    'delete tags': Key("c-d"),
    'delete tags': Key("c-d"),
    '(get|retrieve) meta-data': Key("c-m"),
    'rename attachments': Key("c-a"),
}

zotero_context = aenea.ProxyCustomAppContext(id="Zotero")
zotero_grammar = dragonfly.Grammar('Zotero', context=zotero_context)

##########
class MappingZotero(dragonfly.MappingRule):
    mapping = zotero_mapping
    extras = [
        IntegerRef('n', 1, 60),
        Dictation('text'),
    ]
    defaults = {
        "n": 1,
    }

zotero_grammar.add_rule(MappingZotero())
zotero_grammar.load()

def unload():
    global zotero_grammar
    if zotero_grammar:
        zotero_grammar.unload()
    zotero_grammar = None

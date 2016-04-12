# Commands for interacting with MailMail

import aenea
import aenea.configuration
from aenea.lax import Key, Text, Dictation
import dragonfly
from aenea import *

mm_mapping = {
    'open message': Key("w-o"),
    'reply message': Key("w-r"),
    'send message': Key("sw-d"),
    'added as new message': Key("asw-d"),
    'forward message': Key("sw-f"),
    'reply all': Key("ws-r"),
    'new message': Key("w-n"),
    'copy as link': Key("saw-c"),
    'select thread': Key("ca-a"),
    '[go] to inbox': Key("g, i"),
    '[go] to sent': Key("g, t"),
    '[go] to archive': Key("g, a"),
    '[go] to (mailbox|label)': Key("w-t"),
    '[go] to (mailbox|label) <text>': Key("w-t") + Text("%(text)s") + Key("enter"),

    '[go] to list': Key("0"),
    '[go] to message': Key("9"),
    '[go] to editor': Key("c-j"),  # working ?

    'archive message': Key("sw-m"),
    'junk message': Key("sw-j"),
    'move message': Key("aw-t"),
    'flag message': Key("sw-l"),
    'next [<n>]': Key("w-down:%(n)d"),
    'preeve [<n>]': Key("w-up:%(n)d"),
    'next thread [<n>]': Key("cw-down:%(n)d"),
    'preeve thread [<n>]': Key("cw-up:%(n)d"),
    'root of thread [<n>]': Key("cw-r"),
    'last of thread [<n>]': Key("cw-l"),
    'find': Key("aw-f"),
    'find here': Key("caw-f"),
    'find message from <text>': Key("aw-f") + Text("f %(text)s"),
    'synchronize': Key("ws-n"),
    'edit in vim': Key("f12"),

    'go back': Key("at,lbracket"),
    'go forward': Key("at,rbracket"),
    'load images': Key("s-l"),
    'next alternative': Key("h"),
    'show correspondence': Key("s-C"),
    'show thread': Key("s-T"),
    'save attachments': Key("s-D"),

}

mm_context = aenea.ProxyCustomAppContext(id="MailMate")
mm_grammar = dragonfly.Grammar('mailmate', context=mm_context)

class MappingChrome(dragonfly.MappingRule):
    mapping = mm_mapping
    extras = [
        IntegerRef('n', 1, 60),
        Dictation('text'),
    ]
    defaults = {
        "n": 1,
    }

mm_grammar.add_rule(MappingChrome())
mm_grammar.load()

def unload():
    global mm_grammar
    if mm_grammar:
        mm_grammar.unload()
    mm_grammar = None

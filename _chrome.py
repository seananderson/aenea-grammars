# Commands for interatcting with MS Word

import aenea
import aenea.configuration
from aenea.lax import Key, Text, Dictation
import dragonfly
from aenea import *

chrome_mapping = {
    # Tab navigation
    '(preev|left) tab': Key("cs-tab"),
    '(next|right) tab': Key("c-tab"),
    'new (window|tab)': Key("w-t"),
    'reopen (window|tab)': Key("ws-t"),
    'close (window|tab)': Key("w-w"),
    'close all (windows|tab)': Key("ws-w"),
    'go back': Key("w-lbracket"),
    'go forward': Key("w-rbracket"),
    'go to': Key("w-l"),
    'refresh': Key("w-r"),
    'link|show links|links': Key("f"),
    'link new': Key("s-f"),
    # 'press <letters1>': Key("%(letters1)s"),
    # 'two press <letters1> <letters2>': Key("%(letters1)s") + Key("%(letters2)s"),
    # 'one click [<letters1>]': Key("%(letters1)s"),
    # "page up": Key("pgup"),
    # "page down": Key("pgdown"),

    # "<letters1>": Key("%(letters1)s"),

    # "(delete|del) [<n>]": Key("del:%(n)d"),
    # "(backspace|chuck) [<n>]": Key("backspace:%(n)d"),
    # "(enter|slap|slop)": Key("enter"),

    #  Moving around
    'mort': Key("j:10"),
    'lest': Key("k:10"),
    # 'go to top': Key("g, g"),
    # 'go to bottom': Key("s-g"),
    'edit in vim': Key("f12"),


    #  Searching
    # 'find <text>': Key("escape, slash") + Text("%(text)s") + Key("enter"),
    # 'next': Key("n"),
    # 'prev|previous': Key("N"),
}

gmail_mapping = {
    'open message': Key("o"),
    'reply message': Key("r"),
    'send message': Key("w-enter"),
    'mark (message|that)': Key("x"),
    'undo action': Key("z"),
    'reply all': Key("a"),
    'gmail back': Key("u"),
    '[go] to inbox': Key("g, i"),
    '[go] to sent': Key("g, t"),
    '[go] to archive': Key("g, a"),
    '[go] to label': Key("g, l"),
    '[go to] label <text>': Key("g, l") + Text("%(text)s") + Key("enter"),
    '(delete|trash) message': Key("hash"),
    'archive message': Key("e"),
    'next [<n>]': Key("n:%(n)d"),
    'preeve [<n>]': Key("p:%(n)d"),
}

chrome_context = aenea.ProxyCustomAppContext(id="Google Chrome")
gmail_context = aenea.ProxyCustomAppContext(titl="Mail") & aenea.ProxyCustomAppContext(id = "Google Chrome")
chrome_grammar = dragonfly.Grammar('chrome', context=chrome_context)
gmail_grammar = dragonfly.Grammar('gmail', context=gmail_context)

class MappingChrome(dragonfly.MappingRule):
    mapping = chrome_mapping
    extras = [
        IntegerRef('n', 1, 60),
        Dictation('text'),
        # Choice('letters1', pressKeyMap),
        # Choice('letters2', pressKeyMap),
    ]
    defaults = {
        "n": 1,
    }

class MappingMail(dragonfly.MappingRule):
     mapping = gmail_mapping
     extras = [
        IntegerRef('n', 1, 60),
        Dictation('text')
     ]
     defaults = {
        "n": 1,
     }

chrome_grammar.add_rule(MappingChrome())
chrome_grammar.load()

gmail_grammar.add_rule(MappingMail())
gmail_grammar.load()

def unload():
    global chrome_grammar
    if chrome_grammar:
        chrome_grammar.unload()
    chrome_grammar = None

    global gmail_grammar
    if gmail_grammar:
        gmail_grammar.unload()
    gmail_grammar = None

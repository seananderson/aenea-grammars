# Commands for interatcting with Google Chrome

import aenea
import aenea.configuration
from aenea.lax import Key, Text, Dictation
import dragonfly
from aenea import *

chrome_mapping = {
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
    'easy proxy that': Key("cs-e"),
    'easy proxy and zotero that': Key("cs-o"),
    'zotero that': Key("cs-z"),
    'mort': Key("j:10"),
    'lest': Key("k:10"),
    'edit in vim': Key("f12"),

    #  Searching
    'jump till <text>': Key("escape, slash") + Text("%(text)s") + Key("enter"),
    'previous [<n>]': Key("s-N:%(n)d"),
    'next [<n>]': Key("n:%(n)d"),
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
    'archive (message|that)': Key("e"),
    'preeve [<n>]': Key("p:%(n)d"),
}

chrome_context = aenea.ProxyCustomAppContext(id="Google Chrome")
gmail_context = aenea.ProxyCustomAppContext(titl="Mail") & aenea.ProxyCustomAppContext(id = "Google Chrome")
chrome_grammar = dragonfly.Grammar('chrome', context=chrome_context)
gmail_grammar = dragonfly.Grammar('gmail', context=gmail_context)

class MappingChrome(dragonfly.MappingRule):
    mapping = chrome_mapping
    extras = [
        IntegerRef('n', 1, 25),
        Dictation('text'),
    ]
    defaults = {
        "n": 1,
    }

class MappingMail(dragonfly.MappingRule):
     mapping = gmail_mapping
     extras = [
        IntegerRef('n', 1, 25),
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

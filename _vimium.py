# Created for aenea using libraries from the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# Commands for interatcting with Chrome. Requires the Vimium extension.
# http://vimium.github.io/
#
# Author: Tony Grosinger
#
# Licensed under LGPL

import aenea
import aenea.configuration
from aenea.lax import Key, Text, Dictation
from aenea import (
    IntegerRef
)
import dragonfly

chrome_context = aenea.ProxyCustomAppContext(id="Google Chrome")
grammar = dragonfly.Grammar('chrome', context=chrome_context)
# grammar = dragonfly.Grammar('chrome')

letterMap = {
    "(alpha|arch)": "a",
    "(bravo|brav|brov) ": "b",
    "(charlie|char) ": "c",
    "(delta|dell) ": "d",
    "(echo|eck) ": "e",
    "(foxtrot|fox) ": "f",
    "(golf|goof) ": "g",
    "(hotel|hark) ": "h",
    "(india|ice) ": "i",
    "(juliet|julia|jinks) ": "j",
    "(kilo|koop) ": "k",
    "(lima|lug) ": "l",
    "(mike|mowsh) ": "m",
    "(november|nerb) ": "n",
    "(Oscar|ork) ": "o",
    "(papa|poppa|pooch) ": "p",
    "(quebec|queen|quash) ": "q",
    "(romeo|rosh) ": "r",
    "(sierra|souk) ": "s",
    "(tango|teek) ": "t",
    "(uniform|union|unks) ": "u",
    "(victor|verge) ": "v",
    "(whiskey|womp) ": "w",
    "(x-ray|trex) ": "x",
    "(yankee|yang) ": "y",
    "(zulu|zooch) ": "z",
}

window_mapping = {
    # Tab navigation
    'page (previous|left)': Key("cs-tab"),
    'page (next|right)': Key("c-tab"),
    'page new': Key("w-t"),
    'page reopen': Key("ws-t"),
    'page close': Key("w-w"),
    'window close': Key("ws-w"),
    'page back': Key("w-lbracket"),
    'page forward': Key("w-rbracket"),
    'refresh': Key("w-r"),
    'link': Key("f"),
    'link new': Key("s-f"),
    # 'click [<letters1>] [<letters2>]': Key("%(letters1)s") + Key("%(letters2)s"),
    # 'one click [<letters1>]': Key("%(letters1)s"),

    #  Moving around
    'more': Key("j:10"),
    'less': Key("k:10"),
    'top': Key("g, g"),
    'bottom': Key("s-g"),
    'back': Key("s-h"),
    'forward': Key("s-l"),

    #  Searching
    'find <text>': Key("escape, slash") + Text("%(text)s") + Key("enter"),
    'next': Key("n"),
    'prev|previous': Key("N"),
}

gmail_mapping = {
    'open': Key("o"),
    'inbox': Key("g, i"),
    '[go to] label <text>': Key("g, l") + Text("%(text)s") + Key("enter"),
    'trash': Key("hash"),
    'archive': Key("e"),
    '(earl|early|earlier)': Key("j"),
    '(late|later)': Key("k"),
}


class Mapping(dragonfly.MappingRule):
    mapping = window_mapping
    extras = [
        IntegerRef('n', 1, 99),
        Dictation('text'),
    ]

class MappingMail(dragonfly.MappingRule):
     mapping = gmail_mapping
     extras = [
        Dictation('text')
     ]


grammar.add_rule(Mapping())
grammar.add_rule(MappingMail())
grammar.load()


def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

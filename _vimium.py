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
import dragonfly
from aenea import *
import words

chrome_context = aenea.ProxyCustomAppContext(id="Google Chrome")
chrome_grammar = dragonfly.Grammar('chrome', context=chrome_context)
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

numberMap = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    }

controlKeyMap = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "page up": "pgup",
    "page down": "pgdown",
    "home": "home",
    "end": "end",
    "space": "space",
    "(enter|return)": "enter",
    "escape": "escape",
    "tab": "tab",
    "backspace": "backspace"
}


specialCharKeyMap = {
    "ampersand": "ampersand",
    "apostrophe": "apostrophe",
    "asterisk": "asterisk",
    "at symbol": "at",
    "backslash": "backslash",
    "backtick": "backtick",
    "bar": "bar",
    "caret": "caret",
    "colon": "colon",
    "comma": "comma",
    "dollar": "dollar",
    "dot": "dot",
    "[double] quote": "dquote",
    "equal": "equal",
    "bang": "exclamation",
    "pound symbol": "hash",
    "hyphen": "hyphen",
    "minus": "minus",
    "percent": "percent",
    "plus": "plus",
    "question": "question",
    "slash": "slash",
    "single quote": "squote",
    "tilde": "tilde",
    "underscore | score": "underscore",
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(specialCharKeyMap)

window_mapping = {
    # Tab navigation
    '(previous|left) window': Key("cs-tab"),
    '(next|right) window': Key("c-tab"),
    'new window': Key("w-t"),
    'reopen window': Key("ws-t"),
    'close window': Key("w-w"),
    'close all window': Key("ws-w"),
    'go back': Key("w-lbracket"),
    'go forward': Key("w-rbracket"),
    'go to': Key("w-l"),
    'refresh': Key("w-r"),
    'link|show links|links': Key("f"),
    'link new': Key("s-f"),
    'press <letters1>': Key("%(letters1)s"),
    'two press <letters1> <letters2>': Key("%(letters1)s") + Key("%(letters2)s"),
    # 'one click [<letters1>]': Key("%(letters1)s"),
    "page up": Key("pgup"),
    "page down": Key("pgdown"),

    "<letters1>": Key("%(letters1)s"),

    "(delete|del) [<n>]": Key("del:%(n)d"),
    "(backspace|chuck) [<n>]": Key("backspace:%(n)d"),
    "(enter|slap|slop)": Key("enter"),

    #  Moving around
    'more': Key("j:10"),
    'less': Key("k:10"),
    'top': Key("g, g"),
    'bottom': Key("s-g"),

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
        Choice('letters1', pressKeyMap),
        Choice('letters2', pressKeyMap),
    ]

class MappingMail(dragonfly.MappingRule):
     mapping = gmail_mapping
     extras = [
        Dictation('text')
     ]

alternatives = []
alternatives.append(RuleRef(rule=Mapping()))
alternatives.append(RuleRef(rule=MappingMail()))
alternatives.append(RuleRef(rule=words.FormatRule()))
alternatives.append(RuleRef(rule=words.ReFormatRule()))
alternatives.append(RuleRef(rule=words.NopeFormatRule()))
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

# chrome_grammar.add_rule(Mapping())
# chrome_grammar.add_rule(MappingMail())
chrome_grammar.add_rule(RepeatRule())
chrome_grammar.load()

def unload():
    global chrome_grammar
    if chrome_grammar:
        chrome_grammar.unload()
    chrome_grammar = None

# TODO fix the consistency of split , screen,window
# Low-level keyboard input module
#
# Based on the work done by the creators of the Dictation Toolbox
# https://github.com/dictation-toolbox/dragonfly-scripts
#
# and _multiedit-en.py found at:
# http://dragonfly-modules.googlecode.com/svn/trunk/command-modules/documentation/mod-_multiedit.html
#
# Modifications by: Tony Grosinger
#
# Licensed under LGPL

from natlink import setMicState
from aenea import (
    Grammar,
    MappingRule,
    Text,
    Key,
    Mimic,
    Function,
    Dictation,
    Choice,
    Window,
    Config,
    Section,
    Item,
    IntegerRef,
    Alternative,
    RuleRef,
    Repetition,
    CompoundRule,
    AppContext,
)

from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
if 'semicolon' not in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')

release = Key("shift:up, ctrl:up, alt:up")
esc = Key("escape")

def goto_line(line1):
    for c in str(line1):
        Key(c).execute()
    Key("s-g").execute()

def yank_lines(line1, line2):
    goto_line(line1)
    Key("s-V").execute()
    goto_line(line2)
    Key("y").execute()

def delete_lines(line1, line2):
    goto_line(line1)
    Key("s-V").execute()
    goto_line(line2)
    Key("d").execute()


def cancel_and_sleep(text=None, text2=None):
    """Used to cancel an ongoing dictation and puts microphone to sleep.

    This method notifies the user that the dictation was in fact canceled,
     a message in the Natlink feedback window.
    Then the the microphone is put to sleep.
    Example:
    "'random mumbling go to sleep'" => Microphone sleep.

    """
    print("* Dictation canceled. Going to sleep. *")
    setMicState("sleeping")

# For repeating of characters.
specialCharMap = {
    "(bar|vertical bar|pipe)": "|",
    "(dash|hyphen)": "-",
    "minus": " - ",
    "M-dash": "---",
    "N-dash": "--",
    "dot|point": ".",
    "comma": ",",
    "backslash": "\\",
    "underscore": "_",
    "(star|asterisk|times)": " * ",
    "colon": ":",
    "(semicolon|semi-colon)": ";",
    "at symbol": "@",
    "[double] quote": '"',
    "single quote": "'",
    "hash|pound": "# ",
    "dollar": "$",
    "percent": "%",
    "ampersand": "&",
    "slash": "/",
    "equal": " = ",
    "plus": " + ",
    "space": " ",
    'backtick': "`",
    "bang|exclamation-mark": "!",
    "question-mark": "?",
    "caret": "^",
    "greate-than": " > ",
    "less-than": " < ",
    "R-pipe": " %>% ",
    "assign": " <- ",
    "tilde": "~",
}

# # Modifiers for the press-command.
# modifierMap = {
#     "alt": "a",
#     "control": "c",
#     "shift": "s",
#     "super": "w",
# }

# # Modifiers for the press-command, if only the modifier is pressed.
# singleModifierMap = {
#     "alt": "alt",
#     "control": "ctrl",
#     "shift": "shift",
#     "super": "win",
# }

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

# generate uppercase versions of every letter
upperLetterMap = {}
for letter in letterMap:
    upperLetterMap["(upper|sky) " + letter] = letterMap[letter].upper()
letterMap.update(upperLetterMap)

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

navCharMap = {
    "colon": "colon",
    "comma": "comma",
    "dollar": "dollar",
    "dot": "dot",
    "equal": "equal",
    "percent": "percent",
    "underscore | score": "underscore",
    "wren": "rparen",
    "rack": "rbracket",
    "quote": "dquote",
    "single quote": "squote",
}

operateCharMap = {
    "parens": "rparen",
    "word": "w",
    "scent": "s",
    "para": "p",
    "bracks": "rbracket",
    "braces": "rbrace",
    "quotes": "dquote",
    "single quotes": "squote",
}

# TODO , is not working.
advCharMap = {
        "inner": "i",
        "around": "a",
}

verbCharMap = {
        "dell": "d",
        "yank": "y",
        "change": "c",
        "sell": "v",
}

lineVerbCharMap = {
        "dine": "d:2",
        "yank line": "y:2",
        "chine": "c:2",
        "vine": "s-V",
        "diner": "s-D",
        "viner": "v,dollar",
        "yanker": "y,dollar",
        "chiner": "s-C",
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(specialCharKeyMap)

def handle_word(text):
    words = str(text).split()
    print 'word (', words, ')'
    if len(words) > 0:
        Text(words[0]).execute()
        if len(words) > 1:
            Mimic(' '.join(words[1:])).execute()


grammarCfg = Config("multi edit")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(
       {
    "ampersand": Key("ampersand"),
    "apostrophe": Key("apostrophe"),
    "asterisk": Key("asterisk"),
    "at symbol": Key("at"),
    "backslash": Key("backslash"),
    "backtick": Key("backtick"),
    "bar": Key("bar"),
    "caret": Key("caret"),
    "colon": Key("colon"),
    "calm": Key("comma"),
    "dollar": Key("dollar"),
    "dot": Key("dot"),
    "period": Key("dot,space"),
    "[double] quote": Key("dquote"),
    "equals": Key("equal"),
    "bang|exclamation [mark]": Key("exclamation"),
    "pound symbol": Key("hash"),
    "hyphen": Key("hyphen"),
    "minus": Key("minus"),
    "percent": Key("percent"),
    "plus": Key("plus"),
    "question": Key("question"),
    "slash": Key("slash"),
    "single quote": Key("squote"),
    "tilde": Key("tilde"),
    "underscore | score": Key("underscore"),

    # Navigation keys.
    "[<n>] up | up [<n>]": Key("up:%(n)d"),
    "[<n>] down | down [<n>]": Key("down:%(n)d"),
    "[<n>] left | left [<n>]": Key("left:%(n)d"),
    "[<n>] right | right [<n>]": Key("right:%(n)d"),
    "page up [<n>]": Key("pgup:%(n)d"),
    "page down [<n>]": Key("pgdown:%(n)d"),
    "left <n> (word|words)": Key("a-left/3:%(n)d"),
    "right <n> (word|words)": Key("a-right/3:%(n)d"),
    "home": Key("home"),
    "end": Key("end"),
    "go to top": esc + Key("g,g"),
    "go to bottom": esc + Key("s-G"),
    "space": Key("space"),
    "space [<n>]": Key("space:%(n)d"),
    "(enter|slap|slop) [<n>]": Key("enter:%(n)d"),
    "tab [<n>]": Key("tab:%(n)d"),
    "(delete|del) [<n>]": Key("del:%(n)d"),
    "(backspace|chuck) [<n>]": Key("backspace:%(n)d"),
    "extract [<n>]": Key("x:%(n)d"),
    "release [all]": release,
    # "<pressKey>": Key("%(pressKey)s"),

    # Shorthand multiple characters.
    # "double <char>": Text("%(char)s%(char)s"),
    "double escape": Key("escape, escape"), # Exiting menus.

    # Punctuation and separation characters, for quick editing.
    # "colon [<n>]": Key("colon/2:%(n)d"),
    # "semi-colon [<n>]": Key("semicolon/2:%(n)d"),
    # "comma [<n>]": Key("comma/2:%(n)d"),
    "period": Key("dot, space"), # cannot be followed by a repeat count
    "(dash|hyphen|minus) [<n>]": Key("hyphen/2:%(n)d"),
    # "underscore [<n>]": Key("underscore/2:%(n)d"),
    "press <letters>": Key("%(letters)s"),
    "<letters>": Text("%(letters)s"), # TODO
    #"<char>": Text("%(char)s"),

    'langle [<n>]': Key('langle:%(n)d'),
    'lace [<n>]': Key('lbrace:%(n)d'),
    'lack [<n>]': Key('lbracket:%(n)d'),
    'len [<n>]': Key('lparen:%(n)d'),
    'rangle [<n>]': Key('rangle:%(n)d'),
    'race [<n>]': Key('rbrace:%(n)d'),
    'rack [<n>]': Key('rbracket:%(n)d'),
    '(ren|wren) [<n>]': Key('rparen:%(n)d'),

    # 'chuck [<n>]': Key('del:%(n)d'),
    # 'scratch [<n>]': Key('backspace:%(n)d'),

    # 'yoop [<n>]': Key('pgup:%(n)d'),
    # 'drop [<n>]': Key('pgdown:%(n)d'),

    'lope [<n>]': Key('a-left:%(n)d'),
    'rope [<n>]': Key('a-right:%(n)d'),
    'drop [<n>]': Key('a-backspace:%(n)d'),

    'word <text>': Function(handle_word),
    # 'num <num>': Text("%(num)d"),
    'change <text> to <text2>': Key("home, slash") + Text("%(text)s") + Key("enter, c, e") + Text("%(text2)s") + Key("escape"),

    # Text corrections.
    # "(add|fix) missing space": Key("a-left/3, space, a-right/3"),
    # "(delete|remove) (double|extra) (space|whitespace)": Key("a-left/3, backspace, a-right/3"),
    # "(delete|remove) (double|extra) (type|char|character)": Key("a-left/3, del, a-right/3"),
    # Microphone sleep/cancel started dictation.
    # "[<text>] (go to sleep|cancel and sleep) [<text2>]": Function(cancel_and_sleep),

    "paste": esc + Key("p"),
    "paste up": esc + Key("P"),
    "yank": Key("y"),
    "duplicate line [<n>]": esc + Key("y,y,p:%(n)d"),
    "duplicate line up <n>": esc + Key("y,y,P:%(n)d"),

    "toggle case": esc + Key("tilde"),

    "visual|vis-mode": esc + Key("v"),
    "vis-line|vine|visual line|select line": esc + Key("s-v"),
    "visual block|vis-block": esc + Key("c-v"),

    "next [<n>]": esc + Key("n:%(n)d"),
    "previous | preeve [<n>]": esc + Key("N:%(n)d"),

    # "swan": esc + Key("comma,comma,s"),
    # "swan right": esc + Key("comma,comma,f"), # TODO
    # "swan left": esc + Key("comma,comma,F"),
    # "swan word": esc + Key("comma,comma,w"),
    # "swan word end": esc + Key("comma,comma,e"),
    # "swan (anywhere|anything)": esc + Key("comma,comma,a"),

    'matching': esc + Key("percent"),

    "word [<n>]": esc + Key("%(n)d, w"),
    "word end [<n>]": esc + Key("%(n)d, e"),
    "bird [<n>]": esc + Key("%(n)d, b"),
    "bird end [<n>]": esc + Key("%(n)d, g, e"),
    "next para [<n>]": esc + Key("%(n)d, rbrace"),
    "preev para [<n>]": esc + Key("%(n)d, lbrace"),
    "next scent [<n>]": esc + Key("%(n)d, rparen"),
    "preev scent [<n>]": esc + Key("%(n)d, lparen"),

    "undo [<n>]": esc + Key("u:%(n)d"),
    "redo [<n>]": esc + Key("c-r:%(n)d"),
    "repeat [<n>]": esc + Key("%(n)d, dot"),

    # Magic:
    "<verbKey> <advKey> <opKey>": esc + Key("%(verbKey)s") + Key("%(advKey)s") + Key("%(opKey)s"),
    "<lineVerbKey>": esc + Key("%(lineVerbKey)s"),

## TODO move out or abbreviate
    'sell till <navKey>': Key("escape, v, t") + Key("%(navKey)s"),
    # 'sell clude <navKey>': Key("escape, v, f") + Key("%(navKey)s"),
    'dell till <navKey>': Key("escape, d, t") + Key("%(navKey)s"),
    # 'dell clude <navKey>': Key("escape, d, f") + Key("%(navKey)s"),
    'change till <navKey>': Key("escape, c, t") + Key("%(navKey)s"),
    # 'change clude <navKey>': Key("escape, c, f") + Key("%(navKey)s"),
    'till <navKey>': Key("escape, f") + Key("%(navKey)s"),
    # 'clude <navKey>': Key("escape, f") + Key("%(navKey)s"),

    "indent": esc + Key("rangle,rangle"),
    "out-dent": esc + Key("langle,langle"),
    "join [<n>]": esc + Key("s-J:%(n)d"),

    "go to [line] <line1>": esc + Function(goto_line),
    "(viz|vis) go to [line] <line1>": Function(goto_line),

    "(type|insert)": Key("i"),
    "big insert": esc + Key("s-i"),
    "(append)": Key("a"),
    "big append": esc + Key("s-a"),
    "(out|escape)": Key("escape"),
    "open": esc + Key("o"),
    "big open": esc + Key("s-o"),
    "paste": esc + Key("p"),
    "big paste": esc + Key("s-p"),

    "find <text>": esc + Key("slash") + Text("%(text)s"),
    "find back <text>": esc + Key("question") + Text("%(text)s"),
    "visual find <text>": Key("slash") + Text("%(text)s"),
    "visual find back <text>": Key("question") + Text("%(text)s"),
    "jump to <text>": esc + Key("slash") + Text("%(text)s") + Key("enter"),
    "jump back to <text>": esc + Key("question") + Text("%(text)s") + Key("enter"),
    "find blank": esc + Key("slash"),
    "find back blank": esc + Key("question"),
    "clear search": esc + Key("enter:2"),

    "mark": esc + Key("m,a"),
    "jark": esc + Key("backtick,a"),
    "vark": esc + Key("v,backtick,a"),
    "yark": esc + Key("y,backtick,a"),
    "cark": esc + Key("c,backtick,a"),
    "de-dark": esc + Key("c,backtick,a"),

    "jump forward [<n>]": esc + Key("c-i:%(n)d"),
    "jump back [<n>]": esc + Key("c-o:%(n)d"),
    "ledit [<n>]": esc + Key("%(n)d,g,semicolon"),

    "pleat [<n>]": Key("c-p:%(n)d"),
    "pleat again": Key("c-x,c-p"),
    "pleat next [<n>]": Key("c-n:%(n)d"),
    "pleat next again": Key("c-x,c-n"),
    "pleat file": Key("c-x,c-f"),
    "pleat line": Key("c-x,c-l"),
    "pleat omni": Key("c-x,c-o"),
    # "choose": Key("c-c,a"), # TODO ??

    },
    namespace={
        "Key": Key,
        "Text": Text,
    }
)

# This is a sentence.

class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 20),
        # IntegerRef("num", 0, 2000),
        IntegerRef("line1", 1, 700),
        IntegerRef("line2", 1, 700),
        Dictation("text"),
        Dictation("text2"),
        Choice("char", specialCharMap),
        Choice("letters", letterMap),
        # Choice("modifier1", modifierMap),
        # Choice("modifier2", modifierMap),
        # Choice("modifierSingle", singleModifierMap),
        # Choice("pressKey", pressKeyMap),
        Choice("navKey", navCharMap),
        Choice("opKey", operateCharMap),
        Choice("advKey", advCharMap),
        Choice("verbKey", verbCharMap),
        Choice("lineVerbKey", lineVerbCharMap),
    ]
    defaults = {
        "n": 1,
    }

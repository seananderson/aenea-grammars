from aenea import (
    Key,
    Text,
)

letterMap = {
    "(A|alpha|arch)": "a",
    "(B|bravo|brav|beta) ": "b",
    "(C|charlie|char) ": "c",
    "(D|delta|dell) ": "d",
    "(E|echo|eck) ": "e",
    "(F|foxtrot|fox) ": "f",
    "(golf|goof) ": "g",
    "(H|hotel|hark) ": "h",
    "(india|ice) ": "i",
    "(J|juliet|julia|jinks) ": "j",
    "(K|kilo) ": "k",
    "(L|lima|lug) ": "l",
    "(M|mike) ": "m",
    "(november|noob) ": "n",
    "(O|Oscar|ork) ": "o",
    "(P|papa|poppa|pooch) ": "p",
    "(Q|quebec|queen) ": "q",
    "(romeo|rosh) ": "r",
    "(S|sierra|souk) ": "s",
    "(tango|teek) ": "t",
    "(uniform|union|unks) ": "u",
    "(V|victor|verge) ": "v",
    "(W|whiskey|womp) ": "w",
    "(X|x-ray|trex) ": "x",
    "(yankee|yang) ": "y",
    "(Z|zulu|zooch) ": "z",
}
numberMap = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "duo": "2",
    "three": "3",
    "four": "4",
    "quad": "4",
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

specialCharMap = {
    # "(bar|vertical bar|pipe)": "|",
    # "(dash|minus|hyphen)": "-",
    # "(dot|period)": ".",
    # "comma": ",",
    # "backslash": "\\",
    # "underscore": "_",
    # "asterisk": "*",
    # "colon": ":",
    # "(semicolon|semi-colon)": ";",
    # "at symbol": "@",
    # "[double] quote": '"',
    # "single quote": "'",
    # "pound|hash": "#",
    # "dollar": "$",
    # "percent": "%",
    # "and": "&",
    "slash": "slash",
    # "equal": "=",
    # "plus": "+",
    # "space": " "
}

release = Key("shift:up, ctrl:up, alt:up, win:up")

# Modifiers for the press-command.
modifierMap = {
    "alt|option": "a",
    "control": "c",
    "shift": "s",
    "command": "w",
}

# Modifiers for the press-command, if only the modifier is pressed.
singleModifierMap = {
    "alt|option": "a",
    "control": "c",
    "shift": "s",
    "command": "w",
}

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
pressKeyMap.update(specialCharMap)

# These words can be prefaced by the word "say"
reservedWord = {
    "up": "up",
    "down": "down",
    "left": "left",
    "right": "right",
    "home": "home",
    "end": "end",
    "space": "space",
    "tab": "tab",
    "backspace": "backspace",
    "delete": "delete",
    "enter": "enter",
    "paste": "paste",
    "copy": "copy",
    "cut": "cut",
    "undo": "undo",
    "release": "release",
    "page up": "page up",
    "page down": "page down",
    "say": "say",
    "select": "select",
    "uppercase": "uppercase",
    "lowercase": "lowercase",
    "expand": "expand",
    "squash": "squash",
    "dash": "dash",
    "underscore": "underscore",
    "dot": "dot",
    "period": "period",
    "minus": "minus",
    "semi-colon": "semi-colon",
    "hyphen": "hyphen",
    "triple": "triple",
    "kill": "kill",
    "to end": "to end",
    "slap": "slap",
    "pound": "pound",
    "hash": "hash",
}

genericKeys = {
  "<letters>": Key("%(letters)s"),
    "num <numbers>": Key("%(numbers)s"),
    "(enter|slap|slop)": Key("enter"),
    "undo [<n>]": Key("w-z:%(n)d"),
    "redo [<n>]": Key("sw-z:%(n)d"),
    "kill [<n>]": Key("del:%(n)d"),
    "kill to end": Key("c-k"),
    "cut line": Key("c-a, sw-right, w-x, w-right, del"),
    "copy line": Key("c-a, sw-right, w-c, w-right"),

    "del [<n>]": Key("backspace:%(n)d"),
    "space [<n>]": Key("space:%(n)d"),
    "copy [that]": Key("w-c"),
    "cut [that]": Key("w-x"),
    "paste [that]": Key("w-v"),
    "release all": release,
    "press shift": Key("shift:down"),
    "release shift": Key("shift:up"),
    "press <pressKey>": Key("%(pressKey)s"),

    "ampersand": Key("ampersand"),
    "apostrophe": Key("apostrophe"),
    "asterisk": Key("asterisk"),
    "at symbol": Key("at"),
    "backslash": Key("backslash"),
    "backtick": Key("backtick"),
    "bar": Key("bar"),
    "caret": Key("caret"),
    "colon": Key("colon"),
    "comma": Key("comma,space"),
    "dollar": Key("dollar"),
    "dot": Key("dot"),
    "period": Key("dot,space"),
    "semicolon": Key("semicolon,space"),
    "[double] (quote|quotes)": Key("dquote"),
    "equals": Key("equal"),
    "bang|exclamation mark": Key("exclamation"),
    "pound|hash": Key("hash"),
    "hyphen": Key("hyphen"),
    "minus": Key("minus"),
    "percent": Key("percent"),
    "plus": Key("plus"),
    "question mark": Key("question"),
    "slash": Key("slash"),
    "single quote": Key("squote"),
    "tilde": Key("tilde"),
    "underscore": Key("underscore"),
    "tab [<n>]": Key("tab:%(n)d"),
    "say <reservedWord>": Text("%(reservedWord)s"),

 # Navigation keys.
    "[<n>] up": Key("up:%(n)d"),
    "[<n>] down": Key("down:%(n)d"),
    "[<n>] left": Key("left:%(n)d"),
    "[<n>] right": Key("right:%(n)d"),
    "page up [<n>]": Key("pgup:%(n)d"),
    "page down [<n>]": Key("pgdown:%(n)d"),
    "bit [<n>]": Key("a-left:%(n)d"),
    "fit [<n>]": Key("a-right:%(n)d"),
    "de-bit [<n>]": Key("sa-left:%(n)d") + Key("del"),
    "de-fit [<n>]": Key("sa-right:%(n)d") + Key("del"),
    "home": Key("w-left"),
    "end": Key("w-right"),
    "to top": Key("w-up"),
    "to bottom": Key("w-down"),
    'langle [<n>]': Key('langle:%(n)d'),
    'lace [<n>]': Key('lbrace:%(n)d'),
    'lack [<n>]': Key('lbracket:%(n)d'),
    'len|lape [<n>]': Key('lparen:%(n)d'),
    'rangle [<n>]': Key('rangle:%(n)d'),
    'race [<n>]': Key('rbrace:%(n)d'),
    'rack [<n>]': Key('rbracket:%(n)d'),
    '(ren|wren) [<n>]': Key('rparen:%(n)d'),

    "<modifier1> <pressKey> [<n>]":
      Key("%(modifier1)s-%(pressKey)s:%(n)d"),
    "<modifier1> <modifier2> <pressKey> [<n>]":
      Key("%(modifier1)s%(modifier2)s-%(pressKey)s:%(n)d"),

    "duplicate": Key("c-a, ws-right, w-c, w-right, enter, w-v"),
}

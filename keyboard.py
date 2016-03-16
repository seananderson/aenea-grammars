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
end = Key("i")
append = Key("a")

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

# # F1 to F12. (do these actually work?)
# functionKeyMap = {
#     'F one': 'f1',
#     'F two': 'f2',
#     'F three': 'f3',
#     'F four': 'f4',
#     'F five': 'f5',
#     'F six': 'f6',
#     'F seven': 'f7',
#     'F eight': 'f8',
#     'F nine': 'f9',
#     'F ten': 'f10',
#     'F eleven': 'f11',
#     'F twelve': 'f12',
# }

pressKeyMap = {}
pressKeyMap.update(letterMap)
pressKeyMap.update(numberMap)
pressKeyMap.update(controlKeyMap)
# pressKeyMap.update(functionKeyMap)


def handle_word(text):
    #words = map(list, text)
    #print text
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
 "comma": Key("comma"),
 "dollar": Key("dollar"),
 "dot": Key("dot"),
 "period": Key("dot,space"),
 "[double] quote": Key("dquote"),
 "equal": Key("equal"),
 "bang": Key("exclamation"),
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
        "up [<n>]":                                             Key("up:%(n)d"),
        "down [<n>]":                                           Key("down:%(n)d"),
        "left [<n>]":                                           Key("left:%(n)d"),
        "right [<n>]":                                          Key("right:%(n)d"),
        "page up [<n>]":                                        Key("pgup:%(n)d"),
        "page down [<n>]":                                      Key("pgdown:%(n)d"),
        # "left <n> (word|words)": Key("a-left/30:%(n)d"),
#        "right <n> (word|words)": Key("a-right/3:%(n)d"),
        "home":                                                 Key("home"),
        "end":                                                  Key("end"),
        "doc home":                                             Key("c-home/3"),
        "doc end":                                              Key("c-end/3"),
        # Functional keys.
        "space":                                                Key("space"),
        "space [<n>]":                                          Key("space:%(n)d"),
        "(enter|slap|slop) [<n>]":                              Key("enter:%(n)d"),
        "tab [<n>]":                                            Key("tab:%(n)d"),
        "delete [<n>]":                                         Key("del:%(n)d"),
        #"delete [this] line": Key("home, s-end, del"),  # @IgnorePep8
        "backspace [<n>]":                                      Key("backspace:%(n)d"),
        "extract [<n>]":                                        Key("x:%(n)d"),
        #"application key": Key("apps/3"),
        #"win key": Key("win/3"),
        #"paste [that]": Function(paste_command),
        #"copy [that]": Function(copy_command),
        #"cut [that]": release + Key("c-x/3"),
        #"select all": release + Key("c-a/3"),
        #"[(hold|press)] alt": Key("alt:down/3"),
        #"release alt": Key("alt:up"),
        #"[(hold|press)] shift": Key("shift:down/3"),
        #"release shift": Key("shift:up"),
       # "[(hold|press)] control": Key("ctrl:down/3"),
        #"release control": Key("ctrl:up"),
        #"release [all]": release,
        "press key <pressKey>":                                 Key("%(pressKey)s"),
        # Closures.
        "angle brackets":                                       Key("langle, rangle, left/3"),
        "[square] brackets":                                    Key("lbracket, rbracket, left/3"),
        "[curly] braces":                                       Key("lbrace, rbrace, left/3"),
        "parens":                                               Key("lparen, rparen, left/3"),
       # TODO causes error "quotes": Key("dquote, dquote, left/3"),
        "backticks":                                            Key("backtick:2, left"),
        "single quotes":                                        Key("squote, squote, left/3"),
        # Shorthand multiple characters.
#        "double <char>": Text("%(char)s%(char)s"),
#        "triple <char>": Text("%(char)s%(char)s%(char)s"),
        "double escape":                                        Key("escape, escape"),  # Exiting menus.
        # Punctuation and separation characters, for quick editing.
        "colon [<n>]":                                          Key("colon/2:%(n)d"),
        "semi-colon [<n>]":                                     Key("semicolon/2:%(n)d"),
        "comma [<n>]":                                          Key("comma/2:%(n)d"),
        "(period)":                                             Key("dot, space"),  # cannot be followed by a repeat count
        "(dash|hyphen|minus) [<n>]":                            Key("hyphen/2:%(n)d"),
        "underscore [<n>]":                                     Key("underscore/2:%(n)d"),
        "press <letters>":                                      Key("%(letters)s"),
        "<letters>":                                            Text("%(letters)s"),
        # "<char>":                                               Text("%(char)s"),

        'langle [<n>]':                                         Key('langle:%(n)d'),
        'lace [<n>]':                                           Key('lbrace:%(n)d'),
        '(lack|lair) [<n>]':                                    Key('lbracket:%(n)d'),
        #'(laip|len) [<n>]':   Key('lparen:%(n)d'),
        'len [<n>]':                                            Key('lparen:%(n)d'),
        'rangle [<n>]':                                         Key('rangle:%(n)d'),
        'race [<n>]':                                           Key('rbrace:%(n)d'),
        '(rack|rare) [<n>]':                                    Key('rbracket:%(n)d'),
        #'(raip|ren|wren) [<n>]':   Key('rparen:%(n)d'),
        '(ren|wren) [<n>]':                                     Key('rparen:%(n)d'),

       # "act [<n>]": Key("escape:%(n)d"),
        #"calm [<n>]": Key("comma:%(n)d"),
        'into':                                                 Key('space,bar,space'),
      #  'care':        Key('home'),
    #    '(doll|dole)': Key('end'),
        'chuck [<n>]':                                          Key('del:%(n)d'),
        'scratch [<n>]':                                        Key('backspace:%(n)d'),
        #"visual": Key("v"),
        #"visual line": Key("s-v"),
        #"visual block": Key("c-v"),
        #"doc save": Key("c-s"),

        # 'gope [<n>]':  Key('pgup:%(n)d'),
        # 'drop [<n>]':  Key('pgdown:%(n)d'),

        'lope [<n>]':                                           Key('c-left:%(n)d'),
        '(yope|rope) [<n>]':                                    Key('c-right:%(n)d'),
        '(hill scratch|hatch) [<n>]':                           Key('c-backspace:%(n)d'),

        #'hexadecimal': Text("0x"),
        #'suspend': Key('c-z'),

        'word <text>':                                          Function(handle_word),
        'num <num>':                                            Text("%(num)d"),
        'change <text> to <text2>':                             Key("home, slash") + Text("%(text)s") + Key("enter, c, e") + Text("%(text2)s") + Key("escape"),

        # Text corrections.
        "(add|fix) missing space":                              Key("c-left/3, space, c-right/3"),
        "(delete|remove) (double|extra) (space|whitespace)":    Key("c-left/3, backspace, c-right/3"),  # @IgnorePep8
        "(delete|remove) (double|extra) (type|char|character)": Key("c-left/3, del, c-right/3"),  # @IgnorePep8
        # Microphone sleep/cancel started dictation.
        "[<text>] (go to sleep|cancel and sleep) [<text2>]":    Function(cancel_and_sleep),  # @IgnorePep8

     "paste":                                                   esc + Key("p"),
     "paste up":                                                esc + Key("P"),
     "yank":                                                    esc + Key("y"),
     "duplicate line [<n>]":                                    esc + Key("y,y,p:%(n)d"),
     "duplicate line up <n>":                                   esc + Key("y,y,P:%(n)d"),

    "toggle case":                                              esc + Key("tilde"),

    "visual mode":                                              esc + Key("v"),
    "visual line|select line":                                  esc + Key("s-v"),
    "visual block":                                             esc + Key("c-v"),
    "reselect visual":                                          esc + Key("g,v"),

    "next [<n>]":                                               esc + Key("n:%(n)d"),
    "previous [<n>]":                                           esc + Key("N:%(n)d"),

    "format":                                                   esc + Key("g,q"),

    "swan":                                                     esc + Key("comma,comma,s"),
    "swan right":                                               esc + Key("comma,comma,f"),
    "swan left":                                                esc + Key("comma,comma,F"),
    "swan word":                                                esc + Key("comma,comma,w"),
    "swan word end":                                            esc + Key("comma,comma,e"),
    "swan (anywhere|anything)":                                 esc + Key("comma,comma,a"),

    'matching':                                                 esc + Key("percent"),
    'screen center':                                            esc + Key("z, dot"),
    'screen top':                                               esc + Key("z, t"),
    'screen bottom':                                            esc + Key("z, b"),

    'buffer delete':                                            esc + Key('colon,b,d,enter'),
    'buffer next':                                              esc + Key('colon,b,n,enter'),
    'buffer previous':                                          esc + Key('colon,b,p,enter'),
    'buffer list':                                              esc + Key('colon,l,s,enter'),

    "word [<n>]":                                               esc + Key("%(n)d, w"),
    "word end [<n>]":                                           esc + Key("%(n)d, e") + append,
    "bird [<n>]":                                               esc + Key("%(n)d, b"),
    "bird end [<n>]":                                           esc + Key("%(n)d, g, e") + append,
    "next para [<n>]":                                          esc + Key("%(n)d, rbrace"),
    "preev para [<n>]":                                         esc + Key("%(n)d, lbrace"),
    "next scent [<n>]":                                         esc + Key("%(n)d, rparen"),
    "preev scent [<n>]":                                        esc + Key("%(n)d, lparen"),

    "undo [<n>]":                                               esc + Key("u:%(n)d"),
    "redo [<n>]":                                               esc + Key("c-r:%(n)d"),
    "repeat [<n>]":                                             esc + Key("%(n)d, dot"),

    "delete around word":                                       esc + Key("d,a,w"),
    "delete inner word":                                        esc + Key("d,i,w"),
    "delete around paragraph":                                  esc + Key("d,a,p"),
    "delete inner paragraph":                                   esc + Key("d,i,p"),
    "delete around sentence":                                   esc + Key("d,a,s"),
    "delete inner sentence":                                    esc + Key("d,i,s"),
    "delete around paren":                                      esc + Key("d,a,rparen"),
    "delete inner paren":                                       esc + Key("d,i,rparen"),
    "delete around bracks":                                     esc + Key("d,a,rbracket"),
    "delete inner bracks":                                      esc + Key("d,i,rbracket"),
    "delete around braces":                                     esc + Key("d,a,rbrace"),
    "delete inner braces":                                      esc + Key("d,i,rbrace"),
    "delete around quotes":                                     esc + Key("d,a,s-squote"),
    "delete inner quotes":                                      esc + Key("d,i,s-squote"),
    "delete around single quotes":                              esc + Key("d,a,squote"),
    "delete inner single quotes":                               esc + Key("d,i,squote"),

    "change around word":                                       esc + Key("c,a,w"),
    "change inner word":                                        esc + Key("c,i,w"),
    "change around paragraph":                                  esc + Key("c,a,p"),
    "change inner paragraph":                                   esc + Key("c,i,p"),
    "change around sentence":                                   esc + Key("c,a,s"),
    "change inner sentence":                                    esc + Key("c,i,s"),
    "change around parens":                                     esc + Key("c,a,rparen"),
    "change inner parens":                                      esc + Key("c,i,rparen"),
    "change around bracks":                                     esc + Key("c,a,rbracket"),
    "change inner bracks":                                      esc + Key("c,i,rbracket"),
    "change around braces":                                     esc + Key("c,a,rbrace"),
    "change inner braces":                                      esc + Key("c,i,rbrace"),
    "change around quotes":                                     esc + Key("c,a,dquote"),
    "change inner quotes":                                      esc + Key("c,i,dquote"),
    "change around single quotes":                              esc + Key("c,a,squote"),
    "change inner single quotes":                               esc + Key("c,i,squote"),

    "yank around word":                                         esc + Key("y,a,w"),
    "yank inner word":                                          esc + Key("y,i,w"),
    "yank around paragraph":                                    esc + Key("y,a,p"),
    "yank inner paragraph":                                     esc + Key("y,i,p"),
    "yank around sentence":                                     esc + Key("y,a,s"),
    "yank inner sentence":                                      esc + Key("y,i,s"),
    "yank around parens":                                       esc + Key("y,a,rparen"),
    "yank inner parens":                                        esc + Key("y,i,rparen"),
    "yank around bracks":                                       esc + Key("y,a,rbracket"),
    "yank inner bracks":                                        esc + Key("y,i,rbracket"),
    "yank around braces":                                       esc + Key("y,a,rbrace"),
    "yank inner braces":                                        esc + Key("y,i,rbrace"),
    "yank around quotes":                                       esc + Key("y,a,dquote"),
    "yank inner quotes":                                        esc + Key("y,i,dquote"),
    "yank around single quotes":                                esc + Key("y,a,squote"),
    "yank inner single quotes":                                 esc + Key("y,i,squote"),

    "delete [this] line":                                       esc + Key("d:2"),
    "kill [this] line":                                         esc + Key("D"),
    "delete line <line1>":                                      esc + Key("escape") + Function(goto_line) + Key("d:2"),
    "delete (line|lines) <line1> through <line2>":              esc + Key("escape") + Function(delete_lines),
    "yank [this] line":                                         esc + Key("escape, y:2"),
    "yank line <line1>":                                        esc + Key("escape") + Function(goto_line) + Key("y:2"),
    "yank (line|lines) <line1> through <line2>":                esc + Key("escape") + Function(yank_lines),
     "change [this] line":                                      esc + Key("c:2"),

    "delete through are-paren":                                 esc + Key("d,t,rparen"),
    "delete through laip":                                      esc + Key("d,t,lparen"),
    "delete through rack":                                      esc + Key("d,t,rbrace"),
    "delete through lack":                                      esc + Key("d,t,lbracket"),
    "delete through rack":                                      esc + Key("d,t,rbracket"),
    "delete through quote":                                     esc + Key("d,t,s-squote"),

    "paste":                                                    esc + Key("p"),
    "shift paste":                                              esc + Key("P"),
    "out-dent line":                                            esc + Key("langle,langle"),
    "join [<n>]":                                               esc + Key("J:%(n)d"),

    "indent line":                                              esc + Key("rangle,rangle"),

    "split (screen|window)":                                    esc + Key("c-w,s"),
    "split (screen|window) vertically":                         esc + Key("c-w,v"),
    "(screen|window) left":                                     esc + Key("c-w,h"),
    "(screen|window) right":                                    esc + Key("c-w,l"),
    "(screen|window) up":                                       esc + Key("c-w,k"),
    "(screen|window) down":                                     esc + Key("c-w,j"),
    "close [this] (split|screen)":                                              esc + Key("c-w,c"),
    "close other splits":                                       esc + Key("colon/100,o,n,l,y/100,enter"),
    "make split wide":                                          esc + Key("colon/100,v,e,r,t,i,c,a,l/100,space,r,e,s,i,z,e/100,space,plus,6/100,enter"),
    "make split narrow":                                        esc + Key("colon/100,v,e,r,t,i,c,a,l/100,space,r,e,s,i,z,e/100,space,minus,6/100,enter"),
    "make split tall":                                          esc + Key("colon/100,space,r,e,s,i,z,e/100,space,plus,6/100,enter"),
    "make split short":                                         esc + Key("colon/100,space,r,e,s,i,z,e/100,space,minus,6/100,enter"),

    "go to [line] <line1>":                                     esc + Function(goto_line),
    "visual go to [line] <line1>":                              Function(goto_line),

    "(type|insert)":                                            Key("i"),
    "(big insert)":                                             esc + Key("I"),
    "(append)":                                                 Key("a"),
    "(big append)":                                             esc + Key("A"),
    "(out|escape)":                                             Key("escape"),
    "open":                                                     esc + Key("o"),
    "open up|big open":                                         esc + Key("O"),

    "find <text>":                                              esc + Key("slash") + Text("%(text)s"),
    "find back <text>":                                         esc + Key("question") + Text("%(text)s"),
    "visual find <text>":                                       Key("slash") + Text("%(text)s"),
    "visual find back <text>":                                  Key("question") + Text("%(text)s"),
    "jump to <text>":                                           esc + Key("slash") + Text("%(text)s") + Key("enter"),
    "jump back to <text>":                                      esc + Key("question") + Text("%(text)s") + Key("enter"),
    "find blank":                                               esc + Key("slash"),
    "find back blank":                                          esc + Key("question"),
    "clear search":                                             esc + Key("enter:2"),

    "mark":                                                     esc + Key("m,a"),
    "jark":                                                     esc + Key("backtick,a"),
    "vark":                                                     esc + Key("v,backtick,a"),
    "yark":                                                     esc + Key("y,backtick,a"),
    "cark":                                                     esc + Key("d,backtick,a"),

    "jump forward [<n>]":                                       esc + Key("c-i:%(n)d"),
    "jump back [<n>]":                                          esc + Key("c-o:%(n)d"),
    # "jump back here [<n>]":                                   esc + Key("%(n)d,g,semicolon"),

    "complete [<n>]":                                           Key("c-p:%(n)d"),
    "complete again":                                           Key("c-x,c-p"),
    "complete next [<n>]":                                      Key("c-n:%(n)d"),
    "complete next again":                                      Key("c-x,c-n"),
    "complete file":                                            Key("c-x,c-f"),
    "complete line":                                            Key("c-x,c-l"),
    "complete omni":                                            Key("c-x,c-o"),
    "choose":                                                   Key("c-c,a"),
    "magic star":                                               esc + Key("asterisk"),

    "switch":                                                   esc + Key("escape, c-p"),
    "switch recent":                                            esc + Key("escape,colon,s-C,t,r,l,s-P,s-M,s-R,s-U,enter"),

    "comment":                                                  esc + Key("g,c,c"),
    "comment paragraph":                                        esc + Key("g,c,a,p"),
    "comment <line1> to <line2>":                               esc + Key("colon,%(line1)d") + Text(",") + Key("%(line2)d") + Text("Commentary"),

    "scroll down [<n>]":                                        esc + Key("c-d:%(n)d") ,
    "scroll up [<n>]":                                          esc + Key("c-d:%(n)d") ,
    "scroll up":                                                esc + Key("c-u"),

     "record macro":                                            Key("q,q"),
     "end macro":                                               Key("q"),
     "repeat macro [<n>]":                                      Key("at,at:%(n)d"),
    },
    namespace={
        "Key": Key,
        "Text": Text,
    }
)

class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 100),
        IntegerRef("num", 0, 1000),
        IntegerRef("line1", 1, 900),
        IntegerRef("line2", 1, 900),
        Dictation("text"),
        Dictation("text2"),
        Choice("char", specialCharMap),
        Choice("letters", letterMap),
        # Choice("modifier1", modifierMap),
        # Choice("modifier2", modifierMap),
        # Choice("modifierSingle", singleModifierMap),
        Choice("pressKey", pressKeyMap),
    ]
    defaults = {
        "n": 1,
    }

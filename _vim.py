from natlink import setMicState
from aenea import *

from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
# from dragonfly import Function
if 'semicolon' not in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')

import words
import generic
import osx
import vocab

esc = Key("escape")

def goto_line(line1):
    for c in str(line1):
        Key(c).execute()
    Key("s-g").execute()

# def goto_line2(n1, n2, n3):
#     for c in (str(n1)+str(n2)+str(n3)):
#         Key(c).execute()
#     Key("s-g").execute()

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

navCharMap = {
    "colon": "colon",
    "comma": "comma",
    "dollar": "dollar",
    "dot": "dot",
    "equal": "equal",
    "percent": "percent",
    "underscore": "underscore",
    "rap": "rparen",
    "lap": "lparen",
    "langle": "langle",
    "rangle": "rangle",
    "rack": "rbracket",
    "lack": "lbracket",
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


vimEditing = {
    "husher": Key("0"),
    "hush": esc + Key("caret"),
    "pup": esc + Key("dollar"),
    "[<n>] up": esc + Key("k:%(n)d"),
    "[<n>] down": esc + Key("j:%(n)d"),
    "[<n>] left": esc + Key("h:%(n)d"),
    "[<n>] right": esc + Key("l:%(n)d"),

    "[<n>] arrow up": Key("up:%(n)d"),
    "[<n>] arrow down": Key("down:%(n)d"),
    "[<n>] arrow left": Key("left:%(n)d"),
    "[<n>] arrow right": Key("right:%(n)d"),
    "go to top": esc + Key("g,g"),
    "go to bottom": esc + Key("s-G"),
    "extract [<n>]": Key("x:%(n)d"),
    "paste": esc + Key("p"),
    "paste up": esc + Key("P"),
    "yank": Key("y"),
    "dupe line [<n>]": esc + Key("y,y,p:%(n)d"),
    "dupe line up <n>": esc + Key("y,y,P:%(n)d"),
    "visual|vis-mode": esc + Key("v"),
    "vis-line|vine|visual line|select line": esc + Key("s-v"),
    "visual block|vis-block": esc + Key("c-v"),
    "reselect": esc + Key("g,v"),
    "insert": Key("i"),
    "big insert": Key("s-i"),
    "append": Key("a"),
    "big append": Key("s-a"),
    "escape": Key("escape"),
    "open": esc + Key("o"),
    "big open": esc + Key("s-o"),
    "paste": esc + Key("p"),
    "big paste": esc + Key("s-p"),

    "next [<n>]": esc + Key("n:%(n)d"),
    "preeve [<n>]": esc + Key("N:%(n)d"),

    'matching': esc + Key("percent"),

    "nerd [<n>]": esc + Key("%(n)d, w"),
    "ned [<n>]": esc + Key("%(n)d, e"),
    "bird [<n>]": esc + Key("%(n)d, b"),
    "bed [<n>]": esc + Key("%(n)d, g, e"),
    "next para [<n>]": esc + Key("%(n)d, rbrace"),
    "preev para [<n>]": esc + Key("%(n)d, lbrace"),
    "next scent [<n>]": esc + Key("%(n)d, rparen"),
    "preev scent [<n>]": esc + Key("%(n)d, lparen"),
    "next sec [<n>]": esc + Key("%(n)d, rbracket, rbracket"),
    "preev sec [<n>]": esc + Key("%(n)d, lbracket, lbracket"),

    "undo [<n>]": esc + Key("u:%(n)d"),
    "redo [<n>]": esc + Key("c-r:%(n)d"),
    "repeat [<n>]": esc + Key("%(n)d, dot"),

    'sell till <navKey>': Key("escape, v, t") + Key("%(navKey)s"),
    # 'sell clude <navKey>': Key("escape, v, f") + Key("%(navKey)s"),
    'dell till <navKey>': Key("escape, d, t") + Key("%(navKey)s"),
    # 'dell clude <navKey>': Key("escape, d, f") + Key("%(navKey)s"),
    'change till <navKey>': Key("escape, c, t") + Key("%(navKey)s"),
    # 'change clude <navKey>': Key("escape, c, f") + Key("%(navKey)s"),
    'jump till <navKey> [<n>]': Key("escape, %(n)d, f") + Key("%(navKey)s"),
    'jump bill <navKey> [<n>]': Key("escape, %(n)d, s-F") + Key("%(navKey)s"),
    'jump (bill|till) again [<n>]': Key("escape, %(n)d, s-K"),
     # nnoremap K ;
    'reverse (bill|till) [<n>]': Key("escape, %(n)d, f6"),
     # nnoremap <F6> ,

    # 'naper': Key("escape, f, rparen"),
    # 'paper': Key("escape, s-F, lparen"),
    # 'nacker': Key("escape, f, rbracket"),
    # 'packer': Key("escape, s-F, lbracket"),
    # 'clude <navKey>': Key("escape, f") + Key("%(navKey)s"),

    "indent": esc + Key("rangle,rangle"),
    "out-dent": esc + Key("langle,langle"),
    "join [<n>]": esc + Key("s-J:%(n)d"),

    # "go to [line] <line1>": esc + Function(goto_line),
    # "delete lines <line1> through <line2>": esc + Function(delete_lines),
    # "yank lines <line1> through <line2>": esc + Function(yank_lines),
    # "(viz|vis) go to [line] <line1>": Function(goto_line),

    # Magic:
    "<verbKey> <advKey> <opKey>": esc + Key("%(verbKey)s") + Key("%(advKey)s") + Key("%(opKey)s"),
    "<lineVerbKey>": esc + Key("%(lineVerbKey)s"),


    "find": esc + Key("slash"),
    "find and replace": esc + Key("colon, percent, s, slash, slash, g, left, left"),
    "vis find and replace": Key("colon, s, slash, slash, g, left, left"),
    "find back": esc + Key("question"),
    "find now <text>": esc + Key("slash") + Text("%(text)s"),
    "find back now <text>": esc + Key("question") + Text("%(text)s"),
    "visual find <text>": Key("slash") + Text("%(text)s"),
    "visual find back <text>": Key("question") + Text("%(text)s"),
    "jump to <text>": esc + Key("slash") + Text("%(text)s") + Key("enter"),
    "jump back to <text>": esc + Key("question") + Text("%(text)s") + Key("enter"),
    # "clear search": esc + Key("enter:2"),

    "mark": esc + Key("m,a"),
    "jark": esc + Key("backtick,a"),
    "vark": esc + Key("v,backtick,a"),
    "yark": esc + Key("y,backtick,a"),
    "cark": esc + Key("c,backtick,a"),
    "del-mark": esc + Key("c,backtick,a"),

    "jump forward [<n>]": esc + Key("c-i:%(n)d"),
    "jump back [<n>]": esc + Key("c-o:%(n)d"),
    "last edit [<n>]": esc + Key("%(n)d,g,semicolon"),

    "pop [<n>]": Key("c-p:%(n)d"),
    "pop again": Key("c-x,c-p"),
    "pip [<n>]": Key("c-n:%(n)d"),
    "pip again": Key("c-x,c-n"),
    "(pip|pop) file": Key("c-x,c-f"),
    "(pip|pop) line": Key("c-x,c-l"),
    "(pip|pop) omni": Key("c-x,c-o"),
    "(pip|pop) arg": Key("c-x,c-a"),
    "(pip|pop) cancel": Key("c-e"),
    "snip": Key("c-b"),

    "format": esc + Key("g,q"),
    "edit args": esc+Key("colon,a,r,g,s,space,asterisk,dot"),

    "comment": esc + Key("g,c"),
    "comment line": esc + Key("g,c,c"),
    "comment paragraph": esc + Key("g,c,a,p"),
    # "comment <line1> through <line2>": esc + Key("colon,%(line1)d") + Text(",") + Key("%(line2)d") + Text("Commentary"),

    "(mort|scroll-down) [<n>]": esc + Key("c-d:%(n)d") ,
    "(lest|scroll-up) [<n>]": esc + Key("c-u:%(n)d") ,

    "record macro": Key("q,q"),
    "end macro": Key("q"),
    "repeat macro [<n>]": Key("%(n)d,at,q"),
    "(maru|magic star) [<n>]": esc + Key("%(n)d, asterisk"),
    "(paru|magic pound) [<n>]": esc + Key("%(n)d, hash"),
}

class vimCommands(MappingRule):
    mapping  = {
### splits:
    "split (screen|window)": esc + Key("c-w,s"),
    "split (screen|window) vertically": esc + Key("c-w,v"),
    "(screen|window) left": esc + Key("c-w,h"),
    "(screen|window) right": esc + Key("c-w,l"),
    "(screen|window) up": esc + Key("c-w,k"),
    "(screen|window) down": esc + Key("c-w,j"),
    "(split|screen|window) close": esc + Key("c-w,c"),
    "close other splits": esc + Key("colon/100,o,n,l,y/100,enter"),

    "edit file": esc + Key("colon,e,space,tab"),
    "buff-switch": esc + Key("colon,b,space,tab"),
    'buff-delete': esc + Key('colon,b,d,enter'),
    'buff-next': esc + Key('colon,b,n,enter'),
    'buff-previous': esc + Key('colon,b,p,enter'),
    'buff-list': esc + Key('colon,l,s,enter'),
    'screen (center|middle)': esc + Key("z, dot"),
    'screen top': esc + Key("z, t"),
    'screen bottom': esc + Key("z, b"),
    "swiddle": esc + Key("escape, c-p"),
    "swiddle recent": esc + Key("escape,colon,s-C,t,r,l,s-P,s-M,s-R,s-U,enter"),

    'suspend': Key('c-z'),
    "edit config file": esc + Key("comma, e, v"),
    "table of contents": esc + Key("colon, s-T, s-O, s-C, enter"),
    "source config file": esc + Key("comma, s, v"),
    "source session": esc + Key("colon,s,o,space"),
    "run command": esc + Key("colon,exclamation,space"),
    "exit vim": esc + Key("colon,q,enter"),
    "split explorer": esc + Key("colon,s-S,e,x,enter"),
    "please exit vim": esc + Key("colon,q,exclamation,enter"),
    "save and exit please": esc + Key("colon,w,q,exclamation,enter"),
    "save and (exit|quit)": esc + Key("colon,w,q,enter"),
    "save file": esc + Key("colon,u,p,d,a,t,e,enter"),
    "save all files": esc + Key("colon,w,a,l,l,enter"),
    "save as": esc + Key("colon,s,a,v,e,a,s,space"),
    "toggle numbers": esc + Key("colon,s,e,t,space,r,e,l,a,t,i,v,e,n,u,m,b,e,r,exclamation") + Key("enter"),
    "browse (old|recent) files": esc + Key("colon,b,r,o,space,o,l") + Key("enter"),
    "set theme ocean": esc + Key("colon,c,o,l,o/50,space,b,a,s,e,1,6/50,minus,o,c,e,a,n/50,enter"),
    "set theme mocha": esc + Key("colon,c,o,l,o/50,space,b,a,s,e,1,6/50,minus,m,o,c,h,a/50,enter"),
    "set theme one dark": esc + Key("colon,c,o,l,o/50,space,o,n,e,d,a,r,k") + Key("enter"),
    # "set theme solarized": esc + Key("colon/50,c,o,l,o/50,space,s,o,l,a,r,i,z,e,d") + Key("enter"),
    "set theme Seoul": esc + Key("colon/50,c,o,l,o/50,space,s,e,o,u,l,2,5,6") + Key("enter"),
    "toggle lights": esc + Key("colon/50,s-T,o,g,g,l,e,s-B,s-G") + Key("enter"),
    "toggle spelling": esc + Key("colon/50,s,e,t,l,o,c,a,l,space,s,p,e,l,l,exclamation")+Key("enter"),
    "toggle invisible characters": esc + Key("colon,s,e,space,l,i,s,t,exclamation")+Key("enter"),
    "toggle nerd": esc + Key("colon/50,s-N,s-E,s-R,s-D,s-T,r,e,e,s-T,o,g,g,l,e/50,enter"),
    "toggle cursor-line": esc + Key("colon/50,s,e,space,c,u,r,s,o,r,l,i,n,e/50,exclamation,enter"),
    "get directory": Key("p,w,d/10,enter"),
    "vim help": esc + Key("colon,h,space"),
    "substitute": esc + Key("s,slash"),
    "make split wide": esc + Key("colon/100,v,e,r,t,i,c,a,l/100,space,r,e,s,i,z,e/100,space,plus,6/100,enter"),
    "make split narrow": esc + Key("colon/100,v,e,r,t,i,c,a,l/100,space,r,e,s,i,z,e/100,space,minus,6/100,enter"),
    "make split tall": esc + Key("colon/100,space,r,e,s,i,z,e/100,space,plus,6/100,enter"),
    "make split short": esc + Key("colon/100,space,r,e,s,i,z,e/100,space,minus,6/100,enter"),
    "make splits equal": esc + Key("c-w,equal"),

    "toggle obsession": esc + Key("colon,s-o,b,s,e,s,s,i,o,n,exclamation,enter"),

    "fugitive status": esc + Key("colon,s-G,s,t,a,t,u,s,enter"),
    "fugitive diff": esc + Key("colon,s-G,d,i,f,f,enter"),
    "fugitive commit": esc + Key("colon,s-G,c,o,m,m,i,t,enter,i"),
    "fugitive add": esc + Key("colon,s-G,w,r,i,t,e,enter"),
    "fugitive blame": esc + Key("colon,s-G,b,l,a,m,e,enter"),
    "fugitive remove": esc + Key("colon,s-G,r,e,m,o,v,e,enter"),
    "fugitive grep": esc + Key("colon,s-G,g,r,e,p,space"),
    "fugitive browse": esc + Key("colon,s-G,b,r,o,w,s,e,enter"),
    "fugitive move": esc + Key("colon,s-G,m,o,v,e,space"),
    "fugitive log": esc + Key("colon,s-G,l,o,g,enter"),
    "fugitive commit all": esc + Key("colon,s-G,i,t,space,c,o,m,m,i,t,space,hyphen,a,v,enter"),

}

generalKeys = {}
generalKeys.update(generic.genericKeys)
generalKeys.update(osx.osx)
generalKeys.update(vocab.vocabWord)
generalKeys.update(vimEditing)

grammarCfg = Config("all")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(generalKeys,
       namespace={
        "Key": Key,
        "Text": Text,
    })

class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 65),
        # IntegerRef("line1", 1, 100),
        # IntegerRef("line2", 1, 100),
        Dictation("text"),
        Dictation("text2"),
        Choice("modifier1", generic.modifierMap),
        Choice("modifier2", generic.modifierMap),
        Choice("modifierSingle", generic.singleModifierMap),
        Choice('letters', generic.letterMap),
        Choice('numbers', generic.numberMap),
        Choice("pressKey", generic.pressKeyMap),
        Choice("reservedWord", generic.reservedWord),
        Choice("navKey", navCharMap),
        Choice("opKey", operateCharMap),
        Choice("advKey", advCharMap),
        Choice("verbKey", verbCharMap),
        Choice("lineVerbKey", lineVerbCharMap),
    ]
    defaults = {
        "n": 1,
    }

alternatives = []
alternatives.append(RuleRef(rule=KeystrokeRule()))
alternatives.append(RuleRef(rule=words.FormatRule()))
root_action = Alternative(alternatives)

sequence = Repetition(root_action, min=1, max=16, name="sequence")

class RepeatRule(CompoundRule):
    spec = "<sequence>"
    extras = [sequence]

    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]
        for action in sequence:
            action.execute()

vim_context = aenea.ProxyCustomAppContext(match="substring", titl="nvim") & aenea.ProxyCustomAppContext(id="iTerm2")
grammar = Grammar("root rule", context = vim_context)
grammar.add_rule(RepeatRule())
grammar.load()

exmode_grammar = Grammar("ExMode grammar",context=vim_context)
exmode_grammar.add_rule(vimCommands())
exmode_grammar.load()

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

    global exmode_grammar
    if exmode_grammar:
        exmode_grammar.unload()
    exmode_grammar = None

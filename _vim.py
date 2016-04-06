from natlink import setMicState
from aenea import *

from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
# from dragonfly import Function
if 'semicolon' not in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')
import words
from words import clean_prose, cap_that, lower_that
import generic
import osx
import vocab
import formatting

esc = Key("escape")
LEADER = 'comma'
out = Key("escape:2,l")
ii = Key("i")

# these are the characters that can be jumped to with f or F
# note that I have reprinted the alphabet here
# I get dragonfly complexity errors if I try to append the alphabet
navCharMap = {
    "colon": "colon",
    "calm": "comma",
    "dollar": "dollar",
    "dot": "dot",
    "equal": "equal",
    "percent": "percent",
    "underscore": "underscore",
    "semi": "semicolon",
    "rap": "rparen",
    "lap": "lparen",
    "race": "rbrace",
    "lace": "lbrace",
    "langle": "langle",
    "rangle": "rangle",
    "rack": "rbracket",
    "lack": "lbracket",
    "quote": "dquote",
    "single quote": "squote",
    "hyphen": "hyphen",
    "(alpha|arch)": "a",
    "(bravo)": "b",
    "(charlie|char)": "c",
    "(delta)": "d",
    "(echo|eck)": "e",
    "(foxtrot|fox) ": "f",
    "(golf|gee)": "g",
    "(hotel) ": "h",
    "(india|ice) ": "i",
    "(juliet) ": "j",
    "(kilo) ": "k",
    "(lug) ": "l",
    "(mike) ": "m",
    "(november) ": "n",
    "(oscar|ork) ": "o",
    "pooch ": "p",
    "(quebec|queen) ": "q",
    "(romeo) ": "r",
    "(sierra|souk) ": "s",
    "(tango) ": "t",
    "(union|unks) ": "u",
    "(victor|verge) ": "v",
    "(whiskey|womp) ": "w",
    "(x-ray) ": "x",
    "(yankee) ": "y",
    "(zulu) ": "z",
}
# navCharMap.update(generic.letterMap)

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

advCharMap = {
        "inner": "i",
        "around": "a",
}

verbCharMap = {
        "dosh": "d",
        "copy": "y",
        "change": "c",
        "select": "v",
}

lineVerbCharMap = {
        "dosh line": "d:2",
        "copy line": "y:2",
        "change line": "c:2,escape",
        "select line": "s-V",
        "kill till end": "s-D",
        "select till end": "v,dollar",
        "copy till end": "y,dollar",
        "change till end": "s-C,escape",
}

vimEditing = {
    # inserting:
    "<letters>": Key("%(letters)s"),
    "sky <letters>": Key("s-%(letters)s"),
    "num <numbers>": Key("%(numbers)s"),
    "<numbers>": Key("%(numbers)s"),
    "space [<n>]": Key("space:%(n)d"),
    "<specials> [<n>]": Key("%(specials)s:%(n)d"),
    "say <text>": Function(lower_that),
    # "<text>": Function(lower_that),
    "cap <text>": Function(cap_that),

    "(slap|slop) [<n>]": Key("enter:%(n)d"),
    "chuck [<n>]": Key("backspace:%(n)d"),
    "kill [<n>]": Key("del:%(n)d"),

    "dish [<n>]": esc + Key("%(n)d,d,l"),
    "dosh [<n>]": esc + Key("%(n)d,d,h"),

    # "litteral <letters>": Key("%(letters)s"),
    # "teral sky <letters>": Key("s-%(letters)s"),
    # "litteral num <numbers>":  Key("%(numbers)s"),
    # "litteral <numbers>": Key("%(numbers)s"),
    # "litteral space [<n>]": Key("space:%(n)d"),

    "[<n>] up": esc + Key("k:%(n)d"),
    "[<n>] down": esc + Key("j:%(n)d"),
    "[<n>] left": esc + Key("h:%(n)d"),
    "[<n>] right": esc + Key("l:%(n)d"),

    "gee up [<n>]": esc + Text("%(n)d") + Key("g,k"),
    "gee down [<n>]": esc + Text("%(n)d") + Key("g,j"),
    "gee left [<n>]": esc + Text("%(n)d") + Key("g,h"),
    "gee right [<n>]": esc + Text("%(n)d") + Key("g,l"),

    "[<n>] arrow up": Key("up:%(n)d"),
    "[<n>] arrow down": Key("down:%(n)d"),
    "[<n>] arrow left": Key("left:%(n)d"),
    "[<n>] arrow right": Key("right:%(n)d"),

    "cary": esc + Key("0"),
    "car": esc + Key("caret"),
    "doll": esc + Key("dollar"),
    "go to top": esc + Key("g,g"),
    "go to bottom": esc + Key("s-G"),
    "extract [<n>]": esc + Key("x:%(n)d"),

    "paste": esc + Key("p"),
    "paste up": esc + Key("P"),
    "paste older": esc + Key("comma,p"), # maxbrunsfeld/vim-yankstack
    "paste newer": esc + Key("comma,s-P"), # maxbrunsfeld/vim-yankstack

    "copy that": Key("y"),
    "copy that": Key("y"),

    "duplicate line [<n>]": esc + Key("y,y,p:%(n)d"),
    "duplicate line above <n>": esc + Key("y,y,P:%(n)d"),

    "vis-mode": esc + Key("v"),
    "vis-line": esc + Key("s-v"),
    "vis-block": esc + Key("c-v"),
    "reselect": esc + Key("g,v"),

    "sert": esc + Key("i"),
    "big sert": esc + Key("s-i"),
    "append": esc + Key("a"),
    "big append": esc + Key("s-a"),
    "escape": Key("escape:2"),
    "open": esc + Key("o"),
    "big open": esc + Key("s-o"),
    "paste": esc + Key("p"),
    "big paste": esc + Key("s-p"),

    "next [<n>]": esc + Key("n:%(n)d"),
    "preeve [<n>]": esc + Key("N:%(n)d"),

    'matching': esc + Key("percent"),

    'yope [<n>]': esc + Key('%(n)d, w'),
    'iyope [<n>]': esc + Key('%(n)d, e'),
    'lope [<n>]': esc + Key('%(n)d, b'),
    'ilope [<n>]': esc + Key('%(n)d, g, e'),

    'yopert [<n>]': esc + Key('%(n)d, s-W'),
    'iyopert [<n>]': esc + Key('%(n)d, s-E'),
    'lopert [<n>]': esc + Key('%(n)d, s-B'),
    'ilopert [<n>]': esc + Key('%(n)d, g, s-E'),

    # EasyMotion
    'easy lope': esc + Key('%s:2, b' % LEADER),
    'easy yope': esc + Key('%s:2, w' % LEADER),
    'easy elope': esc + Key('%s:2, g, e' % LEADER),
    'easy iyope': esc + Key('%s:2, e' % LEADER),

    'easy lopert': esc + Key('%s:2, B' % LEADER),
    'easy yopert': esc + Key('%s:2, W' % LEADER),
    'easy elopert': esc + Key('%s:2, g, E' % LEADER),
    'easy eyopert': esc + Key('%s:2, E' % LEADER),

    'easy jump': esc + Key('%s:2, f' % LEADER),
    'easy dosh': esc + Key('d, %s:2, t' % LEADER),

    # Sneak
    'sneaker <letters> <letters2>': esc + Key('s') + Key("%(letters)s") + Key("%(letters2)s"),

    "next para [<n>]": esc + Key("%(n)d, rbrace"),
    "preev para [<n>]": esc + Key("%(n)d, lbrace"),
    "next scent [<n>]": esc + Key("%(n)d, rparen"),
    "preev scent [<n>]": esc + Key("%(n)d, lparen"),
    "next sec [<n>]": esc + Key("%(n)d, rbracket, rbracket"),
    "preev sec [<n>]": esc + Key("%(n)d, lbracket, lbracket"),

    "undo [<n>]": esc + Key("u:%(n)d"),
    "redo [<n>]": esc + Key("c-r:%(n)d"),
    "repeat [<n>]": esc + Key("%(n)d, dot"),

    'copy till <navKey>': esc + Key("escape, y, t") + Key("%(navKey)s"),
    'select till <navKey>': esc + Key("escape, v, t") + Key("%(navKey)s"),
    'dosh till <navKey>': esc + Key("escape, d, t") + Key("%(navKey)s"),
    'change till <navKey>': esc + Key("escape, c, t") + Key("%(navKey)s"),
    'quick <navKey> [<n>]': esc + Key("escape, %(n)d, f") + Key("%(navKey)s"),
    'quick back <navKey> [<n>]': esc + Key("escape, %(n)d, s-F") + Key("%(navKey)s"),
    'skip [<n>]': esc + Key("escape, %(n)d, f"),
    'skip back [<n>]': esc + Key("escape, %(n)d, s-f"),
    # 'jump (bill|till) again [<n>]': esc + Key("escape, %(n)d, semicolon"),
     # nnoremap K ;
    'reverse semi [<n>]': esc + Key("escape, %(n)d, f6"),
     # nnoremap <F6> ,

    "indent": esc + Key("rangle,rangle"),
    "out-dent": esc + Key("langle,langle"),
    "join [<n>]": esc + Key("s-J:%(n)d"),
    "toggle case": esc + Key("tilde"),

    # Magic:
    "<verbKey> <advKey> <opKey>": esc + Key("%(verbKey)s") + Key("%(advKey)s") + Key("%(opKey)s"),
    "chuck <n> (words|word)": esc + Key("d,%(n)d") + Key("s-B"),
    "kill <n> (words|word)": esc + Key("d,%(n)d") + Key("s-W"),
    "<lineVerbKey>": esc + Key("%(lineVerbKey)s"),

    "find": esc + Key("slash"),
    "find and replace": esc + Key("colon, percent, s, slash, slash, g, left, left"),
    "vis find and replace": Key("colon, s, slash, slash, g, left, left"),
    "find back": esc + Key("question"),
    "find now <text>": esc + Key("slash") + Text("%(text)s"),
    "find back now <text>": esc + Key("question") + Text("%(text)s"),
    "vis find <text>": Key("slash") + Text("%(text)s"),
    "vis find back <text>": Key("question") + Text("%(text)s"),
    "jump till <text>": esc + Key("slash") + Text("%(text)s") + Key("enter"),
    "jump back till <text>": esc + Key("question") + Text("%(text)s") + Key("enter"),

    # "mark [<letters>]": esc + Key("m,%(letters)s"),
    # "jump mark [<letters>]": esc + Key("backtick,%(letters)s"),
    # "sel mark [<letters>]": esc + Key("v,backtick,%(letters)s"),
    # "yank mark [<letters>]": esc + Key("y,backtick,%(letters)s"),
    # "change mark [<letters>]": esc + Key("c,backtick,%(letters)s"),
    # "del mark [<letters>]": esc + Key("d,backtick,%(letters)s"),
    "mark that": esc + Key("m,a"),
    "jump mark": esc + Key("backtick,a"),
    "format mark": esc + Key("g,q,backtick,a"),
    "select mark": esc + Key("v,backtick,a"),
    "copy mark": esc + Key("y,backtick,a"),
    "change mark": esc + Key("c,backtick,a"),
    "dosh mark": esc + Key("d,backtick,a"),
    "remove mark": esc + Key("m,hyphen"),

    # "mark that <letters>": esc + Key("m,%(letters)s"),
    # "jump mark <letters>": esc + Key("backtick,%(letters)s"),

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

    "format para": esc + Key("s-Q"),

    "comment": esc + Key("g,c"),
    "comment line": esc + Key("g,c,c"),
    "comment paragraph": esc + Key("g,c,a,p"),

    "(mort|scroll-down) [<n>]": esc + Key("c-d:%(n)d") ,
    "(lest|scroll-up) [<n>]": esc + Key("c-u:%(n)d") ,

    "record macro": esc + Key("q,q"),
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
    "write and exit please": esc + Key("colon,w,q,exclamation,enter"),
    "write and (exit|quit)": esc + Key("colon,w,q,enter"),
    "write file": esc + Key("colon,u,p,d,a,t,e,enter"),
    "write all files": esc + Key("colon,w,a,l,l,enter"),
    "write as": esc + Key("colon,s,a,v,e,a,s,space"),
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
    "get directory": esc + Key("p,w,d/10,enter"),
    "vim help": esc + Key("colon,h,space"),
    "substitute": esc + Key("s,slash"),
    "make split wide": esc + Key("colon/100,v,e,r,t,i,c,a,l/100,space,r,e,s,i,z,e/100,space,plus,6/100,enter"),
    "make split narrow": esc + Key("colon/100,v,e,r,t,i,c,a,l/100,space,r,e,s,i,z,e/100,space,minus,6/100,enter"),
    "make split tall": esc + Key("colon/100,space,r,e,s,i,z,e/100,space,plus,6/100,enter"),
    "make split short": esc + Key("colon/100,space,r,e,s,i,z,e/100,space,minus,6/100,enter"),
    "make splits equal": esc + Key("c-w,equal"),

    "toggle obsession": esc + Key("colon,s-o,b,s,e,s,s,i,o,n,exclamation,enter"),
    'toggle quick scope': esc + Key('colon,s-Q,u,i,c,k,s-S,c,o,p,e,s-T,o,g,g,l,e,enter'),
    'toggle tagbar': esc + Key('colon,s-T,a,g,b,a,r,s-T,o,g,g,l,e,enter'),
    'jump to tag': esc + Key('c-rbracket'),

    "edit args": esc+Key("colon,a,r,g,s,space,asterisk,dot"),

    "show ring": esc+Key("colon,s-Y,s-R,s-S,h,o,w,enter"),

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

    "fuzzy (buffs|buffers)": esc + Key("colon,s-B,u,f,f,e,r,s,enter"),
    "fuzzy files": esc + Key("colon,s-F,i,l,e,s,enter"),
    "fuzzy lines all": esc + Key("colon,s-L,i,n,e,s,enter"),
    "fuzzy lines": esc + Key("colon,s-B,s-L,i,n,e,s,enter"),
    "fuzzy tags all": esc + Key("colon,s-T,a,g,s,enter"),
    "fuzzy tags": esc + Key("colon,s-B,s-T,a,g,s,enter"),
    "fuzzy git files": esc + Key("colon,s-G,i,t,s-F,i,l,e,s,enter"),
    "fuzzy (history|recent)": esc + Key("colon,s-H,i,s,t,o,r,y,enter"),
    "fuzzy commits": esc + Key("colon,s-C,o,m,m,i,t,s,enter"),
    "fuzzy help": esc + Key("colon,s-H,e,l,p,enter"),
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
        Dictation("text"),
        Choice("modifier1", generic.modifierMap),
        Choice("modifier2", generic.modifierMap),
        Choice('letters', generic.letterMap),
        Choice('letters2', generic.letterMap),
        Choice('specials', generic.specialKeys),
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

sequence = Repetition(root_action, min=1, max=9, name="sequence")

class RepeatRule(CompoundRule):
    spec = "<sequence>"
    extras = [sequence]

    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]
        for action in sequence:
            action.execute()

mvim_context = aenea.ProxyCustomAppContext(id="MacVim")
nvim_context = aenea.ProxyCustomAppContext(match="substring", titl="nvim") & aenea.ProxyCustomAppContext(id="iTerm2")
git_context = aenea.ProxyCustomAppContext(match="substring", titl="git") & aenea.ProxyCustomAppContext(id="iTerm2")
gmail_context = aenea.ProxyCustomAppContext(titl="Mail") & aenea.ProxyCustomAppContext(id = "Google Chrome")
vim_plus_wasavi_context = nvim_context | mvim_context | git_context
grammar = Grammar("root rule", context = vim_plus_wasavi_context)
grammar.add_rule(RepeatRule())
grammar.load()

exmode_grammar = Grammar("ExMode grammar",context=vim_plus_wasavi_context)
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

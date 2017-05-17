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
import r_vocab
import vocab
import formatting

esc = Key("escape")
LEADER = 'comma'
out = Key("escape:2,l")
ii = Key("i")

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

vimGeneric = {
    # inserting:
    "<letters>": Key("%(letters)s"),
    "sky <letters>": Key("s-%(letters)s"),
    "num <numbers>": Key("%(numbers)s"),
    "<numbers>": Key("%(numbers)s"),
    "space [repeat <n>]": Key("space:%(n)d"),
    "<specials> [repeat <n>]": Key("%(specials)s:%(n)d"),
    "say <text>": Function(lower_that),
    # "<text>": Function(lower_that),
    "cap <text>": Function(cap_that),

    "(slap|slop) [<n>]": Key("enter:%(n)d"),
    "chuck [<n>]": Key("backspace:%(n)d"),
    "kill [<n>]": Key("del:%(n)d"),

    "rosh [<n>]": esc + Key("%(n)d,d,l"),
    "dosh [<n>]": esc + Key("%(n)d,d,h"),

    "[<n>] up": esc + Key("k:%(n)d"),
    "[<n>] down": esc + Key("j:%(n)d"),
    "[<n>] left": esc + Key("h:%(n)d"),
    "[<n>] right": esc + Key("l:%(n)d"),

#    "gee up [<n>]": esc + Text("%(n)d") + Key("g,k"),
#    "gee down [<n>]": esc + Text("%(n)d") + Key("g,j"),
#    "gee left [<n>]": esc + Text("%(n)d") + Key("g,h"),
#    "gee right [<n>]": esc + Text("%(n)d") + Key("g,l"),

    "[<n>] upper": Key("up:%(n)d"),
    "[<n>] downer": Key("down:%(n)d"),
    "[<n>] lefter": Key("left:%(n)d"),
    "[<n>] righter": Key("right:%(n)d"),

    "cary": esc + Key("0"),
    "car": esc + Key("caret"),
    "doll": esc + Key("dollar"),
    "go to top": esc + Key("g,g"),
    "go to bottom": esc + Key("s-G"),
    "extract [<n>]": esc + Key("x:%(n)d"),

    "paste older": esc + Key("comma,p"), # maxbrunsfeld/vim-yankstack
    "paste newer": esc + Key("comma,s-P"), # maxbrunsfeld/vim-yankstack

    # "copy that": Key("y"),

    "duplicate line [<n>]": esc + Key("y,y,p:%(n)d"),
    # "duplicate line above <n>": esc + Key("y,y,P:%(n)d"),

    "vis-mode": esc + Key("v"),
    "vis-line": esc + Key("s-v"),
    "vis-block": esc + Key("c-v"),
    "reselect that": esc + Key("g,v"),

    "sert": esc + Key("i"),
    "big sert": esc + Key("s-i"),
    "append": esc + Key("a"),
    "big append": esc + Key("s-a"),
    "scape|escape": Key("escape:2"),
    "open": esc + Key("o"),
    "big open": esc + Key("s-o"),
    "paste": esc + Key("p"),
    "big paste": esc + Key("s-p"),

    "next [<n>]": esc + Key("n:%(n)d"),
    "preeve [<n>]": esc + Key("N:%(n)d"),

    # 'match that': esc + Key("percent"),

    'rope [<n>]': esc + Key('%(n)d, w'),
    'irope [<n>]': esc + Key('%(n)d, e'),
    'lope [<n>]': esc + Key('%(n)d, b'),
    'ilope [<n>]': esc + Key('%(n)d, g, e'),

    'ropert [<n>]': esc + Key('%(n)d, s-W'),
    'iropert [<n>]': esc + Key('%(n)d, s-E'),
    'lopert [<n>]': esc + Key('%(n)d, s-B'),
    'ilopert [<n>]': esc + Key('%(n)d, g, s-E'),

    # Sneak
    'sneak': esc + Key('s'),
    'sneak back': esc + Key('s'),

    "next para [<n>]": esc + Key("%(n)d, rbrace"),
    "preev para [<n>]": esc + Key("%(n)d, lbrace"),
    "next scent [<n>]": esc + Key("%(n)d, rparen"),
    "preev scent [<n>]": esc + Key("%(n)d, lparen"),
    "next sec [<n>]": esc + Key("%(n)d, rbracket, rbracket"),
    "preev sec [<n>]": esc + Key("%(n)d, lbracket, lbracket"),

    "(undo|scratch) [<n>]": esc + Key("u:%(n)d"),
    "redo [<n>]": esc + Key("c-r:%(n)d"),
    "repeat [<n>]": esc + Key("%(n)d, dot"),

    'skip [<n>]': esc + Key("%(n)d, f"),
    'skip back [<n>]': esc + Key("%(n)d, s-F"),

    # 'jump (bill|till) again [<n>]': esc + Key("escape, %(n)d, semicolon"),
     # nnoremap K ;
    'reverse semi [<n>]': esc + Key("escape, %(n)d, f6"),
     # nnoremap <F6> ,

    # "indent that": esc + Key("rangle,rangle"),
    # "out-dent that": esc + Key("langle,langle"),
    "join [<n>]": esc + Key("s-J:%(n)d"),
    "toggle case": esc + Key("tilde"),

    # Magic:
    # "<verbKey> <advKey> <opKey>": esc + Key("%(verbKey)s") + Key("%(advKey)s") + Key("%(opKey)s"),
    "dosh [<n>] (words|word)": esc + Key("d,%(n)d") + Key("s-B"),
    "rosh [<n>] (words|word)": esc + Key("d,%(n)d") + Key("s-W"),
    "<lineVerbKey>": esc + Key("%(lineVerbKey)s"),

    "find": esc + Key("slash"),
    "find and replace": esc + Key("colon, percent, s, slash, slash, g, left, left"),
    "vis find and replace": Key("colon, s, slash, slash, g, left, left"),
    "find back": esc + Key("question"),
    # "find now <text>": esc + Key("slash") + Text("%(text)s"),
    # "find back now <text>": esc + Key("question") + Text("%(text)s"),
    # "vis find <text>": Key("slash") + Text("%(text)s"),
    # "vis find back <text>": Key("question") + Text("%(text)s"),
    "jump till <text>": esc + Key("slash") + Text("%(text)s") + Key("enter"),
    "jump back till <text>": esc + Key("question") + Text("%(text)s") + Key("enter"),

    "mark that": esc + Key("m,a"),
    "mark bravo": esc + Key("m,b"),
    "jump mark": esc + Key("backtick,a"),
    "format mark": esc + Key("g,q,backtick,a"),
    "select mark": esc + Key("v,backtick,a"),
    "copy mark": esc + Key("y,backtick,a"),
    "change mark": esc + Key("c,backtick,a"),
    "dosh mark": esc + Key("d,backtick,a"),
    "remove mark": esc + Key("m,hyphen"),

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

    "format para": esc + Key("s-Q"),

    "comment that": esc + Key("g,c"),
    "comment line": esc + Key("g,c,c"),
    "comment para": esc + Key("g,c,a,p"),

    "(mort) [<n>]": esc + Key("c-d:%(n)d") ,
    "(lest) [<n>]": esc + Key("c-u:%(n)d") ,

    "record macro": esc + Key("q,q"),
    "end macro": Key("q"),
    "repeat macro [<n>]": Key("%(n)d,at,q"),
    "(maru) [<n>]": esc + Key("%(n)d, asterisk"),
    "(paru) [<n>]": esc + Key("%(n)d, hash"),

    ### splits:
    "split (screen|window)": esc + Key("c-w,s"),
    "split (screen|window) vertically": esc + Key("c-w,v"),
    "(screen|window) left": esc + Key("c-w,h"),
    "(screen|window) right": esc + Key("c-w,l"),
    "(screen|window) up": esc + Key("c-w,k"),
    "(screen|window) down": esc + Key("c-w,j"),
    "close (split|screen|window)": esc + Key("c-w,c"),
    "close other splits": esc + Key("colon/10,o,n,l,y/10,enter"),

    "edit file": esc + Key("colon,e,space,tab"),
    "buff-switch": esc + Key("colon,b,space,tab"),
    'buff-delete': esc + Key('colon,b,d,enter'),
    'buff-next': esc + Key('colon,b,n,enter'),
    'buff-prev': esc + Key('colon,b,p,enter'),
    'buff-list': esc + Key('colon,l,s,enter'),
    'screen (center|middle)': esc + Key("z, dot"),
    'screen top': esc + Key("z, t"),
    'screen bottom': esc + Key("z, b"),
    "swiddle": esc + Key("escape, c-p"),
    "swiddle recent": esc + Key("escape,colon,s-C,t,r,l,s-P,s-M,s-R,s-U,enter"),

    # Send
     "(eval|rip) File": esc + Key("comma,a,a"),
     # "eval File and echo": esc + Key("comma,a,e"),
     # . "eval File (open .Rout)": esc + Key("comma,a,o"),
     # --------------------------------------------------------
     "(eval Mark|rip mark)": esc + Key("comma,b,d"),
     "eye-rip mark": esc + Key("comma,b,b"),
     # "eval Mark and echo": esc + Key("comma,b,e"),
     # "eval Mark and down": esc + Key("comma,b,d"),
     # "eval Mark and echo and down": esc + Key("comma,b,a"),
     # --------------------------------------------------------
     "eval Chunk": esc + Key("comma,c,d"),
     # "eval Chunk and echo": esc + Key("comma,c,e"),
     # "eval Chunk and down": esc + Key("comma,c,d"),
     # "eval Chunk and echo and down": esc + Key("comma,c,a"),
     "eval Chunks from top": esc + Key("comma,c,h"),
     # --------------------------------------------------------
     "(eval|rip) Func": esc + Key("comma,f,d"),
     # "eval Func and echo": esc + Key("comma,f,e"),
     # "eval Func and down": esc + Key("comma,f,d"),
     # "eval Func and echo and down": esc + Key("comma,f,a"),
     # --------------------------------------------------------
     "(eval|rip) Selected": esc + Key("comma,s,d"),
     # "eval Selected and echo": esc + Key("comma,s,e"),
     # "eval Selected down": esc + Key("comma,s,d"),
     # "eval Selected and echo and down": esc + Key("comma,s,a"),

     "(eval|rip) Preev": esc + Key("g,v/2,comma,s,d"),
     # "eval Preev and echo": esc + Key("g,v/100,comma,s,e"),
     # . "eval Selected (Runuate and insert output in new tab)": esc + Key("comma,s,o"),
     # --------------------------------------------------------
     "eval Para": esc + Key("comma,p,d"),
     # "eval Para and echo": esc + Key("comma,p,e"),
     # "eval Para and down": esc + Key("comma,p,d"),
     # "eval Para and echo and down": esc + Key("comma,p,a"),
     # --------------------------------------------------------
     "eye-rip": esc + Key("comma,l"),
     "rip [<n>]": esc + Key("enter/2:%(n)d"),

     "Print that": esc + Key("comma,r,p"),
     "Name that": esc + Key("comma,r,n"),
     "Structure that": esc + Key("comma,r,t"),
     "View that": esc + Key("comma,r,v"),
     # --------------------------------------------------------
     "Argument that": esc + Key("comma,r,a"),
     "Example that": esc + Key("comma,r,e"),
     "Help that": esc + Key("comma,r,h"),
     # --------------------------------------------------------
     "Summary that": esc + Key("comma,r,s"),
     "Plot that": esc + Key("comma,r,g"),
     "Plot and summary": esc + Key("comma,r,b"),

    "assign that": Key("space,langle,hyphen,space"),
    "pipe that": Key("space,percent,rangle,percent,space"),

    "edit args": esc+Key("colon,a,r,g,s,space,asterisk,dot"),
    "run makefile": esc + Key("colon/100,exclamation,m,a,k,e,enter"),

    "close buffer": esc + Key("colon,q,enter"),
    "write and (exit|quit)": esc + Key("colon,w,q,enter"),
    "write file": esc + Key("colon,u,p,d,a,t,e,enter"),
    "write all files": esc + Key("colon,w,a,l,l,enter"),
    "write as": esc + Key("colon,s,a,v,e,a,s,space"),

    "fugitive status": esc + Key("colon,s-G,s,t,a,t,u,s,enter"),
    "fugitive push": esc + Key("colon,s-G,p,u,s,h,enter"),
    "fugitive pull": esc + Key("colon,s-G,p,u,l,l,enter"),
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
    "fuzzy grep": esc + Key("colon,s-A,g,enter"),
}

class vimCommands(MappingRule):
    mapping  = {

    "that's it": esc + Key("colon,w,q,enter"),
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
    "toggle numbers": esc + Key("colon,s,e,t,space,r,e,l,a,t,i,v,e,n,u,m,b,e,r,exclamation") + Key("enter"),
    "browse (old|recent) files": esc + Key("colon,b,r,o,space,o,l") + Key("enter"),
    # "set theme ocean": esc + Key("colon,c,o,l,o/50,space,b,a,s,e,1,6/50,minus,o,c,e,a,n/50,enter"),
    # "set theme mocha": esc + Key("colon,c,o,l,o/50,space,b,a,s,e,1,6/50,minus,m,o,c,h,a/50,enter"),
    # "set theme one dark": esc + Key("colon,c,o,l,o/50,space,o,n,e,d,a,r,k") + Key("enter"),
    # "set theme solarized": esc + Key("colon/50,c,o,l,o/50,space,s,o,l,a,r,i,z,e,d") + Key("enter"),
    "set theme solarized-light": esc + Key("colon/50,c,o,l,o/50,space,f,l,a,t,t,e,n,e,d,underscore,l,i,g,h,t") + Key("enter"),
    "set theme solarized-dark": esc + Key("colon/50,c,o,l,o/50,space,f,l,a,t,t,e,n,e,d,underscore,d,a,r,k") + Key("enter"),
    "set theme Seoul": esc + Key("colon/50,c,o,l,o/50,space,s,e,o,u,l,2,5,6") + Key("enter"),
    "set theme Seoul light": esc + Key("colon/50,c,o,l,o/50,space,s,e,o,u,l,2,5,6,hyphen,l,i,g,h,t") + Key("enter"),
    "toggle lights": esc + Key("colon/50,s-T,o,g,g,l,e,s-B,s-G") + Key("enter"),
    "toggle spelling": esc + Key("colon/50,s,e,t,l,o,c,a,l,space,s,p,e,l,l,exclamation")+Key("enter"),
    "lucky correct": esc + Key("1,z,equal"),
    "toggle invisible characters": esc + Key("colon,s,e,space,l,i,s,t,exclamation")+Key("enter"),
    "toggle nerdtree": esc + Key("colon/50,s-N,s-E,s-R,s-D,s-T,r,e,e,s-T,o,g,g,l,e/50,enter"),
    "toggle cursor-line": esc + Key("colon/50,s,e,space,c,u,r,s,o,r,l,i,n,e/50,exclamation,enter"),
    "get directory": esc + Key("colon/100,p,w,d/10,enter"),
    "set directory": esc + Key("comma,c,d"),
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

    # "show ring": esc+Key("colon,s-Y,s-R,s-S,h,o,w,enter"),

    "strip all white space": esc+Key("colon,s-C,h,o,m,p,enter"),

    # "disable auto formatting": esc + Key("colon,c,a,l,l,space,p,a,n,d,o,c,hash,f,o,r,m,a,t,t,i,n,g,hash,s-d,i,s,a,b,l,e,s-a,u,t,o,f,o,r,m,a,t,lparen,rparen,enter"),
    # "enable auto formatting": esc + Key("colon,c,a,l,l,space,p,a,n,d,o,c,hash,f,o,r,m,a,t,t,i,n,g,hash,s-e,n,a,b,l,e,s-a,u,t,o,f,o,r,m,a,t,lparen,rparen,enter"),

    "(windows|window) diff on": esc + Key("w,i,n,d,o,w,space,d,i,f,f,o,n,enter"),
    "(windows|window) diff off": esc + Key("w,i,n,d,o,w,space,d,i,f,f,o,f,f,enter"),

    ### R stats - Nvim-R plugin
    # TODO create R language module
     # Start/Close
     "Start are session": esc + Key("comma,r,f"),
     # Start R (custom) \rc
     # --------------------------------------------------------
     "(quit|Close) are session": esc + Key("comma,r,q"),
     "Stop are session": esc + Key("colon,s-R,s-S,t,o,p"),
    # -----------------------------------------------------------

     # "eval Line and new": esc + Key("comma,q"),
     # . "Send Left part of line (cur)": \r<Left>
     # . "Send Right part of line (cur)": \r<Right>
    "eval Line and comment": esc + Key("comma,o"),
    # -----------------------------------------------------------

    # Command
     "List R workspace": esc + Key("comma,r,l"),
     "Clear R console": esc + Key("comma,r,r"),
     "Clear R workspace": esc + Key("comma,r,m"),
     # --------------------------------------------------------
     # --------------------------------------------------------
      "Set R directory": esc + Key("comma,r,d"),
     # --------------------------------------------------------
     # "call Sweave" esc: + Key("comma,s,w"),
     # "call Sweave and PDF file" esc: + Key("comma,s,p"),
     # "Sweave, BibTeX and PDF file) (Linux/Unix)" esc: + Key("comma,s,b"),
     # --------------------------------------------------------
     "Knit this file": esc + Key("comma,k,n"),
     "Knit and PDF this file": esc + Key("comma,k,p"),
     # "Knit BibTeX and PDF this file": esc + Key("comma,k,b"),
     # "Knit and Beamer PDF file) (only .Rmd)": esc + Key("comma,k,l"),
     # "Knit and ODT file) (only .Rmd)": esc + Key("comma,k,o"),
     # "Knit and Word Document file) (only .Rmd)": esc + Key("comma,k,w"),
     "Knit and HTML this file": esc + Key("comma,k,h"),
     # "Spin this file": esc + Key("comma,k,s"),
     # --------------------------------------------------------
     "view PDF this file": esc + Key("comma,o,p"),
     # "SyncTeX": esc + Key("comma,g,p"),
     # "Go to LaTeX (SyncTeX)": esc + Key("comma,g,t"),
     # --------------------------------------------------------
     # "R Build tags": :RBuildTags
    # -----------------------------------------------------------

    # Edit
     # Insert "<-" _
     # Complete object name ^X^O
     # Complete function arguments ^X^A
     # --------------------------------------------------------
     # Indent (line) ==
     # Indent (selected lines) =
     # Indent (whole buffer) gg=G
     # --------------------------------------------------------
     # Toggle comment (line, sel) esc + Key("comma,x,x"),
     # Comment (line, sel) esc + Key("comma,x,c"),
     # Uncomment (line, sel) esc + Key("comma,x,u"),
     # Add/Align right comment (line, sel) esc + Key("comma,semicolon"),
     # --------------------------------------------------------
     "go to next chunk": esc + Key("comma,g,n"),
     "go to preev chunk": esc + Key("comma,g,s-N"),
    # -----------------------------------------------------------

    # Object Browser
     # "(Show|Update) R objects": esc + Key("comma,r,o"),
     # "Expand R objects": esc + Key("comma,r,equal"),
     # "Collapse R objects": esc + Key("comma,r,hyphen"),
     # Toggle (cur) Enter

}

generalKeys = {}
generalKeys.update(generic.genericKeys)
generalKeys.update(osx.osx)
generalKeys.update(vocab.vocabWord)
generalKeys.update(vimGeneric)

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
vim_context = aenea.ProxyCustomAppContext(match="substring", titl="vim") & aenea.ProxyCustomAppContext(id="iTerm2")
mutt_vim_context = aenea.ProxyCustomAppContext(match="substring", titl="mutt") & aenea.ProxyCustomAppContext(id="iTerm2")
tmux_context = aenea.ProxyCustomAppContext(match="substring", titl="tmux") & aenea.ProxyCustomAppContext(id="iTerm2")
git_vim_context = aenea.ProxyCustomAppContext(match="substring", titl="git") & aenea.ProxyCustomAppContext(id="iTerm2")
vim_plus_context = nvim_context | mvim_context | vim_context | git_vim_context | tmux_context | mutt_vim_context
grammar = Grammar("root rule", context = vim_plus_context)
grammar.add_rule(RepeatRule())
grammar.load()

exmode_grammar = Grammar("ExMode grammar",context=vim_plus_context)
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

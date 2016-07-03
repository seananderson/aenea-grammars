from natlink import setMicState
from aenea import *

from dragonfly.actions.keyboard import keyboard
from dragonfly.actions.typeables import typeables
if 'semicolon' not in typeables:
    typeables["semicolon"] = keyboard.get_typeable(char=';')

# import words
# import generic
# import osx
# import vocab
import r_vocab
# from _vim import vimGeneric

# generalKeys = {}
# generalKeys.update(generic.genericKeys)
# generalKeys.update(osx.osx)
# generalKeys.update(vocab.vocabWord)

esc = Key("escape")
LEADER = 'comma'
out = Key("escape,l")
ii = Key("i")

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

rstudioMap = {
    'clear console': Key('c-l'),
    '[go] to start': Key('w-left'),
    '[go] to end': Key('w-right'),
    'pop history': Key('w-up'),
    'sert': Key('i'),
###########################################
    # temp vim paste:
    "cary": esc + Key("0"),
    "car": esc + Key("caret"),
    "doll": esc + Key("dollar"),
    "go to top": esc + Key("g,g"),
    "go to bottom": esc + Key("s-G"),
    "extract [<n>]": esc + Key("x:%(n)d"),

    "copy that": Key("y"),

    "duplicate line [<n>]": esc + Key("y,y,p:%(n)d"),
    "duplicate line above [<n>]": esc + Key("y,y,P:%(n)d"),

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

    'match that': esc + Key("percent"),

    'rope [<n>]': esc + Key('%(n)d, w'),
    'irope [<n>]': esc + Key('%(n)d, e'),
    'lope [<n>]': esc + Key('%(n)d, b'),
    'ilope [<n>]': esc + Key('%(n)d, g, e'),

    'ropert [<n>]': esc + Key('%(n)d, s-W'),
    'iropert [<n>]': esc + Key('%(n)d, s-E'),
    'lopert [<n>]': esc + Key('%(n)d, s-B'),
    'ilopert [<n>]': esc + Key('%(n)d, g, s-E'),

    "(undo|scratch) [<n>]": esc + Key("u:%(n)d"),
    "redo [<n>]": esc + Key("c-r:%(n)d"),
    "repeat [<n>]": esc + Key("%(n)d, dot"),

    'skip [<n>]': esc + Key("%(n)d, f"),
    'skip back [<n>]': esc + Key("%(n)d, s-F"),

    'reverse semi [<n>]': esc + Key("escape, %(n)d, comma"),

    "indent that": esc + Key("rangle,rangle"),
    "out-dent that": esc + Key("langle,langle"),
    "join [<n>]": esc + Key("s-J:%(n)d"),
    "toggle case": esc + Key("tilde"),

    "dosh [<n>] (words|word)": esc + Key("d,%(n)d") + Key("s-B"),
    "rosh [<n>] (words|word)": esc + Key("d,%(n)d") + Key("s-W"),
    "<lineVerbKey>": esc + Key("%(lineVerbKey)s"),

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

    "(mort) [<n>]": esc + Key("c-d:%(n)d") ,
    "(lest) [<n>]": esc + Key("c-u:%(n)d") ,
    ###########################################


    # 'source'

    'set working directory to current [file]': Key('cs-w'), # NOTE custom keyboard shortcut
    'goto file': Key('c-dot'), # or function
    'new document': Key('ws-n'),
    'open document': Key('w-o'),
    'save active document': Key('w-s'),
    'close file': Key('w-w'),
    'close all open documents': Key('ws-w'),
    'preview html': Key('ws-k'),
    'knit (document|file)': Key('ws-k'),
    # 'compile notebook': Key('ws-k'),
    'compile pdf': Key('ws-k'),
    'insert chunk': Key('wa-i'),
    'insert code section': Key('ws-r'),
    '(rip|eval line|eval selected) [<n>]': Key('w-enter/10:%(n)d'),
    'eye-rip': Key('a-enter'),
    're-run that': Key('ws-p'),
    # 'run current document': Key('wa-r'),
    '(rip|eval) to here': Key('wa-b'),
    '(rip|eval) from here': Key('wa-e'),
    '(rip|eval) func': Key('wa-f'),
    '(rip|eval) section': Key('wa-t'),
    '(rip|eval) preeve chunks': Key('wa-p'),
    '(rip|eval) chunk': Key('wa-c'),
    '(rip|eval) next chunk': Key('wa-n'),
    'source doc': Key('ws-s'),
    'source doc and echo': Key('ws-enter'),
    # 'fold selected': Key('wa-l'),
    # 'unfold selected': Key('wsa-l'),
    # 'fold all': Key('wa-o'),
    # 'unfold all': Key('wsa-o'),
    'go to [line]': Key('wsa-g'),
    'jump to': Key('wsa-j'),
    'switch to tab': Key('c-rangle'),
    'preeve tab': Key('c-f11'),
    'next tab': Key('c-f12'),
    'first tab': Key('cs-f11'),
    'last tab': Key('cs-f12'),
    'jump back [<n>]': Key('w-f9:%(n)d'),
    'jump forward [<n>]': Key('w-f10:%(n)d'),
    'extract func from sell': Key('wa-x'),
    # 'extract var from sell': Key('wa-v'),
    'reindent lines': Key('w-i'),
    'comment': Key('ws-c'),
    'reflow comment': Key('ws-slash'),
    'reformat sell': Key('ws-a'),
    'transpose (letters|characters)': Key('c-t'),
    'move up [<n>]': Key('a-up:%(n)d'),
    'move down [<n>]': Key('a-down:%(n)d'),
    'dupe up [<n>]': Key('aw-up:%(n)d'),
    'dupe down [<n>]': Key('aw-down:%(n)d'),
    'jump to matching (brace|paren)': Key('c-p'),
    'expand to matching (brace|paren)': Key('cs-e'),
    # 'select to matching brace/paren': Key('csa-e'),
    'add cursor above [<n>]': Key('ca-up:%(n)d'),
    'add cursor below [<n>]': Key('ca-down:%(n)d'),
    # 'move active cursor up': Key('cas-up'),
    # 'move active cursor down': Key('cas-down'),
    'find': Key('w-f'),
    'find next': Key('w-g'),
    'find preeve': Key('ws-g'),
    'use selection for find': Key('w-e'),
    # 'find [with] selection': Key('ws-j'),
    'find in files': Key('ws-f'),
    'check spelling': Key('f7'),

    # 'editing (console and source)'

    # 'dell line|delline|dine': Key('w-d'),
    # 'select word right': Key('as-right'),
    # 'select word': Key('a-s-left'),
    'expand selection|selection expand': Key('asc-up'),

    # 'sell page up': Key('s-pgup'),
    # 'sell page down': Key('s-pgdown'),

    # 'dell word left': Key('a-backspace'),
    # 'dell word right': Key('a-del'),
    # 'kill': Key('c-k'),
    # 'dell to line start': Key('w-backspace'),
    'indent': Key('tab'),
    'outdent': Key('s-tab'),
    # 'yank to cursor': Key('c-u'),
    # 'insert yanked': Key('c-y'),
    'assign that': Key('space,langle,hyphen,space'),
    'pipe that': Key('ws-m'),

    'help that': Key('f1'),
    'source code that': Key('f2'),

    # 'views'

    '[go] to source': Key('c-1'),
    '[go] to console': Key('c-2'),
    '[go] to help': Key('c-3'),
    '[go] to history': Key('c-4'),
    '[go] to files': Key('c-5'),
    '[go] to plots': Key('c-6'),
    '[go] to packages': Key('c-7'),
    '[go] to environment': Key('c-8'),
    '[go] to git': Key('c-f1'),
    '[go] to build': Key('c-0'),

    'zoom source': Key('cs-1'),
    'zoom console': Key('cs-2'),
    'zoom help': Key('cs-3'),
    'zoom history': Key('cs-4'),
    'zoom files': Key('cs-5'),
    'zoom plots': Key('cs-6'),
    'zoom packages': Key('cs-7'),
    'zoom environment': Key('cs-8'),
    'zoom git': Key('cs-f1'),

    'zoom all': Key('cs-0'),

    'sync pdf': Key('w-f8'),

    # 'build'

    'devtools build and reload': Key('ws-b'),
    'devtools load all': Key('ws-l'),
    'devtools test package': Key('ws-t'),
    'devtools check package': Key('ws-e'),
    'devtools document package': Key('ws-d'),

    ### # 'debug'
    ###
    ### 'toggle breakpoint': Key('s-f9'),
    ### 'execute next line': Key('f10'),
    ### 'step into function': Key('s-f4'),
    ### 'finish function/loop': Key('s-f6'),
    ### 'continue': Key('s-f5'),
    ### 'stop debugging': Key('s-f8'),
    ###
    ### # 'plots'

    'preev plot': Key('wa-f11'),
    'next plot': Key('wa-f12'),

    ### # 'git/svn'
    ###
    'fugitive diff': Key('ca-d'),
    'fugitive commit': Key('ca-m'),
    ### 'scroll diff view': Key('c-up/down'),
    ### 'stage-unstage': Key('spacebar'),
    ### 'stage-unstage and move to next': Key('enter'),
    ###
    'restart R': Key('ws-f10'),
    ###
    ### # more
    ###

    ### 'snip': Key('s-tab'),###

}

rstudioKeys = {}
rstudioKeys.update(rstudioMap)
rstudioKeys.update(r_vocab.r_vocab)

grammarCfg = Config("all")
grammarCfg.cmd = Section("Language section")
grammarCfg.cmd.map = Item(rstudioKeys,
       namespace={
        "Key": Key,
        "Text": Text,
    })

class KeystrokeRule(MappingRule):
    exported = False
    mapping = grammarCfg.cmd.map
    extras = [
        IntegerRef("n", 1, 60),
        Choice("lineVerbKey", lineVerbCharMap),
        # Dictation("text"),
        # Choice("modifier1", generic.modifierMap),
        # Choice("modifier2", generic.modifierMap),
        # Choice("modifierSingle", generic.singleModifierMap),
        # Choice('letters', generic.letterMap),
        # Choice('numbers', generic.numberMap),
        # Choice("pressKey", generic.pressKeyMap),testing
        # Choice("reservedWord", generic.reservedWord),
    ]
    defaults = {
        "n": 1,
    }

alternatives = []
alternatives.append(RuleRef(rule=KeystrokeRule()))
# alternatives.append(RuleRef(rule=words.FormatRule()))
root_action = Alternative(alternatives)

sequence = Repetition(root_action, min=1, max=16, name="sequence")

class RepeatRule(CompoundRule):
    spec = "<sequence>"
    extras = [sequence]

    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]
        for action in sequence:
            action.execute()

rstudio_context = aenea.ProxyCustomAppContext(id="RStudio")
grammar = Grammar("root rule", context=rstudio_context)
grammar.add_rule(RepeatRule())
grammar.load()

def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

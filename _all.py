from natlink import setMicState
from aenea import *

import vim
import words
# import programs

release = Key("shift:up, ctrl:up, alt:up")

alternatives = []
alternatives.append(RuleRef(rule=vim.KeystrokeRule()))
alternatives.append(RuleRef(rule=words.FormatRule()))
alternatives.append(RuleRef(rule=words.ReFormatRule()))
alternatives.append(RuleRef(rule=words.NopeFormatRule()))
# alternatives.append(RuleRef(rule=programs.ProgramsRule()))
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
            #release.execute()

vim_context = aenea.ProxyCustomAppContext(match="substring", titl="nvim") | aenea.ProxyCustomAppContext(match="substring", titl="Vim")
vim_grammar = Grammar("root rule",context=vim_context)
vim_grammar.add_rule(RepeatRule())  # Add the top-level rule.
vim_grammar.load()  # Load the grammar.

#################################

esc = Key("escape")

# handles ExMode control structures
class ExModeCommands(MappingRule):
    mapping  = {
    "edit": esc + Key("colon,e,space"),
    "exit vim": esc + Key("colon,q,enter"),
    "split explorer": esc + Key("colon,s-S,e,x,enter"),
    "please exit vim": esc + Key("colon,q,exclamation,enter"),
    "save and exit please": esc + Key("colon,w,q,exclamation,enter"),
    "save and exit": esc + Key("colon,w,q,enter"),
    "save file": esc + Key("colon,u,p,d,a,t,e,enter"),
    "save as": esc + Key("colon,s,a,v,e,a,s,space"),
    "toggle numbers": esc + Key("colon,s,e,t,space,r,e,l,a,t,i,v,e,n,u,m,b,e,r,exclamation") + Key("enter"),
    "browse (old|recent) files": esc + Key("colon,b,r,o,space,o,l") + Key("enter"),
    "set theme ocean": esc + Key("colon,c,o,l,o/50,space,b,a,s,e,1,6/50,minus,o,c,e,a,n/50,enter"),
    "set theme one dark": esc + Key("colon,c,o,l,o/50,space,o,n,e,d,a,r,k") + Key("enter"),
    "set theme solarized": esc + Key("colon/50,c,o,l,o/50,space,s,o,l,a,r,i,z,e,d") + Key("enter"),
    "set theme Seoul": esc + Key("colon/50,c,o,l,o/50,space,s,e,o,u,l,2,5,6") + Key("enter"),
    "toggle lights": esc + Key("colon/50,s-T,o,g,g,l,e,s-B,s-G") + Key("enter"),
    "toggle spelling": esc + Key("colon/50,s,e,t,l,o,c,a,l,space,s,p,e,l,l,exclamation")+Key("enter"),
    "toggle invisible characters": esc + Key("colon,s,e,space,l,i,s,t,exclamation")+Key("enter"),
    "toggle nerd": esc + Key("colon/50,s-N,s-E,s-R,s-D,s-T,r,e,e,s-T,o,g,g,l,e/50,enter"),
    "toggle cursor-line": esc + Key("colon/50,s,e,space,c,u,r,s,o,r,l,i,n,e/50,exclamation,enter"),
    "get dir": Key("p,w,d/10,enter"),
    "vim help": esc + Key("colon,h,space"),
    "substitute": esc + Key("s,slash"),
    "make split wide": esc + Key("colon/100,v,e,r,t,i,c,a,l/100,space,r,e,s,i,z,e/100,space,plus,6/100,enter"),
    "make split narrow": esc + Key("colon/100,v,e,r,t,i,c,a,l/100,space,r,e,s,i,z,e/100,space,minus,6/100,enter"),
    "make split tall": esc + Key("colon/100,space,r,e,s,i,z,e/100,space,plus,6/100,enter"),
    "make split short": esc + Key("colon/100,space,r,e,s,i,z,e/100,space,minus,6/100,enter"),
    'buff-delete': esc + Key('colon,b,d,enter'),
    'buff-next': esc + Key('colon,b,n,enter'),
    'buff-previous': esc + Key('colon,b,p,enter'),
    'buff-list': esc + Key('colon,l,s,enter'),
    'screen (center|middle)': esc + Key("z, dot"),
    'screen top': esc + Key("z, t"),
    'screen bottom': esc + Key("z, b"),
    "switch": esc + Key("escape, c-p"),
    "switch recent": esc + Key("escape,colon,s-C,t,r,l,s-P,s-M,s-R,s-U,enter"),

    'suspend': Key('c-z'),
    "format": esc + Key("g,q"),
    "edit args": esc+Key("colon,a,r,g,s,space,asterisk,dot"),

### splits:
    "split (screen|window)": esc + Key("c-w,s"),
    "split (screen|window) vertically": esc + Key("c-w,v"),
    "(screen|window) left": esc + Key("c-w,h"),
    "(screen|window) right": esc + Key("c-w,l"),
    "(screen|window) up": esc + Key("c-w,k"),
    "(screen|window) down": esc + Key("c-w,j"),
    "(split|screen|window) close": esc + Key("c-w,c"),
    "close other splits": esc + Key("colon/100,o,n,l,y/100,enter"),

    "comment": esc + Key("g,c,c"),
    "comment paragraph": esc + Key("g,c,a,p"),
    "comment <line1> through <line2>": esc + Key("colon,%(line1)d") + Text(",") + Key("%(line2)d") + Text("Commentary"),

    "scroll-down [<n>]": esc + Key("c-d:%(n)d") ,
    "scroll-up [<n>]": esc + Key("c-u:%(n)d") ,

    "record macro": Key("q,q"),
    "end macro": Key("q"),
    "repeat macro [<n>]": Key("%(n)d,at,q"),
    "magic star": esc + Key("asterisk"),
    "magic pound": esc + Key("hash"),

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
    "app switcher": Key("w-space/50,w-r"),# TODO move this to a module that is always loaded
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
        IntegerRef("line1", 1, 600),
        IntegerRef("line2", 1, 600),
    ]
    defaults = {
        "n": 1,
    }

exmode_grammar = Grammar("ExMode grammar",context=vim_context)
exmode_grammar.add_rule(ExModeCommands())
exmode_grammar.load()

def unload():
    """Unload function which will be called at unload time."""
    global vim_grammar
    if vim_grammar:
        vim_grammar.unload()
    vim_grammar = None

    global exmode_grammar
    if exmode_grammar:
        exmode_grammar.unload()
    exmode_grammar = None

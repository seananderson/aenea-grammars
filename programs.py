# commands for controlling various programs

from aenea import *

gitcommand_array = [
    'add',
    'branch',
    'checkout',
    'clone',
    'commit',
    'diff',
    'fetch',
    'init',
    'log',
    'merge',
    'pull',
    'push',
    'rebase',
    'reset',
    'show',
    'stash',
    'status',
    'tag',
]
gitcommand = {}
for command in gitcommand_array:
    gitcommand[command] = command

class ProgramsRule(MappingRule):
    mapping = {
        # "command (git|get)": Text("git "),
        # "command (git|get) <gitcommand>": Text("git %(gitcommand)s "),
        # "command vim": Text("vim "),
        # "command C D": Text("cd "),
        # "command list": Text("ls "),
        # "command make": Text("make "),
        # "command make clean": Text("make clean "),
        # "command cat": Text("cat "),
        # "command (grep|grip)": Text("grep "),

        # web browser
        # 'address bar': Key('a-d'),
        # 'refresh page': Key('f5'),
        # 'really refresh page': Key('s-f5'),
        # 'go back [<n>]': Key('a-left:%(n)d'),
        # 'go forward [<n>]': Key('a-right:%(n)d'),
        # 'previous tab [<n>]': Key('c-pgup:%(n)d'),
        # 'next tab [<n>]': Key('c-pgdown:%(n)d'),
        # 'open [new] tab': Key('c-t'),
        # 'close tab': Key('c-w'),

        # Xfce-like desktop environment commands
        # '(desk|desktop) left [<n>]': Key('ca-left:%(n)d'),
        # '(desk|desktop) right [<n>]': Key('ca-right:%(n)d'),
        # '(desk|desktop) up [<n>]': Key('ca-up:%(n)d'),
        # '(desk|desktop) down [<n>]': Key('ca-down:%(n)d'),
        # '(desk|desktop) (top|upper) [<n>]': Key('c-f1, ca-left, ca-right:%(n)d'),
        # '(desk|desktop) (bottom|lower) [<n>]': Key('c-f1, ca-down, ca-left, ca-right:%(n)d'),
        # 'switch window [<n>]': Key('a-tab:%(n)d'),
        # 'really close window': Key('a-f4'),
        # 'maximize window': Key('a-f10'),
        # 'minimize window': Key('a-f9'),
    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 100),
        Choice('gitcommand', gitcommand),
    ]
    defaults = {
        "n": 1,
    }

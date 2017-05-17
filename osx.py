from aenea import (
    Key,
    Text,
)

osx = {
    "launchbar": Key("w-space"),
    "switch apps": Key("win:down") + Key("tab"),
    "choose app": Key("win:up"),

    "please quit that": Key("w-q"),
    "please close that": Key("w-w"),
    "hide that": Key("w-h"),
    "new that": Key("w-n"),
    "minimize that": Key("w-m"),

# app switching
    "iterm app": Text("KBM Launch iTerm"),
    "terminal app": Text("KBM Launch Terminal"),
    "PDF app": Text("KBM Launch PDF Expert"),
    "mail-mate app": Text("KBM Launch MailMate"),
    "mail-plane app": Text("KBM Launch Mailplane"),
    "mac-mail app": Text("KBM Launch Mail"),
    "skim app": Text("KBM Launch Skim"),
    "chrome app": Text("KBM Launch Chrome"),
    "calendar app": Text("KBM Launch Calendar"),
    "finder app": Text("KBM Launch Finder"),
    "2-do app": Text("KBM Launch Omnifocus"),
    "spotify app": Text("KBM Launch Spotify"),
    "git-hub app": Text("KBM Launch GitHub"),
    "1-password app": Text("KBM Launch 1Password"),
    "zotero app": Text("KBM Launch Reference Manager"),
    "are-studio app": Text("KBM Launch RStudio"),
    "macvim app": Text("KBM Launch MacVim"),
    "preeve app": Text("KBM Activate previous application"),
    "next app": Text("KBM Activate next application"),

# window management
    "window maximize": Text("KBM Maximize window"),
    "window half left": Text("KBM Half window on left"),
    "window half right": Text("KBM Half window on right"),
    # "window bottom-left": Key("asw-left"),
    # "window bottom-right": Key("asw-down"),
    # "window top-left": Key("asw-up"),
    # "window top-right": Key("asw-right"),
    "window center": Text("KBM Center window"),
    "window third (middle|center)": Text("KBM Window third width middle"),
    "window third left": Text("KBM Window third width left"),
    "window third right": Text("KBM Window third width right"),

# smartnav mouse control

    "smart precise": Key("wa-p"),
    "smart center": Key("wa-c"),
    "smart toggle": Key("wa-s"),

# folder and file opening
    "show downloads": Key("scaw-f1"),

    "toggle dock": Key("aw-d"),
}

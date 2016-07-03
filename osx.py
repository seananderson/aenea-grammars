from aenea import (
    Key,
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
    "iterm app": Key("caw-f1"),
    "terminal app": Key("caw-f2"),
    "PDF app": Key("caw-f3"),
    "mail-mate app": Key("caw-f4"),
    "chrome app": Key("caw-f5"),
    "calendar app": Key("caw-f6"),
    "finder app": Key("caw-f7"),
    "2-do app": Key("caw-f8"),
    "spotify app": Key("caw-f9"),
    "git-hub app": Key("caw-f10"),
    "1-password app": Key("caw-f11"),
    "zotero app": Key("caw-f12"),
    "are app": Key("scaw-f12"),
    "macvim app": Key("scaw-f11"),
    "preeve app": Key("caw-lbracket"),
    "next app": Key("caw-rbracket"),

# window management
    "window maximize": Key("asw-m"),
    "window half left": Key("caw-left"),
    "window half right": Key("caw-right"),
    "window bottom-left": Key("asw-left"),
    "window bottom-right": Key("asw-down"),
    "window top-left": Key("asw-up"),
    "window top-right": Key("asw-right"),
    "window [half] (center|middle)": Key("caw-down"),
    "window third (middle|center)": Key("asw-t"),
    "window third left": Key("asw-l"),
    "window third right": Key("asw-r"),

# folder and file opening
    "show downloads": Key("scaw-f1"),

    "toggle dock": Key("aw-d"),
}

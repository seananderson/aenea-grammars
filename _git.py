import aenea
import aenea.configuration
from aenea.lax import Key
from aenea import Text
import dragonfly

git_context = aenea.ProxyCustomAppContext(id="iTerm2")
grammar = dragonfly.Grammar('git', context=git_context)

git_mapping = aenea.configuration.make_grammar_commands('git', {
    'git': Text("git"),

    'git amend': Text("git commit --amend") + Key("enter"),
    'git commit': Text("git commit") + Key("enter"),
    'git all commit': Text("git commit -av") + Key("enter"),
    'git pull': Text("git pull") + Key("enter"),
    'git branches': Text("git branch -l") + Key("enter"),
    'git status': Text("git status") + Key("enter"),
    # 'git stat': Text("git show --stat") + Key("enter"),
    # 'git log': Text("git log") + Key("enter"),
    'git push': Text("git push") + Key("enter"),
    'git diff': Text("git diff") + Key("enter"),
    'git log': Text("git lg") + Key("enter"),
# lg = log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative

    # Incomplete Commands
    'git add': Text("git add "),
    'git word-diff': Text("git diff --color-words "),
    'git checkout': Text("git checkout "),
    'git interactive rebase': Text("git rebase -i "),
    'git rebase': Text("git rebase "),
    'git push to': Text("git push"),

})

class Mapping(dragonfly.MappingRule):
    mapping = git_mapping

grammar.add_rule(Mapping())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

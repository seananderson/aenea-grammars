import aenea
import aenea.configuration
from aenea.lax import Key
from aenea import Text
import dragonfly

finder_context = aenea.ProxyCustomAppContext(id="Finder")
grammar = dragonfly.Grammar('Finder', context=finder_context)

finder_mapping = aenea.configuration.make_grammar_commands('finder', {
    "sort by name": Key("cw-1"),
    # "sort by kind": Key("cw-2"),
    "sort by opened": Key("cw-3"),
    "sort by added": Key("cw-4"),
    "sort by modified": Key("cw-5"),
    "sort by size": Key("cw-6"),
    "go back": Key("w-lbracket"),
    "go forward": Key("w-rbracket"),
})

class Mapping(dragonfly.MappingRule):
    mapping = finder_mapping

grammar.add_rule(Mapping())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None

# module for dictating words and basic sentences
#
# (based on the multiedit module from dragonfly-modules project)
# (heavily modified)
# (the original copyright notice is reproduced below)
#
# (c) Copyright 2008 by Christo Butcher
# Licensed under the LGPL, see <http://www.gnu.org/licenses/>
#

import aenea
import aenea.misc
import aenea.vocabulary
import aenea.configuration
import aenea.format
import formatting
import re

from aenea import (
    AeneaContext,
    AppContext,
    Alternative,
    CompoundRule,
    Dictation,
    DictList,
    DictListRef,
    Grammar,
    IntegerRef,
    Literal,
    ProxyAppContext,
    MappingRule,
    NeverContext,
    Repetition,
    RuleRef,
    Sequence
)

from aenea import (
    Key,
    Text
)

lastFormatRuleLength = 0
lastFormatRuleWords = []
class NopeFormatRule(CompoundRule):
    spec = ('nope')

    def value(self, node):
        global lastFormatRuleLength
        print "erasing previous format of length", lastFormatRuleLength
        return Key('backspace:' + str(lastFormatRuleLength))

class ReFormatRule(CompoundRule):
    spec = ('that was [upper | natural] ( proper | camel | rel-path | '
    'abs-path | score | scope-resolve | jumble | dotword | titlecase |'
    'dashword | snakeword | brooding-narrative)')

    def value(self, node):
        global lastFormatRuleWords
        words = lastFormatRuleWords
        words = node.words()[2:] + lastFormatRuleWords
        print words

        uppercase = words[0] == 'upper'
        lowercase = words[0] != 'natural'

        if lowercase:
            words = [word.lower() for word in words]
        if uppercase:
            words = [word.upper() for word in words]

        words = [word.split('\\', 1)[0].replace('-', '') for word in words]
        if words[0].lower() in ('upper', 'natural'):
            del words[0]

        function = getattr(aenea.format, 'format_%s' % words[0].lower())
        formatted = function(words[1:])

        global lastFormatRuleLength
        lastFormatRuleLength = len(formatted)
        return Text(formatted)

class FormatRule(CompoundRule):
    spec = ('[upper | natural] ( proper | camel | rel-path | abs-path | score | '
    'scope-resolve | jumble | dotword | dashword |  titlecase |'
    'snakeword ) [<dictation>]')
    extras = [Dictation(name='dictation')]

    def value(self, node):
        words = node.words()
        print "format rule:", words

        uppercase = words[0] == 'upper'
        lowercase = words[0] != 'natural'

        if lowercase:
            words = [word.lower() for word in words]
        if uppercase:
            words = [word.upper() for word in words]

        words = [word.split('\\', 1)[0].replace('-', '') for word in words]
        if words[0].lower() in ('upper', 'natural'):
            del words[0]

        function = getattr(formatting, 'format_%s' % words[0].lower())
        formatted = function(words[1:])

        # Key("i").execute()
        print "  ->", formatted
        return Text(formatted).execute()
        # return Key("escape,l")

def upperfirst(x):
    return x[0].upper() + x[1:]

def clean_prose(text):
    print "was: " + str(text)
    # strip out the \punctuation that Dragon adds in for some reason:
    text = re.sub(r'\\[a-z-]+', r'', str(text))
    text = re.sub(r'space', r' ', str(text))
    # fix the spacing around punctuation:
    text = re.sub(r' ([\?\!\.\:;,])', r'\1 ', text)
    # capitalize the letter I if it's a word on its own:
    text = re.sub(r'i([\' ]+)', r'I\1', text)
    # be smart about double spaces:
    text = re.sub(r'[ ]+', r' ', text)
    # if these punctuation characters are on their own then don't have any spacing:
    text = re.sub(r'^([\:\.;\!,]) $', r'\1', text)
    # enforce space at the at the end:
    text = re.sub(r'[ ]+$', r'', text)
    text = text + ' '
    return text

def cap_that(text):
    # if mode == "normal":
      # Key("i").execute()
    text = clean_prose(str(text))
    text = upperfirst(text)
    print "typing: " + text
    Text(text).execute()
    # if mode == "normal":
      # Key("escape:2,l").execute()

def lower_that(text, mode = "normal"):
    # if mode == "normal":
      # Key("i").execute()
    text = clean_prose(str(text))
    print "typing: " + text
    Text(text).execute()
    # if mode == "normal":
      # Key("escape:2,l").execute()

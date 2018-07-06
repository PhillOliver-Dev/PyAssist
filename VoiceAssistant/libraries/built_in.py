from _version import __version__ as version
from VoiceAssistant.objects.rule import Rule

class BuiltInRules:

    def __init__(self):
        self.rules = []
        self.rules.append(Rule('print version', self.print_version, 'Printing Version'))

    @staticmethod
    def print_version():
        print(version)
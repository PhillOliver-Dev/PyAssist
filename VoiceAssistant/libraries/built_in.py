from _version import __version__ as version
from VoiceAssistant.objects.rule import Rule

class BuiltInRules(dict):

    def __init__(self):
        self.__setitem__('print version', Rule(self.printVersion))

    def printVersion(self):
        print(version)
from VoiceAssistant.engine.ProcessingEngine import ProcessingEngine
from VoiceAssistant.engine.RecognitionEngine import RecognitionEngine
from VoiceAssistant.objects.rule import Rule
from VoiceAssistant.libraries.built_in import BuiltInRules
from _version import __version__ as version

if __name__ == '__main__':

    def printError():
        print('Could not find a suitable command to execute')

    builtIns = BuiltInRules()
    p = ProcessingEngine(builtIns, printError)
    r = RecognitionEngine(p)
    r.run()

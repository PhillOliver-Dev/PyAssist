from VoiceAssistant.engine.ProcessingEngine import ProcessingEngine
from VoiceAssistant.engine.RecognitionEngine import RecognitionEngine
from VoiceAssistant.objects.rule import Rule
from _version import __version__ as version

if __name__ == '__main__':

    def printError():
        print('Could not find a suitable command to execute')

    p = ProcessingEngine({}, printError)
    p.registerRule('print version', Rule(_print))
    r = RecognitionEngine(p)
    r.run()

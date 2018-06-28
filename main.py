from VoiceAssistant.engine.ProcessingEngine import ProcessingEngine
from VoiceAssistant.engine.RecognitionEngine import RecognitionEngine

if __name__ == '__main__':

    def printError():
        print('Could not find a suitable command to execute')

    p = ProcessingEngine({}, printError)
    r = RecognitionEngine(p)
    r.run()

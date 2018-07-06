import speech_recognition as sr
from VoiceAssistant.engine.ProcessingEngine import ProcessingEngine

class RecognitionEngine:

    def __init__(self, procEngine=None):
        self.microphone = sr.Microphone()
        self.recogniser = sr.Recognizer()
        if procEngine:
            self.procEngine = procEngine
        else:
            self.procEngine = ProcessingEngine()
        self.status = True
    
    def run(self):
        while self.status:
            print('Waiting for command...')
            self._try_recognition()

    
    def _try_recognition(self):
        
        with self.microphone as source:
            self.recogniser.adjust_for_ambient_noise(source)
            audio = self.recogniser.listen(source)
            
            try:
                text = (self.recogniser.recognize_google(audio))
                self.procEngine.process_command(text)
            except (sr.RequestError, sr.UnknownValueError):
                pass


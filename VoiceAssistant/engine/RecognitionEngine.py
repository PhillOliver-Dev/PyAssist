import speech_recognition as sr
from VoiceAssistant.objects.transcription import Transcription
mic = sr.Microphone()
r = sr.Recognizer()

with mic as source:
    audio = r.listen(source)
    try:
        r.recognize_google(audio)
    except Exception as e:
        print(e)

class RecognitionEngine:

    def __init__(self, procEngine):
        self.microphone = sr.Microphone()
        self.recogniser = sr.Recognizer()
        self.procEngine = procEngine
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
                self.procEngine.lookupRule(text)
            except (sr.RequestError, sr.UnknownValueError) as e:
                print(e)


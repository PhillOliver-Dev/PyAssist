from VoiceAssistant.Exceptions.Rule import RuleException

class Rule():

    def __init__(self, activator, callback, audio_confirmation=None):
        self.activator = activator
        self.callback = callback
        self.audio_confirmation = audio_confirmation
    
    def run(self):
        try:
            self.callback()
            return self.audio_confirmation
        except Exception as e:
            raise RuleException('Could not run callback function', e)
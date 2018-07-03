from VoiceAssistant.Exceptions.Rule import RuleException

class Rule():

    def __init__(self, callback):
        self.callback = callback
    
    def run(self):
        try:
            self.callback()
        except Exception as e:
            raise RuleException('Could not run callback function', e)
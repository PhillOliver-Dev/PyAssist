class Transcription():

    def __init__(self, text=None, error=None):
        self.error = error
        self.text = text

    def setError(self, error):
        self.error = error
    
    def setText(self, text):
        self.text = text
class Rule():

    def __init__(self, callback):
        self.callback = callback
    
    def run(self):
        self.callback()
class Rule():

    def __init__(self, activator, callback):
        self.activator = activator
        self.callback = callback
    
    def __eq__(self, other):
        if isinstance(other, str):
            return self.activator == other
        return False
    
    def getActivator(self):
        return self.activator
    
    def run(self):
        self.callback()
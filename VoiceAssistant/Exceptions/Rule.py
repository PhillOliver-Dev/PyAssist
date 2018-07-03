class RuleException(Exception):
    def __init__(self, message, caughtException=None):
        self.message = message
        self.caughtException = caughtException
    
    def __str__(self):
        print('Rule Exception: {} - Exception caught: {}'.format(
            self.message,
            self.caughtException
            ))
class EngineException(Exception):
    def __init__(self, engineClass, message):
        self.engineClass = engineClass
        self.message = message
    
    def __str__(self):
        print('{0} Exception: {1} '.format(
            self.engineClass,
            self.message,
            ))
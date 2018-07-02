from VoiceAssistant.objects.rule import Rule
from VoiceAssistant.Exceptions.Rule import RuleException

class ProcessingEngine(object):
    def __init__(self, rules, fallback):
        for key in rules:
            setattr(self, key, rules[key])
        self.fallback = fallback
    
    def registerRule(self, activator, rule):
        if isinstance(rule, Rule):
            setattr(self, activator, rule)
        else:
            raise RuleException('Cannot register provided rule.')

    def lookupRule(self, text):
        print(text)
        try:
            getattr(self, text).run()
        
        except Exception:
            self.fallback()
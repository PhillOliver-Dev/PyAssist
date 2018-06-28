from VoiceAssistant.objects.rule import Rule

class RuleException(Exception):
    def __init__(self, message):
        self.message = message

class ProcessingEngine(object):
    def __init__(self, rules, fallback):
        for key in rules:
            setattr(self, key, rules[key])
        self.fallback = fallback
    
    def registerRule(self, rule):
        if isinstance(rule, Rule):
            setattr(self, rule.getActivator(), rule)
        else:
            raise RuleException('Cannot register provided rule.')

    def lookupRule(self, text):
        print(text)
        try:
            getattr(self, text)
        except Exception:
            self.fallback()
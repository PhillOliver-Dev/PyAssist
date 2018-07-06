from VoiceAssistant.objects.rule import Rule
from VoiceAssistant.engine.SpeechEngine import SpeechEngine
from VoiceAssistant.Exceptions.Rule import RuleException
from VoiceAssistant.Exceptions.Engine import EngineException
from VoiceAssistant.libraries.built_in import BuiltInRules
class ProcessingEngine:
    def __init__(self, rules=None, fallback=None):
        if fallback:
            self.fallback = fallback
        else:
            self.fallback = self.print_error
        self.rules = BuiltInRules().rules
        self.speechEngine = SpeechEngine()
        if rules:
            for item in rules:
                self.register_rule(item)

    def process_command(self, command):
        rule_to_execute = self._lookup_rule_from_command(command)
        if rule_to_execute:
            rule_to_execute.run()
            self._run_rules_speech_text(rule_to_execute)
    
    def register_rule(self, rule):
        if isinstance(rule, Rule):
            self.rules.append(rule)
        else:
            raise RuleException('Cannot register provided rule.')

    def _lookup_rule_from_command(self, command):
        for rule in self.rules:
            if rule.activator == command:
                return rule
        return None

    def _run_rules_speech_text(self, rule):
        if rule.audio_confirmation:
            self.speechEngine.say(rule.audio_confirmation)

    @staticmethod
    def print_error():
        print('Could not find a suitable command to execute')
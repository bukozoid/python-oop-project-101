from validator.int_validator import IntValidator
from validator.string_validator import StringValidator


class Validator:
    def string(self):
        return StringValidator()

    def number(self):
        return IntValidator()

from validator.int_validator import IntValidator
from validator.list_validator import ListValidator
from validator.string_validator import StringValidator


class Validator:
    def string(self):
        return StringValidator()

    def number(self):
        return IntValidator()

    def list(self):
        return ListValidator()

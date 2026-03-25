from validator.dict_validator import DictValidator
from validator.int_validator import IntValidator
from validator.list_validator import ListValidator
from validator.string_validator import StringValidator


class Validator:
    def __init__(self):
        self._ext_validators = {
            "string": {}, "number": {}, "list": {}, "dict": {}}

    def string(self):
        return StringValidator(self._ext_validators["string"])

    def number(self):
        return IntValidator(self._ext_validators["number"])

    def list(self):
        return ListValidator(self._ext_validators["list"])

    def dict(self):
        return DictValidator(self._ext_validators["dict"])

    def add_validator(self, vtype: str, name: str, func):
        if not self._ext_validators.get(vtype):
            self._ext_validators[vtype] = {}
        self._ext_validators[vtype][name] = func

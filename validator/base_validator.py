class BaseValidator:
    def __init__(self, ext_validators=None):
        if ext_validators is None:
            ext_validators = {}
        self._ext_validators = ext_validators
        self._added_validators = {}
        self._required = False
        self._is_valid = True
        self._data = None

    def required(self):
        self._required = True
        return self

    def _validate_required(self):
        if self._is_valid and self._required:
            self._is_valid = self._data is not None
        return self

    def test(self, name, value):
        self._added_validators[name] = value
        return self

    def _validate_custom(self):
        print("_ext_validators: ", self._ext_validators)
        print("_added_validators: ", self._added_validators)
        if self._is_valid:
            for name, arg in self._added_validators.items():
                self._is_valid = self._ext_validators[name](self._data, arg)
                if not self._is_valid:
                    break
        return self

    def is_valid(self, value) -> bool:
        self._data = value
        self._is_valid = True
        self._validate_required()._validate_custom()
        return self._is_valid

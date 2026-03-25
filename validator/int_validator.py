from validator.base_validator import BaseValidator


class IntValidator(BaseValidator):
    def __init__(self, ext_validators=None):
        super().__init__(ext_validators)
        self._range = None
        self._positive = None

    def positive(self):
        self._positive = True
        return self

    def _validate_positive(self):
        if self._is_valid and self._positive:
            self._is_valid = int(self._data) > 0
        return self

    def range(self, start, end):
        self._range = [start, end]
        return self

    def _validate_range(self):
        if self._is_valid and self._range:
            self._is_valid = self._range[0] <= int(self._data) <= self._range[1]
        return self

    def is_valid(self, value):
        self._is_valid = super().is_valid(value)
        self._data = value
        try:
            self._validate_required()._validate_positive()._validate_range()
        except (ValueError, TypeError):
            self._is_valid = False
        return self._is_valid

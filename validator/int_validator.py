from validator.base_validator import BaseValidator


class IntValidator(BaseValidator):
    def __init__(self):
        super().__init__()
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

    def is_valid(self, value):
        self._data = value
        self._is_valid = True
        self._validate_required()._validate_positive()._validate_range()
        return self._is_valid

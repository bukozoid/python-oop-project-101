from validator.base_validator import BaseValidator


class StringValidator(BaseValidator):
    def __init__(self):
        super().__init__()
        self._contains = None
        self._min_len = None

    def contains(self, substring: str):
        self._contains = substring
        return self

    def _validate_contains(self):
        if self._is_valid and self._contains is not None:
            self._is_valid = self._data is not None and self._contains in self._data
        return self

    def min_len(self, lenght: int):
        self._min_len = lenght
        return self

    def _validate_min_len(self):
        if self._is_valid and self._min_len is not None:
            self._is_valid = self._data is not None and (
                self._min_len is None or len(self._data) >= self._min_len
            )
        return self

    def _validate_required(self):
        if self._is_valid and self._required:
            self._is_valid = bool(self._data)
        return self

    def is_valid(self, value):
        self._data = value
        self._is_valid = True
        self._validate_contains()._validate_min_len()._validate_required()
        return self._is_valid

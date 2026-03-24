class Validator:
    def __init__(self, contains=None, min_len=None, required=False):
        self._contains = contains
        self._min_len = min_len
        self._required = required
        self._is_valid = True
        self._data = ""

    def string(self):
        return self.__class__(self._contains, self._min_len, self._required)

    def contains(self, substring: str):
        self._contains = substring
        return self

    def _validate_contains(self):
        if self._is_valid and self._contains is not None:
            self._is_valid = self._data is not None and self._contains in self._data
        return self

    def required(self):
        self._required = True
        return self

    def _validate_required(self):
        if self._is_valid and self._required:
            self._is_valid = bool(self._data)
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

    def is_valid(self, string):
        self._data = string
        self._validate_contains()._validate_min_len()._validate_required()
        return self._is_valid

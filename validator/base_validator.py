class BaseValidator:
    def __init__(self):
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

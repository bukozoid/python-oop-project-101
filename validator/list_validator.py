from validator.base_validator import BaseValidator


class ListValidator(BaseValidator):
    def __init__(self):
        super().__init__()
        self._size = None

    def sizeof(self, value):
        self._size = value
        return self

    def _validate_size(self):
        if self._is_valid and self._size is not None and self._data is not None:
            self._is_valid = len(self._data) == self._size

    def is_valid(self, value):
        self._data = value
        self._is_valid = True
        self._validate_required()._validate_size()
        return self._is_valid

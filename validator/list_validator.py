from validator.base_validator import BaseValidator


class ListValidator(BaseValidator):
    def __init__(self, ext_validators=None):
        super().__init__(ext_validators)
        self._size = None

    def sizeof(self, value):
        self._size = value
        return self

    def _validate_size(self):
        if self._is_valid and self._size is not None and self._data is not None:
            self._is_valid = len(self._data) == self._size

    def is_valid(self, value):
        self._is_valid = super().is_valid(value)
        self._validate_required()._validate_size()
        return self._is_valid

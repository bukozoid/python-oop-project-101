from validator.base_validator import BaseValidator


class DictValidator(BaseValidator):
    def __init__(self, ext_validators=None):
        super().__init__(ext_validators)
        self._shape = {}
        self._data = {}

    def shape(self, value: dict):
        self._shape = value
        return self

    def _validate_shape(self):
        if self._is_valid and self._shape and self._data is not None:
            for key, value in self._data.items():
                if key in self._shape.keys():
                    self._is_valid = self._shape[key].is_valid(value)
                    if self._is_valid is False:
                        break

    def is_valid(self, value: dict):
        if super().is_valid(value):
            self._validate_shape()
        return self._is_valid

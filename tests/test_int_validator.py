import pytest

from validator import Validator


@pytest.fixture
def validator():
    return Validator()


class TestIntSchema:
    def test_number_returns_new_schema(self, validator):
        schema = validator.number()
        schema2 = validator.number()
        assert schema != schema2

    def test_default_none_is_valid(self, validator):
        schema = validator.number()
        assert schema.is_valid(None) is True

    def test_default_int_is_valid(self, validator):
        schema = validator.number()
        assert schema.is_valid(7) is True

    def test_required_makes_none_invalid(self, validator):
        schema = validator.number()
        schema.required()
        assert schema.is_valid(None) is False

    def test_required_int_is_valid(self, validator):
        schema = validator.number()
        schema.required()
        assert schema.is_valid(7) is True

    def test_positive_valid(self, validator):
        schema = validator.number()
        assert schema.positive().is_valid(10) is True

    def test_positive_invalid_for_zero(self, validator):
        schema = validator.number()
        assert schema.positive().is_valid(0) is False

    def test_positive_invalid_for_negative(self, validator):
        schema = validator.number()
        assert schema.positive().is_valid(-10) is False

    def test_range_valid(self, validator):
        schema = validator.number()
        schema.range(-5, 5)
        assert schema.is_valid(5) is True

    def test_range_valid_lower_bound(self, validator):
        schema = validator.number()
        schema.range(-5, 5)
        assert schema.is_valid(-5) is True

    def test_range_invalid_above(self, validator):
        schema = validator.number()
        schema.range(-5, 5)
        assert schema.is_valid(10) is False

    def test_range_invalid_below(self, validator):
        schema = validator.number()
        schema.range(-5, 5)
        assert schema.is_valid(-10) is False

    def test_positive_still_active_after_range(self, validator):
        schema = validator.number()
        schema.positive().range(-5, 5)
        assert schema.is_valid(-5) is False
        assert schema.is_valid(5) is True

    def test_positive_range_combination(self, validator):
        schema = validator.number()
        schema.positive().range(2, 10)
        assert schema.is_valid(5) is True
        assert schema.is_valid(1) is False
        assert schema.is_valid(15) is False

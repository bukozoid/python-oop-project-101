from validator import Validator
import pytest


@pytest.fixture
def validator():
    return Validator()


class TestStringSchema:
    def test_string_returns_new_schema(self, validator):
        schema = validator.string()
        schema2 = validator.string()
        assert schema != schema2

    @pytest.mark.parametrize(
        "value,expected",
        [
            ("", True),
            (None, True),
            ("what does the fox say", True),
        ],
    )
    def test_default_string_validation(self, validator, value, expected):
        schema = validator.string()
        assert schema.is_valid(value) == expected

    def test_required_makes_none_invalid(self, validator):
        schema = validator.string()
        schema.required()
        assert schema.is_valid(None) is False

    def test_required_makes_empty_string_invalid(self, validator):
        schema = validator.string()
        schema.required()
        assert schema.is_valid("") is False

    def test_required_non_empty_string_is_valid(self, validator):
        schema = validator.string()
        schema.required()
        assert schema.is_valid("hexlet") is True

    def test_required_does_not_affect_other_schema(self, validator):
        schema = validator.string()
        schema2 = validator.string()
        schema.required()
        assert schema2.is_valid("") is True


class TestContainsValidator:
    @pytest.mark.parametrize(
        "substring,value,expected",
        [
            ("what", "what does the fox say", True),
            ("whatthe", "what does the fox say", False),
        ],
    )
    def test_contains(self, validator, substring, value, expected):
        schema = validator.string()
        assert schema.contains(substring).is_valid(value) == expected


class TestMinLenValidator:
    def test_min_len_override(self, validator):
        result = validator.string().min_len(10).min_len(4).is_valid("Hexlet")
        assert result is True

    def test__min_len_sequental(self, validator):
        assert validator.string().min_len(10).is_valid("Hexlet") is False
        assert validator.string().min_len(3).is_valid("Hexlet") is True

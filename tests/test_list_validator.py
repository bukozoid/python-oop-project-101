import pytest

from validator import Validator


@pytest.fixture
def validator():
    return Validator()


class TestListSchema:
    def test_list_returns_new_schema(self, validator):
        schema = validator.list()
        schema2 = validator.list()
        assert schema != schema2

    def test_default_none_is_valid(self, validator):
        schema = validator.list()
        assert schema.is_valid(None) is True

    def test_default_list_is_valid(self, validator):
        schema = validator.list()
        assert schema.is_valid([]) is True
        assert schema.is_valid(["hexlet"]) is True

    def test_required_makes_none_invalid(self, validator):
        schema = validator.list()
        schema.required()
        assert schema.is_valid(None) is False

    def test_required_empty_list_is_valid(self, validator):
        schema = validator.list()
        schema.required()
        assert schema.is_valid([]) is True

    def test_required_non_empty_list_is_valid(self, validator):
        schema = validator.list()
        schema.required()
        assert schema.is_valid(["hexlet"]) is True


class TestSizeofValidator:
    def test_sizeof_exact_match(self, validator):
        schema = validator.list()
        schema.sizeof(2)
        assert schema.is_valid(["hexlet", "code-basics"]) is True

    def test_sizeof_too_small(self, validator):
        schema = validator.list()
        schema.sizeof(2)
        assert schema.is_valid(["hexlet"]) is False

    def test_sizeof_too_large(self, validator):
        schema = validator.list()
        schema.sizeof(2)
        assert schema.is_valid(["hexlet", "code-basics", "python"]) is False

    def test_sizeof_empty_list(self, validator):
        schema = validator.list()
        schema.sizeof(0)
        assert schema.is_valid([]) is True

    def test_sizeof_empty_list_invalid(self, validator):
        schema = validator.list()
        schema.sizeof(1)
        assert schema.is_valid([]) is False

    def test_sizeof_with_none(self, validator):
        schema = validator.list()
        schema.sizeof(2)
        assert schema.is_valid(None) is True

    def test_sizeof_with_required_and_none(self, validator):
        schema = validator.list()
        schema.required().sizeof(2)
        assert schema.is_valid(None) is False

    def test_sizeof_override(self, validator):
        schema = validator.list()
        schema.sizeof(5).sizeof(2)
        assert schema.is_valid(["hexlet", "code-basics"]) is True
        assert schema.is_valid(["hexlet"]) is False

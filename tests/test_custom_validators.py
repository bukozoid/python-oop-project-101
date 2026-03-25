from validator import Validator
import pytest


@pytest.fixture
def validator():
    return Validator()


class TestCustomStringValidator:
    def test_startswith_validator_false(self, validator):
        validator.add_validator(
            "string", "startWith", lambda value, start: value.startswith(start)
        )

        schema = validator.string().test("startWith", "H")
        assert schema.is_valid("exlet") is False

    def test_startswith_validator_true(self, validator):
        validator.add_validator(
            "string", "startWith", lambda value, start: value.startswith(start)
        )

        schema = validator.string().test("startWith", "H")
        assert schema.is_valid("Hexlet") is True

    def test_startswith_validator_with_different_prefix(self, validator):
        validator.add_validator(
            "string", "startWith", lambda value, start: value.startswith(start)
        )

        schema = validator.string().test("startWith", "Hello")
        assert schema.is_valid("Hello World") is True
        assert schema.is_valid("World Hello") is False

    def test_multiple_custom_string_validators(self, validator):
        validator.add_validator(
            "string", "startWith", lambda value, start: value.startswith(start)
        )
        validator.add_validator(
            "string", "endsWith", lambda value, end: value.endswith(end)
        )

        schema = validator.string()\
            .test("startWith", "He")\
            .test("endsWith", "et")
        assert schema.is_valid("Hexlet") is True
        assert schema.is_valid("Hexlet!") is False


class TestCustomNumberValidator:
    def test_min_validator_false(self, validator):
        validator.add_validator(
            "number", "min", lambda value, min: value >= min)

        schema = validator.number().test("min", 5)
        assert schema.is_valid(4) is False

    def test_min_validator_true(self, validator):
        validator.add_validator(
            "number", "min", lambda value, min: value >= min)

        schema = validator.number().test("min", 5)
        assert schema.is_valid(6) is True

    def test_min_validator_boundary(self, validator):
        validator.add_validator(
            "number", "min", lambda value, min: value >= min)

        schema = validator.number().test("min", 5)
        assert schema.is_valid(5) is True

    def test_max_validator(self, validator):
        validator.add_validator(
            "number", "max", lambda value, max: value <= max)

        schema = validator.number().test("max", 10)
        assert schema.is_valid(10) is True
        assert schema.is_valid(11) is False
        assert schema.is_valid(9) is True

    def test_range_validator(self, validator):
        validator.add_validator(
            "number", "inRange",
            lambda value, args: args[0] <= value <= args[1]
        )

        schema = validator.number().test("inRange", [5, 10])
        assert schema.is_valid(5) is True
        assert schema.is_valid(10) is True
        assert schema.is_valid(7) is True
        assert schema.is_valid(4) is False
        assert schema.is_valid(11) is False


class TestCustomValidatorWithBuiltIn:
    def test_custom_validator_with_required(self, validator):
        validator.add_validator(
            "string", "startWith", lambda value, start: value.startswith(start)
        )

        schema = validator.string().required().test("startWith", "H")
        assert schema.is_valid("Hexlet") is True
        assert schema.is_valid(None) is False

    def test_custom_validator_with_min_len(self, validator):
        validator.add_validator(
            "string", "startWith", lambda value, start: value.startswith(start)
        )

        schema = validator.string().min_len(5).test("startWith", "He")
        assert schema.is_valid("Hello") is True
        assert schema.is_valid("He") is False  # Too short
        assert schema.is_valid("World") is False  # Doesn't start with 'He'

    def test_custom_validator_with_positive(self, validator):
        validator.add_validator(
            "number", "min", lambda value, min: value >= min)

        schema = validator.number().positive().test("min", 5)
        assert schema.is_valid(10) is True
        assert schema.is_valid(-5) is False
        assert schema.is_valid(3) is False


class TestCustomValidatorIsolation:
    def test_custom_validator_does_not_affect_other_schemas(self, validator):
        validator.add_validator(
            "string", "startWith", lambda value, start: value.startswith(start)
        )

        schema1 = validator.string().test("startWith", "H")
        schema2 = validator.string()

        assert schema1.is_valid("Hexlet") is True
        assert schema2.is_valid("exlet") is True

    def test_different_validators_have_separate_custom_validators(self):
        v1 = Validator()
        v2 = Validator()

        v1.add_validator(
            "string", "startWith", lambda value, start: value.startswith(start)
        )
        v2.add_validator(
            "string", "endsWith", lambda value, end: value.endswith(end))

        schema1 = v1.string().test("startWith", "H")
        schema2 = v2.string().test("endsWith", "t")

        assert schema1.is_valid("Hexlet") is True
        assert schema2.is_valid("Hexlet") is True

import pytest
from validator import Validator


@pytest.fixture
def validator():
    return Validator()


class TestDictSchema:
    def test_dict_returns_new_schema(self, validator):
        schema = validator.dict()
        schema2 = validator.dict()
        assert schema != schema2

    def test_default_none_is_valid(self, validator):
        schema = validator.dict()
        assert schema.is_valid(None) is True

    def test_default_dict_is_valid(self, validator):
        schema = validator.dict()
        assert schema.is_valid({}) is True
        assert schema.is_valid({"key": "value"}) is True

    def test_required_makes_none_invalid(self, validator):
        schema = validator.dict()
        schema.required()
        assert schema.is_valid(None) is False

    def test_required_dict_is_valid(self, validator):
        schema = validator.dict()
        schema.required()
        assert schema.is_valid({}) is True
        assert schema.is_valid({"key": "value"}) is True


class TestDictShape:
    def test_shape_with_valid_data(self, validator):
        schema = validator.dict()
        schema.shape(
            {
                "name": validator.string().required(),
                "age": validator.number().positive(),
            }
        )
        assert schema.is_valid({"name": "kolya", "age": 100}) is True

    def test_shape_with_empty_required_string(self, validator):
        schema = validator.dict()
        schema.shape(
            {
                "name": validator.string().required(),
                "age": validator.number().positive(),
            }
        )
        assert schema.is_valid({"name": "", "age": None}) is False

    def test_shape_with_negative_positive_number(self, validator):
        schema = validator.dict()
        schema.shape(
            {
                "name": validator.string().required(),
                "age": validator.number().positive(),
            }
        )
        assert schema.is_valid({"name": "ada", "age": -5}) is False

    def test_shape_with_extra_keys(self, validator):
        schema = validator.dict()
        schema.shape(
            {
                "name": validator.string().required(),
            }
        )
        assert schema.is_valid({"name": "john", "extra": "value"}) is True

    def test_shape_with_missing_optional_key(self, validator):
        schema = validator.dict()
        schema.shape(
            {
                "name": validator.string().required(),
                "age": validator.number().positive(),
            }
        )
        assert schema.is_valid({"name": "test"}) is True

    def test_shape_empty_dict(self, validator):
        schema = validator.dict()
        schema.shape(
            {
                "name": validator.string().required(),
            }
        )
        assert schema.is_valid({}) is True

    def test_shape_nested_validators(self, validator):
        schema = validator.dict()
        schema.shape(
            {
                "name": validator.string().min_len(3),
                "age": validator.number().range(0, 120),
            }
        )
        assert schema.is_valid({"name": "alex", "age": 25}) is True
        assert schema.is_valid({"name": "ab", "age": 25}) is False
        assert schema.is_valid({"name": "alex", "age": 150}) is False

    def test_shape_multiple_validators_per_field(self, validator):
        schema = validator.dict()
        schema.shape(
            {
                "email": validator.string().required().contains("@"),
                "age": validator.number().positive().range(1, 100),
            }
        )
        assert schema.is_valid({"email": "test@example.com", "age": 50}) is True
        assert schema.is_valid({"email": "invalid", "age": 50}) is False
        assert schema.is_valid({"email": "test@example.com", "age": 0}) is False

    def test_shape_with_list_validator(self, validator):
        schema = validator.dict()
        schema.shape(
            {
                "tags": validator.list().required(),
            }
        )
        assert schema.is_valid({"tags": ["python", "testing"]}) is True
        assert schema.is_valid({"tags": []}) is True
        assert schema.is_valid({"tags": None}) is False

    def test_shape_returns_self(self, validator):
        schema = validator.dict()
        result = schema.shape({"name": validator.string()})
        assert result == schema

    def test_required_dict_with_shape(self, validator):
        schema = validator.dict()
        schema.required().shape(
            {
                "name": validator.string().required(),
            }
        )
        assert schema.is_valid(None) is False
        assert schema.is_valid({"name": "test"}) is True

from dyntamic import factory


def test_schema_generation():
    """Test model generation and validation by this model"""
    schema = {
        "$defs": {
            "Nested": {
                "properties": {
                    "id": {
                        "title": "Id",
                        "type": "string"
                    },
                    "sum": {
                        "title": "Sum",
                        "type": "number"
                    }
                },
                "required": [
                    "id",
                    "sum"
                ],
                "title": "Nested",
                "type": "object"
            },
            "Nested2": {
                "properties": {
                    "id2": {
                        "title": "Id2",
                        "type": "string"
                    },
                    "sum2": {
                        "title": "Sum2",
                        "type": "number"
                    },
                    "nested": {
                        "$ref": "Nested"
                    }
                },
                "required": [
                    "id2",
                    "sum2",
                    "nested"
                ],
                "title": "Nested2",
                "type": "object"
            }
        },
        "properties": {
            "name": {
                "title": "Name",
                "type": "string"
            },
            "address": {
                "title": "Address",
                "type": "integer"
            },
            "is_b": {
                "title": "Is B",
                "type": "boolean"
            },
            "some_value_1": {
                "items": {
                    "$ref": "Nested"
                },
                "title": "Some L",
                "type": "array"
            },
            "some_value_2": {
                "items": {
                    "$ref": "Nested2"
                },
                "title": "Some L2",
                "type": "array"
            },
            "some_value_3": {
                "$ref": "Nested"
            },
            "some_value_4": {
                "items": {
                    "type": "string"
                },
                "title": "Some L4",
                "type": "array"
            }
        },
        "required": [
            "name",
            "address",
            "is_b",
            "some_value_1",
            "some_value_2",
            "some_value_3"
        ],
        "title": "TestSchema",
        "type": "object"
    }
    f = factory.DyntamicFactory(schema)
    model = f.make()
    assert model
    sample_data = {
        "name": "Some name",
        "address": 12,
        "is_b": True,
        "some_value_1": [
            {"id": "1", "sum": 123.0}
        ],
        "some_value_2": [
            {"id2": "1", "sum2": 123.0, "nested": {"id": "1", "sum": 123.0}}
        ],
        "some_value_3": {"id": "1", "sum": 123.0},
        "some_value_4": ["asd", "adsads"]
    }
    validated_model = model.model_validate(sample_data)
    dumped_data = validated_model.model_dump()
    assert dumped_data == sample_data

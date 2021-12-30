from lorem_text import lorem


def generate_item(schema: dict, short_text_size=2, long_text_size=6):
    data_item = schema.copy()

    for field in schema:
        if schema[field] == "ST":
            data_item[field] = lorem.words(short_text_size)
        elif schema[field] == "LT":
            data_item[field] = lorem.words(long_text_size)
        elif schema[field] == "S":
            data_item[field] = lorem.sentence()
        elif schema[field] == "P":
            data_item[field] = lorem.paragraph()

    return data_item


def generate_data(size: int, schema: dict):
    response_data = []

    for _ in range(size):
        data_item = generate_item(schema)
        response_data.append(data_item)

    return response_data

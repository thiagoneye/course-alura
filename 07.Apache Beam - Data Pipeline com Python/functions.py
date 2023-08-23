def string_to_list(text, delimiter = "|"):
    return text.split(delimiter)

def list_to_dict(input, columns_name):
    return dict(zip(columns_name, input))

def create_feature_from_date_string(input, key_of_date):
    input["year_month"] = "-".join(input[key_of_date].split("-")[:2])
    return input

def create_tuple_from_dict_and_feature(input, feature):
    key = input[feature]
    return (key, input)

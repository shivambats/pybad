""""" While getting the value from key, always use get """

dict_1 = {'key1': 'value1', 'key2': 'value2'}


def avoid(key: str) -> str:
    return dict_1[key]


def prefer(key: str) -> str:
    return dict_1.get(key, "default str")


# avoid('key1')

# prefer('key1')

# avoid('key_not_present')
# # The above will break when the key won't be present in the dict

# prefer('key_not_present')

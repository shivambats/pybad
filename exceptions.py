""""" Try to catch the exact exception """

dict_1 = {'key1': 'value1'}


def foo_avoid() -> str:
    try:
        return dict_1['key_not_present']
    except Exception as e:
        return str(e)


def foo_prefer() -> str:
    try:
        return dict_1['key_not_present']
    except KeyError as e:
        return str(e)


foo_avoid()
foo_prefer()

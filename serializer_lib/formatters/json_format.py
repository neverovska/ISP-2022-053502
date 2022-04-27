import re
from typing import Any


FLOAT_REGEX = "-?[\d]+\.[\d]+"
INT_REGEX = "^-?[\d]+$"


def dumps(obj: Any) -> str:
    """
    Method serialize object to string.
    Args:
        obj(): object that should be serialized

    Returns:
        dumps_complex(obj):
    """
    def dumps_complex(complex_obj: Any) -> str:
        """
        Method serialize complex object to string.
        Args:
            complex_obj(): object that should be serialized

        Returns:
            ans: string with serialized object
        """
        if len(complex_obj) == 0:
            return '{}'
        ans = str()
        ans += '{'
        for key, item in complex_obj.items():
            ans += '\'' + key + '\'' + ': '
            obj_type = type(item)
            if obj_type is dict:
                ans += dumps_complex(item) + ', '
            elif obj_type is list or obj_type is tuple:
                ans += dumps_simple(item) + ', '
            elif obj_type is str:
                ans += '\'' + item + '\'' + ', '
            elif obj_type is bool:
                if item:
                    ans += "true" + ', '
                else:
                    ans += "false" + ', '
            elif item is None:
                ans += "null" + ', '
            else:
                ans += str(item) + ', '
        ans = ans[0:len(ans)-2]
        ans += '}'
        return ans

    def dumps_simple(simple_obj: Any) -> str:
        """
        Method serialize simple object to string.
        Args:
            simple_obj(): object that should be serialized

        Returns:
            ans: string with serialized object
        """
        if len(simple_obj) == 0:
            return "[]"
        ans = str()
        ans += '['
        for item in simple_obj:
            obj_type = type(item)
            if obj_type == str:
                ans += '\'' + item + '\'' + ', '
            elif obj_type == dict:
                ans += dumps_complex(item) + ', '
            elif obj_type == list or type(item) == tuple:
                ans += dumps_simple(item) + ', '
            elif obj_type == bool:
                if item:
                    ans += "true" + ', '
                else:
                    ans += "false" + ', '
            elif item is None:
                ans += "null" + ', '
            else:
                ans += str(item) + ', '
        ans = ans[0:len(ans)-2]
        ans += ']'
        return ans

    return dumps_complex(obj)


def dump(obj: Any, file: str):
    """
    Method write string with serialized object to file.
    Args:
        obj(): object that should be serialized
        file(str): name of file for serialized object
    """
    with open(file, 'w') as f:
        f.write(dumps(obj))


def loads(temp_str: str) -> dict:
    """
    Method deserialize python object from string.
    Args:
        temp_str: string contains serialized object(s)

    Returns:

    """
    def loads_obj(str_obj: str) -> dict:
        """

        Args:
            str_obj: string contains serialized object(s)

        Returns:

        """
        obj = dict()
        str_obj = str_obj[1:len(str_obj)-1]
        brackets = 0
        braces = 0
        quotes = 0
        is_key = True
        definition = ""
        key = ""
        i = 0
        while i < len(str_obj):
            if str_obj[i] == ':' and is_key:
                is_key = False
            elif str_obj[i] == '[':
                brackets += 1
                temp_i = i + 1
                while brackets:
                    if str_obj[temp_i] == '[':
                        brackets += 1
                    elif str_obj[temp_i] == ']':
                        brackets -= 1
                    temp_i += 1
                    if temp_i > len(str_obj):
                        raise ValueError()
                obj[key] = load_arr(str_obj[i:temp_i])
                key = ""
                i = temp_i + 1
                is_key = True
            elif str_obj[i] == '{':
                braces += 1
                temp_i = i + 1
                while braces:
                    if str_obj[temp_i] == '{':
                        braces += 1
                    elif str_obj[temp_i] == '}':
                        braces -= 1
                    temp_i += 1
                    if temp_i > len(str_obj):
                        raise ValueError()
                obj[key] = loads_obj(str_obj[i:temp_i])
                key = ""
                i = temp_i + 1
                is_key = True
            elif str_obj[i] == '\'':
                temp_i = i + 1
                quotes += 1
                while quotes:
                    if str_obj[temp_i] == '\'':
                        quotes = 0
                    temp_i += 1
                    if temp_i > len(str_obj):
                        raise ValueError()
                if is_key:
                    key = str_obj[(i+1):(temp_i-1)]
                else:
                    obj[key] = str_obj[(i+1):(temp_i-1)]
                    key = ""
                    is_key = True
                    temp_i += 2
                i = temp_i - 1
            elif str_obj[i] == ' ' and not is_key:
                i += 1
                continue
            elif str_obj[i] == ',' and not is_key:
                if definition == 'true':
                    obj[key] = True
                elif definition == 'false':
                    obj[key] = False
                elif definition == 'null':
                    obj[key] = None
                elif re.fullmatch(FLOAT_REGEX, definition):
                    obj[key] = float(definition)
                elif re.fullmatch(INT_REGEX, definition):
                    obj[key] = int(definition)
                else:
                    raise ValueError()
                definition = ""
                key = ""
                is_key = True
                i += 1
            else:
                if is_key:
                    raise KeyError()
                else:
                    definition += str_obj[i]
            i += 1
        if key != "":
            if definition == 'true':
                obj[key] = True
            elif definition == 'false':
                obj[key] = False
            elif definition == 'null':
                obj[key] = None
            elif re.fullmatch(FLOAT_REGEX, definition):
                obj[key] = float(definition)
            elif re.fullmatch(INT_REGEX, definition):
                obj[key] = int(definition)
        return obj

    def load_arr(str_obj: str) -> list:
        """

        Args:
            str_obj:

        Returns:

        """
        obj = list()
        str_obj = str_obj[1:len(str_obj)-1]
        brackets = 0
        braces = 0
        quotes = 0
        definition = ""
        i = 0
        while i < len(str_obj):
            if str_obj[i] != ' ':
                if str_obj[i] == '[':
                    brackets += 1
                    temp_i = i + 1
                    while brackets:
                        if str_obj[temp_i] == '[':
                            brackets += 1
                        elif str_obj[temp_i] == ']':
                            brackets -= 1
                        temp_i += 1
                        if temp_i > len(str_obj):
                            raise ValueError()
                    obj.append(load_arr(str_obj[i:temp_i]))
                    i = temp_i
                elif str_obj[i] == '{':
                    braces += 1
                    temp_i = i + 1
                    while braces:
                        if str_obj[temp_i] == '{':
                            braces += 1
                        elif str_obj[temp_i] == '}':
                            braces -= 1
                        temp_i += 1
                        if temp_i > len(str_obj):
                            raise ValueError()
                    obj.append(loads_obj(str_obj[i:temp_i]))
                    i = temp_i
                elif str_obj[i] == '\'':
                    temp_i = i + 1
                    quotes += 1
                    while quotes:
                        if str_obj[temp_i] == '\'':
                            quotes = 0
                        temp_i += 1
                        if temp_i > len(str_obj):
                            raise ValueError()
                    obj.append(str_obj[i+1:temp_i-1])
                    i = temp_i
                elif str_obj[i] == ',':
                    if re.fullmatch(FLOAT_REGEX, definition):
                        obj.append(float(definition))
                    elif definition == 'true':
                        obj.append(True)
                    elif definition == 'false':
                        obj.append(False)
                    elif definition == 'null':
                        obj.append(None)
                    elif re.fullmatch(INT_REGEX, definition):
                        obj.append(int(definition))
                    else:
                        raise ValueError()
                    definition = ""
                else:
                    definition += str_obj[i]
            i += 1
        if definition != "":
            if re.fullmatch(FLOAT_REGEX, definition):
                obj.append(float(definition))
            elif definition == 'true':
                obj.append(True)
            elif definition == 'false':
                obj.append(False)
            elif definition == 'null':
                obj.append(None)
            elif re.fullmatch(INT_REGEX, definition):
                obj.append(int(definition))
            else:
                raise ValueError()
        return obj

    return loads_obj(temp_str)


def load(file: str) -> dict:
    """
    Method load string of serialized object to method loads.
    Args:
        file: name of file with serialized object(s)

    Returns:

    """
    with open(file, 'r') as f:
        result = f.read()
        return loads(result)

class PlocException(Exception):
    pass


class Ploc(dict):
    def __init__(self, special_hashmap: dict):
        super().__init__()
        self.special_hashmap = special_hashmap

    @staticmethod
    def compare(key, operation, condition_digit) -> bool:
        comparison = {
            "=": key == condition_digit,
            "<": key < condition_digit,
            ">": key > condition_digit,
            "<=": key <= condition_digit,
            ">=": key >= condition_digit,
            "<>": key != condition_digit,
        }
        return comparison.get(operation, False)

    @staticmethod
    def check_condition(operation, digit) -> bool:
        operations = ["=", "<", ">", "<=", ">=", "<>"]
        return operation in operations and digit.isdigit()

    @staticmethod
    def parse_condition(_condition):
        trimmed_conditions = "".join(_condition.split())
        conditions_list = []

        symbols = ["<", ">", "="]

        for condition_str in trimmed_conditions.split(","):
            condition = {"operation": "", "digit": ""}
            for char in condition_str:
                if char in symbols:
                    condition["operation"] += char
                elif char.isdigit():
                    condition["digit"] += char
                elif char == ",":
                    if Ploc.check_condition(condition["operation"], condition["digit"]):
                        condition["digit"] = float(condition["digit"])
                        conditions_list.append(condition)
                    else:
                        raise PlocException("Bad condition")
                    condition = {"operation": "", "digit": ""}
            if Ploc.check_condition(condition["operation"], condition["digit"]):
                condition["digit"] = float(condition["digit"])
                conditions_list.append(condition)
            else:
                raise PlocException("Bad condition")

        return conditions_list

    @staticmethod
    def parse_key(_key):
        key_values = []
        key = _key[1:-1] if _key[0] == '(' else _key
        key = "".join(key.split()).split(',')
        
        if len(key) == 1 and key[0].isdigit():
            key_values.append(float(key[0]))
        else:
            key_values = [float(k) for k in key if k.isdigit()]

        return key_values

    def __getitem__(self, condition):
        if not isinstance(condition, str):
            raise PlocException("Invalid condition")

        parsed_conditions = self.parse_condition(condition)
        selected = "{"

        for k, v in self.special_hashmap.items():
            key_values = self.parse_key(k)

            if len(key_values) != len(parsed_conditions):
                continue

            matched = True
            for j, key in enumerate(key_values):
                operation = parsed_conditions[j]["operation"]
                digit = parsed_conditions[j]["digit"]

                if not self.compare(key, operation, digit):
                    matched = False
                    break

            if matched:
                selected += f", {k} = {v}" if len(selected) > 1 else f"{k} = {v}"

        selected += "}"
        return selected

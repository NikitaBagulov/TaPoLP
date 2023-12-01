class SpecialHashMap(dict):
    def __init__(self):
        super().__init__()

    @property
    def iloc(self):
        sorted_keys = sorted(sorted(self.keys()), key=lambda k: (',' in k and '(' in k))
        return [self[key] for key in sorted_keys]

    @property
    def ploc(self):
        def parse(condition):
            ops = ['<>', '<=', '>=','<', '>', '=']
            condition = condition.replace(' ', '')
            for op in ops:
                if op in condition:
                    condition = condition.replace(op, f' {op} ')
            return condition.split()

        def check(key, conditions):
            key_parts = [part for part in key.strip('()').split(',')]

            if len(key_parts) != len(conditions):
                return False
            
            for i, part in enumerate(key_parts):
                try:
                    part = int(part)
                except ValueError:
                    return False
                if conditions[i] == '<' and not (part < conditions[i + 1]):
                    return False
                elif conditions[i] == '>' and not (part > conditions[i + 1]):
                    return False
                elif conditions[i] == '=' and not (part == conditions[i + 1]):
                    return False
                elif conditions[i] == '<=' and not (part <= conditions[i + 1]):  # Добавлено сравнение для <=
                    return False
                elif conditions[i] == '>=' and not (part >= conditions[i + 1]):  # Добавлено сравнение для >=
                    return False
                elif conditions[i] == '<>' and not (part != conditions[i + 1]):
                    return False
            return True

        result = {}
        for key in self.keys():
            conditions = []
            for k in key.strip('()').split(','):
                try:
                    conditions.append(int(k))
                except ValueError:
                    pass

            if conditions:
                conditions = parse(' '.join(map(str, conditions)))
                filtered = {k: v for k, v in self.items() if check(k, conditions)}
                result.update(filtered)

        return result

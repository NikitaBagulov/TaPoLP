from .ploc import Ploc
from .iloc import Iloc

class SpecialHashMap(dict):
    def __init__(self, values=None):
        if values is None:
            values = {}
        super().__init__(values)
        self.iloc = Iloc(self)
        self.ploc = Ploc(self)

    # @property
    # def iloc(self):
    #     sorted_keys = sorted(sorted(self.keys()), key=lambda k: ("," in k and "(" in k))
    #     return [self[key] for key in sorted_keys]

    # @property
    # def ploc(self):
    #     pass

    # def ploc(self):
    #     condition = self.condition
    #     if condition is not None:
    #         filtered = {}
    #         operators = {'<', '>', '=', '<>', '<=', '>='}

    #         conditions = condition.split(',')
    #         for key in self.keys():
    #             key_values = [int(val) for val in key.strip('()').split(',') if val.isdigit()]
    #             if len(key_values) != len(conditions):
    #                 continue

    #             valid = True
    #             for i, cond in enumerate(conditions):
    #                 op = None
    #                 for operator in operators:
    #                     if operator in cond:
    #                         op = operator
    #                         break

    #                 if op is None:
    #                     raise ValueError("Invalid condition")

    #                 value = int(cond.strip('><= '))
    #                 if op == '<' and not (key_values[i] < value):
    #                     valid = False
    #                     break
    #                 elif op == '>' and not (key_values[i] > value):
    #                     valid = False
    #                     break
    #                 elif op == '=' and not (key_values[i] == value):
    #                     valid = False
    #                     break
    #                 elif op == '<>' and not (key_values[i] != value):
    #                     valid = False
    #                     break
    #                 elif op == '<=' and not (key_values[i] <= value):
    #                     valid = False
    #                     break
    #                 elif op == '>=' and not (key_values[i] >= value):
    #                     valid = False
    #                     break

    #             if valid:
    #                 filtered[key] = self[key]

    #         return filtered
    #     else:
    #         raise ValueError("Condition argument is missing.")

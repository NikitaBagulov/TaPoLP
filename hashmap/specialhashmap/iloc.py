class IlocException(Exception):
    pass

class Iloc(dict):

    def __init__(self, special_hashmap: dict):
        super().__init__()
        self.special_hashmap = special_hashmap

    def __getitem__(self, item_index):
        if not isinstance(item_index, int) or item_index > len(self.special_hashmap) or item_index < 0:
            raise IlocException("Invalid index")
        else:
            self.special_hashmap = {k: v for k, v in sorted(self.special_hashmap.items(), key=lambda item: item[0])}
            sorted_indices = list(self.special_hashmap.keys())
            return self.special_hashmap[sorted_indices[item_index]]
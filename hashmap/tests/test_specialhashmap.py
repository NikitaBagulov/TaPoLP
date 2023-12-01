import pytest
from specialhashmap import SpecialHashMap

@pytest.fixture()
def specialhashmap():
    map = SpecialHashMap()
    # map["value1"] = 1
    # map["value2"] = 2
    # map["value3"] = 3
    map["1"] = 10
    map["2"] = 20
    map["3"] = 30
    map["1, 5"] = 100
    map["5, 5"] = 200
    map["10, 5"] = 300
    map["(1, 5)"] = 100
    map["(5, 5)"] = 200
    map["(10, 5)"] = 300
    map["(1, 5, 3)"] = 400
    map["(5, 5, 4)"] = 500
    map["(10, 5, 5)"] = 600
    return map

class Test_SpecialHashMap:

    def test_iloc(self, specialhashmap):
        assert specialhashmap.iloc[0] == 10
        assert specialhashmap.iloc[2] == 300
        assert specialhashmap.iloc[5] == 200
        # assert specialhashmap.iloc[8] == 3

    def test_ploc(self, specialhashmap):
        assert specialhashmap.ploc[">=1"] == {1: 10, 2: 20, 3: 30}
        assert specialhashmap.ploc["<3"] == {1: 10, 2: 20}
        assert specialhashmap.ploc[">0, >0"] == {(1, 5): 100, (5, 5): 200, (10, 5): 300}
        assert specialhashmap.ploc[">=10, >0"] == {(10, 5): 300}
        assert specialhashmap.ploc["<5, >=5, >=3"] == {(1, 5, 3): 400}
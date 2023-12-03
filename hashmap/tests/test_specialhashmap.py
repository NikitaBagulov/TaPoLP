import pytest
from specialhashmap import SpecialHashMap
from specialhashmap import IlocException
from specialhashmap import PlocException


@pytest.fixture()
def specialhashmap_iloc():
    map = SpecialHashMap()
    map["value1"] = 1
    map["value2"] = 2
    map["value3"] = 3
    map["1"] = 10
    map["2"] = 20
    map["3"] = 30
    map["1, 5"] = 100
    map["5, 5"] = 200
    map["10, 5"] = 300
    return map

@pytest.fixture()
def specialhashmap_ploc():
    map = SpecialHashMap()
    map["value1"] = 1
    map["value2"] = 2
    map["value3"] = 3
    map["1"] = 10
    map["2"] = 20
    map["3"] = 30
    map["(1, 5)"] = 100
    map["(5, 5)"] = 200
    map["(10, 5)"] = 300
    map["(1, 5, 3)"] = 400
    map["(5, 5, 4)"] = 500
    map["(10, 5, 5)"] = 600
    return map

class Test_SpecialHashMap:

    def test_iloc(self, specialhashmap_iloc):
        assert specialhashmap_iloc.iloc[0] == 10
        assert specialhashmap_iloc.iloc[2] == 300
        assert specialhashmap_iloc.iloc[5] == 200
        assert specialhashmap_iloc.iloc[8] == 3

    def test_iloc_exception(self, specialhashmap_iloc):
        with pytest.raises(IlocException):
            specialhashmap_iloc.iloc[10]
    
    def test_ploc_exception(self, specialhashmap_ploc):
        with pytest.raises(PlocException):
            specialhashmap_ploc.ploc[">=10, d"]

    def test_ploc_invalid_condition(self, specialhashmap_ploc):
        with pytest.raises(PlocException):
            specialhashmap_ploc.ploc[11]

    def test_ploc_bad_condition(self, specialhashmap_ploc):
        with pytest.raises(PlocException):
            specialhashmap_ploc.ploc["<5, =>b, =1"]


    def test_ploc(self, specialhashmap_ploc):
        assert specialhashmap_ploc.ploc[">=1"] == "{1 = 10, 2 = 20, 3 = 30}"
        assert specialhashmap_ploc.ploc["<3"] == "{1 = 10, 2 = 20}"
        assert specialhashmap_ploc.ploc[">0, >0"] == "{(1, 5) = 100, (5, 5) = 200, (10, 5) = 300}"
        assert specialhashmap_ploc.ploc[">=10, >0"] == "{(10, 5) = 300}"
        assert specialhashmap_ploc.ploc["<5, >=5, >=3"] == "{(1, 5, 3) = 400}"
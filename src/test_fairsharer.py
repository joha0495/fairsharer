from fairsharer import fair_sharer
import pytest   

def test_fair_sharer():
    assert fair_sharer([1000, 0, 800, 0], 1) == [800, 100, 800, 100]   
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]
    
import pytest
from utils import arrs

#@pytest.mark.parametrize('array, index, type_array, default',[
    #([1, 3, 3], 1, "test", 3),
    #(['test'], 0, 'test', 'test')  # 'test'
#])

def test_get():  # array, index, type_array, default
    #assert arrs.get(array, index, type_array) == default
    assert arrs.get([1, 3, 3], 1, "test") == 3
    assert arrs.get(['test'], 0, "test") == 'test'


#@pytest.mark.parametrize('array, default', [
    #(([1, 2, 3, 4], 1, 3), ([1, 2, 3, 4], 1, 3)),  # ==2,3
    #(([1, 2, 3], 1), ([1, 2, 3], 1))  #
#])

def test_slice():  # array, default
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

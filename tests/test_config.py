
from ast import Not
import pytest
class NotInrange(Exception):
    def __init__(self,message='values not in range'):
        self.message=message
        super().__init__(self.message)             

def test_generic():
    a=2
    with pytest.raises(NotInrange):
        if a not in range(10,20):
            raise NotInrange     

def test_something():           
    a=2
    b=2
    assert a==b


                                                
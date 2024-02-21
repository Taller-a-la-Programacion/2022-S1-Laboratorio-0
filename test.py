import Laboratorio0;
import pytest;
    
def test_eliminarRepetidos_1():
    assert Laboratorio6.eliminarRepetidos( [12, 78, 12, 0, 5.2, "abc", 0, 12, 5.2, 12] ) == [78, "abc"]

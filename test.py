import Laboratorio0;
import pytest;
    
def test_areaTrapecio_1():
    assert Laboratorio0.areaTrapecio(10, 5, 5) == 37.5


def test_grupoPoblacion_1():
    assert Laboratorio0.grupoPoblacion(15) == "Adolescentes"

def test_grupoPoblacion_2():
    assert Laboratorio0.grupoPoblacion(5) ==  "Niños"

def test_grupoPoblacion_3():
    assert Laboratorio0.grupoPoblacion(-5) == "Error: El valor debe ser desde 0 hasta 125"

def test_grupoPoblacion_4():
    assert Laboratorio0.grupoPoblacion(155) == "Error: Es una edad poco probable, favor consultar"


def test_sonImpares_1():
    assert Laboratorio0.sonImpares(1357) == True

def test_sonImpares_2():
    assert Laboratorio0.sonImpares(4131) == False

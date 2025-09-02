def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # A suposição aqui é que 'b' nunca será zero.
    return a / b

def test_somar(): 
    assert somar(2,3) == 5

def test_dividir(): 
    assert dividir(10,0) == 5
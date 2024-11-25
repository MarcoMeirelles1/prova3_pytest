import pytest
from codigoBala import Calculadora

# Fixture para inicializar valores
@pytest.fixture
def valores():
    return {
        'a': 2,
        'b': 3,
        'c': -1,
        'd': -4,
    }

# Fixture para inicializar uma instância da classe Calculadora, se necessário
@pytest.fixture
def calc():
    return Calculadora()

# Teste de soma com fixtures====================#
def somar(a, b):
    return a + b 

def test_somar(valores): 
    assert somar(valores['a'], valores['b']) == 5
    assert somar(1, 1) == 2
    assert somar(2, 2) == 4

def test_somar_negativos(valores): 
    assert somar(valores['c'], valores['d']) == -5
    assert somar(-1, -1) == -2
    assert somar(-2, -2) == -4
#==========================================#

# Teste de subtração com fixtures================#
def subtrair(a, b):
    return a - b 

def test_subtrair(valores): 
    assert subtrair(valores['a'], valores['b']) == -1
    assert subtrair(4, 2) == 2
    assert subtrair(8, 2) == 6
    
def test_subtrair_negativos(valores): 
    assert subtrair(valores['c'], valores['d']) == 3
    assert subtrair(-1, -1) == 0
    assert subtrair(-4, -2) == -2
#==========================================#

# Teste de multiplicação com fixtures=============#
def multiplicar(a, b):
    return a * b 

def test_multiplicar(valores): 
    assert multiplicar(valores['a'], valores['b']) == 6
    assert multiplicar(1, 1) == 1
    assert multiplicar(2, 2) == 4
    
def test_multiplicar_negativos(valores): 
    assert multiplicar(valores['c'], valores['d']) == 4
    assert multiplicar(-1, -1) == 1
    assert multiplicar(-2, -2) == 4
#==========================================#

# Teste de divisão com fixtures==================#
def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero não permitida"
    return a / b 

def test_dividir(valores): 
    assert dividir(valores['b'], valores['a']) == 1.5
    assert dividir(4, 2) == 2
    assert dividir(9, 3) == 3
    
def test_dividir_negativos(valores): 
    assert dividir(valores['c'], valores['d']) == 0.25
    assert dividir(-6, -2) == 3
    assert dividir(-8, 2) == -4
#==========================================#

# Teste de divisão por zero
def test_dividir_por_zero():
    assert dividir(1, 0) == "Erro: divisão por zero não permitida"

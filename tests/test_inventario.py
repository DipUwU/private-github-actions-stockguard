import pytest 
from src.inventario import clasificar_stock, evaluar_dias_stock
 
def test_stock_agotado(): 
    assert clasificar_stock(0, 20) == "AGOTADO" 
 
def test_stock_critico(): 
    assert clasificar_stock(7, 20) == "CRITICO" 
 
def test_stock_bajo(): 
    assert clasificar_stock(15, 20) == "BAJO" 
 
def test_stock_normal(): 
    assert clasificar_stock(30, 20) == "NORMAL" 
 
def test_stock_invalido(): 
    with pytest.raises(ValueError): 
        clasificar_stock(-2, 20) 

def test_dias_stock_urgente():
    # 10 unidades en stock, vendiendo 4 al día = dura 2.5 días (Urgente)
    assert evaluar_dias_stock(10, 4) == "REABASTECER_URGENTE"

def test_dias_stock_seguro():
    # 50 unidades en stock, vendiendo 2 al día = dura 25 días (Seguro)
    assert evaluar_dias_stock(50, 2) == "STOCK_SEGURO"

def test_dias_stock_demanda_invalida():
    # Demanda cero o negativa debe lanzar error
    with pytest.raises(ValueError):
        evaluar_dias_stock(15, 0)
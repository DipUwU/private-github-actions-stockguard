def clasificar_stock(stock_actual: int, stock_minimo: int) -> str: 
    if stock_actual < 0: 
        raise ValueError("El stock actual no puede ser negativo") 
    if stock_minimo <= 0: 
        raise ValueError("El stock minimo debe ser mayor que cero") 
    if stock_actual == 0: 
        return "AGOTADO"
    if stock_actual <= stock_minimo * 0.5: 
        return "CRITICO" 
    if stock_actual <= stock_minimo: 
        return "BAJO" 
    return "NORMAL" 

def evaluar_dias_stock(stock_actual: int, demanda_diaria: int) -> str:
    """Evalúa la urgencia de compra basada en cuántos días durará el inventario."""
    if stock_actual < 0:
        raise ValueError("El stock actual no puede ser negativo")
    if demanda_diaria <= 0:
        raise ValueError("La demanda diaria debe ser mayor a cero")
        
    dias_restantes = stock_actual / demanda_diaria
    
    if dias_restantes == 0:
        return "RUPTURA_INMEDIATA"
    if dias_restantes <= 3:
        return "REABASTECER_URGENTE"
    if dias_restantes <= 7:
        return "PLANIFICAR_COMPRA"
        
    return "STOCK_SEGURO"
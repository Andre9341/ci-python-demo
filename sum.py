def soma(a, b):
    """
    Função simples que retorna a soma de dois números.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Os parâmetros devem ser numéricos.")
    return a + b

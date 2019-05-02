class StatusEstudo:
    
    CONCLUIDO = 1
    EM_ANDAMENTO = 2
    INCOMPLETO = 3

    def __init__(self, valor : int) : 
        self._valor = valor
        if valor == StatusEstudo.CONCLUIDO:
            self._nome = "Concluido"
        elif valor == StatusEstudo.EM_ANDAMENTO:
            self._nome = "Em Andamento"
        elif valor == StatusEstudo.INCOMPLETO:
            self._nome = "Incompleto"
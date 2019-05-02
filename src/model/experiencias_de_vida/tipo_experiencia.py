class TipoExperienciaDeVida:

    PROFISSIONAL = "Profissional"
    ESTUDO = "Estudo"
    ACONTECIMENTOS = "Acontecimentos"
    ITERATIVIDADES = "Iteratividades"
    LUGARES_E_VIAGENS = "Lugares e Viagens"

    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self) -> str:
        return self._nome


    def filtrar(self,experiencias_de_vida , tipo_estudo : str = None) -> list:
        experiencias_de_vida_filtro = []
        
        for experiencia in experiencias_de_vida :
            if experiencia.tipo.nome == self.nome:
                if (experiencia.tipo.nome == self.ESTUDO and experiencia.tipo_estudo.nome == tipo_estudo):
                    experiencias_de_vida_filtro.append(experiencia)
                elif experiencia.tipo.nome == self.PROFISSIONAL:
                    experiencias_de_vida_filtro.append(experiencia)

        return experiencias_de_vida_filtro
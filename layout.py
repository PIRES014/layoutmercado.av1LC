class SertorSupermercado:
    def _init_(self,nome_setor,capacidade):
        self._nome_setor = nome_setor
        self._capacidade = capacidade
        self._produtos = []

        # Propiedades
        @property
        def nome_setor(self):
            return self._nome_setor
        
        @property
        def capacidade(self):
            return self._capacidade
        
        # Método Público




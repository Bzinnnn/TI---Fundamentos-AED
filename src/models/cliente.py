# cliente.py

class Cliente:
    """representa um cliente do hotel"""
    
    _contador_codigo = 1
    
    def __init__(self, nome, endereco, telefone, codigo=None):
        if codigo:
            self.codigo = codigo
            if codigo >= Cliente._contador_codigo:
                Cliente._contador_codigo = codigo + 1
        else:
            self.codigo = Cliente._contador_codigo
            Cliente._contador_codigo += 1
        
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
    
    def __str__(self):
        return f"Cliente {self.codigo}: {self.nome} - Tel: {self.telefone}"
    
    def __repr__(self):
        return f"<Cliente {self.codigo}>"
    
    def calcular_pontos_fidelidade(self, estadias):
        """calcula pontos de fidelidade - 10 pontos por diaria"""
        total_diarias = 0
        for estadia in estadias:
            if estadia.codigo_cliente == self.codigo:
                total_diarias += estadia.quantidade_diarias
        return total_diarias * 10
    
    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'endereco': self.endereco,
            'telefone': self.telefone
        }
    
    @staticmethod
    def from_dict(data):
        return Cliente(
            nome=data['nome'],
            endereco=data['endereco'],
            telefone=data['telefone'],
            codigo=data['codigo']
        )

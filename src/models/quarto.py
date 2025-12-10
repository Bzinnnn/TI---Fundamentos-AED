# quarto.py

class Quarto:
    """representa um quarto do hotel"""
    
    def __init__(self, numero, tipo, quantidade_hospedes, preco_diaria):
        self.numero = numero
        self.tipo = tipo
        self.quantidade_hospedes = quantidade_hospedes
        self.preco_diaria = preco_diaria
        self.status = "Disponível"
    
    def __str__(self):
        return f"Quarto {self.numero} - {self.tipo} - Quantidade hospedes: {self.quantidade_hospedes} - R${self.preco_diaria:.2f}/diaria - {self.status}"
    
    def __repr__(self):
        return f"<Quarto {self.numero}>"
    
    def marcar_ocupado(self):
        """Marca o quarto como ocupado"""
        self.status = "Ocupado"
        return True
    
    def marcar_desocupado(self):
        """Marca o quarto como desocupado/disponível"""
        self.status = "Disponível"
    
    def marcar_disponivel(self):
        """Alias para marcar_desocupado"""
        self.status = "Disponível"
    
    def marcar_manutencao(self):
        """Marca o quarto como em manutenção"""
        self.status = "Manutenção"
    
    def esta_disponivel(self):
        """Verifica se o quarto está disponível"""
        return self.status == "Disponível"
    
    def to_dict(self):
        return {
            'numero': self.numero,
            'tipo': self.tipo,
            'quantidade_hospedes': self.quantidade_hospedes,
            'preco_diaria': self.preco_diaria,
            'status': self.status
        }
    
    @staticmethod
    def from_dict(data):
        q = Quarto(data['numero'], data['tipo'], data['quantidade_hospedes'], data['preco_diaria'])
        q.status = data['status']
        return q

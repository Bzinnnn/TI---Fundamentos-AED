"""
Módulo responsável pela classe Quarto do sistema de gerenciamento do Hotel Descanso Garantido
"""

class Quarto:
    """
    Classe que representa um quarto do hotel
    
    Atributos:
        numero (int): Número do quarto
        tipo (str): Tipo do quarto (Simples, Duplo, Suíte)
        capacidade (int): Capacidade máxima de hóspedes
        preco_diaria (float): Preço da diária
        status (str): Status do quarto (Disponível, Ocupado, Manutenção)
    """
    
    def __init__(self, numero, tipo, capacidade, preco_diaria):
        """
        Inicializa um quarto
        
        Args:
            numero (int): Número do quarto
            tipo (str): Tipo do quarto
            capacidade (int): Capacidade de hóspedes
            preco_diaria (float): Preço da diária
        """
        self.numero = numero
        self.tipo = tipo
        self.capacidade = capacidade
        self.preco_diaria = preco_diaria
        self.status = "Disponível"
    
    def __str__(self):
        """Retorna representação em string do quarto"""
        return f"Quarto {self.numero} - {self.tipo} - Capacidade: {self.capacidade} - R${self.preco_diaria:.2f}/diária - {self.status}"
    
    def __repr__(self):
        """Retorna representação técnica do quarto"""
        return f"Quarto(numero={self.numero}, tipo='{self.tipo}', capacidade={self.capacidade}, preco={self.preco_diaria}, status='{self.status}')"
    
    def marcar_ocupado(self):
        """Marca o quarto como ocupado"""
        if self.status == "Disponível":
            self.status = "Ocupado"
            return True
        return False
    
    def marcar_disponivel(self):
        """Marca o quarto como disponível"""
        self.status = "Disponível"
    
    def marcar_manutencao(self):
        """Marca o quarto como em manutenção"""
        self.status = "Manutenção"
    
    def esta_disponivel(self):
        """Verifica se o quarto está disponível"""
        return self.status == "Disponível"
    
    def to_dict(self):
        """Converte o quarto para dicionário"""
        return {
            'numero': self.numero,
            'tipo': self.tipo,
            'capacidade': self.capacidade,
            'preco_diaria': self.preco_diaria,
            'status': self.status
        }
    
    @staticmethod
    def from_dict(data):
        """Cria um quarto a partir de um dicionário"""
        quarto = Quarto(data['numero'], data['tipo'], data['capacidade'], data['preco_diaria'])
        quarto.status = data['status']
        return quarto

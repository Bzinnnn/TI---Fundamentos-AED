# estadia.py

from datetime import datetime, date

class Estadia:
    """representa uma estadia no hotel"""
    
    _contador_codigo = 1
    
    def __init__(self, codigo_cliente, quarto, data_entrada, data_saida, codigo=None):
        if codigo:
            self.codigo = codigo
            if codigo >= Estadia._contador_codigo:
                Estadia._contador_codigo = codigo + 1
        else:
            self.codigo = Estadia._contador_codigo
            Estadia._contador_codigo += 1
        
        self.codigo_cliente = codigo_cliente
        self.quarto = quarto
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.status = "Pendente"
        self.quantidade_diarias = self.calcular_diarias()
        self.valor_total = self.calcular_valor_total()
    
    def calcular_diarias(self):
        return (self.data_saida - self.data_entrada).days
    
    def calcular_valor_total(self):
        return self.quantidade_diarias * self.quarto.preco_diaria
    
    def __str__(self):
        return f"Estadia {self.codigo}: Cliente {self.codigo_cliente} - Quarto {self.quarto.numero} ({self.status})"
    
    def __repr__(self):
        return f"<Estadia {self.codigo}>"
    
    def confirmar(self):
        if self.status != "Pendente":
            return False
        self.status = "Confirmada"
        return True
    
    def cancelar(self):
        # so cancela se pendente ou confirmada
        if self.status == "Pendente" or self.status == "Confirmada":
            self.status = "Cancelada"
            self.quarto.marcar_desocupado()
            return True
        else:
            return False
    
    def concluir(self):
        if self.status == "Confirmada":
            self.status = "Concluida"
            return True
        return False
    
    def fazer_checkin(self):
        if self.status == "Confirmada":
            self.quarto.marcar_ocupado()
            return True
        return False
    
    def fazer_checkout(self):
        """realiza checkout validando datas"""
        if self.status != "Confirmada":
            return False
        
        # validacao: checkout nao pode ser antes da entrada
        data_hoje = date.today()
        if data_hoje < self.data_entrada:
            return False
        
        self.quarto.marcar_desocupado()
        self.concluir()
        return True
    
    def to_dict(self):
        return {
            'codigo': self.codigo,
            'codigo_cliente': self.codigo_cliente,
            'quarto_numero': self.quarto.numero,
            'data_entrada': self.data_entrada.isoformat(),
            'data_saida': self.data_saida.isoformat(),
            'status': self.status,
            'quantidade_diarias': self.quantidade_diarias,
            'valor_total': self.valor_total
        }
    
    @staticmethod
    def from_dict(data, quarto):
        estadia = Estadia(
            codigo_cliente=data['codigo_cliente'],
            quarto=quarto,
            data_entrada=date.fromisoformat(data['data_entrada']),
            data_saida=date.fromisoformat(data['data_saida']),
            codigo=data['codigo']
        )
        estadia.status = data['status']
        return estadia

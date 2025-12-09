"""
Módulo responsável pela classe Reserva do sistema de gerenciamento do Hotel Descanso Garantido
"""

from datetime import datetime, date

class Reserva:
    """
    Classe que representa uma reserva de quarto no hotel
    
    Atributos:
        id (int): Identificador único da reserva
        nome_hospede (str): Nome do hóspede
        cpf_hospede (str): CPF do hóspede
        quarto (Quarto): Quarto reservado
        data_checkin (date): Data de check-in
        data_checkout (date): Data de check-out
        status (str): Status da reserva (Pendente, Confirmada, Cancelada, Concluída)
        valor_total (float): Valor total da reserva
    """
    
    _contador_id = 1  # Contador estático para gerar IDs únicos
    
    def __init__(self, nome_hospede, cpf_hospede, quarto, data_checkin, data_checkout):
        """
        Inicializa uma reserva
        
        Args:
            nome_hospede (str): Nome do hóspede
            cpf_hospede (str): CPF do hóspede
            quarto (Quarto): Quarto a ser reservado
            data_checkin (date): Data de check-in
            data_checkout (date): Data de check-out
        """
        self.id = Reserva._contador_id
        Reserva._contador_id += 1
        self.nome_hospede = nome_hospede
        self.cpf_hospede = cpf_hospede
        self.quarto = quarto
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.status = "Pendente"
        self.valor_total = self.calcular_valor_total()
    
    def calcular_valor_total(self):
        """Calcula o valor total da reserva baseado no número de diárias"""
        num_diarias = (self.data_checkout - self.data_checkin).days
        return num_diarias * self.quarto.preco_diaria
    
    def __str__(self):
        """Retorna representação em string da reserva"""
        return (f"Reserva #{self.id} - {self.nome_hospede} (CPF: {self.cpf_hospede})\n"
                f"  Quarto: {self.quarto.numero} - {self.quarto.tipo}\n"
                f"  Check-in: {self.data_checkin.strftime('%d/%m/%Y')} | "
                f"Check-out: {self.data_checkout.strftime('%d/%m/%Y')}\n"
                f"  Diárias: {(self.data_checkout - self.data_checkin).days} | "
                f"Valor Total: R${self.valor_total:.2f}\n"
                f"  Status: {self.status}")
    
    def __repr__(self):
        """Retorna representação técnica da reserva"""
        return f"Reserva(id={self.id}, hospede='{self.nome_hospede}', quarto={self.quarto.numero}, status='{self.status}')"
    
    def confirmar(self):
        """Confirma a reserva"""
        if self.status == "Pendente":
            self.status = "Confirmada"
            return True
        return False
    
    def cancelar(self):
        """Cancela a reserva"""
        if self.status in ["Pendente", "Confirmada"]:
            self.status = "Cancelada"
            self.quarto.marcar_disponivel()
            return True
        return False
    
    def concluir(self):
        """Marca a reserva como concluída"""
        if self.status == "Confirmada":
            self.status = "Concluída"
            return True
        return False
    
    def fazer_checkin(self):
        """Realiza o check-in do hóspede"""
        if self.status == "Confirmada":
            self.quarto.marcar_ocupado()
            return True
        return False
    
    def fazer_checkout(self):
        """Realiza o check-out do hóspede"""
        if self.status == "Confirmada":
            self.quarto.marcar_disponivel()
            self.concluir()
            return True
        return False
    
    def to_dict(self):
        """Converte a reserva para dicionário"""
        return {
            'id': self.id,
            'nome_hospede': self.nome_hospede,
            'cpf_hospede': self.cpf_hospede,
            'quarto_numero': self.quarto.numero,
            'data_checkin': self.data_checkin.isoformat(),
            'data_checkout': self.data_checkout.isoformat(),
            'status': self.status,
            'valor_total': self.valor_total
        }

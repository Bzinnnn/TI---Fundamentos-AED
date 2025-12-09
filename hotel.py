"""
Módulo responsável pela classe Hotel do sistema de gerenciamento do Hotel Descanso Garantido
"""

from datetime import date, datetime
from quarto import Quarto
from reserva import Reserva
import json
import os

class Hotel:
    """
    Classe que gerencia todo o sistema do hotel
    
    Atributos:
        nome (str): Nome do hotel
        quartos (list): Lista de quartos do hotel
        reservas (list): Lista de reservas
    """
    
    def __init__(self, nome="Hotel Descanso Garantido"):
        """
        Inicializa o hotel
        
        Args:
            nome (str): Nome do hotel
        """
        self.nome = nome
        self.quartos = []
        self.reservas = []
    
    # ==================== GERENCIAMENTO DE QUARTOS ====================
    
    def adicionar_quarto(self, numero, tipo, capacidade, preco_diaria):
        """
        Adiciona um novo quarto ao hotel
        
        Args:
            numero (int): Número do quarto
            tipo (str): Tipo do quarto
            capacidade (int): Capacidade de hóspedes
            preco_diaria (float): Preço da diária
            
        Returns:
            bool: True se adicionado com sucesso, False caso contrário
        """
        # Verifica se o quarto já existe
        if self.buscar_quarto_por_numero(numero):
            return False
        
        quarto = Quarto(numero, tipo, capacidade, preco_diaria)
        self.quartos.append(quarto)
        return True
    
    def buscar_quarto_por_numero(self, numero):
        """
        Busca um quarto pelo número
        
        Args:
            numero (int): Número do quarto
            
        Returns:
            Quarto ou None: Quarto encontrado ou None
        """
        for quarto in self.quartos:
            if quarto.numero == numero:
                return quarto
        return None
    
    def listar_quartos(self):
        """
        Lista todos os quartos do hotel
        
        Returns:
            list: Lista de quartos
        """
        return self.quartos
    
    def listar_quartos_disponiveis(self):
        """
        Lista apenas os quartos disponíveis
        
        Returns:
            list: Lista de quartos disponíveis
        """
        return [q for q in self.quartos if q.esta_disponivel()]
    
    def listar_quartos_ocupados(self):
        """
        Lista apenas os quartos ocupados
        
        Returns:
            list: Lista de quartos ocupados
        """
        return [q for q in self.quartos if q.status == "Ocupado"]
    
    def listar_quartos_por_tipo(self, tipo):
        """
        Lista quartos de um tipo específico
        
        Args:
            tipo (str): Tipo do quarto
            
        Returns:
            list: Lista de quartos do tipo especificado
        """
        return [q for q in self.quartos if q.tipo.lower() == tipo.lower()]
    
    # ==================== GERENCIAMENTO DE RESERVAS ====================
    
    def fazer_reserva(self, nome_hospede, cpf_hospede, numero_quarto, data_checkin, data_checkout):
        """
        Cria uma nova reserva
        
        Args:
            nome_hospede (str): Nome do hóspede
            cpf_hospede (str): CPF do hóspede
            numero_quarto (int): Número do quarto
            data_checkin (date): Data de check-in
            data_checkout (date): Data de check-out
            
        Returns:
            Reserva ou None: Reserva criada ou None se não for possível
        """
        # Busca o quarto
        quarto = self.buscar_quarto_por_numero(numero_quarto)
        if not quarto:
            return None
        
        # Verifica se o quarto está disponível
        if not quarto.esta_disponivel():
            return None
        
        # Verifica se as datas são válidas
        if data_checkout <= data_checkin:
            return None
        
        # Verifica se o quarto está disponível no período
        if not self.verificar_disponibilidade(numero_quarto, data_checkin, data_checkout):
            return None
        
        # Cria a reserva
        reserva = Reserva(nome_hospede, cpf_hospede, quarto, data_checkin, data_checkout)
        reserva.confirmar()
        self.reservas.append(reserva)
        
        return reserva
    
    def verificar_disponibilidade(self, numero_quarto, data_checkin, data_checkout):
        """
        Verifica se um quarto está disponível em um período
        
        Args:
            numero_quarto (int): Número do quarto
            data_checkin (date): Data de check-in
            data_checkout (date): Data de check-out
            
        Returns:
            bool: True se disponível, False caso contrário
        """
        for reserva in self.reservas:
            if reserva.quarto.numero == numero_quarto and reserva.status != "Cancelada":
                # Verifica se há sobreposição de datas
                if not (data_checkout <= reserva.data_checkin or data_checkin >= reserva.data_checkout):
                    return False
        return True
    
    def buscar_reserva_por_id(self, id_reserva):
        """
        Busca uma reserva pelo ID
        
        Args:
            id_reserva (int): ID da reserva
            
        Returns:
            Reserva ou None: Reserva encontrada ou None
        """
        for reserva in self.reservas:
            if reserva.id == id_reserva:
                return reserva
        return None
    
    def cancelar_reserva(self, id_reserva):
        """
        Cancela uma reserva
        
        Args:
            id_reserva (int): ID da reserva
            
        Returns:
            bool: True se cancelada com sucesso, False caso contrário
        """
        reserva = self.buscar_reserva_por_id(id_reserva)
        if reserva:
            return reserva.cancelar()
        return False
    
    def listar_reservas(self):
        """
        Lista todas as reservas
        
        Returns:
            list: Lista de reservas
        """
        return self.reservas
    
    def listar_reservas_ativas(self):
        """
        Lista reservas ativas (confirmadas)
        
        Returns:
            list: Lista de reservas ativas
        """
        return [r for r in self.reservas if r.status == "Confirmada"]
    
    def listar_reservas_por_hospede(self, cpf_hospede):
        """
        Lista reservas de um hóspede específico
        
        Args:
            cpf_hospede (str): CPF do hóspede
            
        Returns:
            list: Lista de reservas do hóspede
        """
        return [r for r in self.reservas if r.cpf_hospede == cpf_hospede]
    
    # ==================== CHECK-IN E CHECK-OUT ====================
    
    def fazer_checkin(self, id_reserva):
        """
        Realiza o check-in de uma reserva
        
        Args:
            id_reserva (int): ID da reserva
            
        Returns:
            bool: True se check-in realizado, False caso contrário
        """
        reserva = self.buscar_reserva_por_id(id_reserva)
        if reserva and reserva.status == "Confirmada":
            return reserva.fazer_checkin()
        return False
    
    def fazer_checkout(self, id_reserva):
        """
        Realiza o check-out de uma reserva
        
        Args:
            id_reserva (int): ID da reserva
            
        Returns:
            bool: True se check-out realizado, False caso contrário
        """
        reserva = self.buscar_reserva_por_id(id_reserva)
        if reserva and reserva.status == "Confirmada":
            return reserva.fazer_checkout()
        return False
    
    # ==================== RELATÓRIOS ====================
    
    def relatorio_ocupacao(self):
        """
        Gera relatório de ocupação do hotel
        
        Returns:
            dict: Dicionário com estatísticas de ocupação
        """
        total_quartos = len(self.quartos)
        quartos_disponiveis = len(self.listar_quartos_disponiveis())
        quartos_ocupados = len(self.listar_quartos_ocupados())
        quartos_manutencao = len([q for q in self.quartos if q.status == "Manutenção"])
        
        taxa_ocupacao = (quartos_ocupados / total_quartos * 100) if total_quartos > 0 else 0
        
        return {
            'total_quartos': total_quartos,
            'quartos_disponiveis': quartos_disponiveis,
            'quartos_ocupados': quartos_ocupados,
            'quartos_manutencao': quartos_manutencao,
            'taxa_ocupacao': taxa_ocupacao
        }
    
    def relatorio_receita(self):
        """
        Calcula a receita total do hotel
        
        Returns:
            dict: Dicionário com informações de receita
        """
        receita_total = sum(r.valor_total for r in self.reservas if r.status in ["Confirmada", "Concluída"])
        receita_pendente = sum(r.valor_total for r in self.reservas if r.status == "Pendente")
        receita_concluida = sum(r.valor_total for r in self.reservas if r.status == "Concluída")
        
        return {
            'receita_total': receita_total,
            'receita_pendente': receita_pendente,
            'receita_concluida': receita_concluida,
            'total_reservas': len(self.reservas)
        }
    
    # ==================== PERSISTÊNCIA DE DADOS ====================
    
    def salvar_dados(self, arquivo='hotel_dados.json'):
        """
        Salva os dados do hotel em um arquivo JSON
        
        Args:
            arquivo (str): Nome do arquivo
        """
        dados = {
            'nome': self.nome,
            'quartos': [q.to_dict() for q in self.quartos],
            'reservas': [r.to_dict() for r in self.reservas]
        }
        
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
    
    def carregar_dados(self, arquivo='hotel_dados.json'):
        """
        Carrega os dados do hotel de um arquivo JSON
        
        Args:
            arquivo (str): Nome do arquivo
            
        Returns:
            bool: True se carregado com sucesso, False caso contrário
        """
        if not os.path.exists(arquivo):
            return False
        
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            self.nome = dados.get('nome', self.nome)
            
            # Carrega quartos
            self.quartos = []
            for q_data in dados.get('quartos', []):
                self.quartos.append(Quarto.from_dict(q_data))
            
            # Carrega reservas
            self.reservas = []
            for r_data in dados.get('reservas', []):
                quarto = self.buscar_quarto_por_numero(r_data['quarto_numero'])
                if quarto:
                    reserva = Reserva(
                        r_data['nome_hospede'],
                        r_data['cpf_hospede'],
                        quarto,
                        datetime.fromisoformat(r_data['data_checkin']).date(),
                        datetime.fromisoformat(r_data['data_checkout']).date()
                    )
                    reserva.id = r_data['id']
                    reserva.status = r_data['status']
                    reserva.valor_total = r_data['valor_total']
                    self.reservas.append(reserva)
            
            return True
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return False

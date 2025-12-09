"""
Módulo de utilitários para o sistema de gerenciamento do Hotel Descanso Garantido
"""

from datetime import datetime, date
import re

class ValidadorEntradas:
    """Classe responsável por validar entradas do usuário"""
    
    @staticmethod
    def validar_cpf(cpf):
        """
        Valida o formato do CPF
        
        Args:
            cpf (str): CPF a ser validado
            
        Returns:
            str ou None: CPF formatado ou None se inválido
        """
        # Remove caracteres não numéricos
        cpf = re.sub(r'\D', '', cpf)
        
        # Verifica se tem 11 dígitos
        if len(cpf) != 11:
            return None
        
        # Verifica se não é uma sequência de números iguais
        if cpf == cpf[0] * 11:
            return None
        
        return cpf
    
    @staticmethod
    def validar_data(data_str, formato='%d/%m/%Y'):
        """
        Valida e converte uma string de data
        
        Args:
            data_str (str): String da data
            formato (str): Formato da data
            
        Returns:
            date ou None: Objeto date ou None se inválido
        """
        try:
            return datetime.strptime(data_str, formato).date()
        except ValueError:
            return None
    
    @staticmethod
    def validar_numero_inteiro(valor_str, minimo=None, maximo=None):
        """
        Valida se uma string representa um número inteiro válido
        
        Args:
            valor_str (str): String a ser validada
            minimo (int): Valor mínimo permitido
            maximo (int): Valor máximo permitido
            
        Returns:
            int ou None: Número inteiro ou None se inválido
        """
        try:
            valor = int(valor_str)
            if minimo is not None and valor < minimo:
                return None
            if maximo is not None and valor > maximo:
                return None
            return valor
        except ValueError:
            return None
    
    @staticmethod
    def validar_numero_float(valor_str, minimo=None, maximo=None):
        """
        Valida se uma string representa um número decimal válido
        
        Args:
            valor_str (str): String a ser validada
            minimo (float): Valor mínimo permitido
            maximo (float): Valor máximo permitido
            
        Returns:
            float ou None: Número decimal ou None se inválido
        """
        try:
            # Substitui vírgula por ponto
            valor_str = valor_str.replace(',', '.')
            valor = float(valor_str)
            if minimo is not None and valor < minimo:
                return None
            if maximo is not None and valor > maximo:
                return None
            return valor
        except ValueError:
            return None
    
    @staticmethod
    def validar_tipo_quarto(tipo):
        """
        Valida o tipo de quarto
        
        Args:
            tipo (str): Tipo do quarto
            
        Returns:
            str ou None: Tipo válido ou None
        """
        tipos_validos = ['simples', 'duplo', 'suite', 'suíte']
        tipo_lower = tipo.lower().strip()
        
        if tipo_lower in tipos_validos:
            # Normaliza o tipo
            if tipo_lower == 'suíte':
                return 'Suíte'
            elif tipo_lower == 'suite':
                return 'Suíte'
            elif tipo_lower == 'duplo':
                return 'Duplo'
            elif tipo_lower == 'simples':
                return 'Simples'
        return None

class FormatadorSaida:
    """Classe responsável por formatar saídas para o console"""
    
    @staticmethod
    def linha(caractere='=', tamanho=80):
        """Imprime uma linha separadora"""
        print(caractere * tamanho)
    
    @staticmethod
    def titulo(texto):
        """Imprime um título formatado"""
        FormatadorSaida.linha()
        print(f" {texto.center(78)} ")
        FormatadorSaida.linha()
    
    @staticmethod
    def subtitulo(texto):
        """Imprime um subtítulo formatado"""
        print(f"\n>>> {texto}")
        FormatadorSaida.linha('-', 80)
    
    @staticmethod
    def sucesso(mensagem):
        """Imprime mensagem de sucesso"""
        print(f"\n✓ {mensagem}")
    
    @staticmethod
    def erro(mensagem):
        """Imprime mensagem de erro"""
        print(f"\n✗ ERRO: {mensagem}")
    
    @staticmethod
    def alerta(mensagem):
        """Imprime mensagem de alerta"""
        print(f"\n⚠ ALERTA: {mensagem}")
    
    @staticmethod
    def info(mensagem):
        """Imprime mensagem informativa"""
        print(f"\nℹ {mensagem}")
    
    @staticmethod
    def tabela_quartos(quartos):
        """Formata e imprime uma tabela de quartos"""
        if not quartos:
            print("\nNenhum quarto encontrado.")
            return
        
        print("\n{:<8} {:<15} {:<12} {:<15} {:<15}".format(
            "Número", "Tipo", "Capacidade", "Preço/Diária", "Status"
        ))
        FormatadorSaida.linha('-', 80)
        
        for quarto in quartos:
            print("{:<8} {:<15} {:<12} R${:<13.2f} {:<15}".format(
                quarto.numero,
                quarto.tipo,
                quarto.capacidade,
                quarto.preco_diaria,
                quarto.status
            ))
    
    @staticmethod
    def tabela_reservas(reservas):
        """Formata e imprime uma tabela de reservas"""
        if not reservas:
            print("\nNenhuma reserva encontrada.")
            return
        
        print("\n{:<5} {:<20} {:<12} {:<12} {:<12} {:<15}".format(
            "ID", "Hóspede", "Quarto", "Check-in", "Check-out", "Status"
        ))
        FormatadorSaida.linha('-', 80)
        
        for reserva in reservas:
            print("{:<5} {:<20} {:<12} {:<12} {:<12} {:<15}".format(
                reserva.id,
                reserva.nome_hospede[:18],
                reserva.quarto.numero,
                reserva.data_checkin.strftime('%d/%m/%Y'),
                reserva.data_checkout.strftime('%d/%m/%Y'),
                reserva.status
            ))

def limpar_tela():
    """Limpa a tela do console"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Pausa a execução até o usuário pressionar Enter"""
    input("\nPressione ENTER para continuar...")

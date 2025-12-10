# menu.py - Interface de usuario separada

from src.utils.utils import *

class MenuUI:
    """classe para gerenciar interface de usuario"""
    
    @staticmethod
    def exibir_menu_principal(nome_hotel):
        """exibe o menu principal do sistema"""
        limpar_tela()
        titulo(f"{nome_hotel.upper()}")
        print("\n=== CLIENTES ===")
        print("1.  Cadastrar Cliente")
        print("2.  Listar Clientes")
        print("3.  Pesquisar Cliente")
        print("4.  Pontos de Fidelidade")
        print("\n=== FUNCIONARIOS ===")
        print("5.  Cadastrar Funcionario")
        print("6.  Listar Funcionarios")
        print("7.  Pesquisar Funcionario")
        print("\n=== QUARTOS ===")
        print("8.  Cadastrar Quarto")
        print("9.  Listar Quartos")
        print("10. Consultar Quartos Disponiveis")
        print("11. Alterar Status do Quarto")
        print("\n=== ESTADIAS ===")
        print("12. Fazer Estadia")
        print("13. Listar Estadias")
        print("14. Consultar Estadia")
        print("15. Cancelar Estadia")
        print("16. Estadias por Cliente")
        print("\n=== CHECK-IN/OUT ===")
        print("17. Realizar Check-in")
        print("18. Realizar Check-out (Baixa)")
        print("\n=== RELATORIOS ===")
        print("19. Relatorio de Ocupacao")
        print("20. Relatorio de Receita")
        print("\n0.  Sair")
        linha()
    
    @staticmethod
    def ler_opcao(mensagem="Escolha uma opcao: "):
        """le opcao do usuario"""
        try:
            return int(input(mensagem))
        except ValueError:
            return -1
    
    @staticmethod
    def ler_texto(mensagem):
        """le texto do usuario"""
        return input(mensagem).strip()
    
    @staticmethod
    def ler_numero(mensagem, minimo=None):
        """le numero do usuario com validacao"""
        while True:
            texto = input(mensagem).strip()
            if validar_numero(texto, minimo):
                return int(texto)
            msg_erro("Numero invalido!")
    
    @staticmethod
    def ler_preco(mensagem):
        """le preco do usuario com validacao"""
        while True:
            texto = input(mensagem).strip()
            if validar_preco(texto):
                return float(texto)
            msg_erro("Preco invalido!")
    
    @staticmethod
    def ler_data(mensagem):
        """le data do usuario com validacao"""
        while True:
            texto = input(mensagem).strip()
            data = validar_data(texto)
            if data:
                return data
            msg_erro("Data invalida! Use dd/mm/aaaa")
    
    @staticmethod
    def confirmar(mensagem):
        """pede confirmacao do usuario"""
        resp = input(f"{mensagem} (s/n): ").strip().lower()
        return resp == 's'

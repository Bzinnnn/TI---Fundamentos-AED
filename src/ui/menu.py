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
        print("5.  Remover Cliente")
        print("\n=== FUNCIONARIOS ===")
        print("6.  Cadastrar Funcionario")
        print("7.  Listar Funcionarios")
        print("8.  Pesquisar Funcionario")
        print("9.  Remover Funcionario")
        print("\n=== QUARTOS ===")
        print("10. Cadastrar Quarto")
        print("11. Listar Quartos")
        print("12. Consultar Quartos Disponiveis")
        print("13. Alterar Status do Quarto")
        print("14. Remover Quarto")
        print("\n=== ESTADIAS ===")
        print("15. Fazer Estadia")
        print("16. Listar Estadias")
        print("17. Consultar Estadia")
        print("18. Cancelar Estadia")
        print("19. Estadias por Cliente")
        print("\n=== CHECK-IN/OUT ===")
        print("20. Realizar Check-in")
        print("21. Realizar Check-out (Baixa)")
        print("\n=== RELATORIOS ===")
        print("22. Relatorio de Ocupacao")
        print("23. Relatorio de Receita")
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

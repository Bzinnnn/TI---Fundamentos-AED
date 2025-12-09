"""
Sistema de Gerenciamento do Hotel Descanso Garantido
Trabalho Prático de Algoritmos e Estruturas de Dados

Autor: [Seu Nome]
Data: Dezembro de 2025
"""

from datetime import date, datetime, timedelta
from hotel import Hotel
from utils import ValidadorEntradas, FormatadorSaida, limpar_tela, pausar

class SistemaHotel:
    """Classe principal que gerencia a interface do sistema"""
    
    def __init__(self):
        """Inicializa o sistema"""
        self.hotel = Hotel("Hotel Descanso Garantido")
        self.validador = ValidadorEntradas()
        self.formatador = FormatadorSaida()
        self.executando = True
    
    def inicializar(self):
        """Inicializa o sistema com dados de exemplo"""
        # Carrega dados salvos ou cria dados de exemplo
        if not self.hotel.carregar_dados():
            self.criar_dados_exemplo()
            self.formatador.info("Dados de exemplo carregados.")
        else:
            self.formatador.sucesso("Dados carregados com sucesso!")
    
    def criar_dados_exemplo(self):
        """Cria alguns quartos de exemplo"""
        # Quartos Simples
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        self.hotel.adicionar_quarto(102, "Simples", 1, 150.00)
        self.hotel.adicionar_quarto(103, "Simples", 2, 180.00)
        
        # Quartos Duplos
        self.hotel.adicionar_quarto(201, "Duplo", 2, 250.00)
        self.hotel.adicionar_quarto(202, "Duplo", 2, 250.00)
        self.hotel.adicionar_quarto(203, "Duplo", 3, 300.00)
        
        # Suítes
        self.hotel.adicionar_quarto(301, "Suíte", 2, 400.00)
        self.hotel.adicionar_quarto(302, "Suíte", 4, 500.00)
        self.hotel.adicionar_quarto(303, "Suíte", 4, 500.00)
    
    def menu_principal(self):
        """Exibe o menu principal"""
        limpar_tela()
        self.formatador.titulo(f"🏨 {self.hotel.nome.upper()} 🏨")
        print("\n1.  Cadastrar Quarto")
        print("2.  Listar Quartos")
        print("3.  Consultar Quartos Disponíveis")
        print("4.  Fazer Reserva")
        print("5.  Listar Reservas")
        print("6.  Consultar Reserva")
        print("7.  Cancelar Reserva")
        print("8.  Realizar Check-in")
        print("9.  Realizar Check-out")
        print("10. Relatório de Ocupação")
        print("11. Relatório de Receita")
        print("12. Buscar Reservas por Hóspede")
        print("13. Alterar Status do Quarto")
        print("0.  Sair")
        self.formatador.linha()
    
    def executar(self):
        """Loop principal do sistema"""
        self.inicializar()
        pausar()
        
        while self.executando:
            self.menu_principal()
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao == '1':
                self.cadastrar_quarto()
            elif opcao == '2':
                self.listar_quartos()
            elif opcao == '3':
                self.consultar_quartos_disponiveis()
            elif opcao == '4':
                self.fazer_reserva()
            elif opcao == '5':
                self.listar_reservas()
            elif opcao == '6':
                self.consultar_reserva()
            elif opcao == '7':
                self.cancelar_reserva()
            elif opcao == '8':
                self.realizar_checkin()
            elif opcao == '9':
                self.realizar_checkout()
            elif opcao == '10':
                self.relatorio_ocupacao()
            elif opcao == '11':
                self.relatorio_receita()
            elif opcao == '12':
                self.buscar_reservas_hospede()
            elif opcao == '13':
                self.alterar_status_quarto()
            elif opcao == '0':
                self.sair()
            else:
                self.formatador.erro("Opção inválida!")
                pausar()
    
    # ==================== FUNCIONALIDADES ====================
    
    def cadastrar_quarto(self):
        """Cadastra um novo quarto"""
        limpar_tela()
        self.formatador.subtitulo("Cadastrar Novo Quarto")
        
        # Número do quarto
        numero_str = input("Número do quarto: ").strip()
        numero = self.validador.validar_numero_inteiro(numero_str, minimo=1)
        if not numero:
            self.formatador.erro("Número inválido!")
            pausar()
            return
        
        # Verifica se já existe
        if self.hotel.buscar_quarto_por_numero(numero):
            self.formatador.erro("Quarto já cadastrado!")
            pausar()
            return
        
        # Tipo do quarto
        print("\nTipos disponíveis: Simples, Duplo, Suíte")
        tipo_input = input("Tipo do quarto: ").strip()
        tipo = self.validador.validar_tipo_quarto(tipo_input)
        if not tipo:
            self.formatador.erro("Tipo inválido!")
            pausar()
            return
        
        # Capacidade
        capacidade_str = input("Capacidade (número de hóspedes): ").strip()
        capacidade = self.validador.validar_numero_inteiro(capacidade_str, minimo=1, maximo=10)
        if not capacidade:
            self.formatador.erro("Capacidade inválida!")
            pausar()
            return
        
        # Preço da diária
        preco_str = input("Preço da diária (R$): ").strip()
        preco = self.validador.validar_numero_float(preco_str, minimo=0.01)
        if not preco:
            self.formatador.erro("Preço inválido!")
            pausar()
            return
        
        # Adiciona o quarto
        if self.hotel.adicionar_quarto(numero, tipo, capacidade, preco):
            self.formatador.sucesso(f"Quarto {numero} cadastrado com sucesso!")
            self.hotel.salvar_dados()
        else:
            self.formatador.erro("Erro ao cadastrar quarto!")
        
        pausar()
    
    def listar_quartos(self):
        """Lista todos os quartos"""
        limpar_tela()
        self.formatador.subtitulo("Todos os Quartos do Hotel")
        
        quartos = self.hotel.listar_quartos()
        self.formatador.tabela_quartos(quartos)
        
        print(f"\nTotal de quartos: {len(quartos)}")
        pausar()
    
    def consultar_quartos_disponiveis(self):
        """Consulta quartos disponíveis"""
        limpar_tela()
        self.formatador.subtitulo("Quartos Disponíveis")
        
        quartos_disponiveis = self.hotel.listar_quartos_disponiveis()
        self.formatador.tabela_quartos(quartos_disponiveis)
        
        print(f"\nTotal de quartos disponíveis: {len(quartos_disponiveis)}")
        pausar()
    
    def fazer_reserva(self):
        """Faz uma nova reserva"""
        limpar_tela()
        self.formatador.subtitulo("Fazer Nova Reserva")
        
        # Nome do hóspede
        nome = input("Nome do hóspede: ").strip()
        if not nome:
            self.formatador.erro("Nome não pode ser vazio!")
            pausar()
            return
        
        # CPF do hóspede
        cpf_input = input("CPF do hóspede (apenas números): ").strip()
        cpf = self.validador.validar_cpf(cpf_input)
        if not cpf:
            self.formatador.erro("CPF inválido!")
            pausar()
            return
        
        # Mostra quartos disponíveis
        print("\nQuartos disponíveis:")
        quartos_disponiveis = self.hotel.listar_quartos_disponiveis()
        self.formatador.tabela_quartos(quartos_disponiveis)
        
        if not quartos_disponiveis:
            self.formatador.erro("Não há quartos disponíveis!")
            pausar()
            return
        
        # Número do quarto
        numero_str = input("\nNúmero do quarto: ").strip()
        numero = self.validador.validar_numero_inteiro(numero_str)
        if not numero:
            self.formatador.erro("Número inválido!")
            pausar()
            return
        
        # Data de check-in
        checkin_str = input("Data de check-in (DD/MM/AAAA): ").strip()
        data_checkin = self.validador.validar_data(checkin_str)
        if not data_checkin:
            self.formatador.erro("Data inválida!")
            pausar()
            return
        
        # Verifica se a data é futura
        if data_checkin < date.today():
            self.formatador.erro("Data de check-in deve ser futura!")
            pausar()
            return
        
        # Data de check-out
        checkout_str = input("Data de check-out (DD/MM/AAAA): ").strip()
        data_checkout = self.validador.validar_data(checkout_str)
        if not data_checkout:
            self.formatador.erro("Data inválida!")
            pausar()
            return
        
        # Faz a reserva
        reserva = self.hotel.fazer_reserva(nome, cpf, numero, data_checkin, data_checkout)
        
        if reserva:
            self.formatador.sucesso("Reserva realizada com sucesso!")
            print(f"\n{reserva}")
            self.hotel.salvar_dados()
        else:
            self.formatador.erro("Não foi possível fazer a reserva. Verifique os dados e a disponibilidade.")
        
        pausar()
    
    def listar_reservas(self):
        """Lista todas as reservas"""
        limpar_tela()
        self.formatador.subtitulo("Todas as Reservas")
        
        reservas = self.hotel.listar_reservas()
        self.formatador.tabela_reservas(reservas)
        
        print(f"\nTotal de reservas: {len(reservas)}")
        pausar()
    
    def consultar_reserva(self):
        """Consulta uma reserva específica"""
        limpar_tela()
        self.formatador.subtitulo("Consultar Reserva")
        
        id_str = input("ID da reserva: ").strip()
        id_reserva = self.validador.validar_numero_inteiro(id_str, minimo=1)
        
        if not id_reserva:
            self.formatador.erro("ID inválido!")
            pausar()
            return
        
        reserva = self.hotel.buscar_reserva_por_id(id_reserva)
        
        if reserva:
            print(f"\n{reserva}")
        else:
            self.formatador.erro("Reserva não encontrada!")
        
        pausar()
    
    def cancelar_reserva(self):
        """Cancela uma reserva"""
        limpar_tela()
        self.formatador.subtitulo("Cancelar Reserva")
        
        # Mostra reservas ativas
        print("Reservas ativas:")
        reservas_ativas = self.hotel.listar_reservas_ativas()
        self.formatador.tabela_reservas(reservas_ativas)
        
        if not reservas_ativas:
            self.formatador.info("Não há reservas ativas para cancelar.")
            pausar()
            return
        
        id_str = input("\nID da reserva a cancelar: ").strip()
        id_reserva = self.validador.validar_numero_inteiro(id_str, minimo=1)
        
        if not id_reserva:
            self.formatador.erro("ID inválido!")
            pausar()
            return
        
        if self.hotel.cancelar_reserva(id_reserva):
            self.formatador.sucesso("Reserva cancelada com sucesso!")
            self.hotel.salvar_dados()
        else:
            self.formatador.erro("Não foi possível cancelar a reserva!")
        
        pausar()
    
    def realizar_checkin(self):
        """Realiza check-in"""
        limpar_tela()
        self.formatador.subtitulo("Realizar Check-in")
        
        # Mostra reservas confirmadas
        print("Reservas confirmadas:")
        reservas_confirmadas = [r for r in self.hotel.listar_reservas() if r.status == "Confirmada"]
        self.formatador.tabela_reservas(reservas_confirmadas)
        
        if not reservas_confirmadas:
            self.formatador.info("Não há reservas confirmadas para check-in.")
            pausar()
            return
        
        id_str = input("\nID da reserva: ").strip()
        id_reserva = self.validador.validar_numero_inteiro(id_str, minimo=1)
        
        if not id_reserva:
            self.formatador.erro("ID inválido!")
            pausar()
            return
        
        if self.hotel.fazer_checkin(id_reserva):
            self.formatador.sucesso("Check-in realizado com sucesso!")
            self.hotel.salvar_dados()
        else:
            self.formatador.erro("Não foi possível realizar o check-in!")
        
        pausar()
    
    def realizar_checkout(self):
        """Realiza check-out"""
        limpar_tela()
        self.formatador.subtitulo("Realizar Check-out")
        
        # Mostra quartos ocupados
        print("Quartos ocupados:")
        quartos_ocupados = self.hotel.listar_quartos_ocupados()
        self.formatador.tabela_quartos(quartos_ocupados)
        
        if not quartos_ocupados:
            self.formatador.info("Não há quartos ocupados.")
            pausar()
            return
        
        # Mostra reservas ativas
        print("\nReservas ativas:")
        reservas_ativas = [r for r in self.hotel.listar_reservas() if r.status == "Confirmada"]
        self.formatador.tabela_reservas(reservas_ativas)
        
        id_str = input("\nID da reserva: ").strip()
        id_reserva = self.validador.validar_numero_inteiro(id_str, minimo=1)
        
        if not id_reserva:
            self.formatador.erro("ID inválido!")
            pausar()
            return
        
        reserva = self.hotel.buscar_reserva_por_id(id_reserva)
        
        if reserva and self.hotel.fazer_checkout(id_reserva):
            self.formatador.sucesso("Check-out realizado com sucesso!")
            print(f"\nValor total da estadia: R${reserva.valor_total:.2f}")
            self.hotel.salvar_dados()
        else:
            self.formatador.erro("Não foi possível realizar o check-out!")
        
        pausar()
    
    def relatorio_ocupacao(self):
        """Exibe relatório de ocupação"""
        limpar_tela()
        self.formatador.subtitulo("Relatório de Ocupação")
        
        relatorio = self.hotel.relatorio_ocupacao()
        
        print(f"\nTotal de quartos: {relatorio['total_quartos']}")
        print(f"Quartos disponíveis: {relatorio['quartos_disponiveis']}")
        print(f"Quartos ocupados: {relatorio['quartos_ocupados']}")
        print(f"Quartos em manutenção: {relatorio['quartos_manutencao']}")
        print(f"Taxa de ocupação: {relatorio['taxa_ocupacao']:.2f}%")
        
        pausar()
    
    def relatorio_receita(self):
        """Exibe relatório de receita"""
        limpar_tela()
        self.formatador.subtitulo("Relatório de Receita")
        
        relatorio = self.hotel.relatorio_receita()
        
        print(f"\nReceita total: R${relatorio['receita_total']:.2f}")
        print(f"Receita concluída: R${relatorio['receita_concluida']:.2f}")
        print(f"Receita pendente: R${relatorio['receita_pendente']:.2f}")
        print(f"Total de reservas: {relatorio['total_reservas']}")
        
        pausar()
    
    def buscar_reservas_hospede(self):
        """Busca reservas por hóspede"""
        limpar_tela()
        self.formatador.subtitulo("Buscar Reservas por Hóspede")
        
        cpf_input = input("CPF do hóspede: ").strip()
        cpf = self.validador.validar_cpf(cpf_input)
        
        if not cpf:
            self.formatador.erro("CPF inválido!")
            pausar()
            return
        
        reservas = self.hotel.listar_reservas_por_hospede(cpf)
        
        if reservas:
            self.formatador.tabela_reservas(reservas)
            print(f"\nTotal de reservas: {len(reservas)}")
        else:
            self.formatador.info("Nenhuma reserva encontrada para este hóspede.")
        
        pausar()
    
    def alterar_status_quarto(self):
        """Altera o status de um quarto"""
        limpar_tela()
        self.formatador.subtitulo("Alterar Status do Quarto")
        
        # Mostra todos os quartos
        quartos = self.hotel.listar_quartos()
        self.formatador.tabela_quartos(quartos)
        
        numero_str = input("\nNúmero do quarto: ").strip()
        numero = self.validador.validar_numero_inteiro(numero_str)
        
        if not numero:
            self.formatador.erro("Número inválido!")
            pausar()
            return
        
        quarto = self.hotel.buscar_quarto_por_numero(numero)
        
        if not quarto:
            self.formatador.erro("Quarto não encontrado!")
            pausar()
            return
        
        print(f"\nStatus atual: {quarto.status}")
        print("\n1. Disponível")
        print("2. Manutenção")
        
        opcao = input("\nNovo status: ").strip()
        
        if opcao == '1':
            quarto.marcar_disponivel()
            self.formatador.sucesso("Status alterado para Disponível!")
            self.hotel.salvar_dados()
        elif opcao == '2':
            quarto.marcar_manutencao()
            self.formatador.sucesso("Status alterado para Manutenção!")
            self.hotel.salvar_dados()
        else:
            self.formatador.erro("Opção inválida!")
        
        pausar()
    
    def sair(self):
        """Sai do sistema"""
        limpar_tela()
        self.formatador.titulo("Obrigado por usar o Sistema do Hotel Descanso Garantido!")
        print("\nSalvando dados...")
        self.hotel.salvar_dados()
        self.formatador.sucesso("Dados salvos com sucesso!")
        print("\nAté logo! 👋\n")
        self.executando = False

def main():
    """Função principal"""
    sistema = SistemaHotel()
    sistema.executar()

if __name__ == "__main__":
    main()

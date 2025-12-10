# Sistema Hotel Descanso Garantido
# TP de AED - 2025/2

from datetime import date, datetime, timedelta
from src.models.hotel import Hotel
from src.utils.utils import *
from src.ui.menu import MenuUI

class SistemaHotel:
    """sistema de gerenciamento do hotel"""
    
    def __init__(self):
        self.hotel = Hotel("Villa Prado Resort  - Um Hotel 5 Estrelas")
        self.executando = True
        self.menu = MenuUI()
    
    def inicializar(self):
        """carrega dados salvos ou cria exemplos"""
        if not self.hotel.carregar_dados():
            self.criar_dados_exemplo()
            msg_info("Dados de exemplo carregados.")
        else:
            msg_sucesso("Dados carregados!")
    
    def criar_dados_exemplo(self):
        # quartos
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        self.hotel.adicionar_quarto(102, "Simples", 1, 150.00)
        self.hotel.adicionar_quarto(103, "Simples", 2, 180.00)
        self.hotel.adicionar_quarto(201, "Duplo", 2, 250.00)
        self.hotel.adicionar_quarto(202, "Duplo", 2, 250.00)
        self.hotel.adicionar_quarto(203, "Duplo", 3, 300.00)
        self.hotel.adicionar_quarto(301, "Suíte", 2, 400.00)
        self.hotel.adicionar_quarto(302, "Suíte", 4, 500.00)
        self.hotel.adicionar_quarto(303, "Suíte", 4, 500.00)
        
        # alguns clientes exemplo
        self.hotel.cadastrar_cliente("Maria Silva", "Rua A, 123", "31999991111")
        self.hotel.cadastrar_cliente("João Santos", "Av B, 456", "31988882222")
        
        # funcionarios exemplo
        self.hotel.cadastrar_funcionario("Ana Costa", "31977773333", "Recepcionista", 2500.00)
        self.hotel.cadastrar_funcionario("Carlos Souza", "31966664444", "Gerente", 5000.00)
    
    def executar(self):
        """loop principal do sistema"""
        self.inicializar()
        pausar()
        
        while self.executando:
            self.menu.exibir_menu_principal(self.hotel.nome)
            opcao = self.menu.ler_opcao("\nOpcao: ")
            
            if opcao == 1:
                self.cadastrar_cliente()
            elif opcao == 2:
                self.listar_clientes()
            elif opcao == 3:
                self.pesquisar_cliente()
            elif opcao == 4:
                self.pontos_fidelidade()
            elif opcao == 5:
                self.remover_cliente()
            elif opcao == 6:
                self.cadastrar_funcionario()
            elif opcao == 7:
                self.listar_funcionarios()
            elif opcao == 8:
                self.pesquisar_funcionario()
            elif opcao == 9:
                self.remover_funcionario()
            elif opcao == 10:
                self.cadastrar_quarto()
            elif opcao == 11:
                self.listar_quartos()
            elif opcao == 12:
                self.consultar_quartos_disponiveis()
            elif opcao == 13:
                self.alterar_status_quarto()
            elif opcao == 14:
                self.remover_quarto()
            elif opcao == 15:
                self.fazer_estadia()
            elif opcao == 16:
                self.listar_estadias()
            elif opcao == 17:
                self.consultar_estadia()
            elif opcao == 18:
                self.cancelar_estadia()
            elif opcao == 19:
                self.estadias_por_cliente()
            elif opcao == 20:
                self.realizar_checkin()
            elif opcao == 21:
                self.realizar_checkout()
            elif opcao == 22:
                self.relatorio_ocupacao()
            elif opcao == 23:
                self.relatorio_receita()
            elif opcao == 0:
                self.sair()
            else:
                msg_erro("Opcao invalida!")
                pausar()
    
    # --- clientes ---
    
    def cadastrar_cliente(self):
        limpar_tela()
        subtitulo("Cadastrar Cliente")
        msg_info("Digite 0 para cancelar a qualquer momento\n")
        
        nome = input("Nome: ").strip()
        if nome == "0":
            msg_info("Cadastro cancelado.")
            pausar()
            return
        if not nome:
            msg_erro("Nome nao pode ser vazio")
            pausar()
            return
        
        endereco = input("Endereco: ").strip()
        if endereco == "0":
            msg_info("Cadastro cancelado.")
            pausar()
            return
        if not endereco:
            msg_erro("Endereco nao pode ser vazio")
            pausar()
            return
        
        telefone = input("Telefone: ").strip()
        if telefone == "0":
            msg_info("Cadastro cancelado.")
            pausar()
            return
        if not telefone:
            msg_erro("Telefone nao pode ser vazio")
            pausar()
            return
        
        cliente = self.hotel.cadastrar_cliente(nome, endereco, telefone)
        msg_sucesso(f"Cliente cadastrado! Codigo: {cliente.codigo}")
        self.hotel.salvar_dados()
        pausar()
    
    def listar_clientes(self):
        limpar_tela()
        subtitulo("Todos os Clientes")
        
        clientes = self.hotel.listar_clientes()
        
        if not clientes:
            msg_info("Nenhum cliente cadastrado.")
        else:
            print("\n{:<8} {:<25} {:<30} {:<15}".format(
                "Codigo", "Nome", "Endereco", "Telefone"
            ))
            linha('-', 80)
            for c in clientes:
                print("{:<8} {:<25} {:<30} {:<15}".format(
                    c.codigo, c.nome[:24], c.endereco[:29], c.telefone
                ))
        
        print(f"\nTotal: {len(clientes)}")
        pausar()
    
    def pesquisar_cliente(self):
        limpar_tela()
        subtitulo("Pesquisar Cliente")
        
        termo = input("Digite nome ou codigo: ").strip()
        if not termo:
            msg_erro("Termo nao pode ser vazio")
            pausar()
            return
        
        resultados = self.hotel.pesquisar_cliente(termo)
        
        if not resultados:
            msg_info("Nenhum cliente encontrado.")
        else:
            print("\nResultados:")
            for c in resultados:
                print(f"\nCodigo: {c.codigo}")
                print(f"Nome: {c.nome}")
                print(f"Endereco: {c.endereco}")
                print(f"Telefone: {c.telefone}")
                linha('-', 40)
        
        pausar()
    
    def pontos_fidelidade(self):
        limpar_tela()
        subtitulo("Pontos de Fidelidade")
        
        termo = input("Codigo do cliente: ").strip()
        codigo = validar_numero(termo, minimo=1)
        
        if not codigo:
            msg_erro("Codigo invalido")
            pausar()
            return
        
        cliente = self.hotel.buscar_cliente_por_codigo(codigo)
        if not cliente:
            msg_erro("Cliente nao encontrado")
            pausar()
            return
        
        estadias_cliente = self.hotel.listar_estadias_por_cliente(codigo)
        pontos = cliente.calcular_pontos_fidelidade(estadias_cliente)
        
        print(f"\nCliente: {cliente.nome}")
        print(f"Total de estadias: {len(estadias_cliente)}")
        print(f"Pontos de fidelidade: {pontos}")
        print("\n(10 pontos por diaria)")
        
        pausar()
    
    def remover_cliente(self):
        limpar_tela()
        subtitulo("Remover Cliente")
        msg_info("Digite 0 para cancelar\n")
        
        # Lista clientes
        clientes = self.hotel.listar_clientes()
        if not clientes:
            msg_info("Nenhum cliente cadastrado.")
            pausar()
            return
        
        print("Clientes cadastrados:")
        for c in clientes:
            print(f"  {c.codigo} - {c.nome}")
        
        codigo_str = input("\nCodigo do cliente a remover: ").strip()
        if codigo_str == "0":
            msg_info("Operacao cancelada.")
            pausar()
            return
        
        codigo = validar_numero(codigo_str, minimo=1)
        if not codigo:
            msg_erro("Codigo invalido")
            pausar()
            return
        
        cliente = self.hotel.buscar_cliente_por_codigo(codigo)
        if not cliente:
            msg_erro("Cliente nao encontrado")
            pausar()
            return
        
        # Confirmação
        print(f"\nCliente: {cliente.nome}")
        print(f"Endereco: {cliente.endereco}")
        print(f"Telefone: {cliente.telefone}")
        
        confirmar = input("\nTem certeza que deseja remover? (s/n): ").strip().lower()
        if confirmar != 's':
            msg_info("Operacao cancelada.")
            pausar()
            return
        
        sucesso, mensagem = self.hotel.remover_cliente(codigo)
        if sucesso:
            msg_sucesso(mensagem)
            self.hotel.salvar_dados()
        else:
            msg_erro(mensagem)
        
        pausar()
    
    # --- funcionarios ---
    
    def cadastrar_funcionario(self):
        limpar_tela()
        subtitulo("Cadastrar Funcionario")
        msg_info("Digite 0 para cancelar a qualquer momento\n")
        
        nome = input("Nome: ").strip()
        if nome == "0":
            msg_info("Cadastro cancelado.")
            pausar()
            return
        if not nome:
            msg_erro("Nome nao pode ser vazio")
            pausar()
            return
        
        telefone = input("Telefone: ").strip()
        if telefone == "0":
            msg_info("Cadastro cancelado.")
            pausar()
            return
        if not telefone:
            msg_erro("Telefone nao pode ser vazio")
            pausar()
            return
        
        print("\nCargos sugeridos: Recepcionista, Gerente, Garcom, Auxiliar de Limpeza")
        cargo = input("Cargo: ").strip()
        if cargo == "0":
            msg_info("Cadastro cancelado.")
            pausar()
            return
        if not cargo:
            msg_erro("Cargo nao pode ser vazio")
            pausar()
            return
        
        salario_str = input("Salario (R$): ").strip()
        if salario_str == "0":
            msg_info("Cadastro cancelado.")
            pausar()
            return
        salario = validar_preco(salario_str)
        if not salario:
            msg_erro("Salario invalido")
            pausar()
            return
        
        func = self.hotel.cadastrar_funcionario(nome, telefone, cargo, salario)
        msg_sucesso(f"Funcionario cadastrado! Codigo: {func.codigo}")
        self.hotel.salvar_dados()
        pausar()
    
    def listar_funcionarios(self):
        limpar_tela()
        subtitulo("Todos os Funcionarios")
        
        funcionarios = self.hotel.listar_funcionarios()
        
        if not funcionarios:
            msg_info("Nenhum funcionario cadastrado.")
        else:
            print("\n{:<8} {:<25} {:<15} {:<20} {:<12}".format(
                "Codigo", "Nome", "Telefone", "Cargo", "Salario"
            ))
            linha('-', 80)
            for f in funcionarios:
                print("{:<8} {:<25} {:<15} {:<20} R${:<10.2f}".format(
                    f.codigo, f.nome[:24], f.telefone, f.cargo[:19], f.salario
                ))
        
        print(f"\nTotal: {len(funcionarios)}")
        pausar()
    
    def pesquisar_funcionario(self):
        limpar_tela()
        subtitulo("Pesquisar Funcionario")
        
        termo = input("Digite nome ou codigo: ").strip()
        if not termo:
            msg_erro("Termo nao pode ser vazio")
            pausar()
            return
        
        resultados = self.hotel.pesquisar_funcionario(termo)
        
        if not resultados:
            msg_info("Nenhum funcionario encontrado.")
        else:
            print("\nResultados:")
            for f in resultados:
                print(f"\nCodigo: {f.codigo}")
                print(f"Nome: {f.nome}")
                print(f"Telefone: {f.telefone}")
                print(f"Cargo: {f.cargo}")
                print(f"Salario: R${f.salario:.2f}")
                linha('-', 40)
        
        pausar()
    
    def remover_funcionario(self):
        limpar_tela()
        subtitulo("Remover Funcionario")
        msg_info("Digite 0 para cancelar\n")
        
        # Lista funcionários
        funcionarios = self.hotel.listar_funcionarios()
        if not funcionarios:
            msg_info("Nenhum funcionario cadastrado.")
            pausar()
            return
        
        print("Funcionarios cadastrados:")
        for f in funcionarios:
            print(f"  {f.codigo} - {f.nome} ({f.cargo})")
        
        codigo_str = input("\nCodigo do funcionario a remover: ").strip()
        if codigo_str == "0":
            msg_info("Operacao cancelada.")
            pausar()
            return
        
        codigo = validar_numero(codigo_str, minimo=1)
        if not codigo:
            msg_erro("Codigo invalido")
            pausar()
            return
        
        funcionario = self.hotel.buscar_funcionario_por_codigo(codigo)
        if not funcionario:
            msg_erro("Funcionario nao encontrado")
            pausar()
            return
        
        # Confirmação
        print(f"\nFuncionario: {funcionario.nome}")
        print(f"Cargo: {funcionario.cargo}")
        print(f"Telefone: {funcionario.telefone}")
        print(f"Salario: R${funcionario.salario:.2f}")
        
        confirmar = input("\nTem certeza que deseja remover? (s/n): ").strip().lower()
        if confirmar != 's':
            msg_info("Operacao cancelada.")
            pausar()
            return
        
        sucesso, mensagem = self.hotel.remover_funcionario(codigo)
        if sucesso:
            msg_sucesso(mensagem)
            self.hotel.salvar_dados()
        else:
            msg_erro(mensagem)
        
        pausar()
    
    # --- quartos ---
    
    def cadastrar_quarto(self):
        limpar_tela()
        subtitulo("Cadastrar Novo Quarto")
        msg_info("Digite 0 para cancelar a qualquer momento\n")
        
        numero_str = input("Numero do quarto: ").strip()
        if numero_str == "0":
            msg_info("Cadastro cancelado.")
            pausar()
            return
        numero = validar_numero(numero_str, minimo=1)
        if not numero:
            print("numero invalido")
            pausar()
            return
        
        if self.hotel.buscar_quarto_por_numero(numero):
            msg_erro("Quarto ja cadastrado!")
            pausar()
            return
        
        print("\nTipos: Simples, Duplo, Suite")
        tipo_input = input("Tipo: ").strip()
        if tipo_input == "0":
            msg_info("Cadastro cancelado.")
            pausar()
            return
        tipo = validar_tipo_quarto(tipo_input)
        if not tipo:
            print("tipo invalido")
            pausar()
            return
        
        capacidade_str = input("Quantidade de hospedes: ").strip()
        if capacidade_str == "0":
            msg_info("Cadastro cancelado.")
            pausar()
            return
        quantidade_hospedes = validar_numero(capacidade_str, minimo=1)
        if not quantidade_hospedes or quantidade_hospedes > 10:
            msg_erro("Quantidade invalida (1-10)")
            pausar()
            return
        
        preco_str = input("Preco da diaria (R$): ").strip()
        if preco_str == "0":
            msg_info("Cadastro cancelado.")
            pausar()
            return
        preco = validar_preco(preco_str)
        if not preco:
            msg_erro("Preco invalido")
            pausar()
            return
        
        if self.hotel.adicionar_quarto(numero, tipo, quantidade_hospedes, preco):
            msg_sucesso(f"Quarto {numero} cadastrado!")
            self.hotel.salvar_dados()
        else:
            msg_erro("Erro ao cadastrar")
        
        pausar()
    
    def listar_quartos(self):
        limpar_tela()
        subtitulo("Todos os Quartos")
        
        quartos = self.hotel.listar_quartos()
        tabela_quartos(quartos)
        
        print(f"\nTotal: {len(quartos)}")
        pausar()
    
    def consultar_quartos_disponiveis(self):
        limpar_tela()
        subtitulo("Quartos Disponiveis")
        
        disponiveis = self.hotel.listar_quartos_disponiveis()
        tabela_quartos(disponiveis)
        
        print(f"\nDisponiveis: {len(disponiveis)}")
        pausar()
    
    def alterar_status_quarto(self):
        limpar_tela()
        subtitulo("Alterar Status do Quarto")
        msg_info("Digite 0 para cancelar\n")
        
        quartos = self.hotel.listar_quartos()
        tabela_quartos(quartos)
        
        numero_str = input("\nNumero do quarto: ").strip()
        if numero_str == "0":
            msg_info("Operacao cancelada.")
            pausar()
            return
        numero = validar_numero(numero_str)
        
        if not numero:
            print("numero invalido")
            pausar()
            return
        
        quarto = self.hotel.buscar_quarto_por_numero(numero)
        
        if not quarto:
            msg_erro("Quarto nao encontrado")
            pausar()
            return
        
        print(f"\nStatus atual: {quarto.status}")
        print("\n1. Disponivel")
        print("2. Manutencao")
        
        opcao = input("\nNovo status: ").strip()
        
        if opcao == '1':
            quarto.marcar_disponivel()
            msg_sucesso("Status alterado para Disponivel!")
            self.hotel.salvar_dados()
        elif opcao == '2':
            quarto.marcar_manutencao()
            msg_sucesso("Status alterado para Manutencao!")
            self.hotel.salvar_dados()
        else:
            msg_erro("Opcao invalida")
        
        pausar()
    
    def remover_quarto(self):
        limpar_tela()
        subtitulo("Remover Quarto")
        msg_info("Digite 0 para cancelar\n")
        
        # Lista quartos
        quartos = self.hotel.listar_quartos()
        if not quartos:
            msg_info("Nenhum quarto cadastrado.")
            pausar()
            return
        
        print("Quartos cadastrados:")
        tabela_quartos(quartos)
        
        numero_str = input("\nNumero do quarto a remover: ").strip()
        if numero_str == "0":
            msg_info("Operacao cancelada.")
            pausar()
            return
        
        numero = validar_numero(numero_str, minimo=1)
        if not numero:
            msg_erro("Numero invalido")
            pausar()
            return
        
        quarto = self.hotel.buscar_quarto_por_numero(numero)
        if not quarto:
            msg_erro("Quarto nao encontrado")
            pausar()
            return
        
        # Confirmação
        print(f"\nQuarto: {quarto.numero}")
        print(f"Tipo: {quarto.tipo}")
        print(f"Capacidade: {quarto.quantidade_hospedes} hospede(s)")
        print(f"Preco: R${quarto.preco_diaria:.2f}/diaria")
        print(f"Status: {quarto.status}")
        
        confirmar = input("\nTem certeza que deseja remover? (s/n): ").strip().lower()
        if confirmar != 's':
            msg_info("Operacao cancelada.")
            pausar()
            return
        
        sucesso, mensagem = self.hotel.remover_quarto(numero)
        if sucesso:
            msg_sucesso(mensagem)
            self.hotel.salvar_dados()
        else:
            msg_erro(mensagem)
        
        pausar()
    
    # --- estadias ---
    
    def fazer_estadia(self):
        limpar_tela()
        subtitulo("Fazer Estadia")
        msg_info("Digite 0 para cancelar a qualquer momento\n")
        
        # mostra clientes
        print("Clientes cadastrados:")
        clientes = self.hotel.listar_clientes()
        if not clientes:
            msg_erro("Nenhum cliente cadastrado! Cadastre primeiro.")
            pausar()
            return
        
        for c in clientes[:10]:  # mostra ate 10
            print(f"  {c.codigo} - {c.nome}")
        
        codigo_str = input("\nCodigo do cliente: ").strip()
        if codigo_str == "0":
            msg_info("Operacao cancelada.")
            pausar()
            return
        codigo_cliente = validar_numero(codigo_str, minimo=1)
        if not codigo_cliente:
            msg_erro("Codigo invalido")
            pausar()
            return
        
        cliente = self.hotel.buscar_cliente_por_codigo(codigo_cliente)
        if not cliente:
            msg_erro("Cliente nao encontrado")
            pausar()
            return
        
        print(f"\nEstadia para: {cliente.nome}")
        
        # CONFORME PDF ITEM 4: pede quantidade de hospedes
        hospedes_str = input("Quantidade de hospedes: ").strip()
        if hospedes_str == "0":
            msg_info("Operacao cancelada.")
            pausar()
            return
        quantidade_hospedes = validar_numero(hospedes_str, minimo=1)
        if not quantidade_hospedes:
            msg_erro("Quantidade invalida")
            pausar()
            return
        
        entrada_str = input("Data entrada (DD/MM/AAAA): ").strip()
        if entrada_str == "0":
            msg_info("Operacao cancelada.")
            pausar()
            return
        data_entrada = validar_data(entrada_str)
        if not data_entrada:
            msg_erro("Data invalida")
            pausar()
            return
        
        if data_entrada < date.today():
            msg_erro("Data deve ser futura!")
            pausar()
            return
        
        saida_str = input("Data saida (DD/MM/AAAA): ").strip()
        if saida_str == "0":
            msg_info("Operacao cancelada.")
            pausar()
            return
        data_saida = validar_data(saida_str)
        if not data_saida:
            msg_erro("Data invalida")
            pausar()
            return
        
        # CONFORME PDF: sistema encontra quarto automaticamente
        estadia = self.hotel.cadastrar_estadia(codigo_cliente, quantidade_hospedes, data_entrada, data_saida)
        
        if estadia:
            msg_sucesso("Estadia cadastrada!")
            print(f"\n{estadia}")
            print(f"Quarto alocado: {estadia.quarto.numero} (quantidade hospedes: {estadia.quarto.quantidade_hospedes})")
            print(f"Diarias: {estadia.quantidade_diarias}")
            print(f"Valor: R${estadia.valor_total:.2f}")
            print(f"\nStatus: {estadia.status}")
            print(f"Status do quarto: {estadia.quarto.status} (sera Ocupado apos check-in)")
            self.hotel.salvar_dados()
        else:
            msg_erro("Nao foi possivel fazer a estadia.")
            print("Possiveis motivos:")
            print("  - Datas invalidas (saida anterior ou igual a entrada)")
            print("  - Nenhum quarto disponivel com capacidade suficiente para o periodo")
            print("  - Todos quartos com capacidade estao ocupados nas datas")
        
        pausar()
    
    def listar_estadias(self):
        limpar_tela()
        subtitulo("Todas as Estadias")
        
        estadias = self.hotel.listar_estadias()
        
        if not estadias:
            msg_info("Nenhuma estadia cadastrada.")
        else:
            print("\n{:<8} {:<12} {:<12} {:<12} {:<12} {:<10}".format(
                "Codigo", "Cliente", "Quarto", "Entrada", "Saida", "Status"
            ))
            linha('-', 80)
            for e in estadias:
                cliente = self.hotel.buscar_cliente_por_codigo(e.codigo_cliente)
                nome_cliente = cliente.nome[:10] if cliente else f"#{e.codigo_cliente}"
                print("{:<8} {:<12} {:<12} {:<12} {:<12} {:<10}".format(
                    e.codigo,
                    nome_cliente,
                    e.quarto.numero,
                    e.data_entrada.strftime('%d/%m/%Y'),
                    e.data_saida.strftime('%d/%m/%Y'),
                    e.status
                ))
        
        print(f"\nTotal: {len(estadias)}")
        pausar()
    
    def consultar_estadia(self):
        limpar_tela()
        subtitulo("Consultar Estadia")
        msg_info("Digite 0 para cancelar\n")
        
        codigo_str = input("Codigo da estadia: ").strip()
        if codigo_str == "0":
            msg_info("Operacao cancelada.")
            pausar()
            return
        codigo = validar_numero(codigo_str, minimo=1)
        
        if not codigo:
            msg_erro("Codigo invalido")
            pausar()
            return
        
        estadia = self.hotel.buscar_estadia_por_codigo(codigo)
        
        if estadia:
            cliente = self.hotel.buscar_cliente_por_codigo(estadia.codigo_cliente)
            print(f"\n{estadia}")
            print(f"Cliente: {cliente.nome if cliente else 'N/A'}")
            print(f"Quarto: {estadia.quarto.numero}")
            print(f"Entrada: {estadia.data_entrada.strftime('%d/%m/%Y')}")
            print(f"Saida: {estadia.data_saida.strftime('%d/%m/%Y')}")
            print(f"Diarias: {estadia.quantidade_diarias}")
            print(f"Valor: R${estadia.valor_total:.2f}")
            print(f"Status: {estadia.status}")
        else:
            msg_erro("Estadia nao encontrada")
        
        pausar()
    
    def cancelar_estadia(self):
        limpar_tela()
        subtitulo("Cancelar Estadia")
        msg_info("Digite 0 para cancelar\n")
        
        print("Estadias ativas:")
        ativas = self.hotel.listar_estadias_ativas()
        
        if not ativas:
            msg_info("Nao ha estadias ativas para cancelar.")
            pausar()
            return
        
        for e in ativas:
            cliente = self.hotel.buscar_cliente_por_codigo(e.codigo_cliente)
            print(f"  {e.codigo} - {cliente.nome if cliente else 'N/A'} - Quarto {e.quarto.numero}")
        
        codigo_str = input("\nCodigo da estadia: ").strip()
        if codigo_str == "0":
            msg_info("Operacao cancelada.")
            pausar()
            return
        codigo = validar_numero(codigo_str, minimo=1)
        
        if not codigo:
            print("Codigo invalido")
            pausar()
            return
        
        if self.hotel.cancelar_estadia(codigo):
            msg_sucesso("Estadia cancelada!")
            self.hotel.salvar_dados()
        else:
            msg_erro("Nao foi possivel cancelar")
        
        pausar()
    
    def estadias_por_cliente(self):
        limpar_tela()
        subtitulo("Estadias por Cliente")
        
        codigo_str = input("Codigo do cliente: ").strip()
        codigo = validar_numero(codigo_str, minimo=1)
        
        if not codigo:
            msg_erro("Codigo invalido")
            pausar()
            return
        
        cliente = self.hotel.buscar_cliente_por_codigo(codigo)
        if not cliente:
            msg_erro("Cliente nao encontrado")
            pausar()
            return
        
        estadias = self.hotel.listar_estadias_por_cliente(codigo)
        
        print(f"\nCliente: {cliente.nome}")
        
        if not estadias:
            msg_info("Nenhuma estadia encontrada.")
        else:
            print("\n{:<8} {:<12} {:<12} {:<12} {:<10}".format(
                "Codigo", "Quarto", "Entrada", "Saida", "Status"
            ))
            linha('-', 60)
            for e in estadias:
                print("{:<8} {:<12} {:<12} {:<12} {:<10}".format(
                    e.codigo,
                    e.quarto.numero,
                    e.data_entrada.strftime('%d/%m/%Y'),
                    e.data_saida.strftime('%d/%m/%Y'),
                    e.status
                ))
        
        print(f"\nTotal: {len(estadias)}")
        pausar()
    
    # --- checkin/checkout ---
    
    def realizar_checkin(self):
        limpar_tela()
        subtitulo("Realizar Check-in")
        msg_info("Digite 0 para cancelar\n")
        
        print("Estadias confirmadas:")
        confirmadas = [e for e in self.hotel.listar_estadias() if e.status == "Confirmada"]
        
        if not confirmadas:
            msg_info("Nao ha estadias confirmadas.")
            pausar()
            return
        
        for e in confirmadas:
            cliente = self.hotel.buscar_cliente_por_codigo(e.codigo_cliente)
            print(f"  {e.codigo} - {cliente.nome if cliente else 'N/A'} - Quarto {e.quarto.numero}")
        
        codigo_str = input("\nCodigo da estadia: ").strip()
        if codigo_str == "0":
            msg_info("Operacao cancelada.")
            pausar()
            return
        codigo = validar_numero(codigo_str, minimo=1)
        
        if not codigo:
            print("Codigo invalido")
            pausar()
            return
        
        if self.hotel.fazer_checkin(codigo):
            msg_sucesso("Check-in realizado!")
            self.hotel.salvar_dados()
        else:
            msg_erro("Nao foi possivel fazer check-in")
        
        pausar()
    
    def realizar_checkout(self):
        limpar_tela()
        subtitulo("Realizar Check-out (Baixa)")
        msg_info("Digite 0 para cancelar\n")
        
        print("Quartos ocupados:")
        ocupados = self.hotel.listar_quartos_ocupados()
        tabela_quartos(ocupados)
        
        if not ocupados:
            msg_info("Nao ha quartos ocupados.")
            pausar()
            return
        
        print("\nEstadias ativas:")
        ativas = [e for e in self.hotel.listar_estadias() if e.status == "Confirmada"]
        
        for e in ativas:
            cliente = self.hotel.buscar_cliente_por_codigo(e.codigo_cliente)
            print(f"  {e.codigo} - {cliente.nome if cliente else 'N/A'} - Quarto {e.quarto.numero}")
        
        codigo_str = input("\nCodigo da estadia: ").strip()
        if codigo_str == "0":
            msg_info("Operacao cancelada.")
            pausar()
            return
        codigo = validar_numero(codigo_str, minimo=1)
        
        if not codigo:
            print("Codigo invalido")
            pausar()
            return
        
        estadia = self.hotel.buscar_estadia_por_codigo(codigo)
        
        if not estadia:
            msg_erro("Estadia nao encontrada")
            pausar()
            return
        
        print(f"\nEstadia: {estadia.codigo}")
        print(f"Data entrada: {estadia.data_entrada.strftime('%d/%m/%Y')}")
        print(f"Data saida prevista: {estadia.data_saida.strftime('%d/%m/%Y')}")
        
        data_checkout_str = input("\nData do checkout (DD/MM/AAAA): ").strip()
        if data_checkout_str == "0":
            msg_info("Operacao cancelada.")
            pausar()
            return
        
        data_checkout = validar_data(data_checkout_str)
        if not data_checkout:
            msg_erro("Data invalida")
            pausar()
            return
        
        sucesso, resultado = self.hotel.fazer_checkout(codigo, data_checkout)
        
        if sucesso:
            msg_sucesso("Check-out realizado!")
            print(f"\nValor total: R${resultado:.2f}")
            print(f"Diarias: {estadia.quantidade_diarias}")
            self.hotel.salvar_dados()
        else:
            msg_erro(f"Erro: {resultado}")
        
        pausar()
    
    # --- relatorios ---
    
    def relatorio_ocupacao(self):
        limpar_tela()
        subtitulo("Relatorio de Ocupacao")
        
        rel = self.hotel.relatorio_ocupacao()
        
        print(f"\nTotal de quartos: {rel['total_quartos']}")
        print(f"Quartos disponiveis: {rel['quartos_disponiveis']}")
        print(f"Quartos ocupados: {rel['quartos_ocupados']}")
        print(f"Quartos em manutencao: {rel['quartos_manutencao']}")
        print(f"Taxa de ocupacao: {rel['taxa_ocupacao']:.2f}%")
        
        pausar()
    
    def relatorio_receita(self):
        limpar_tela()
        subtitulo("Relatorio de Receita")
        
        rel = self.hotel.relatorio_receita()
        
        print(f"\nReceita total: R${rel['receita_total']:.2f}")
        print(f"Receita concluida: R${rel['receita_concluida']:.2f}")
        print(f"Receita pendente: R${rel['receita_pendente']:.2f}")
        print(f"Total de estadias: {rel['total_estadias']}")
        
        pausar()
    
    def sair(self):
        limpar_tela()
        titulo("Obrigado por usar o Sistema do Hotel Descanso Garantido!")
        print("\nSalvando dados...")
        self.hotel.salvar_dados()
        msg_sucesso("Dados salvos!")
        print("\nAte logo!\n")
        self.executando = False

def main():
    sistema = SistemaHotel()
    sistema.executar()

if __name__ == "__main__":
    main()

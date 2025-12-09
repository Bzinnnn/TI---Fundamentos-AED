"""
Arquivo de testes para demonstrar o funcionamento do sistema
Pode ser executado para verificar se todas as funcionalidades estão operando corretamente
"""

from datetime import date, timedelta
from hotel import Hotel
from quarto import Quarto
from reserva import Reserva

def teste_quartos():
    """Testa funcionalidades de quartos"""
    print("=" * 80)
    print("TESTANDO GERENCIAMENTO DE QUARTOS")
    print("=" * 80)
    
    hotel = Hotel("Hotel Teste")
    
    # Teste 1: Adicionar quartos
    print("\n1. Adicionando quartos...")
    assert hotel.adicionar_quarto(101, "Simples", 1, 150.00) == True
    assert hotel.adicionar_quarto(102, "Duplo", 2, 250.00) == True
    assert hotel.adicionar_quarto(201, "Suíte", 4, 500.00) == True
    print("✓ Quartos adicionados com sucesso!")
    
    # Teste 2: Verificar duplicação
    print("\n2. Testando prevenção de duplicação...")
    assert hotel.adicionar_quarto(101, "Simples", 1, 150.00) == False
    print("✓ Duplicação corretamente prevenida!")
    
    # Teste 3: Buscar quarto
    print("\n3. Buscando quarto...")
    quarto = hotel.buscar_quarto_por_numero(101)
    assert quarto is not None
    assert quarto.numero == 101
    print(f"✓ Quarto encontrado: {quarto}")
    
    # Teste 4: Listar quartos disponíveis
    print("\n4. Listando quartos disponíveis...")
    disponiveis = hotel.listar_quartos_disponiveis()
    assert len(disponiveis) == 3
    print(f"✓ {len(disponiveis)} quartos disponíveis")
    
    # Teste 5: Alterar status
    print("\n5. Testando alteração de status...")
    quarto.marcar_ocupado()
    assert quarto.status == "Ocupado"
    print("✓ Status alterado para Ocupado")
    
    quarto.marcar_disponivel()
    assert quarto.status == "Disponível"
    print("✓ Status alterado para Disponível")
    
    print("\n" + "=" * 80)
    print("TODOS OS TESTES DE QUARTOS PASSARAM! ✓")
    print("=" * 80)

def teste_reservas():
    """Testa funcionalidades de reservas"""
    print("\n\n" + "=" * 80)
    print("TESTANDO SISTEMA DE RESERVAS")
    print("=" * 80)
    
    hotel = Hotel("Hotel Teste")
    
    # Adiciona quartos
    hotel.adicionar_quarto(101, "Simples", 1, 150.00)
    hotel.adicionar_quarto(102, "Duplo", 2, 250.00)
    
    # Teste 1: Fazer reserva
    print("\n1. Fazendo reserva...")
    hoje = date.today()
    amanha = hoje + timedelta(days=1)
    daqui_3_dias = hoje + timedelta(days=3)
    
    reserva = hotel.fazer_reserva(
        "João Silva",
        "12345678901",
        101,
        amanha,
        daqui_3_dias
    )
    
    assert reserva is not None
    assert reserva.nome_hospede == "João Silva"
    assert reserva.status == "Confirmada"
    print(f"✓ Reserva criada: ID {reserva.id}")
    
    # Teste 2: Cálculo de valor
    print("\n2. Testando cálculo de valor...")
    num_diarias = (daqui_3_dias - amanha).days
    valor_esperado = num_diarias * 150.00
    assert reserva.valor_total == valor_esperado
    print(f"✓ Valor correto: R${reserva.valor_total:.2f} ({num_diarias} diárias)")
    
    # Teste 3: Verificar disponibilidade
    print("\n3. Testando verificação de disponibilidade...")
    # Tenta reservar o mesmo quarto no mesmo período
    disponivel = hotel.verificar_disponibilidade(101, amanha, daqui_3_dias)
    assert disponivel == False
    print("✓ Conflito de datas corretamente detectado")
    
    # Teste 4: Cancelar reserva
    print("\n4. Testando cancelamento...")
    assert hotel.cancelar_reserva(reserva.id) == True
    assert reserva.status == "Cancelada"
    print("✓ Reserva cancelada com sucesso")
    
    # Teste 5: Check-in e Check-out
    print("\n5. Testando check-in e check-out...")
    reserva2 = hotel.fazer_reserva(
        "Maria Santos",
        "98765432109",
        102,
        amanha,
        daqui_3_dias
    )
    
    assert hotel.fazer_checkin(reserva2.id) == True
    quarto = hotel.buscar_quarto_por_numero(102)
    assert quarto.status == "Ocupado"
    print("✓ Check-in realizado")
    
    assert hotel.fazer_checkout(reserva2.id) == True
    assert quarto.status == "Disponível"
    assert reserva2.status == "Concluída"
    print("✓ Check-out realizado")
    
    print("\n" + "=" * 80)
    print("TODOS OS TESTES DE RESERVAS PASSARAM! ✓")
    print("=" * 80)

def teste_relatorios():
    """Testa geração de relatórios"""
    print("\n\n" + "=" * 80)
    print("TESTANDO RELATÓRIOS")
    print("=" * 80)
    
    hotel = Hotel("Hotel Teste")
    
    # Adiciona quartos
    hotel.adicionar_quarto(101, "Simples", 1, 150.00)
    hotel.adicionar_quarto(102, "Duplo", 2, 250.00)
    hotel.adicionar_quarto(103, "Suíte", 4, 500.00)
    
    # Faz algumas reservas
    hoje = date.today()
    amanha = hoje + timedelta(days=1)
    daqui_3_dias = hoje + timedelta(days=3)
    
    reserva1 = hotel.fazer_reserva("João Silva", "12345678901", 101, amanha, daqui_3_dias)
    hotel.fazer_checkin(reserva1.id)
    
    reserva2 = hotel.fazer_reserva("Maria Santos", "98765432109", 102, amanha, daqui_3_dias)
    
    # Teste 1: Relatório de ocupação
    print("\n1. Testando relatório de ocupação...")
    relatorio_ocupacao = hotel.relatorio_ocupacao()
    assert relatorio_ocupacao['total_quartos'] == 3
    assert relatorio_ocupacao['quartos_ocupados'] == 1
    assert relatorio_ocupacao['quartos_disponiveis'] == 2
    print(f"✓ Ocupação: {relatorio_ocupacao['taxa_ocupacao']:.2f}%")
    
    # Teste 2: Relatório de receita
    print("\n2. Testando relatório de receita...")
    relatorio_receita = hotel.relatorio_receita()
    assert relatorio_receita['total_reservas'] == 2
    print(f"✓ Receita total: R${relatorio_receita['receita_total']:.2f}")
    
    print("\n" + "=" * 80)
    print("TODOS OS TESTES DE RELATÓRIOS PASSARAM! ✓")
    print("=" * 80)

def teste_persistencia():
    """Testa salvamento e carregamento de dados"""
    print("\n\n" + "=" * 80)
    print("TESTANDO PERSISTÊNCIA DE DADOS")
    print("=" * 80)
    
    import os
    arquivo_teste = "teste_hotel_dados.json"
    
    # Remove arquivo de teste se existir
    if os.path.exists(arquivo_teste):
        os.remove(arquivo_teste)
    
    # Teste 1: Salvar dados
    print("\n1. Salvando dados...")
    hotel1 = Hotel("Hotel Teste")
    hotel1.adicionar_quarto(101, "Simples", 1, 150.00)
    hotel1.adicionar_quarto(102, "Duplo", 2, 250.00)
    
    hoje = date.today()
    amanha = hoje + timedelta(days=1)
    daqui_3_dias = hoje + timedelta(days=3)
    reserva = hotel1.fazer_reserva("João Silva", "12345678901", 101, amanha, daqui_3_dias)
    
    hotel1.salvar_dados(arquivo_teste)
    assert os.path.exists(arquivo_teste)
    print("✓ Dados salvos com sucesso")
    
    # Teste 2: Carregar dados
    print("\n2. Carregando dados...")
    hotel2 = Hotel("Hotel Novo")
    assert hotel2.carregar_dados(arquivo_teste) == True
    assert hotel2.nome == "Hotel Teste"
    assert len(hotel2.quartos) == 2
    assert len(hotel2.reservas) == 1
    print("✓ Dados carregados com sucesso")
    
    # Teste 3: Verificar integridade
    print("\n3. Verificando integridade dos dados...")
    quarto_carregado = hotel2.buscar_quarto_por_numero(101)
    assert quarto_carregado is not None
    assert quarto_carregado.preco_diaria == 150.00
    
    reserva_carregada = hotel2.reservas[0]
    assert reserva_carregada.nome_hospede == "João Silva"
    assert reserva_carregada.cpf_hospede == "12345678901"
    print("✓ Dados íntegros")
    
    # Limpa arquivo de teste
    os.remove(arquivo_teste)
    
    print("\n" + "=" * 80)
    print("TODOS OS TESTES DE PERSISTÊNCIA PASSARAM! ✓")
    print("=" * 80)

def executar_todos_testes():
    """Executa todos os testes"""
    print("\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " EXECUTANDO BATERIA COMPLETA DE TESTES ".center(78) + "║")
    print("╚" + "═" * 78 + "╝")
    
    try:
        teste_quartos()
        teste_reservas()
        teste_relatorios()
        teste_persistencia()
        
        print("\n\n")
        print("╔" + "═" * 78 + "╗")
        print("║" + " ✓✓✓ TODOS OS TESTES PASSARAM COM SUCESSO! ✓✓✓ ".center(78) + "║")
        print("╚" + "═" * 78 + "╝")
        print("\n")
        
        return True
    
    except AssertionError as e:
        print("\n\n")
        print("╔" + "═" * 78 + "╗")
        print("║" + " ✗✗✗ FALHA NOS TESTES ✗✗✗ ".center(78) + "║")
        print("╚" + "═" * 78 + "╝")
        print(f"\nErro: {e}")
        return False
    
    except Exception as e:
        print("\n\n")
        print("╔" + "═" * 78 + "╗")
        print("║" + " ✗✗✗ ERRO INESPERADO ✗✗✗ ".center(78) + "║")
        print("╚" + "═" * 78 + "╝")
        print(f"\nErro: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    executar_todos_testes()

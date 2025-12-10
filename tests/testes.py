# testes.py - BATERIA DE TESTES
# Conforme especificacao do PDF - Adequado para primeiro periodo

from datetime import date, timedelta
import sys
import os
import time

# Adiciona o diretorio raiz ao path para importar os modulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.hotel import Hotel
from src.models.cliente import Cliente
from src.models.funcionario import Funcionario
from src.models.quarto import Quarto
from src.models.estadia import Estadia

def teste_clientes():
    """Testa TODAS as funcionalidades relacionadas a clientes"""
    print("\n" + "=" * 70)
    print("TESTANDO CLIENTES - BATERIA COMPLETA (6 testes)")
    print("=" * 70)
    
    inicio = time.time()
    hotel = Hotel("Hotel Teste")
    
    # TESTE 1: Cadastrar clientes com codigo auto-gerado
    print("\n[TC-CLI-001] Cadastrando clientes (codigo auto-gerado)...")
    c1 = hotel.cadastrar_cliente("Maria Silva", "Rua A, 123", "31999991111")
    c2 = hotel.cadastrar_cliente("João Santos", "Av B, 456", "31988882222")
    c3 = hotel.cadastrar_cliente("Ana Costa", "Praca C, 789", "31977773333")
    assert c1.codigo == 1, "Codigo do primeiro cliente deve ser 1"
    assert c2.codigo == 2, "Codigo do segundo cliente deve ser 2"
    assert c3.codigo == 3, "Codigo do terceiro cliente deve ser 3"
    print("✓ PASSOU - 3 clientes cadastrados com codigos 1, 2, 3")
    
    # TESTE 2: Validar que nao ha codigos duplicados
    print("\n[TC-CLI-002] Validando unicidade de codigos...")
    codigos = [c.codigo for c in hotel.clientes]
    assert len(codigos) == len(set(codigos)), "Nao deve haver codigos duplicados"
    print(f"✓ PASSOU - {len(codigos)} codigos unicos validados")
    
    # TESTE 3: Buscar cliente por codigo existente
    print("\n[TC-CLI-003] Buscando cliente por codigo existente...")
    cliente = hotel.buscar_cliente_por_codigo(1)
    assert cliente is not None, "Deve encontrar cliente"
    assert cliente.nome == "Maria Silva", "Nome deve corresponder"
    assert cliente.codigo == 1, "Codigo deve corresponder"
    print(f"✓ PASSOU - Cliente encontrado: {cliente.nome} (codigo: {cliente.codigo})")
    
    # TESTE 4: Pesquisar por nome (parcial)
    print("\n[TC-CLI-004] Pesquisando por nome parcial...")
    resultado = hotel.pesquisar_cliente("Maria")
    assert len(resultado) == 1, "Deve encontrar 1 cliente"
    assert resultado[0].nome == "Maria Silva", "Deve ser Maria Silva"
    print(f"✓ PASSOU - Pesquisa 'Maria' retornou {len(resultado)} resultado")
    
    # TESTE 5: Listar todos os clientes
    print("\n[TC-CLI-005] Listando todos os clientes...")
    todos = hotel.listar_clientes()
    assert len(todos) == 3, "Deve ter 3 clientes"
    print(f"✓ PASSOU - Lista retornou {len(todos)} clientes cadastrados")
    
    # TESTE 6: Validar estrutura do cliente (PDF)
    print("\n[TC-CLI-006] Validando estrutura do cliente conforme PDF...")
    assert hasattr(c1, 'codigo'), "Cliente deve ter codigo"
    assert hasattr(c1, 'nome'), "Cliente deve ter nome"
    assert hasattr(c1, 'endereco'), "Cliente deve ter endereco"
    assert hasattr(c1, 'telefone'), "Cliente deve ter telefone"
    print("✓ PASSOU - Campos obrigatorios: codigo, nome, endereco, telefone")
    
    tempo = time.time() - inicio
    print("\n" + "=" * 70)
    print(f"✓✓✓ TODOS OS TESTES DE CLIENTES PASSARAM! (6/6) [{tempo:.3f}s]")
    print("=" * 70)

def teste_funcionarios():
    """Testa TODAS as funcionalidades relacionadas a funcionarios"""
    print("\n" + "=" * 70)
    print("TESTANDO FUNCIONARIOS - BATERIA COMPLETA (6 testes)")
    print("=" * 70)
    
    inicio = time.time()
    hotel = Hotel("Hotel Teste")
    
    # TESTE 1: Cadastrar funcionarios com codigo auto-gerado
    print("\n[TC-FUNC-001] Cadastrando funcionarios (codigo auto-gerado)...")
    f1 = hotel.cadastrar_funcionario("Ana Costa", "31977773333", "Recepcionista", 2500.00)
    f2 = hotel.cadastrar_funcionario("Carlos Souza", "31966664444", "Gerente", 5000.00)
    f3 = hotel.cadastrar_funcionario("Maria Lima", "31955555555", "Auxiliar de limpeza", 1800.00)
    f4 = hotel.cadastrar_funcionario("Jose Silva", "31944446666", "Garçom", 2000.00)
    assert f1.codigo == 1, "Primeiro funcionario codigo 1"
    assert f2.codigo == 2, "Segundo funcionario codigo 2"
    assert f3.codigo == 3, "Terceiro funcionario codigo 3"
    assert f4.codigo == 4, "Quarto funcionario codigo 4"
    print("✓ PASSOU - 4 funcionarios (Recepcionista, Gerente, Auxiliar, Garçom)")
    
    # TESTE 2: Validar unicidade de codigos
    print("\n[TC-FUNC-002] Validando unicidade de codigos...")
    codigos = [f.codigo for f in hotel.funcionarios]
    assert len(codigos) == len(set(codigos)), "Codigos devem ser unicos"
    print(f"✓ PASSOU - {len(codigos)} codigos unicos")
    
    # TESTE 3: Buscar funcionario por codigo
    print("\n[TC-FUNC-003] Buscando funcionario por codigo...")
    func = hotel.buscar_funcionario_por_codigo(1)
    assert func is not None, "Deve encontrar"
    assert func.cargo == "Recepcionista", "Cargo deve corresponder"
    assert func.salario == 2500.00, "Salario deve corresponder"
    print(f"✓ PASSOU - Encontrado: {func.nome} - {func.cargo} - R${func.salario:.2f}")
    
    # TESTE 4: Buscar funcionario inexistente
    print("\n[TC-FUNC-004] Buscando funcionario inexistente...")
    func = hotel.buscar_funcionario_por_codigo(999)
    assert func is None, "Deve retornar None"
    print("✓ PASSOU - Retornou None para codigo 999 (inexistente)")
    
    # TESTE 5: Pesquisar por nome
    print("\n[TC-FUNC-005] Pesquisando funcionario por nome...")
    resultado = hotel.pesquisar_funcionario("Carlos")
    assert len(resultado) >= 1, "Deve encontrar Carlos"
    print(f"✓ PASSOU - Pesquisa 'Carlos' retornou {len(resultado)} resultado(s)")
    
    # TESTE 6: Validar estrutura conforme PDF
    print("\n[TC-FUNC-006] Validando estrutura conforme PDF...")
    assert hasattr(f1, 'codigo'), "Deve ter codigo"
    assert hasattr(f1, 'nome'), "Deve ter nome"
    assert hasattr(f1, 'telefone'), "Deve ter telefone"
    assert hasattr(f1, 'cargo'), "Deve ter cargo"
    assert hasattr(f1, 'salario'), "Deve ter salario"
    print("✓ PASSOU - Campos obrigatorios: codigo, nome, telefone, cargo, salario")
    
    tempo = time.time() - inicio
    print("\n" + "=" * 70)
    print(f"✓✓✓ TODOS OS TESTES DE FUNCIONARIOS PASSARAM! (6/6) [{tempo:.3f}s]")
    print("=" * 70)

def teste_quartos():
    """Testa TODAS as funcionalidades relacionadas a quartos"""
    print("\n" + "=" * 70)
    print("TESTANDO QUARTOS - BATERIA COMPLETA (8 testes)")
    print("=" * 70)
    
    inicio = time.time()
    hotel = Hotel("Hotel Teste")
    
    # TESTE 1: Adicionar quartos com sucesso
    print("\n[TC-QTO-001] Adicionando quartos...")
    assert hotel.adicionar_quarto(101, "Simples", 1, 150.00) == True
    assert hotel.adicionar_quarto(102, "Duplo", 2, 250.00) == True
    assert hotel.adicionar_quarto(201, "Suíte", 4, 500.00) == True
    assert hotel.adicionar_quarto(202, "Simples", 1, 150.00) == True
    print(f"✓ PASSOU - 4 quartos cadastrados (101, 102, 201, 202)")
    
    # TESTE 2: Prevenir numero duplicado
    print("\n[TC-QTO-002] Testando prevencao de numero duplicado...")
    assert hotel.adicionar_quarto(101, "Simples", 1, 150.00) == False
    print("✓ PASSOU - Bloqueou cadastro duplicado do quarto 101")
    
    # TESTE 3: Buscar quarto por numero
    print("\n[TC-QTO-003] Buscando quarto por numero...")
    quarto = hotel.buscar_quarto_por_numero(101)
    assert quarto is not None, "Deve encontrar quarto"
    assert quarto.numero == 101, "Numero deve corresponder"
    print(f"✓ PASSOU - Quarto 101 encontrado (capacidade: {quarto.quantidade_hospedes})")
    
    # TESTE 4: Validar estrutura conforme PDF
    print("\n[TC-QTO-004] Validando estrutura do quarto conforme PDF...")
    q = hotel.quartos[0]
    assert hasattr(q, 'numero'), "Deve ter numero"
    assert hasattr(q, 'quantidade_hospedes'), "Deve ter quantidade_hospedes"
    assert hasattr(q, 'preco_diaria'), "Deve ter preco_diaria"
    assert hasattr(q, 'status'), "Deve ter status"
    print("✓ PASSOU - Campos obrigatorios: numero, quantidade_hospedes, valor diaria, status")
    
    # TESTE 5: Validar status inicial (desocupado)
    print("\n[TC-QTO-005] Validando status inicial...")
    assert q.status == "desocupado", "Status inicial deve ser desocupado"
    print("✓ PASSOU - Status inicial 'desocupado' (conforme PDF)")
    
    # TESTE 6: Validar possiveis status conforme PDF
    print("\n[TC-QTO-006] Testando mudanca de status (ocupado/desocupado)...")
    assert q.marcar_ocupado() == True, "Deve marcar como ocupado"
    assert q.status == "ocupado", "Status deve ser ocupado"
    q.marcar_desocupado()
    assert q.status == "desocupado", "Status deve voltar a desocupado"
    print("✓ PASSOU - Apenas 2 status conforme PDF: ocupado/desocupado")
    
    # TESTE 7: Listar quartos disponiveis (desocupados)
    print("\n[TC-QTO-007] Listando quartos disponiveis...")
    disponiveis = hotel.listar_quartos_disponiveis()
    assert len(disponiveis) == 4, "Todos devem estar disponiveis"
    print(f"✓ PASSOU - {len(disponiveis)} quartos com status 'desocupado'")
    
    # TESTE 8: Testar quantidade_hospedes (campo do PDF)
    print("\n[TC-QTO-008] Validando campo quantidade_hospedes...")
    q = hotel.quartos[0]
    assert q.quantidade_hospedes == 1, "Quantidade deve ser 1"
    assert isinstance(q.quantidade_hospedes, int), "Deve ser inteiro"
    print(f"✓ PASSOU - Campo quantidade_hospedes = {q.quantidade_hospedes} (tipo: int)")
    
    tempo = time.time() - inicio
    print("\n" + "=" * 70)
    print(f"✓✓✓ TODOS OS TESTES DE QUARTOS PASSARAM! (8/8) [{tempo:.3f}s]")
    print("=" * 70)

def teste_estadias():
    """Testa TODAS as funcionalidades relacionadas a estadias"""
    print("\n" + "=" * 70)
    print("TESTANDO ESTADIAS - BATERIA COMPLETA (10 testes)")
    print("=" * 70)
    
    inicio = time.time()
    
    hotel = Hotel("Hotel Teste")
    
    # Setup
    cliente1 = hotel.cadastrar_cliente("Teste Cliente", "End Teste", "31999999999")
    cliente2 = hotel.cadastrar_cliente("Outro Cliente", "End 2", "31988888888")
    hotel.adicionar_quarto(101, "Simples", 1, 150.00)
    hotel.adicionar_quarto(102, "Duplo", 2, 250.00)
    hotel.adicionar_quarto(201, "Suíte", 4, 500.00)
    hotel.adicionar_quarto(202, "Simples", 1, 150.00)
    
    # TESTE 1: Cadastrar estadia COM BUSCA AUTOMATICA (conforme PDF item 4)
    print("\n1. Cadastrando estadia com busca automatica de quarto...")
    entrada = date.today() + timedelta(days=1)
    saida = entrada + timedelta(days=2)
    estadia = hotel.cadastrar_estadia(cliente1.codigo, 1, entrada, saida)
    assert estadia is not None, "Deve criar estadia"
    assert estadia.quantidade_diarias == 2, "Deve ter 2 diarias"
    assert estadia.quarto.quantidade_hospedes >= 1, "Quarto deve ter capacidade suficiente"
    print(f"✓ OK - estadia criada com quarto alocado automaticamente: {estadia.quarto.numero}")
    
    # TESTE 2: Validar estrutura da estadia conforme PDF
    print("\n2. Validando estrutura da estadia conforme PDF...")
    assert hasattr(estadia, 'codigo'), "Deve ter codigo"
    assert hasattr(estadia, 'data_entrada'), "Deve ter data_entrada"
    assert hasattr(estadia, 'data_saida'), "Deve ter data_saida"
    assert hasattr(estadia, 'quantidade_diarias'), "Deve ter quantidade_diarias"
    assert hasattr(estadia, 'codigo_cliente'), "Deve ter codigo_cliente"
    assert hasattr(estadia, 'quarto'), "Deve ter referencia ao quarto"
    print("✓ OK - estrutura conforme PDF completa")
    
    # TESTE 3: Validar calculo de diarias
    print("\n3. Validando calculo de diarias...")
    assert estadia.quantidade_diarias == (saida - entrada).days, "Calculo deve estar correto"
    print(f"✓ OK - {estadia.quantidade_diarias} diarias calculadas corretamente")
    
    # TESTE 4: Validar calculo de valor total
    print("\n4. Validando calculo de valor total...")
    valor_esperado = estadia.quantidade_diarias * estadia.quarto.preco_diaria
    assert estadia.valor_total == valor_esperado, "Valor deve estar correto"
    print(f"✓ OK - valor R${estadia.valor_total:.2f} calculado corretamente")
    
    # TESTE 5: Validar que cliente deve existir
    print("\n5. Testando validacao: cliente deve existir...")
    estadia_invalida = hotel.cadastrar_estadia(999, 1, entrada, saida)
    assert estadia_invalida is None, "Nao deve criar estadia com cliente inexistente"
    print("✓ OK - nao permite estadia sem cliente cadastrado")
    
    # TESTE 6: Validar que quarto deve estar desocupado
    print("\n6. Testando validacao: quarto deve estar desocupado...")
    entrada2 = date.today() + timedelta(days=1)
    saida2 = entrada2 + timedelta(days=2)
    # Tenta criar outra estadia no mesmo quarto e periodo
    estadia2 = hotel.fazer_estadia(cliente2.codigo, estadia.quarto.numero, entrada2, saida2)
    assert estadia2 is None, "Nao deve permitir conflito de datas"
    print("✓ OK - nao permite conflito de periodo (quarto ja reservado)")
    
    # TESTE 7: Testar cancelamento de estadia
    print("\n7. Testando cancelamento de estadia...")
    assert hotel.cancelar_estadia(estadia.codigo) == True, "Deve cancelar"
    assert estadia.status == "Cancelada", "Status deve ser Cancelada"
    assert estadia.quarto.status == "desocupado", "Quarto deve voltar a desocupado"
    print("✓ OK - cancelamento libera quarto (status = desocupado)")
    
    # TESTE 8: Testar check-in
    print("\n8. Testando check-in...")
    entrada3 = date.today() - timedelta(days=1)  # ontem (ja passou)
    saida3 = entrada3 + timedelta(days=3)        # daqui 2 dias
    estadia3 = hotel.fazer_estadia(cliente2.codigo, 102, entrada3, saida3)
    assert hotel.fazer_checkin(estadia3.codigo) == True, "Check-in deve funcionar"
    assert estadia3.quarto.status == "ocupado", "Quarto deve ficar ocupado"
    print("✓ OK - check-in marca quarto como ocupado")
    
    # TESTE 9: Testar checkout (funcao 5 do PDF) com validacao de data
    print("\n9. Testando checkout conforme item 5 do PDF...")
    sucesso, resultado = hotel.fazer_checkout(estadia3.codigo)
    assert sucesso == True, f"Checkout deve funcionar: {resultado}"
    assert estadia3.status == "Concluida", "Status deve ser Concluida"
    assert estadia3.quarto.status == "desocupado", "Quarto deve voltar a desocupado"
    print(f"✓ OK - checkout: status=Concluida, quarto=desocupado, valor=R${resultado:.2f}")
    
    # TESTE 10: Testar busca de quarto automatica com quantidade_hospedes
    print("\n10. Testando busca automatica por quantidade_hospedes...")
    entrada4 = date.today() + timedelta(days=20)
    saida4 = entrada4 + timedelta(days=1)
    estadia4 = hotel.cadastrar_estadia(cliente1.codigo, 4, entrada4, saida4)  # 4 hospedes
    assert estadia4 is not None, "Deve encontrar quarto"
    assert estadia4.quarto.quantidade_hospedes >= 4, "Quarto deve ter capacidade >= 4"
    print(f"✓ OK - encontrou quarto {estadia4.quarto.numero} com capacidade {estadia4.quarto.quantidade_hospedes}")
    
    print("\n" + "=" * 60)
    print("✓✓✓ TODOS OS TESTES DE ESTADIAS PASSARAM! (10/10)")
    print("=" * 60)

def teste_pontos_fidelidade():
    """Testa funcao 8 do PDF: pontos de fidelidade"""
    print("\n" + "=" * 60)
    print("TESTANDO PONTOS DE FIDELIDADE (Item 8 do PDF)")
    print("=" * 60)
    
    hotel = Hotel("Hotel Teste")
    
    # Setup
    cliente = hotel.cadastrar_cliente("Cliente Fiel", "End", "31999999999")
    hotel.adicionar_quarto(101, "Simples", 1, 150.00)
    hotel.adicionar_quarto(102, "Duplo", 2, 250.00)
    hotel.adicionar_quarto(103, "Suite", 4, 500.00)
    
    # TESTE 1: Cliente sem estadias = 0 pontos
    print("\n1. Cliente sem estadias...")
    estadias = hotel.listar_estadias_por_cliente(cliente.codigo)
    pontos = cliente.calcular_pontos_fidelidade(estadias)
    assert pontos == 0, "Cliente sem estadias deve ter 0 pontos"
    print("✓ OK - 0 pontos para cliente sem estadias")
    
    # TESTE 2: Cliente com 1 estadia
    print("\n2. Cliente com 1 estadia (3 diarias)...")
    entrada1 = date.today() + timedelta(days=1)
    saida1 = entrada1 + timedelta(days=3)  # 3 diarias
    estadia1 = hotel.fazer_estadia(cliente.codigo, 101, entrada1, saida1)
    estadias = hotel.listar_estadias_por_cliente(cliente.codigo)
    pontos = cliente.calcular_pontos_fidelidade(estadias)
    assert pontos == 30, "3 diarias x 10 = 30 pontos"
    print(f"✓ OK - {pontos} pontos (3 diarias x 10)")
    
    # TESTE 3: Cliente com multiplas estadias (conforme menciona PDF)
    print("\n3. Cliente com multiplas estadias...")
    entrada2 = date.today() + timedelta(days=10)
    saida2 = entrada2 + timedelta(days=5)  # 5 diarias
    estadia2 = hotel.fazer_estadia(cliente.codigo, 102, entrada2, saida2)
    
    entrada3 = date.today() + timedelta(days=20)
    saida3 = entrada3 + timedelta(days=2)  # 2 diarias
    estadia3 = hotel.fazer_estadia(cliente.codigo, 103, entrada3, saida3)
    
    estadias = hotel.listar_estadias_por_cliente(cliente.codigo)
    pontos = cliente.calcular_pontos_fidelidade(estadias)
    assert pontos == 100, "10 diarias totais x 10 = 100 pontos"
    print(f"✓ OK - {pontos} pontos (3+5+2 = 10 diarias x 10)")
    
    # TESTE 4: Validar calculo correto (10 pontos por diaria)
    print("\n4. Validando regra: 10 pontos por diaria...")
    total_diarias = sum(e.quantidade_diarias for e in estadias if e.codigo_cliente == cliente.codigo)
    pontos_esperados = total_diarias * 10
    assert pontos == pontos_esperados, "Deve ser 10 pontos por diaria"
    print(f"✓ OK - regra validada: {total_diarias} diarias x 10 = {pontos} pontos")
    
    print("\n" + "=" * 60)
    print("✓✓✓ TODOS OS TESTES DE PONTOS PASSARAM! (4/4)")
    print("=" * 60)

def teste_pesquisas():
    """Testa funcao 6 e 7 do PDF: pesquisas"""
    print("\n" + "=" * 60)
    print("TESTANDO PESQUISAS (Item 6 e 7 do PDF)")
    print("=" * 60)
    
    hotel = Hotel("Hotel Teste")
    
    # Setup
    c1 = hotel.cadastrar_cliente("Maria Silva", "Rua A", "31999991111")
    c2 = hotel.cadastrar_cliente("João Silva", "Rua B", "31988882222")
    c3 = hotel.cadastrar_cliente("Ana Costa", "Rua C", "31977773333")
    
    f1 = hotel.cadastrar_funcionario("Carlos Santos", "31966664444", "Gerente", 5000.00)
    f2 = hotel.cadastrar_funcionario("Julia Lima", "31955555555", "Recepcionista", 2500.00)
    
    hotel.adicionar_quarto(101, "Simples", 1, 150.00)
    hotel.adicionar_quarto(102, "Duplo", 2, 250.00)
    
    # TESTE 1: Pesquisar cliente por nome
    print("\n1. Pesquisando cliente por nome...")
    resultado = hotel.pesquisar_cliente("Maria")
    assert len(resultado) == 1, "Deve encontrar Maria"
    assert resultado[0].nome == "Maria Silva", "Deve ser Maria Silva"
    print("✓ OK - pesquisa por nome funcionou")
    
    # TESTE 2: Pesquisar cliente por codigo
    print("\n2. Pesquisando cliente por codigo...")
    resultado = hotel.pesquisar_cliente(str(c2.codigo))
    assert len(resultado) == 1, "Deve encontrar 1"
    assert resultado[0].codigo == c2.codigo, "Codigo deve corresponder"
    print("✓ OK - pesquisa por codigo funcionou")
    
    # TESTE 3: Pesquisar cliente por nome parcial
    print("\n3. Pesquisando cliente por nome parcial...")
    resultado = hotel.pesquisar_cliente("Silva")  # deve encontrar Maria e Joao
    assert len(resultado) == 2, "Deve encontrar 2 (Maria e Joao Silva)"
    print("✓ OK - pesquisa parcial encontrou multiplos resultados")
    
    # TESTE 4: Pesquisar funcionario por nome
    print("\n4. Pesquisando funcionario por nome...")
    resultado = hotel.pesquisar_funcionario("Carlos")
    assert len(resultado) == 1, "Deve encontrar Carlos"
    assert resultado[0].nome == "Carlos Santos", "Deve ser Carlos Santos"
    print("✓ OK - pesquisa funcionario por nome")
    
    # TESTE 5: Pesquisar funcionario por codigo
    print("\n5. Pesquisando funcionario por codigo...")
    resultado = hotel.pesquisar_funcionario(str(f1.codigo))
    assert len(resultado) == 1, "Deve encontrar 1"
    assert resultado[0].codigo == f1.codigo, "Codigo deve corresponder"
    print("✓ OK - pesquisa funcionario por codigo")
    
    # TESTE 6: Listar estadias de cliente (item 7 do PDF)
    print("\n6. Listando estadias de um cliente (item 7 do PDF)...")
    entrada = date.today() + timedelta(days=1)
    saida = entrada + timedelta(days=2)
    estadia1 = hotel.fazer_estadia(c1.codigo, 101, entrada, saida)
    
    entrada2 = date.today() + timedelta(days=10)
    saida2 = entrada2 + timedelta(days=3)
    estadia2 = hotel.fazer_estadia(c1.codigo, 102, entrada2, saida2)
    
    estadias_maria = hotel.listar_estadias_por_cliente(c1.codigo)
    assert len(estadias_maria) == 2, "Maria deve ter 2 estadias"
    assert all(e.codigo_cliente == c1.codigo for e in estadias_maria), "Todas devem ser da Maria"
    print(f"✓ OK - listou {len(estadias_maria)} estadias da cliente Maria")
    
    print("\n" + "=" * 60)
    print("✓✓✓ TODOS OS TESTES DE PESQUISAS PASSARAM! (6/6)")
    print("=" * 60)

def teste_relatorios():
    """Testa funcionalidades de relatorios"""
    print("\n" + "=" * 60)
    print("TESTANDO RELATORIOS")
    print("=" * 60)
    
    hotel = Hotel("Hotel Teste")
    
    # Setup
    cliente = hotel.cadastrar_cliente("Teste", "End", "31999999999")
    hotel.adicionar_quarto(101, "Simples", 1, 150.00)
    hotel.adicionar_quarto(102, "Duplo", 2, 250.00)
    hotel.adicionar_quarto(103, "Suite", 4, 500.00)
    
    entrada = date.today() + timedelta(days=1)
    saida = entrada + timedelta(days=2)
    estadia = hotel.fazer_estadia(cliente.codigo, 101, entrada, saida)
    hotel.fazer_checkin(estadia.codigo)
    
    # TESTE 1: Relatorio de ocupacao
    print("\n1. Testando relatorio de ocupacao...")
    rel = hotel.relatorio_ocupacao()
    assert rel['total_quartos'] == 3, "Total deve ser 3"
    assert rel['quartos_ocupados'] == 1, "Ocupados deve ser 1"
    taxa_esperada = (1 / 3) * 100
    assert abs(rel['taxa_ocupacao'] - taxa_esperada) < 0.01, "Taxa deve estar correta"
    print(f"✓ OK - Ocupacao: {rel['taxa_ocupacao']:.2f}% (1/3 quartos)")
    
    # TESTE 2: Relatorio de receita
    print("\n2. Testando relatorio de receita...")
    rel = hotel.relatorio_receita()
    assert rel['receita_total'] == 300.00, "Receita deve ser 300"
    assert rel['receita_pendente'] == 300.00, "Pendente deve ser 300"
    print(f"✓ OK - Receita total: R${rel['receita_total']:.2f}")
    
    print("\n" + "=" * 60)
    print("✓✓✓ TODOS OS TESTES DE RELATORIOS PASSARAM! (2/2)")
    print("=" * 60)

def teste_persistencia():
    """Testa salvamento e carregamento de dados"""
    print("\n" + "=" * 60)
    print("TESTANDO PERSISTENCIA DE DADOS")
    print("=" * 60)
    
    # TESTE 1: Salvar dados
    print("\n1. Salvando dados completos...")
    hotel1 = Hotel("Hotel Teste")
    cliente = hotel1.cadastrar_cliente("Maria", "Rua X", "31999999999")
    hotel1.cadastrar_funcionario("Ana", "31988888888", "Recepcionista", 2500.00)
    hotel1.adicionar_quarto(101, "Simples", 1, 150.00)
    entrada = date.today() + timedelta(days=1)
    saida = entrada + timedelta(days=2)
    hotel1.fazer_estadia(cliente.codigo, 101, entrada, saida)
    
    assert hotel1.salvar_dados('data/teste_hotel.json') == True
    print("✓ OK - dados salvos em arquivo")
    
    # TESTE 2: Carregar dados
    print("\n2. Carregando dados...")
    hotel2 = Hotel("Vazio")
    assert hotel2.carregar_dados('data/teste_hotel.json') == True
    print("✓ OK - dados carregados")
    
    # TESTE 3: Verificar integridade
    print("\n3. Verificando integridade dos dados...")
    assert len(hotel2.clientes) == 1, "Deve ter 1 cliente"
    assert len(hotel2.funcionarios) == 1, "Deve ter 1 funcionario"
    assert len(hotel2.quartos) == 1, "Deve ter 1 quarto"
    assert len(hotel2.estadias) == 1, "Deve ter 1 estadia"
    assert hotel2.clientes[0].nome == "Maria", "Nome deve ser preservado"
    assert hotel2.quartos[0].quantidade_hospedes == 1, "Quantidade_hospedes preservada"
    assert hotel2.quartos[0].status == "desocupado", "Status preservado"
    print("✓ OK - todos os dados integros e com campos corretos do PDF")
    
    # Limpa arquivo de teste
    import os
    if os.path.exists('data/teste_hotel.json'):
        os.remove('data/teste_hotel.json')
    
    print("\n" + "=" * 60)
    print("✓✓✓ TODOS OS TESTES DE PERSISTENCIA PASSARAM! (3/3)")
    print("=" * 60)

def teste_validacoes_restricoes():
    """Testa TODAS as validacoes e restricoes mencionadas no PDF"""
    print("\n" + "=" * 60)
    print("TESTANDO VALIDACOES E RESTRICOES DO PDF")
    print("=" * 60)
    
    hotel = Hotel("Hotel Teste")
    cliente = hotel.cadastrar_cliente("Cliente Teste", "End", "31999999999")
    hotel.adicionar_quarto(101, "Simples", 1, 150.00)
    
    # TESTE 1: Cliente deve existir para criar estadia
    print("\n1. Validando: cliente deve existir para criar estadia...")
    entrada = date.today() + timedelta(days=1)
    saida = entrada + timedelta(days=2)
    estadia_invalida = hotel.cadastrar_estadia(999, 1, entrada, saida)
    assert estadia_invalida is None, "Nao deve criar estadia sem cliente"
    print("✓ OK - nao permite estadia sem cliente cadastrado")
    
    # TESTE 2: Quarto deve existir para criar estadia (modo manual)
    print("\n2. Validando: quarto deve existir...")
    estadia_invalida = hotel.fazer_estadia(cliente.codigo, 999, entrada, saida)
    assert estadia_invalida is None, "Nao deve criar estadia sem quarto"
    print("✓ OK - nao permite estadia sem quarto cadastrado")
    
    # TESTE 3: Status do quarto: apenas ocupado e desocupado
    print("\n3. Validando: status conforme PDF (ocupado/desocupado)...")
    q = hotel.quartos[0]
    assert q.status in ["ocupado", "desocupado"], "Status deve ser ocupado ou desocupado"
    print("✓ OK - apenas 2 status possiveis conforme PDF")
    
    print("\n" + "=" * 60)
    print("✓✓✓ TODOS OS TESTES DE VALIDACOES PASSARAM! (3/3)")
    print("=" * 60)

def main():
    """Executa TODA a bateria de testes"""
    print("\n" + "=" * 80)
    print("  BATERIA COMPLETA DE TESTES DO SISTEMA")
    print("  Validando conformidade com especificacao do PDF")
    print("  Apropriado para primeiro periodo de AED")
    print("=" * 80)
    
    inicio_geral = time.time()
    
    teste_clientes()              # 6 testes
    teste_funcionarios()          # 6 testes
    teste_quartos()               # 8 testes
    teste_estadias()              # 10 testes
    teste_pontos_fidelidade()     # 4 testes
    teste_pesquisas()             # 6 testes
    teste_relatorios()            # 2 testes
    teste_persistencia()          # 3 testes
    teste_validacoes_restricoes() # 3 testes
    
    tempo_total = time.time() - inicio_geral
    total_testes = 6 + 6 + 8 + 10 + 4 + 6 + 2 + 3 + 3
    
    print("\n" + "=" * 80)
    print(f"  ✓✓✓ SUCESSO TOTAL! {total_testes}/48 TESTES PASSARAM! ✓✓✓")
    print(f"  Sistema 100% conforme especificacao PDF")
    print(f"  Tempo total de execucao: {tempo_total:.3f}s")
    print(f"  Media por teste: {(tempo_total/total_testes)*1000:.1f}ms")
    print("=" * 80)

if __name__ == "__main__":
    main()

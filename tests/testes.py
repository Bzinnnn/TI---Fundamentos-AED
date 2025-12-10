# testes_unittest.py - BATERIA DE TESTES
# Conforme especificacao do PDF - Adequado para primeiro periodo
# Usando unittest (biblioteca padrao do Python)

from datetime import date, timedelta
import sys
import os
import unittest

# Adiciona o diretorio raiz ao path para importar os modulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.hotel import Hotel
from src.models.cliente import Cliente
from src.models.funcionario import Funcionario
from src.models.quarto import Quarto
from src.models.estadia import Estadia


class TestClientes(unittest.TestCase):
    """Testa TODAS as funcionalidades relacionadas a clientes (6 testes)"""
    
    def setUp(self):
        """Executado antes de cada teste"""
        self.hotel = Hotel("Hotel Teste")
    
    def test_01_cadastrar_clientes_codigo_auto_gerado(self):
        """TC-CLI-001: Cadastrar clientes com codigo auto-gerado"""
        c1 = self.hotel.cadastrar_cliente("Maria Silva", "Rua A, 123", "31999991111")
        c2 = self.hotel.cadastrar_cliente("João Santos", "Av B, 456", "31988882222")
        c3 = self.hotel.cadastrar_cliente("Ana Costa", "Praca C, 789", "31977773333")
        
        self.assertEqual(c1.codigo, 1, "Codigo do primeiro cliente deve ser 1")
        self.assertEqual(c2.codigo, 2, "Codigo do segundo cliente deve ser 2")
        self.assertEqual(c3.codigo, 3, "Codigo do terceiro cliente deve ser 3")
    
    def test_02_validar_unicidade_codigos(self):
        """TC-CLI-002: Validar que nao ha codigos duplicados"""
        self.hotel.cadastrar_cliente("Maria Silva", "Rua A, 123", "31999991111")
        self.hotel.cadastrar_cliente("João Santos", "Av B, 456", "31988882222")
        self.hotel.cadastrar_cliente("Ana Costa", "Praca C, 789", "31977773333")
        
        codigos = [c.codigo for c in self.hotel.clientes]
        self.assertEqual(len(codigos), len(set(codigos)), "Nao deve haver codigos duplicados")
    
    def test_03_buscar_cliente_por_codigo(self):
        """TC-CLI-003: Buscar cliente por codigo existente"""
        c1 = self.hotel.cadastrar_cliente("Maria Silva", "Rua A, 123", "31999991111")
        
        cliente = self.hotel.buscar_cliente_por_codigo(c1.codigo)
        self.assertIsNotNone(cliente, "Deve encontrar cliente")
        self.assertEqual(cliente.nome, "Maria Silva", "Nome deve corresponder")
        self.assertEqual(cliente.codigo, c1.codigo, "Codigo deve corresponder")
    
    def test_04_pesquisar_por_nome_parcial(self):
        """TC-CLI-004: Pesquisar por nome parcial"""
        self.hotel.cadastrar_cliente("Maria Silva", "Rua A, 123", "31999991111")
        self.hotel.cadastrar_cliente("João Santos", "Av B, 456", "31988882222")
        
        resultado = self.hotel.pesquisar_cliente("Maria")
        self.assertEqual(len(resultado), 1, "Deve encontrar 1 cliente")
        self.assertEqual(resultado[0].nome, "Maria Silva", "Deve ser Maria Silva")
    
    def test_05_listar_todos_clientes(self):
        """TC-CLI-005: Listar todos os clientes"""
        self.hotel.cadastrar_cliente("Maria Silva", "Rua A, 123", "31999991111")
        self.hotel.cadastrar_cliente("João Santos", "Av B, 456", "31988882222")
        self.hotel.cadastrar_cliente("Ana Costa", "Praca C, 789", "31977773333")
        
        todos = self.hotel.listar_clientes()
        self.assertEqual(len(todos), 3, "Deve ter 3 clientes")
    
    def test_06_validar_estrutura_cliente(self):
        """TC-CLI-006: Validar estrutura do cliente conforme PDF"""
        c1 = self.hotel.cadastrar_cliente("Maria Silva", "Rua A, 123", "31999991111")
        
        self.assertTrue(hasattr(c1, 'codigo'), "Cliente deve ter codigo")
        self.assertTrue(hasattr(c1, 'nome'), "Cliente deve ter nome")
        self.assertTrue(hasattr(c1, 'endereco'), "Cliente deve ter endereco")
        self.assertTrue(hasattr(c1, 'telefone'), "Cliente deve ter telefone")


class TestFuncionarios(unittest.TestCase):
    """Testa TODAS as funcionalidades relacionadas a funcionarios (6 testes)"""
    
    def setUp(self):
        """Executado antes de cada teste"""
        self.hotel = Hotel("Hotel Teste")
    
    def test_01_cadastrar_funcionarios_codigo_auto_gerado(self):
        """TC-FUNC-001: Cadastrar funcionarios com codigo auto-gerado"""
        f1 = self.hotel.cadastrar_funcionario("Ana Costa", "31977773333", "Recepcionista", 2500.00)
        f2 = self.hotel.cadastrar_funcionario("Carlos Souza", "31966664444", "Gerente", 5000.00)
        f3 = self.hotel.cadastrar_funcionario("Maria Lima", "31955555555", "Auxiliar de limpeza", 1800.00)
        f4 = self.hotel.cadastrar_funcionario("Jose Silva", "31944446666", "Garçom", 2000.00)
        
        self.assertEqual(f1.codigo, 1, "Primeiro funcionario codigo 1")
        self.assertEqual(f2.codigo, 2, "Segundo funcionario codigo 2")
        self.assertEqual(f3.codigo, 3, "Terceiro funcionario codigo 3")
        self.assertEqual(f4.codigo, 4, "Quarto funcionario codigo 4")
    
    def test_02_validar_unicidade_codigos_funcionarios(self):
        """TC-FUNC-002: Validar unicidade de codigos"""
        self.hotel.cadastrar_funcionario("Ana Costa", "31977773333", "Recepcionista", 2500.00)
        self.hotel.cadastrar_funcionario("Carlos Souza", "31966664444", "Gerente", 5000.00)
        
        codigos = [f.codigo for f in self.hotel.funcionarios]
        self.assertEqual(len(codigos), len(set(codigos)), "Nao deve haver codigos duplicados")
    
    def test_03_buscar_funcionario_por_codigo(self):
        """TC-FUNC-003: Buscar funcionario por codigo"""
        f1 = self.hotel.cadastrar_funcionario("Ana Costa", "31977773333", "Recepcionista", 2500.00)
        
        func = self.hotel.buscar_funcionario_por_codigo(f1.codigo)
        self.assertIsNotNone(func, "Deve encontrar")
        self.assertEqual(func.cargo, "Recepcionista", "Cargo deve corresponder")
        self.assertEqual(func.salario, 2500.00, "Salario deve corresponder")
    
    def test_04_buscar_funcionario_inexistente(self):
        """TC-FUNC-004: Buscar funcionario inexistente"""
        func = self.hotel.buscar_funcionario_por_codigo(999)
        self.assertIsNone(func, "Deve retornar None")
    
    def test_05_pesquisar_por_nome(self):
        """TC-FUNC-005: Pesquisar funcionario por nome"""
        self.hotel.cadastrar_funcionario("Carlos Souza", "31966664444", "Gerente", 5000.00)
        
        resultado = self.hotel.pesquisar_funcionario("Carlos")
        self.assertGreaterEqual(len(resultado), 1, "Deve encontrar Carlos")
    
    def test_06_validar_estrutura_conforme_pdf(self):
        """TC-FUNC-006: Validar estrutura conforme PDF"""
        f1 = self.hotel.cadastrar_funcionario("Ana Costa", "31977773333", "Recepcionista", 2500.00)
        
        self.assertTrue(hasattr(f1, 'codigo'), "Deve ter codigo")
        self.assertTrue(hasattr(f1, 'nome'), "Deve ter nome")
        self.assertTrue(hasattr(f1, 'telefone'), "Deve ter telefone")
        self.assertTrue(hasattr(f1, 'cargo'), "Deve ter cargo")
        self.assertTrue(hasattr(f1, 'salario'), "Deve ter salario")


class TestQuartos(unittest.TestCase):
    """Testa TODAS as funcionalidades relacionadas a quartos (8 testes)"""
    
    def setUp(self):
        """Executado antes de cada teste"""
        self.hotel = Hotel("Hotel Teste")
    
    def test_01_adicionar_quartos(self):
        """TC-QTO-001: Adicionar quartos com sucesso"""
        self.assertTrue(self.hotel.adicionar_quarto(101, "Simples", 1, 150.00))
        self.assertTrue(self.hotel.adicionar_quarto(102, "Duplo", 2, 250.00))
        self.assertTrue(self.hotel.adicionar_quarto(201, "Suíte", 4, 500.00))
        self.assertTrue(self.hotel.adicionar_quarto(202, "Simples", 1, 150.00))
        self.assertEqual(len(self.hotel.quartos), 4, "Deve ter 4 quartos")
    
    def test_02_prevenir_numero_duplicado(self):
        """TC-QTO-002: Prevenir numero duplicado"""
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        self.assertFalse(self.hotel.adicionar_quarto(101, "Simples", 1, 150.00))
    
    def test_03_buscar_quarto_por_numero(self):
        """TC-QTO-003: Buscar quarto por numero"""
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        
        quarto = self.hotel.buscar_quarto_por_numero(101)
        self.assertIsNotNone(quarto, "Deve encontrar quarto")
        self.assertEqual(quarto.numero, 101, "Numero deve corresponder")
    
    def test_04_validar_estrutura_conforme_pdf(self):
        """TC-QTO-004: Validar estrutura do quarto conforme PDF"""
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        q = self.hotel.quartos[0]
        
        self.assertTrue(hasattr(q, 'numero'), "Deve ter numero")
        self.assertTrue(hasattr(q, 'quantidade_hospedes'), "Deve ter quantidade_hospedes")
        self.assertTrue(hasattr(q, 'preco_diaria'), "Deve ter preco_diaria")
        self.assertTrue(hasattr(q, 'status'), "Deve ter status")
    
    def test_05_validar_status_inicial(self):
        """TC-QTO-005: Validar status inicial"""
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        q = self.hotel.quartos[0]
        self.assertEqual(q.status, "Disponível", "Status inicial deve ser Disponível")
    
    def test_06_testar_mudanca_status(self):
        """TC-QTO-006: Testar mudanca de status"""
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        q = self.hotel.quartos[0]
        
        self.assertTrue(q.marcar_ocupado(), "Deve marcar como ocupado")
        self.assertEqual(q.status, "Ocupado", "Status deve ser Ocupado")
        
        q.marcar_desocupado()
        self.assertEqual(q.status, "Disponível", "Status deve voltar a Disponível")
    
    def test_07_listar_quartos_disponiveis(self):
        """TC-QTO-007: Listar quartos disponiveis"""
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        self.hotel.adicionar_quarto(102, "Duplo", 2, 250.00)
        self.hotel.adicionar_quarto(201, "Suíte", 4, 500.00)
        self.hotel.adicionar_quarto(202, "Simples", 1, 150.00)
        
        disponiveis = self.hotel.listar_quartos_disponiveis()
        self.assertEqual(len(disponiveis), 4, "Todos devem estar disponiveis")
    
    def test_08_testar_quantidade_hospedes(self):
        """TC-QTO-008: Validar campo quantidade_hospedes"""
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        q = self.hotel.quartos[0]
        
        self.assertEqual(q.quantidade_hospedes, 1, "Quantidade deve ser 1")
        self.assertIsInstance(q.quantidade_hospedes, int, "Deve ser inteiro")


class TestEstadias(unittest.TestCase):
    """Testa TODAS as funcionalidades relacionadas a estadias (10 testes)"""
    
    def setUp(self):
        """Executado antes de cada teste"""
        self.hotel = Hotel("Hotel Teste")
        self.cliente1 = self.hotel.cadastrar_cliente("Teste Cliente", "End Teste", "31999999999")
        self.cliente2 = self.hotel.cadastrar_cliente("Outro Cliente", "End 2", "31988888888")
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        self.hotel.adicionar_quarto(102, "Duplo", 2, 250.00)
        self.hotel.adicionar_quarto(201, "Suíte", 4, 500.00)
        self.hotel.adicionar_quarto(202, "Simples", 1, 150.00)
    
    def test_01_cadastrar_estadia_com_busca_automatica(self):
        """TC-EST-001: Cadastrar estadia COM BUSCA AUTOMATICA"""
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        estadia = self.hotel.cadastrar_estadia(self.cliente1.codigo, 1, entrada, saida)
        
        self.assertIsNotNone(estadia, "Deve criar estadia")
        self.assertEqual(estadia.quantidade_diarias, 2, "Deve ter 2 diarias")
        self.assertGreaterEqual(estadia.quarto.quantidade_hospedes, 1, "Quarto deve ter capacidade suficiente")
    
    def test_02_validar_estrutura_estadia_conforme_pdf(self):
        """TC-EST-002: Validar estrutura da estadia conforme PDF"""
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        estadia = self.hotel.cadastrar_estadia(self.cliente1.codigo, 1, entrada, saida)
        
        self.assertTrue(hasattr(estadia, 'codigo'), "Deve ter codigo")
        self.assertTrue(hasattr(estadia, 'data_entrada'), "Deve ter data_entrada")
        self.assertTrue(hasattr(estadia, 'data_saida'), "Deve ter data_saida")
        self.assertTrue(hasattr(estadia, 'quantidade_diarias'), "Deve ter quantidade_diarias")
        self.assertTrue(hasattr(estadia, 'codigo_cliente'), "Deve ter codigo_cliente")
        self.assertTrue(hasattr(estadia, 'quarto'), "Deve ter referencia ao quarto")
    
    def test_03_validar_calculo_diarias(self):
        """TC-EST-003: Validar calculo de diarias"""
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        estadia = self.hotel.cadastrar_estadia(self.cliente1.codigo, 1, entrada, saida)
        
        self.assertEqual(estadia.quantidade_diarias, (saida - entrada).days, "Calculo deve estar correto")
    
    def test_04_validar_calculo_valor_total(self):
        """TC-EST-004: Validar calculo de valor total"""
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        estadia = self.hotel.cadastrar_estadia(self.cliente1.codigo, 1, entrada, saida)
        
        valor_esperado = estadia.quantidade_diarias * estadia.quarto.preco_diaria
        self.assertEqual(estadia.valor_total, valor_esperado, "Valor deve estar correto")
    
    def test_05_validar_cliente_deve_existir(self):
        """TC-EST-005: Cliente deve existir"""
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        estadia_invalida = self.hotel.cadastrar_estadia(999, 1, entrada, saida)
        
        self.assertIsNone(estadia_invalida, "Nao deve criar estadia com cliente inexistente")
    
    def test_06_validar_quarto_disponivel(self):
        """TC-EST-006: Quarto deve estar disponivel"""
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        estadia = self.hotel.cadastrar_estadia(self.cliente1.codigo, 1, entrada, saida)
        
        entrada2 = date.today() + timedelta(days=1)
        saida2 = entrada2 + timedelta(days=2)
        estadia2 = self.hotel.fazer_estadia(self.cliente2.codigo, estadia.quarto.numero, entrada2, saida2)
        
        self.assertIsNone(estadia2, "Nao deve permitir conflito de datas")
    
    def test_07_testar_cancelamento_estadia(self):
        """TC-EST-007: Testar cancelamento de estadia"""
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        estadia = self.hotel.cadastrar_estadia(self.cliente1.codigo, 1, entrada, saida)
        
        self.assertTrue(self.hotel.cancelar_estadia(estadia.codigo), "Deve cancelar")
        self.assertEqual(estadia.status, "Cancelada", "Status deve ser Cancelada")
        self.assertEqual(estadia.quarto.status, "Disponível", "Quarto deve voltar a Disponível")
    
    def test_08_testar_checkin(self):
        """TC-EST-008: Testar check-in"""
        entrada3 = date.today() - timedelta(days=1)
        saida3 = entrada3 + timedelta(days=3)
        estadia3 = self.hotel.fazer_estadia(self.cliente2.codigo, 102, entrada3, saida3)
        
        self.assertTrue(self.hotel.fazer_checkin(estadia3.codigo), "Check-in deve funcionar")
        self.assertEqual(estadia3.quarto.status, "Ocupado", "Quarto deve ficar Ocupado")
    
    def test_09_testar_checkout(self):
        """TC-EST-009: Testar checkout conforme PDF"""
        entrada = date.today() - timedelta(days=1)
        saida = entrada + timedelta(days=3)
        estadia = self.hotel.fazer_estadia(self.cliente2.codigo, 102, entrada, saida)
        self.hotel.fazer_checkin(estadia.codigo)
        
        sucesso, resultado = self.hotel.fazer_checkout(estadia.codigo)
        self.assertTrue(sucesso, f"Checkout deve funcionar: {resultado}")
        self.assertEqual(estadia.status, "Concluida", "Status deve ser Concluida")
        self.assertEqual(estadia.quarto.status, "Disponível", "Quarto deve voltar a Disponível")
    
    def test_10_busca_automatica_por_quantidade_hospedes(self):
        """TC-EST-010: Busca automatica por quantidade_hospedes"""
        entrada4 = date.today() + timedelta(days=20)
        saida4 = entrada4 + timedelta(days=1)
        estadia4 = self.hotel.cadastrar_estadia(self.cliente1.codigo, 4, entrada4, saida4)
        
        self.assertIsNotNone(estadia4, "Deve encontrar quarto")
        self.assertGreaterEqual(estadia4.quarto.quantidade_hospedes, 4, "Quarto deve ter capacidade >= 4")


class TestPontosFidelidade(unittest.TestCase):
    """Testa funcao 8 do PDF: pontos de fidelidade (4 testes)"""
    
    def setUp(self):
        """Executado antes de cada teste"""
        self.hotel = Hotel("Hotel Teste")
        self.cliente = self.hotel.cadastrar_cliente("Cliente Fiel", "End", "31999999999")
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        self.hotel.adicionar_quarto(102, "Duplo", 2, 250.00)
        self.hotel.adicionar_quarto(103, "Suite", 4, 500.00)
    
    def test_01_cliente_sem_estadias_zero_pontos(self):
        """TC-PTS-001: Cliente sem estadias = 0 pontos"""
        estadias = self.hotel.listar_estadias_por_cliente(self.cliente.codigo)
        pontos = self.cliente.calcular_pontos_fidelidade(estadias)
        self.assertEqual(pontos, 0, "Cliente sem estadias deve ter 0 pontos")
    
    def test_02_cliente_com_uma_estadia(self):
        """TC-PTS-002: Cliente com 1 estadia"""
        entrada1 = date.today() + timedelta(days=1)
        saida1 = entrada1 + timedelta(days=3)
        self.hotel.fazer_estadia(self.cliente.codigo, 101, entrada1, saida1)
        
        estadias = self.hotel.listar_estadias_por_cliente(self.cliente.codigo)
        pontos = self.cliente.calcular_pontos_fidelidade(estadias)
        self.assertEqual(pontos, 30, "3 diarias x 10 = 30 pontos")
    
    def test_03_cliente_com_multiplas_estadias(self):
        """TC-PTS-003: Cliente com multiplas estadias"""
        entrada1 = date.today() + timedelta(days=1)
        saida1 = entrada1 + timedelta(days=3)
        self.hotel.fazer_estadia(self.cliente.codigo, 101, entrada1, saida1)
        
        entrada2 = date.today() + timedelta(days=10)
        saida2 = entrada2 + timedelta(days=5)
        self.hotel.fazer_estadia(self.cliente.codigo, 102, entrada2, saida2)
        
        entrada3 = date.today() + timedelta(days=20)
        saida3 = entrada3 + timedelta(days=2)
        self.hotel.fazer_estadia(self.cliente.codigo, 103, entrada3, saida3)
        
        estadias = self.hotel.listar_estadias_por_cliente(self.cliente.codigo)
        pontos = self.cliente.calcular_pontos_fidelidade(estadias)
        self.assertEqual(pontos, 100, "10 diarias totais x 10 = 100 pontos")
    
    def test_04_validar_regra_10_pontos_por_diaria(self):
        """TC-PTS-004: Validar regra: 10 pontos por diaria"""
        entrada1 = date.today() + timedelta(days=1)
        saida1 = entrada1 + timedelta(days=3)
        self.hotel.fazer_estadia(self.cliente.codigo, 101, entrada1, saida1)
        
        entrada2 = date.today() + timedelta(days=10)
        saida2 = entrada2 + timedelta(days=5)
        self.hotel.fazer_estadia(self.cliente.codigo, 102, entrada2, saida2)
        
        estadias = self.hotel.listar_estadias_por_cliente(self.cliente.codigo)
        pontos = self.cliente.calcular_pontos_fidelidade(estadias)
        total_diarias = sum(e.quantidade_diarias for e in estadias if e.codigo_cliente == self.cliente.codigo)
        pontos_esperados = total_diarias * 10
        
        self.assertEqual(pontos, pontos_esperados, "Deve ser 10 pontos por diaria")


class TestPesquisas(unittest.TestCase):
    """Testa funcao 6 e 7 do PDF: pesquisas (6 testes)"""
    
    def setUp(self):
        """Executado antes de cada teste"""
        self.hotel = Hotel("Hotel Teste")
        self.c1 = self.hotel.cadastrar_cliente("Maria Silva", "Rua A", "31999991111")
        self.c2 = self.hotel.cadastrar_cliente("João Silva", "Rua B", "31988882222")
        self.c3 = self.hotel.cadastrar_cliente("Ana Costa", "Rua C", "31977773333")
        self.f1 = self.hotel.cadastrar_funcionario("Carlos Santos", "31966664444", "Gerente", 5000.00)
        self.f2 = self.hotel.cadastrar_funcionario("Julia Lima", "31955555555", "Recepcionista", 2500.00)
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        self.hotel.adicionar_quarto(102, "Duplo", 2, 250.00)
    
    def test_01_pesquisar_cliente_por_nome(self):
        """TC-PESQ-001: Pesquisar cliente por nome"""
        resultado = self.hotel.pesquisar_cliente("Maria")
        self.assertEqual(len(resultado), 1, "Deve encontrar Maria")
        self.assertEqual(resultado[0].nome, "Maria Silva", "Deve ser Maria Silva")
    
    def test_02_pesquisar_cliente_por_codigo(self):
        """TC-PESQ-002: Pesquisar cliente por codigo"""
        resultado = self.hotel.pesquisar_cliente(str(self.c2.codigo))
        self.assertEqual(len(resultado), 1, "Deve encontrar 1")
        self.assertEqual(resultado[0].codigo, self.c2.codigo, "Codigo deve corresponder")
    
    def test_03_pesquisar_cliente_por_nome_parcial(self):
        """TC-PESQ-003: Pesquisar cliente por nome parcial"""
        resultado = self.hotel.pesquisar_cliente("Silva")
        self.assertEqual(len(resultado), 2, "Deve encontrar 2 (Maria e Joao Silva)")
    
    def test_04_pesquisar_funcionario_por_nome(self):
        """TC-PESQ-004: Pesquisar funcionario por nome"""
        resultado = self.hotel.pesquisar_funcionario("Carlos")
        self.assertEqual(len(resultado), 1, "Deve encontrar Carlos")
        self.assertEqual(resultado[0].nome, "Carlos Santos", "Deve ser Carlos Santos")
    
    def test_05_pesquisar_funcionario_por_codigo(self):
        """TC-PESQ-005: Pesquisar funcionario por codigo"""
        resultado = self.hotel.pesquisar_funcionario(str(self.f1.codigo))
        self.assertEqual(len(resultado), 1, "Deve encontrar 1")
        self.assertEqual(resultado[0].codigo, self.f1.codigo, "Codigo deve corresponder")
    
    def test_06_listar_estadias_de_cliente(self):
        """TC-PESQ-006: Listar estadias de um cliente"""
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        self.hotel.fazer_estadia(self.c1.codigo, 101, entrada, saida)
        
        entrada2 = date.today() + timedelta(days=10)
        saida2 = entrada2 + timedelta(days=3)
        self.hotel.fazer_estadia(self.c1.codigo, 102, entrada2, saida2)
        
        estadias_maria = self.hotel.listar_estadias_por_cliente(self.c1.codigo)
        self.assertEqual(len(estadias_maria), 2, "Maria deve ter 2 estadias")
        self.assertTrue(all(e.codigo_cliente == self.c1.codigo for e in estadias_maria), "Todas devem ser da Maria")


class TestRelatorios(unittest.TestCase):
    """Testa funcionalidades de relatorios (2 testes)"""
    
    def setUp(self):
        """Executado antes de cada teste"""
        self.hotel = Hotel("Hotel Teste")
        self.cliente = self.hotel.cadastrar_cliente("Teste", "End", "31999999999")
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        self.hotel.adicionar_quarto(102, "Duplo", 2, 250.00)
        self.hotel.adicionar_quarto(103, "Suite", 4, 500.00)
    
    def test_01_relatorio_ocupacao(self):
        """TC-REL-001: Relatorio de ocupacao"""
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        estadia = self.hotel.fazer_estadia(self.cliente.codigo, 101, entrada, saida)
        self.hotel.fazer_checkin(estadia.codigo)
        
        rel = self.hotel.relatorio_ocupacao()
        self.assertEqual(rel['total_quartos'], 3, "Total deve ser 3")
        self.assertEqual(rel['quartos_ocupados'], 1, "Ocupados deve ser 1")
        taxa_esperada = (1 / 3) * 100
        self.assertAlmostEqual(rel['taxa_ocupacao'], taxa_esperada, places=2, msg="Taxa deve estar correta")
    
    def test_02_relatorio_receita(self):
        """TC-REL-002: Relatorio de receita"""
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        estadia = self.hotel.fazer_estadia(self.cliente.codigo, 101, entrada, saida)
        self.hotel.fazer_checkin(estadia.codigo)
        
        rel = self.hotel.relatorio_receita()
        self.assertEqual(rel['receita_total'], 300.00, "Receita deve ser 300")
        self.assertEqual(rel['receita_pendente'], 300.00, "Pendente deve ser 300")


class TestPersistencia(unittest.TestCase):
    """Testa salvamento e carregamento de dados (3 testes)"""
    
    def test_01_salvar_dados(self):
        """TC-PERS-001: Salvar dados"""
        hotel1 = Hotel("Hotel Teste")
        cliente = hotel1.cadastrar_cliente("Maria", "Rua X", "31999999999")
        hotel1.cadastrar_funcionario("Ana", "31988888888", "Recepcionista", 2500.00)
        hotel1.adicionar_quarto(101, "Simples", 1, 150.00)
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        hotel1.fazer_estadia(cliente.codigo, 101, entrada, saida)
        
        self.assertTrue(hotel1.salvar_dados('data/teste_hotel.json'))
    
    def test_02_carregar_dados(self):
        """TC-PERS-002: Carregar dados"""
        hotel1 = Hotel("Hotel Teste")
        cliente = hotel1.cadastrar_cliente("Maria", "Rua X", "31999999999")
        hotel1.cadastrar_funcionario("Ana", "31988888888", "Recepcionista", 2500.00)
        hotel1.adicionar_quarto(101, "Simples", 1, 150.00)
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        hotel1.fazer_estadia(cliente.codigo, 101, entrada, saida)
        hotel1.salvar_dados('data/teste_hotel.json')
        
        hotel2 = Hotel("Vazio")
        self.assertTrue(hotel2.carregar_dados('data/teste_hotel.json'))
    
    def test_03_verificar_integridade_dados(self):
        """TC-PERS-003: Verificar integridade dos dados"""
        hotel1 = Hotel("Hotel Teste")
        cliente = hotel1.cadastrar_cliente("Maria", "Rua X", "31999999999")
        hotel1.cadastrar_funcionario("Ana", "31988888888", "Recepcionista", 2500.00)
        hotel1.adicionar_quarto(101, "Simples", 1, 150.00)
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        hotel1.fazer_estadia(cliente.codigo, 101, entrada, saida)
        hotel1.salvar_dados('data/teste_hotel.json')
        
        hotel2 = Hotel("Vazio")
        hotel2.carregar_dados('data/teste_hotel.json')
        
        self.assertEqual(len(hotel2.clientes), 1, "Deve ter 1 cliente")
        self.assertEqual(len(hotel2.funcionarios), 1, "Deve ter 1 funcionario")
        self.assertEqual(len(hotel2.quartos), 1, "Deve ter 1 quarto")
        self.assertEqual(len(hotel2.estadias), 1, "Deve ter 1 estadia")
        self.assertEqual(hotel2.clientes[0].nome, "Maria", "Nome deve ser preservado")
        self.assertEqual(hotel2.quartos[0].quantidade_hospedes, 1, "Quantidade_hospedes preservada")
        self.assertEqual(hotel2.quartos[0].status, "Disponível", "Status preservado")
        
        # Limpa arquivo de teste
        if os.path.exists('data/teste_hotel.json'):
            os.remove('data/teste_hotel.json')


class TestValidacoesRestricoes(unittest.TestCase):
    """Testa TODAS as validacoes e restricoes mencionadas no PDF (3 testes)"""
    
    def setUp(self):
        """Executado antes de cada teste"""
        self.hotel = Hotel("Hotel Teste")
        self.cliente = self.hotel.cadastrar_cliente("Cliente Teste", "End", "31999999999")
        self.hotel.adicionar_quarto(101, "Simples", 1, 150.00)
    
    def test_01_cliente_deve_existir_para_criar_estadia(self):
        """TC-VAL-001: Cliente deve existir para criar estadia"""
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        estadia_invalida = self.hotel.cadastrar_estadia(999, 1, entrada, saida)
        
        self.assertIsNone(estadia_invalida, "Nao deve criar estadia sem cliente")
    
    def test_02_quarto_deve_existir(self):
        """TC-VAL-002: Quarto deve existir"""
        entrada = date.today() + timedelta(days=1)
        saida = entrada + timedelta(days=2)
        estadia_invalida = self.hotel.fazer_estadia(self.cliente.codigo, 999, entrada, saida)
        
        self.assertIsNone(estadia_invalida, "Nao deve criar estadia sem quarto")
    
    def test_03_status_do_quarto_conforme_pdf(self):
        """TC-VAL-003: Status do quarto conforme PDF"""
        q = self.hotel.quartos[0]
        self.assertIn(q.status, ["Ocupado", "Disponível", "Manutenção"], "Status deve ser Ocupado, Disponível ou Manutenção")


if __name__ == '__main__':
    # Configurar o runner do unittest para mostrar mais detalhes
    unittest.main(verbosity=2)

# hotel_novo.py - classe principal atualizada

from datetime import date, datetime
from .quarto import Quarto
from .estadia import Estadia
from .cliente import Cliente
from .funcionario import Funcionario
import pickle
import os

class Hotel:
    """gerencia quartos, estadias, clientes e funcionarios"""
    
    def __init__(self, nome="Hotel Descanso Garantido"):
        self.nome = nome
        self.quartos = []
        self.estadias = []
        self.clientes = []
        self.funcionarios = []
    
    # --- clientes ---
    
    def cadastrar_cliente(self, nome, endereco, telefone):
        cliente = Cliente(nome, endereco, telefone)
        self.clientes.append(cliente)
        return cliente
    
    def buscar_cliente_por_codigo(self, codigo):
        for c in self.clientes:
            if c.codigo == codigo:
                return c
        return None
    
    def pesquisar_cliente(self, termo):
        """pesquisa por nome ou codigo"""
        resultado = []
        # tenta converter pra codigo
        try:
            codigo = int(termo)
            cliente = self.buscar_cliente_por_codigo(codigo)
            if cliente:
                return [cliente]
        except:
            pass
        
        # busca por nome
        termo_lower = termo.lower()
        for cliente in self.clientes:
            if termo_lower in cliente.nome.lower():
                resultado.append(cliente)
        return resultado
    
    def listar_clientes(self):
        return self.clientes
    
    def remover_cliente(self, codigo):
        """Remove um cliente se ele não tiver estadias ativas"""
        cliente = self.buscar_cliente_por_codigo(codigo)
        if not cliente:
            return False, "Cliente não encontrado"
        
        # Verifica se tem estadias ativas
        estadias_ativas = [e for e in self.estadias if e.codigo_cliente == codigo and e.status in ["Confirmada", "ativa"]]
        if estadias_ativas:
            return False, f"Cliente possui {len(estadias_ativas)} estadia(s) ativa(s). Não é possível remover."
        
        # Remove o cliente
        self.clientes.remove(cliente)
        return True, "Cliente removido com sucesso"
    
    # --- funcionarios ---
    
    def cadastrar_funcionario(self, nome, telefone, cargo, salario):
        funcionario = Funcionario(nome, telefone, cargo, salario)
        self.funcionarios.append(funcionario)
        return funcionario
    
    def buscar_funcionario_por_codigo(self, codigo):
        for f in self.funcionarios:
            if f.codigo == codigo:
                return f
        return None
    
    def pesquisar_funcionario(self, termo):
        """pesquisa por nome ou codigo"""
        resultado = []
        try:
            codigo = int(termo)
            func = self.buscar_funcionario_por_codigo(codigo)
            if func:
                return [func]
        except:
            pass
        
        termo_lower = termo.lower()
        for func in self.funcionarios:
            if termo_lower in func.nome.lower():
                resultado.append(func)
        return resultado
    
    def listar_funcionarios(self):
        return self.funcionarios
    
    def remover_funcionario(self, codigo):
        """Remove um funcionário se ele não tiver estadias vinculadas"""
        funcionario = self.buscar_funcionario_por_codigo(codigo)
        if not funcionario:
            return False, "Funcionário não encontrado"
        
        # Verifica se tem estadias vinculadas
        estadias_vinculadas = [e for e in self.estadias if e.codigo_funcionario == codigo]
        if estadias_vinculadas:
            return False, f"Funcionário possui {len(estadias_vinculadas)} estadia(s) vinculada(s). Não é possível remover."
        
        # Remove o funcionário
        self.funcionarios.remove(funcionario)
        return True, "Funcionário removido com sucesso"
    
    # --- quartos ---
    
    def adicionar_quarto(self, numero, tipo, quantidade_hospedes, preco_diaria):
        if self.buscar_quarto_por_numero(numero):
            return False
        
        quarto = Quarto(numero, tipo, quantidade_hospedes, preco_diaria)
        self.quartos.append(quarto)
        return True
    
    def buscar_quarto_por_numero(self, numero):
        for q in self.quartos:
            if q.numero == numero:
                return q
        return None
    
    def listar_quartos(self):
        return self.quartos
    
    def listar_quartos_disponiveis(self):
        disponiveis = []
        for quarto in self.quartos:
            if quarto.status == "Disponível":
                disponiveis.append(quarto)
        return disponiveis
    
    def listar_quartos_ocupados(self):
        return [q for q in self.quartos if q.status == "Ocupado"]
    
    def remover_quarto(self, numero):
        """Remove um quarto se ele não tiver estadias vinculadas"""
        quarto = self.buscar_quarto_por_numero(numero)
        if not quarto:
            return False, "Quarto não encontrado"
        
        # Verifica se tem estadias vinculadas
        estadias_vinculadas = [e for e in self.estadias if e.quarto.numero == numero]
        if estadias_vinculadas:
            return False, f"Quarto possui {len(estadias_vinculadas)} estadia(s) vinculada(s). Não é possível remover."
        
        # Remove o quarto
        self.quartos.remove(quarto)
        return True, "Quarto removido com sucesso"
    
    def listar_quartos_por_tipo(self, tipo):
        resultado = []
        for q in self.quartos:
            if q.tipo == tipo:
                resultado.append(q)
        return resultado
    
    # --- estadias ---
    
    def cadastrar_estadia(self, codigo_cliente, quantidade_hospedes, data_entrada, data_saida):
        """
        CONFORME ITEM 4 DO PDF:
        Recebe codigo do cliente, quantidade de hospedes, datas
        e ENCONTRA AUTOMATICAMENTE um quarto disponivel
        """
        # valida cliente
        cliente = self.buscar_cliente_por_codigo(codigo_cliente)
        if not cliente:
            return None
        
        # valida datas
        if data_saida <= data_entrada:
            return None
        
        # BUSCA AUTOMATICAMENTE um quarto disponivel com capacidade suficiente
        quarto_disponivel = None
        for quarto in self.quartos:
            # verifica capacidade
            if quarto.quantidade_hospedes < quantidade_hospedes:
                continue
            
            # NÃO verifica status - verifica disponibilidade por período
            # (quarto pode estar em manutenção mas livre na data)
            if quarto.status == "Manutenção":
                continue
            
            # verifica disponibilidade no periodo
            if self.verificar_disponibilidade(quarto.numero, data_entrada, data_saida):
                quarto_disponivel = quarto
                break
        
        # se nao encontrou quarto disponivel
        if not quarto_disponivel:
            return None
        
        # cria estadia no quarto encontrado
        estadia = Estadia(codigo_cliente, quarto_disponivel, data_entrada, data_saida)
        estadia.confirmar()
        # NÃO marca como ocupado aqui - só no check-in
        self.estadias.append(estadia)
        return estadia
    
    def fazer_estadia(self, codigo_cliente, numero_quarto, data_entrada, data_saida):
        """
        Funcao ANTIGA mantida para compatibilidade com testes
        Permite escolher quarto manualmente
        """
        # valida cliente
        cliente = self.buscar_cliente_por_codigo(codigo_cliente)
        if not cliente:
            return None
        
        # valida quarto
        quarto = self.buscar_quarto_por_numero(numero_quarto)
        if not quarto:
            return None
        
        # Não verifica status - apenas disponibilidade por data
        if quarto.status == "Manutenção":
            return None
        
        # valida datas
        if data_saida <= data_entrada:
            return None
        
        # verifica disponibilidade
        if not self.verificar_disponibilidade(numero_quarto, data_entrada, data_saida):
            return None
        
        # cria estadia
        estadia = Estadia(codigo_cliente, quarto, data_entrada, data_saida)
        estadia.confirmar()
        self.estadias.append(estadia)
        return estadia
    
    def verificar_disponibilidade(self, numero_quarto, data_entrada, data_saida):
        """verifica se quarto ta livre no periodo - considera apenas estadias ativas"""
        for estadia in self.estadias:
            # Só considera estadias que não foram canceladas ou concluídas
            if estadia.quarto.numero == numero_quarto and estadia.status in ["Pendente", "Confirmada"]:
                # checa sobreposicao de datas
                if not (data_saida <= estadia.data_entrada or data_entrada >= estadia.data_saida):
                    return False
        return True
    
    def buscar_estadia_por_codigo(self, codigo):
        for e in self.estadias:
            if e.codigo == codigo:
                return e
        return None
    
    def cancelar_estadia(self, codigo):
        estadia = self.buscar_estadia_por_codigo(codigo)
        if estadia:
            return estadia.cancelar()
        return False
    
    def listar_estadias(self):
        return self.estadias
    
    def listar_estadias_ativas(self):
        return [e for e in self.estadias if e.status == "Confirmada"]
    
    def listar_estadias_por_cliente(self, codigo_cliente):
        resultado = []
        for estadia in self.estadias:
            if estadia.codigo_cliente == codigo_cliente:
                resultado.append(estadia)
        return resultado
    
    # --- checkin e checkout ---
    
    def fazer_checkin(self, codigo_estadia):
        estadia = self.buscar_estadia_por_codigo(codigo_estadia)
        if estadia and estadia.status == "Confirmada":
            return estadia.fazer_checkin()
        return False
    
    def fazer_checkout(self, codigo_estadia, data_checkout=None):
        """realiza checkout com validacao de data"""
        estadia = self.buscar_estadia_por_codigo(codigo_estadia)
        if not estadia or estadia.status != "Confirmada":
            return False, "Estadia não encontrada ou não está confirmada"
        
        # Se não informar data, usa a data atual
        if data_checkout is None:
            data_checkout = date.today()
        
        # validacao: checkout nao pode ser antes do checkin
        if data_checkout < estadia.data_entrada:
            return False, "Não é possível fazer checkout antes da data de entrada"
        
        # realiza checkout com a data informada
        sucesso = estadia.fazer_checkout(data_checkout)
        if sucesso:
            return True, estadia.valor_total
        return False, "Erro ao processar checkout"
    
    # --- relatorios ---
    
    def relatorio_ocupacao(self):
        total_quartos = len(self.quartos)
        quartos_disponiveis = len(self.listar_quartos_disponiveis())
        quartos_ocupados = len(self.listar_quartos_ocupados())
        quartos_manutencao = len([q for q in self.quartos if q.status == "Manutenção"])
        
        taxa_ocupacao = 0
        if total_quartos > 0:
            taxa_ocupacao = (quartos_ocupados / total_quartos) * 100
        
        return {
            'total_quartos': total_quartos,
            'quartos_disponiveis': quartos_disponiveis,
            'quartos_ocupados': quartos_ocupados,
            'quartos_manutencao': quartos_manutencao,
            'taxa_ocupacao': taxa_ocupacao
        }
    
    def relatorio_receita(self):
        receita_total = 0
        receita_concluida = 0
        receita_pendente = 0
        
        for estadia in self.estadias:
            if estadia.status == "Concluida":
                receita_concluida += estadia.valor_total
            elif estadia.status == "Confirmada":
                receita_pendente += estadia.valor_total
            
            if estadia.status in ["Confirmada", "Concluida"]:
                receita_total += estadia.valor_total
        
        return {
            'receita_total': receita_total,
            'receita_concluida': receita_concluida,
            'receita_pendente': receita_pendente,
            'total_estadias': len(self.estadias)
        }
    
    # --- persistencia ---
    
    def salvar_dados(self, arquivo='data/hotel_dados.bin'):
        """salva dados em arquivo binario usando pickle"""
        dados = {
            'nome': self.nome,
            'clientes': self.clientes,
            'funcionarios': self.funcionarios,
            'quartos': self.quartos,
            'estadias': self.estadias,
            'contadores': {
                'cliente': Cliente._contador_codigo,
                'funcionario': Funcionario._contador_codigo,
                'estadia': Estadia._contador_codigo
            }
        }
        
        # garante que diretorio existe
        os.makedirs(os.path.dirname(arquivo) if os.path.dirname(arquivo) else '.', exist_ok=True)
        
        with open(arquivo, 'wb') as f:
            pickle.dump(dados, f)
        
        return True
    
    def carregar_dados(self, arquivo='data/hotel_dados.bin'):
        """carrega dados de arquivo binario usando pickle"""
        if not os.path.exists(arquivo):
            return False
        
        try:
            with open(arquivo, 'rb') as f:
                dados = pickle.load(f)
            
            self.nome = dados.get('nome', self.nome)
            self.clientes = dados.get('clientes', [])
            self.funcionarios = dados.get('funcionarios', [])
            self.quartos = dados.get('quartos', [])
            self.estadias = dados.get('estadias', [])
            
            # restaura contadores
            contadores = dados.get('contadores', {})
            Cliente._contador_codigo = contadores.get('cliente', 1)
            Funcionario._contador_codigo = contadores.get('funcionario', 1)
            Estadia._contador_codigo = contadores.get('estadia', 1)
            
            return True
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return False

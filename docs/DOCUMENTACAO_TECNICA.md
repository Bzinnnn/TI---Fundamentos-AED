# 📘 Documentação Técnica - Sistema Hotel Descanso Garantido

> **Para usuários:** Veja o [README.md](../README.md) para instruções de uso  
> **Para desenvolvedores:** Continue lendo esta documentação técnica

---

## 🎯 Visão Geral

Sistema de gerenciamento hoteleiro desenvolvido em **Python 3.12** usando **Programação Orientada a Objetos**. 

**Características principais:**
- ✅ 100% Python puro (apenas bibliotecas padrão)
- ✅ Persistência automática de dados (pickle)
- ✅ Interface de console amigável
- ✅ 48 testes automatizados
- ✅ Validações robustas de entrada

---

## 🏗️ Arquitetura do Sistema

### Estrutura de Diretórios

```
TI---Fundamentos-AED/
│
├── main.py                      # Ponto de entrada do sistema
│
├── src/
│   ├── __init__.py
│   │
│   ├── models/                  # Camada de Modelo (Dados + Lógica)
│   │   ├── __init__.py
│   │   ├── hotel.py            # Classe principal (orquestra tudo)
│   │   ├── cliente.py          # Entidade Cliente
│   │   ├── funcionario.py      # Entidade Funcionário
│   │   ├── quarto.py           # Entidade Quarto
│   │   └── estadia.py          # Entidade Estadia
│   │
│   ├── ui/                      # Camada de Interface (View)
│   │   ├── __init__.py
│   │   └── menu.py             # Menus e navegação
│   │
│   └── utils/                   # Utilitários
│       ├── __init__.py
│       └── utils.py            # Funções auxiliares (validação, formatação)
│
├── data/                        # Dados persistidos
│   └── hotel_dados.bin         # Arquivo pickle com todos os dados
│
├── tests/                       # Testes automatizados
│   ├── __init__.py
│   └── testes.py               # 48 testes de unidade
│
└── docs/                        # Documentação
    ├── README.md               # Guia do usuário (movido para raiz)
    ├── DOCUMENTACAO_TECNICA.md # Este arquivo
    └── CASOS_DE_TESTE.md       # Especificação dos testes
```

---

## 🔄 Fluxo de Dados e Relacionamentos

### Diagrama de Classes Simplificado

```
┌─────────────────────────────────────────────────┐
│                    Hotel                        │
│  ─────────────────────────────────────────────  │
│  - nome: str                                    │
│  - clientes: List[Cliente]                      │
│  - funcionarios: List[Funcionario]              │
│  - quartos: List[Quarto]                        │
│  - estadias: List[Estadia]                      │
│  ─────────────────────────────────────────────  │
│  + cadastrar_cliente()                          │
│  + cadastrar_estadia()    (busca automática!)   │
│  + fazer_checkin()                              │
│  + fazer_checkout()                             │
│  + salvar_dados()                               │
│  + carregar_dados()                             │
└─────────────────────────────────────────────────┘
           │                │               │
           ▼                ▼               ▼
    ┌──────────┐    ┌─────────────┐  ┌──────────┐
    │ Cliente  │    │ Funcionário │  │  Quarto  │
    └──────────┘    └─────────────┘  └──────────┘
           │                                  │
           └─────────┐           ┌────────────┘
                     ▼           ▼
              ┌──────────────────────┐
              │      Estadia         │
              │  ──────────────────  │
              │  - codigo_cliente    │
              │  - quarto            │
              │  - data_entrada      │
              │  - data_saida        │
              │  - status            │
              └──────────────────────┘
```

---

## 📦 Detalhamento dos Módulos

### 1️⃣ `cliente.py` - Entidade Cliente

**Responsabilidade:** Representa um cliente do hotel com seus dados e pontos de fidelidade.

**Atributos:**
```python
- codigo: int              # Gerado automaticamente (1, 2, 3...)
- nome: str               # Nome completo
- endereco: str           # Endereço residencial
- telefone: str           # Telefone de contato
```

**Métodos principais:**
```python
calcular_pontos_fidelidade(estadias: List[Estadia]) -> int
    # Calcula: soma de (quantidade_diarias × 10) de todas estadias
    # Exemplo: 3 estadias com 2, 3 e 5 diárias = 100 pontos
```

**Código automático:**
- Usa variável de classe `_contador_codigo` 
- Incrementa automaticamente a cada novo cliente
- Preservado ao salvar/carregar dados

---

### 2️⃣ `funcionario.py` - Entidade Funcionário

**Responsabilidade:** Armazena dados dos funcionários do hotel.

**Atributos:**
```python
- codigo: int              # Gerado automaticamente
- nome: str               # Nome completo  
- telefone: str           # Telefone de contato
- cargo: str              # Ex: Recepcionista, Gerente, Garçom
- salario: float          # Valor do salário
```

**Cargos comuns no sistema:**
- Recepcionista (R$ 2.500,00)
- Gerente (R$ 5.000,00)
- Auxiliar de limpeza (R$ 1.800,00)
- Garçom (R$ 2.000,00)

---

### 3️⃣ `quarto.py` - Entidade Quarto

**Responsabilidade:** Representa um quarto físico do hotel com status e capacidade.

**Atributos:**
```python
- numero: int                    # Número único do quarto (101, 102, 201...)
- tipo: str                      # "Simples", "Duplo", "Suíte"
- quantidade_hospedes: int       # Capacidade máxima (1, 2, 4...)
- preco_diaria: float           # Valor por dia (150.00, 250.00, 500.00)
- status: str                    # "Disponível", "Ocupado", "Manutenção"
```

**Métodos de status:**
```python
marcar_ocupado() -> bool           # Marca quarto como "Ocupado"
marcar_desocupado()                # Volta para "Disponível"
marcar_disponivel()                # Alias para marcar_desocupado()
marcar_manutencao()                # Marca como "Manutenção"
esta_disponivel() -> bool          # Retorna True se status == "Disponível"
```

**Estados possíveis:**
- `"Disponível"` (inicial) → Pode ser reservado
- `"Ocupado"` → Com hóspede no momento
- `"Manutenção"` → Indisponível temporariamente

**Nota:** Campos usam **maiúsculas** (ex: "Disponível", não "disponível")

---

### 4️⃣ `estadia.py` - Entidade Estadia (Reserva/Hospedagem)

**Responsabilidade:** Representa uma reserva ou hospedagem de um cliente em um quarto.

**Atributos:**
```python
- codigo: int                    # Gerado automaticamente
- codigo_cliente: int            # Referência ao cliente
- quarto: Quarto                # Objeto quarto reservado
- data_entrada: date            # Data de check-in
- data_saida: date              # Data de check-out
- quantidade_diarias: int       # Calculado automaticamente
- valor_total: float            # quantidade_diarias × preco_diaria
- status: str                   # Status da estadia
```

**Estados possíveis:**
- `"Pendente"` → Recém criada (não usado atualmente)
- `"Confirmada"` → Ativa (pode fazer check-in/check-out)
- `"Cancelada"` → Cancelada pelo cliente
- `"Concluida"` → Check-out realizado

**Métodos principais:**
```python
calcular_diarias() -> int
    # Retorna: (data_saida - data_entrada).days
    
calcular_valor_total() -> float
    # Retorna: quantidade_diarias × quarto.preco_diaria

confirmar() -> bool
    # Muda status de "Pendente" para "Confirmada"
    
cancelar() -> bool
    # Cancela estadia e libera quarto (marca como "Disponível")
    # Só funciona se status == "Pendente" ou "Confirmada"

fazer_checkin() -> bool
    # Marca quarto como "Ocupado"
    # Só funciona se status == "Confirmada"
    
fazer_checkout(data_checkout: date = None) -> bool
    # Libera quarto ("Disponível"), muda status para "Concluida"
    # Recalcula diárias e valor se data_checkout diferente da prevista
    # Validação: data_checkout não pode ser < data_entrada
```

---

### 5️⃣ `hotel.py` - Orquestrador Central (A Classe Mais Importante!)

**Responsabilidade:** Coordena TODAS as operações do sistema. É o "cérebro" que une tudo.

**Atributos:**
```python
- nome: str                              # Nome do hotel
- clientes: List[Cliente]               # Todos os clientes
- funcionarios: List[Funcionario]       # Todos os funcionários  
- quartos: List[Quarto]                 # Todos os quartos
- estadias: List[Estadia]               # Todas as estadias
```

**Métodos principais por categoria:**

#### 👤 Gestão de Clientes
```python
cadastrar_cliente(nome, endereco, telefone) -> Cliente
buscar_cliente_por_codigo(codigo: int) -> Cliente | None
pesquisar_cliente(termo: str) -> List[Cliente]
    # Busca por nome (case-insensitive) ou código
listar_clientes() -> List[Cliente]
remover_cliente(codigo: int) -> Tuple[bool, str]
    # Só remove se não tiver estadias ativas
```

#### 👔 Gestão de Funcionários  
```python
cadastrar_funcionario(nome, telefone, cargo, salario) -> Funcionario
buscar_funcionario_por_codigo(codigo: int) -> Funcionario | None
pesquisar_funcionario(termo: str) -> List[Funcionario]
listar_funcionarios() -> List[Funcionario]
remover_funcionario(codigo: int) -> Tuple[bool, str]
```

#### 🛏️ Gestão de Quartos
```python
adicionar_quarto(numero, tipo, quantidade_hospedes, preco_diaria) -> bool
    # Retorna False se número duplicado
    
buscar_quarto_por_numero(numero: int) -> Quarto | None
listar_quartos() -> List[Quarto]
listar_quartos_disponiveis() -> List[Quarto]
    # Filtra apenas status == "Disponível"
    
listar_quartos_ocupados() -> List[Quarto]
listar_quartos_por_tipo(tipo: str) -> List[Quarto]
remover_quarto(numero: int) -> Tuple[bool, str]
```

#### 🎫 Gestão de Estadias (A Mágica Acontece Aqui!)
```python
cadastrar_estadia(codigo_cliente, quantidade_hospedes, data_entrada, data_saida) -> Estadia | None
    # 🎯 BUSCA AUTOMÁTICA DE QUARTO!
    # 1. Valida se cliente existe
    # 2. Valida datas (saida > entrada)
    # 3. Procura quarto disponível com capacidade suficiente
    # 4. Verifica disponibilidade no período
    # 5. Cria estadia automaticamente
    # Retorna None se qualquer validação falhar

fazer_estadia(codigo_cliente, numero_quarto, data_entrada, data_saida) -> Estadia | None  
    # Modo MANUAL: usuário escolhe o quarto
    # Mantido para compatibilidade com testes antigos
    
verificar_disponibilidade(numero_quarto, data_entrada, data_saida) -> bool
    # Verifica se quarto está livre no período
    # Considera apenas estadias "Pendente" ou "Confirmada"
    # Detecta sobreposição de datas
    
buscar_estadia_por_codigo(codigo: int) -> Estadia | None
cancelar_estadia(codigo: int) -> bool
listar_estadias() -> List[Estadia]
listar_estadias_ativas() -> List[Estadia]
    # Filtra apenas status == "Confirmada"
    
listar_estadias_por_cliente(codigo_cliente: int) -> List[Estadia]
```

#### 🔑 Check-in e Check-out
```python
fazer_checkin(codigo_estadia: int) -> bool
    # 1. Busca estadia
    # 2. Valida status == "Confirmada"
    # 3. Marca quarto como "Ocupado"
    
fazer_checkout(codigo_estadia: int, data_checkout: date = None) -> Tuple[bool, Any]
    # 1. Busca estadia
    # 2. Valida status == "Confirmada"  
    # 3. Valida data (>= data_entrada)
    # 4. Recalcula valor se necessário
    # 5. Marca quarto "Disponível"
    # 6. Muda status para "Concluida"
    # Retorna: (True, valor_total) ou (False, mensagem_erro)
```

#### 📊 Relatórios
```python
relatorio_ocupacao() -> dict
    # Retorna:
    # {
    #     'total_quartos': int,
    #     'quartos_disponiveis': int,
    #     'quartos_ocupados': int,
    #     'quartos_manutencao': int,
    #     'taxa_ocupacao': float  # porcentagem
    # }

relatorio_receita() -> dict
    # Retorna:
    # {
    #     'receita_total': float,
    #     'receita_concluida': float,      # Check-outs já feitos
    #     'receita_pendente': float,       # Hóspedes ainda no hotel
    #     'total_estadias': int
    # }
```

#### 💾 Persistência de Dados
```python
salvar_dados(arquivo: str = 'data/hotel_dados.bin') -> bool
    # Salva TUDO em arquivo .bin usando pickle:
    # - Todos os clientes, funcionários, quartos, estadias
    # - Contadores de código para manter sequência
    # Cria diretório 'data/' se não existir
    
carregar_dados(arquivo: str = 'data/hotel_dados.bin') -> bool
    # Carrega tudo do arquivo
    # Restaura contadores de código
    # Retorna False se arquivo não existir
```

---

## 🎨 Interface do Usuário (`ui/menu.py`)

**Responsabilidade:** Gerencia toda a interface visual do sistema em console.

**Principais funções:**
- Exibição de menus com bordas e formatação
- Navegação entre diferentes seções
- Coleta e validação de entradas do usuário

**Menus implementados:**
- Menu Principal (7 opções + sair)
- Menu de Clientes (5 opções)
- Menu de Funcionários (5 opções)
- Menu de Quartos (6 opções)
- Menu de Estadias (5 opções)
- Menu de Check-in/Check-out (3 opções)
- Menu de Relatórios (3 opções)
- Menu de Pesquisas (3 opções)

---

## 🛠️ Utilitários (`utils/utils.py`)

**Responsabilidade:** Funções auxiliares usadas em todo o sistema.

**Categorias de funções:**

### Validação de Entrada
```python
validar_numero_inteiro(prompt: str, min_val: int, max_val: int) -> int
validar_numero_float(prompt: str, min_val: float) -> float
validar_data(prompt: str) -> date
    # Formato: dd/mm/aaaa
    # Validações: data válida, não pode ser passado
validar_texto_nao_vazio(prompt: str) -> str
```

### Mensagens Formatadas
```python
msg_sucesso(texto: str)      # Verde com ✓
msg_erro(texto: str)         # Vermelho com ✗  
msg_info(texto: str)         # Azul com ℹ
msg_alerta(texto: str)       # Amarelo com ⚠
```

### Formatação
```python
formatar_moeda(valor: float) -> str
    # Retorna: "R$ 150,00"
    
formatar_data(data: date) -> str
    # Retorna: "15/12/2025"
```

### Controle de Tela
```python
limpar_tela()                # Limpa o console
pausar()                     # Aguarda Enter do usuário
titulo(texto: str)           # Exibe título com bordas
linha()                      # Exibe linha separadora
```

---

## 🔄 Fluxo de Execução (`main.py`)

### Classe `SistemaHotel`

Ponto de entrada do sistema. Gerencia o loop principal.

**Métodos principais:**

```python
__init__()
    # Inicializa hotel e menu UI
    
inicializar()
    # 1. Tenta carregar dados salvos
    # 2. Se não existir, cria dados de exemplo
    # 3. Exibe mensagem de status
    
criar_dados_exemplo()
    # Popula sistema com:
    # - 9 quartos (Simples, Duplo, Suíte)
    # - 2 clientes
    # - 2 funcionários
    
executar()
    # Loop principal:
    # 1. Inicializa sistema
    # 2. Exibe menu
    # 3. Processa opção escolhida
    # 4. Salva dados automaticamente
    # 5. Repete até usuário sair
```

### Inicialização do Sistema

```python
if __name__ == "__main__":
    sistema = SistemaHotel()
    sistema.executar()
```

**Sequência de eventos:**
1. ✅ Cria instância de `SistemaHotel`
2. ✅ Chama `inicializar()` → tenta carregar dados
3. ✅ Se não houver dados, cria exemplos
4. ✅ Entra no loop principal
5. ✅ Cada operação salva dados automaticamente
6. ✅ Usuário escolhe "Sair" → salva e encerra

---

## 💾 Persistência de Dados (Pickle)

### Por que Pickle?

- ✅ Preserva estrutura completa dos objetos Python
- ✅ Mantém referências entre objetos (Estadia → Quarto)
- ✅ Rápido para ler/escrever
- ✅ Não precisa biblioteca externa
- ❌ Não é legível por humanos (binário)
- ❌ Específico do Python (não interoperável)

### Estrutura do Arquivo Salvo

```python
{
    'nome': str,                           # Nome do hotel
    'clientes': List[Cliente],             # Todos os clientes
    'funcionarios': List[Funcionario],     # Todos os funcionários
    'quartos': List[Quarto],               # Todos os quartos
    'estadias': List[Estadia],             # Todas as estadias
    'contadores': {                        # Preserva sequência de IDs
        'cliente': int,
        'funcionario': int,
        'estadia': int
    }
}
```

### Quando os Dados São Salvos?

**Automaticamente após cada operação:**
- ✅ Cadastrar cliente/funcionário/quarto
- ✅ Criar estadia
- ✅ Check-in / Check-out
- ✅ Cancelar estadia
- ✅ Remover cliente/funcionário/quarto
- ✅ Ao sair do sistema

**Local:** `data/hotel_dados.bin` (criado automaticamente)

---

## ✅ Validações e Regras de Negócio

### Validações de Cliente
- ✅ Nome não pode ser vazio
- ✅ Código gerado automaticamente (único)
- ✅ Não pode remover se tiver estadias ativas

### Validações de Quarto  
- ✅ Número único (não permite duplicados)
- ✅ Quantidade de hóspedes > 0
- ✅ Preço da diária > 0
- ✅ Status inicial sempre "Disponível"
- ✅ Não pode remover se tiver estadias vinculadas

### Validações de Estadia
- ✅ Cliente deve existir
- ✅ Data de saída > Data de entrada
- ✅ Quarto deve ter capacidade suficiente
- ✅ Quarto deve estar disponível no período (não sobrepor datas)
- ✅ Quarto não pode estar em manutenção
- ✅ Código gerado automaticamente

### Validações de Check-in
- ✅ Estadia deve existir
- ✅ Status deve ser "Confirmada"
- ✅ Marca quarto como "Ocupado"

### Validações de Check-out
- ✅ Estadia deve existir
- ✅ Status deve ser "Confirmada"  
- ✅ Data de checkout >= Data de entrada
- ✅ Recalcula valor se data diferente
- ✅ Marca quarto como "Disponível"
- ✅ Muda status para "Concluida"

### Cálculo de Pontos de Fidelidade
- **Regra:** 10 pontos por diária
- **Exemplo:** 3 estadias com 2, 3 e 5 diárias = 100 pontos

---

## 🧪 Testes Automatizados (`tests/testes.py`)

### Estrutura dos Testes

**48 testes** organizados em **9 módulos:**

```python
teste_clientes()              # 6 testes
teste_funcionarios()          # 6 testes  
teste_quartos()               # 8 testes
teste_estadias()              # 10 testes
teste_pontos_fidelidade()     # 4 testes
teste_pesquisas()             # 6 testes
teste_relatorios()            # 2 testes
teste_persistencia()          # 3 testes
teste_validacoes_restricoes() # 3 testes
```

### Como Executar

```bash
python tests/testes.py
```

### O Que É Testado?

✅ **Cadastros:** Códigos automáticos, unicidade, estrutura de dados  
✅ **Buscas:** Por código, por nome, case-insensitive  
✅ **Estadias:** Busca automática, validações, cálculos  
✅ **Check-in/out:** Mudanças de status, cálculos de valor  
✅ **Pontos:** Cálculo correto (diárias × 10)  
✅ **Persistência:** Salvar, carregar, integridade  
✅ **Validações:** Todas as regras de negócio

### Exemplo de Saída

```
═══════════════════════════════════════════════
  TESTANDO CLIENTES - BATERIA COMPLETA (6 testes)
═══════════════════════════════════════════════

[TC-CLI-001] Cadastrando clientes...
✓ PASSOU - 3 clientes cadastrados com códigos 1, 2, 3

[TC-CLI-002] Validando unicidade de códigos...
✓ PASSOU - 3 códigos únicos validados

...

✓✓✓ TODOS OS TESTES PASSARAM! (6/6)
```

---

## 🚀 Decisões de Design e Boas Práticas

### Por que Orientação a Objetos?

- ✅ **Encapsulamento:** Cada entidade cuida dos seus dados
- ✅ **Reutilização:** Métodos compartilhados (to_dict, from_dict)
- ✅ **Manutenção:** Mudanças localizadas em classes específicas
- ✅ **Clareza:** Código reflete o mundo real (Hotel tem Quartos)

### Por que Separar em Módulos?

- ✅ **models/**: Lógica de negócio isolada
- ✅ **ui/**: Interface separada (fácil trocar para web depois)
- ✅ **utils/**: Funções reutilizáveis em um só lugar

### Por que Validações Robustas?

- ✅ Evita dados inconsistentes
- ✅ Melhora experiência do usuário (mensagens claras)
- ✅ Facilita manutenção (bugs detectados cedo)

### Por que Pickle?

- ✅ Simples de usar
- ✅ Preserva objetos complexos
- ✅ Não precisa converter para JSON manualmente
- ✅ Apropriado para projeto educacional

---

## 📊 Complexidade e Performance

### Operações Principais

| Operação | Complexidade | Observação |
|----------|--------------|------------|
| Cadastrar cliente | O(1) | Adiciona no final da lista |
| Buscar por código | O(n) | Percorre lista linearmente |
| Pesquisar por nome | O(n) | Percorre lista e compara strings |
| Busca automática de quarto | O(n×m) | n quartos, m estadias |
| Salvar dados | O(n) | Serializa todas as listas |
| Carregar dados | O(n) | Deserializa arquivo |

**Nota:** Para um hotel pequeno/médio (< 1000 registros), performance é excelente.

### Melhorias Futuras Possíveis

- 🔄 Usar dicionários para buscas O(1)
- 🔄 Indexar quartos por tipo/status
- 🔄 Cache para relatórios
- 🔄 Banco de dados SQL para grandes volumes

---

## 🎓 Conceitos de AED Aplicados

### Estruturas de Dados Usadas

✅ **Listas (List):** Armazenamento de clientes, quartos, estadias  
✅ **Dicionários (Dict):** Serialização para pickle  
✅ **Objetos:** Representação de entidades  
✅ **Strings:** Manipulação e validação  
✅ **Datas (date):** Cálculos e comparações

### Algoritmos Implementados

✅ **Busca Linear:** Procurar por código/nome  
✅ **Filtragem:** Listar quartos disponíveis  
✅ **Validação:** Verificar disponibilidade por período  
✅ **Cálculo:** Diárias, valores, pontos  
✅ **Ordenação implícita:** Códigos sequenciais

---

## 🔧 Troubleshooting (Problemas Comuns)

### "Arquivo não encontrado"
**Solução:** O sistema cria automaticamente. Se der erro, crie a pasta `data/` manualmente.

### "Código já existe"
**Solução:** Os códigos são automáticos. Se deu erro, pode ser problema no arquivo salvo. Delete `data/hotel_dados.bin` e recomece.

### "Data inválida"
**Solução:** Use o formato correto: `dd/mm/aaaa` (ex: 15/12/2025)

### "Quarto não disponível"
**Solução:** Verifique se o quarto não está ocupado ou em manutenção no período desejado.

### Testes falhando
**Solução:** Execute `python tests/testes.py` do diretório raiz do projeto.

---

## 📚 Referências e Recursos

- [Documentação Python 3.12](https://docs.python.org/3.12/)
- [Pickle](https://docs.python.org/3/library/pickle.html)
- [Datetime](https://docs.python.org/3/library/datetime.html)
- [POO em Python](https://docs.python.org/3/tutorial/classes.html)

---

## 👨‍💻 Para Desenvolvedores

### Adicionar Nova Funcionalidade

1. Adicione método na classe apropriada (`models/`)
2. Adicione opção de menu (`ui/menu.py`)  
3. Conecte no `main.py`
4. Crie testes (`tests/testes.py`)
5. Documente aqui

### Modificar Entidades

1. Altere a classe (`models/`)
2. Atualize `to_dict()` e `from_dict()`
3. Delete `data/hotel_dados.bin` (incompatível)
4. Atualize testes
5. Atualize documentação

### Contribuir

1. Fork o repositório
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

---

**📅 Última atualização:** 10/12/2025  
**✍️ Autor:** Bzinnnn  
**🎓 Projeto:** Trabalho Prático - AED - PUC Minas
- clientes: lista de todos os clientes
- funcionarios: lista de funcionarios
- quartos: lista de quartos
- estadias: lista de estadias

**Funcoes para Clientes:**
- cadastrar_cliente(): adiciona novo cliente
- buscar_cliente_por_codigo(): encontra cliente
- pesquisar_cliente(): busca por nome parcial
- listar_clientes(): mostra todos
- remover_cliente(): remove se nao tiver estadia ativa

**Funcoes para Funcionarios:**
- cadastrar_funcionario(): adiciona funcionario
- buscar_funcionario_por_codigo(): encontra funcionario
- pesquisar_funcionario(): busca por nome
- listar_funcionarios(): mostra todos
- remover_funcionario(): remove funcionario

**Funcoes para Quartos:**
- cadastrar_quarto(): adiciona quarto
- buscar_quarto_por_numero(): encontra quarto
- listar_quartos(): mostra todos
- listar_quartos_disponiveis(): so os livres
- alterar_status_quarto(): muda status
- remover_quarto(): remove se nao tiver estadia ativa

**Funcoes para Estadias:**
- cadastrar_estadia(): cria estadia e busca quarto automaticamente
- buscar_estadia_por_codigo(): encontra estadia
- listar_estadias(): mostra todas
- cancelar_estadia(): cancela estadia
- estadias_por_cliente(): busca estadias de um cliente
- verificar_disponibilidade(): checa se quarto esta livre no periodo

**Funcoes de Checkin/Checkout:**
- fazer_checkin(): marca quarto como ocupado
- fazer_checkout(): libera quarto e finaliza estadia

**Funcoes de Relatorios:**
- relatorio_ocupacao(): mostra quantos quartos ocupados/disponiveis
- relatorio_receita(): mostra valores de receita

**Funcoes de Dados:**
- salvar_dados(): salva tudo em arquivo binario
- carregar_dados(): carrega dados salvos

### 6. menu.py - Interface do Usuario

Exibe o menu e le opcoes do usuario.

**Funcoes:**
- exibir_menu_principal(): mostra as 23 opcoes
- ler_opcao(): le numero digitado pelo usuario

### 7. utils.py - Funcoes Auxiliares

Funcoes para validacao e formatacao.

**Validacoes:**
- validar_cpf(): verifica se CPF tem 11 digitos
- validar_data(): converte texto para data (DD/MM/AAAA)
- validar_numero(): garante que e um numero valido

**Formatacao:**
- limpar_tela(): limpa o console
- pausar(): espera usuario pressionar Enter
- linha(): desenha linha separadora
- titulo(): exibe titulo formatado
- msg_sucesso(): mensagem de sucesso
- msg_erro(): mensagem de erro
- msg_info(): mensagem informativa

### 8. main.py - Programa Principal

Arquivo que executa o sistema. Contem o loop principal e todas as funcoes do menu.

**Funcoes do menu (23 opcoes):**
- cadastrar_cliente()
- listar_clientes()
- pesquisar_cliente()
- pontos_fidelidade()
- remover_cliente()
- cadastrar_funcionario()
- listar_funcionarios()
- pesquisar_funcionario()
- remover_funcionario()
- cadastrar_quarto()
- listar_quartos()
- consultar_quartos_disponiveis()
- alterar_status_quarto()
- remover_quarto()
- fazer_estadia()
- listar_estadias()
- consultar_estadia()
- cancelar_estadia()
- estadias_por_cliente()
- realizar_checkin()
- realizar_checkout()
- relatorio_ocupacao()
- relatorio_receita()

## Como o Sistema Funciona

### Fluxo 1: Fazer uma Estadia

1. Usuario escolhe opcao 15 (Fazer Estadia)
2. Sistema pede codigo do cliente
3. Sistema pede quantidade de hospedes
4. Sistema pede datas de entrada e saida
5. Sistema busca automaticamente um quarto disponivel com capacidade suficiente
6. Sistema cria a estadia e calcula o valor total
7. Estadia fica com status "Confirmada"
8. Quarto ainda fica "Disponivel" (so muda no checkin)
9. Sistema salva tudo automaticamente

### Fluxo 2: Fazer Checkin

1. Usuario escolhe opcao 20 (Realizar Check-in)
2. Sistema pede codigo da estadia
3. Sistema busca a estadia
4. Sistema marca o quarto como "Ocupado"
5. Sistema salva

### Fluxo 3: Fazer Checkout

1. Usuario escolhe opcao 21 (Realizar Check-out)
2. Sistema pede codigo da estadia
3. Sistema pede data do checkout (ou usa data atual)
4. Sistema recalcula diarias e valor se data for diferente
5. Sistema marca quarto como "Disponivel"
6. Estadia muda para status "Concluida"
7. Cliente ganha pontos de fidelidade
8. Sistema salva

### Fluxo 4: Verificar Disponibilidade

Quando usuario tenta fazer estadia, o sistema:
1. Percorre todos os quartos
2. Verifica capacidade suficiente
3. Verifica se nao esta em manutencao
4. Verifica se tem alguma estadia ativa (Confirmada ou Pendente) no periodo
5. Se encontrar quarto livre, aloca automaticamente

## Persistencia de Dados

Os dados sao salvos em arquivo binario usando a biblioteca pickle do Python.

**Arquivo:** data/hotel_dados.bin

**O que e salvo:**
- Todos os clientes
- Todos os funcionarios
- Todos os quartos
- Todas as estadias

**Quando e salvo:**
- Apos cada operacao (cadastro, alteracao, remocao)
- Automaticamente quando usuario sai do sistema

**Carregamento:**
- Sistema carrega dados automaticamente ao iniciar
- Se arquivo nao existir, comeca vazio

## Validacoes Implementadas

### Validacao de CPF
- Deve ter exatamente 11 digitos
- Remove espacos e tracos automaticamente
- Nao aceita CPFs com todos digitos iguais (11111111111)

### Validacao de Datas
- Formato obrigatorio: DD/MM/AAAA
- Data de entrada deve ser hoje ou futura
- Data de saida deve ser depois da entrada
- Sistema verifica conflitos com outras estadias

### Validacao de Quartos
- Numero do quarto deve ser unico
- Tipo deve ser: Simples, Duplo ou Suite
- Capacidade deve ser maior que zero
- Preco deve ser maior que zero

### Validacao de Estadias
- Cliente deve existir
- Quantidade de hospedes deve ser maior que zero
- Deve existir quarto disponivel com capacidade suficiente
- Periodo nao pode ter conflito com outras estadias do mesmo quarto

### Validacao de Remocao
- Nao pode remover cliente com estadia ativa
- Nao pode remover quarto com estadia ativa
- Estadia ativa = status Pendente ou Confirmada

## Regras de Negocio

### Status de Quarto
- **Disponivel**: quarto livre, pode ser reservado
- **Ocupado**: quarto com hospede (apos checkin)
- **Manutencao**: quarto em manutencao, nao pode ser usado

### Status de Estadia
- **Pendente**: estadia criada mas nao confirmada (nao usado atualmente)
- **Confirmada**: estadia confirmada, aguardando checkin
- **Cancelada**: estadia foi cancelada
- **Concluida**: checkout foi feito, estadia finalizada

### Calculo de Valor
```
valor_total = quantidade_diarias * preco_diaria_do_quarto
```

### Pontos de Fidelidade
```
pontos = quantidade_diarias * 10
```
Cliente ganha 10 pontos por diaria quando faz checkout.

### Busca Automatica de Quarto
Sistema busca quarto que:
1. Tenha capacidade >= quantidade de hospedes solicitada
2. Nao esteja em manutencao
3. Esteja disponivel no periodo (sem conflito de datas)

## Complexidade das Operacoes

Tabela mostrando o tempo de execucao das principais funcoes:

| Operacao | Tempo | Explicacao |
|----------|-------|------------|
| Cadastrar cliente | Rapido | Apenas adiciona na lista |
| Buscar por codigo | Medio | Percorre lista ate encontrar |
| Listar todos | Rapido | Retorna lista completa |
| Verificar disponibilidade | Medio | Percorre estadias do quarto |
| Salvar dados | Medio | Grava arquivo no disco |
| Carregar dados | Medio | Le arquivo do disco |

Para um hotel com ate 1000 quartos e 10000 estadias, todas as operacoes sao rapidas (menos de 1 segundo).

## Estrutura de Dados

O sistema usa principalmente **listas** do Python para armazenar os dados:

```python
# Exemplos
clientes = []        # lista de objetos Cliente
quartos = []         # lista de objetos Quarto
estadias = []        # lista de objetos Estadia
```

Quando precisa buscar, o sistema percorre a lista comparando valores:
```python
for cliente in clientes:
    if cliente.codigo == codigo_procurado:
        return cliente
```

## Requisitos Tecnicos

**Python:** 3.12 ou superior

**Bibliotecas usadas (todas padrao):**
- datetime: para trabalhar com datas
- pickle: para salvar e carregar dados
- os: para limpar tela e operacoes de sistema

**Nao precisa instalar nada extra.**

## Boas Praticas Aplicadas

1. **Codigo organizado**: cada classe em seu arquivo
2. **Nomes claros**: variaveis e funcoes com nomes que explicam o que fazem
3. **Comentarios**: explicacoes onde necessario
4. **Validacoes**: sistema verifica dados antes de aceitar
5. **Salvamento automatico**: dados nao se perdem
6. **Separacao de responsabilidades**: cada modulo tem sua funcao
7. **Interface amigavel**: mensagens claras para o usuario
8. **Opcao de cancelar**: usuario pode digitar 0 para sair de qualquer operacao

## Limitacoes Conhecidas

1. Sistema nao permite editar dados (apenas cadastrar e remover)
2. Nao tem sistema de login/senha
3. Nao calcula impostos ou taxas adicionais
4. Relatorios sao basicos (sem graficos)
5. Busca e sequencial (poderia ser mais rapida com indices)

## Possibilidades de Melhoria

Para versoes futuras:
- Adicionar edicao de cadastros
- Implementar sistema de usuarios e permissoes
- Criar relatorios mais detalhados
- Adicionar busca por data
- Implementar reserva antecipada
- Adicionar calculo de impostos
- Criar interface grafica

---

Desenvolvido para disciplina de Algoritmos e Estruturas de Dados
PUC Minas - Primeiro Periodo
Dezembro de 2025

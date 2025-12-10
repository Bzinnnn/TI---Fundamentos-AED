# Documentação Técnica - Sistema Hotel Descanso Garantido

## 📚 Visão Geral Técnica

Sistema de gerenciamento hoteleiro orientado a objetos desenvolvido em Python 3, utilizando apenas bibliotecas padrão da linguagem.

## 🏗️ Arquitetura do Sistema

### Diagrama de Classes

```
┌─────────────────┐
│     Hotel       │
├─────────────────┤
│ - nome          │
│ - quartos[]     │───────┐
│ - reservas[]    │───┐   │
├─────────────────┤   │   │
│ + adicionar_    │   │   │
│   quarto()      │   │   │
│ + fazer_        │   │   │
│   reserva()     │   │   │
│ + fazer_        │   │   │
│   checkin()     │   │   │
│ + relatorios()  │   │   │
└─────────────────┘   │   │
                      │   │
        ┌─────────────┘   └──────────────┐
        │                                 │
        ▼                                 ▼
┌──────────────┐                  ┌──────────────┐
│   Reserva    │                  │    Quarto    │
├──────────────┤                  ├──────────────┤
│ - id         │                  │ - numero     │
│ - hospede    │                  │ - tipo       │
│ - cpf        │                  │ - capacidade │
│ - quarto     │◄─────────────────│ - preco      │
│ - datas      │                  │ - status     │
│ - status     │                  ├──────────────┤
│ - valor      │                  │ + marcar_    │
├──────────────┤                  │   ocupado()  │
│ + confirmar()│                  │ + marcar_    │
│ + cancelar() │                  │   disponivel()│
│ + checkin()  │                  └──────────────┘
│ + checkout() │
└──────────────┘
```

### Módulos do Sistema

#### 1. `quarto.py` - Módulo de Quartos
**Responsabilidade:** Gerenciar informações e estados dos quartos

**Classe Principal:** `Quarto`

**Atributos:**
- `numero: int` - Identificador único do quarto
- `tipo: str` - Tipo do quarto (Simples, Duplo, Suíte)
- `capacidade: int` - Número máximo de hóspedes
- `preco_diaria: float` - Valor da diária
- `status: str` - Estado atual (Disponível, Ocupado, Manutenção)

**Métodos Principais:**
```python
marcar_ocupado() -> bool
    Marca o quarto como ocupado
    Retorna True se bem-sucedido

marcar_disponivel() -> None
    Marca o quarto como disponível

marcar_manutencao() -> None
    Marca o quarto para manutenção

esta_disponivel() -> bool
    Verifica se o quarto está disponível

to_dict() -> dict
    Serializa o quarto para JSON

from_dict(data: dict) -> Quarto
    Deserializa quarto de JSON
```

#### 2. `reserva.py` - Módulo de Reservas
**Responsabilidade:** Gerenciar reservas e estadias

**Classe Principal:** `Reserva`

**Atributos:**
- `id: int` - ID único (auto-incremento)
- `nome_hospede: str` - Nome do hóspede
- `cpf_hospede: str` - CPF do hóspede (11 dígitos)
- `quarto: Quarto` - Referência ao quarto reservado
- `data_checkin: date` - Data de entrada
- `data_checkout: date` - Data de saída
- `status: str` - Estado (Pendente, Confirmada, Cancelada, Concluída)
- `valor_total: float` - Valor calculado automaticamente

**Métodos Principais:**
```python
calcular_valor_total() -> float
    Calcula valor baseado em número de diárias

confirmar() -> bool
    Confirma a reserva

cancelar() -> bool
    Cancela a reserva e libera o quarto

fazer_checkin() -> bool
    Executa check-in e marca quarto como ocupado

fazer_checkout() -> bool
    Executa check-out e libera quarto

to_dict() -> dict
    Serializa reserva para JSON
```

**Variável de Classe:**
```python
_contador_id: int
    Contador estático para gerar IDs únicos
```

#### 3. `hotel.py` - Módulo Central
**Responsabilidade:** Coordenar todas as operações do hotel

**Classe Principal:** `Hotel`

**Atributos:**
- `nome: str` - Nome do hotel
- `quartos: list[Quarto]` - Lista de todos os quartos
- `reservas: list[Reserva]` - Lista de todas as reservas

**Métodos de Quartos:**
```python
adicionar_quarto(numero, tipo, capacidade, preco) -> bool
    Adiciona novo quarto ao hotel

buscar_quarto_por_numero(numero: int) -> Quarto | None
    Busca quarto pelo número

listar_quartos() -> list[Quarto]
    Retorna todos os quartos

listar_quartos_disponiveis() -> list[Quarto]
    Filtra apenas quartos disponíveis

listar_quartos_ocupados() -> list[Quarto]
    Filtra apenas quartos ocupados

listar_quartos_por_tipo(tipo: str) -> list[Quarto]
    Filtra quartos por tipo
```

**Métodos de Reservas:**
```python
fazer_reserva(nome, cpf, numero_quarto, checkin, checkout) -> Reserva | None
    Cria nova reserva com validações

verificar_disponibilidade(numero_quarto, checkin, checkout) -> bool
    Verifica conflitos de datas

buscar_reserva_por_id(id_reserva: int) -> Reserva | None
    Busca reserva pelo ID

cancelar_reserva(id_reserva: int) -> bool
    Cancela reserva existente

listar_reservas() -> list[Reserva]
    Retorna todas as reservas

listar_reservas_ativas() -> list[Reserva]
    Filtra reservas confirmadas

listar_reservas_por_hospede(cpf: str) -> list[Reserva]
    Busca reservas de um hóspede
```

**Métodos de Check-in/Check-out:**
```python
fazer_checkin(id_reserva: int) -> bool
    Executa check-in

fazer_checkout(id_reserva: int) -> bool
    Executa check-out
```

**Métodos de Relatórios:**
```python
relatorio_ocupacao() -> dict
    Retorna estatísticas de ocupação:
    - total_quartos
    - quartos_disponiveis
    - quartos_ocupados
    - quartos_manutencao
    - taxa_ocupacao (%)

relatorio_receita() -> dict
    Retorna estatísticas financeiras:
    - receita_total
    - receita_pendente
    - receita_concluida
    - total_reservas
```

**Métodos de Persistência:**
```python
salvar_dados(arquivo: str = 'hotel_dados.json') -> None
    Salva estado do hotel em JSON

carregar_dados(arquivo: str = 'hotel_dados.json') -> bool
    Carrega estado do hotel de JSON
```

#### 4. `utils.py` - Módulo de Utilitários
**Responsabilidade:** Validações e formatação

**Classe:** `ValidadorEntradas`

**Métodos de Validação:**
```python
validar_cpf(cpf: str) -> str | None
    Valida formato do CPF (11 dígitos)
    Remove formatação
    Rejeita sequências iguais

validar_data(data_str: str, formato: str) -> date | None
    Converte string para objeto date
    Formato padrão: DD/MM/AAAA

validar_numero_inteiro(valor_str: str, minimo, maximo) -> int | None
    Valida e converte para inteiro
    Opcionalmente verifica limites

validar_numero_float(valor_str: str, minimo, maximo) -> float | None
    Valida e converte para float
    Aceita vírgula ou ponto decimal

validar_tipo_quarto(tipo: str) -> str | None
    Normaliza tipo de quarto
    Aceita variações de capitalização
```

**Classe:** `FormatadorSaida`

**Métodos de Formatação:**
```python
linha(caractere: str, tamanho: int) -> None
    Imprime linha separadora

titulo(texto: str) -> None
    Imprime título formatado

subtitulo(texto: str) -> None
    Imprime subtítulo

sucesso(mensagem: str) -> None
    Mensagem de sucesso com ✓

erro(mensagem: str) -> None
    Mensagem de erro com ✗

alerta(mensagem: str) -> None
    Mensagem de alerta com ⚠

info(mensagem: str) -> None
    Mensagem informativa com ℹ

tabela_quartos(quartos: list[Quarto]) -> None
    Formata lista de quartos em tabela

tabela_reservas(reservas: list[Reserva]) -> None
    Formata lista de reservas em tabela
```

**Funções Auxiliares:**
```python
limpar_tela() -> None
    Limpa console (multiplataforma)

pausar() -> None
    Aguarda Enter do usuário
```

#### 5. `main.py` - Módulo Principal
**Responsabilidade:** Interface com usuário e controle de fluxo

**Classe:** `SistemaHotel`

**Métodos Principais:**
```python
inicializar() -> None
    Carrega dados ou cria exemplos

menu_principal() -> None
    Exibe menu interativo

executar() -> None
    Loop principal do sistema

criar_dados_exemplo() -> None
    Cria 9 quartos pré-configurados
```

**Métodos de Funcionalidades:**
- `cadastrar_quarto()` - Interface para cadastro
- `listar_quartos()` - Exibe todos os quartos
- `consultar_quartos_disponiveis()` - Mostra disponíveis
- `fazer_reserva()` - Interface para reservas
- `listar_reservas()` - Exibe todas as reservas
- `consultar_reserva()` - Busca reserva específica
- `cancelar_reserva()` - Interface de cancelamento
- `realizar_checkin()` - Interface de check-in
- `realizar_checkout()` - Interface de check-out
- `relatorio_ocupacao()` - Mostra estatísticas
- `relatorio_receita()` - Mostra financeiro
- `buscar_reservas_hospede()` - Busca por CPF
- `alterar_status_quarto()` - Altera disponibilidade
- `sair()` - Finaliza e salva dados

## 🔄 Fluxo de Dados

### 1. Fluxo de Criação de Reserva

```
Usuário
  │
  ├─→ main.fazer_reserva()
  │     │
  │     ├─→ utils.validar_cpf()
  │     ├─→ utils.validar_data()
  │     │
  │     ├─→ hotel.fazer_reserva()
  │     │     │
  │     │     ├─→ hotel.buscar_quarto_por_numero()
  │     │     ├─→ hotel.verificar_disponibilidade()
  │     │     │     └─→ Itera sobre reservas existentes
  │     │     │
  │     │     └─→ Reserva.__init__()
  │     │           ├─→ Reserva.calcular_valor_total()
  │     │           └─→ Reserva.confirmar()
  │     │
  │     └─→ hotel.salvar_dados()
  │
  └─→ Confirmação exibida
```

### 2. Fluxo de Check-in

```
Usuário fornece ID
  │
  ├─→ main.realizar_checkin()
  │     │
  │     ├─→ hotel.fazer_checkin(id)
  │     │     │
  │     │     ├─→ hotel.buscar_reserva_por_id(id)
  │     │     │
  │     │     └─→ reserva.fazer_checkin()
  │     │           └─→ quarto.marcar_ocupado()
  │     │
  │     └─→ hotel.salvar_dados()
  │
  └─→ Confirmação exibida
```

### 3. Fluxo de Persistência

```
Salvar:
  hotel.salvar_dados()
    │
    ├─→ Converte quartos: [q.to_dict() for q in quartos]
    ├─→ Converte reservas: [r.to_dict() for r in reservas]
    │
    └─→ json.dump() → hotel_dados.json

Carregar:
  hotel.carregar_dados()
    │
    ├─→ json.load() ← hotel_dados.json
    │
    ├─→ Reconstrói quartos: Quarto.from_dict()
    └─→ Reconstrói reservas: Reserva()
```

## 💾 Formato de Dados (JSON)

### Estrutura do arquivo `hotel_dados.json`:

```json
{
    "nome": "Hotel Descanso Garantido",
    "quartos": [
        {
            "numero": 101,
            "tipo": "Simples",
            "capacidade": 1,
            "preco_diaria": 150.00,
            "status": "Disponível"
        }
    ],
    "reservas": [
        {
            "id": 1,
            "nome_hospede": "João Silva",
            "cpf_hospede": "12345678901",
            "quarto_numero": 101,
            "data_checkin": "2025-12-10",
            "data_checkout": "2025-12-12",
            "status": "Confirmada",
            "valor_total": 300.00
        }
    ]
}
```

## 🔐 Validações Implementadas

### 1. Validação de CPF
- Deve ter 11 dígitos numéricos
- Não aceita sequências iguais (11111111111)
- Remove automaticamente formatação

### 2. Validação de Datas
- Formato: DD/MM/AAAA
- Check-in deve ser futuro ou hoje
- Check-out deve ser posterior ao check-in
- Verifica conflitos com reservas existentes

### 3. Validação de Quartos
- Número único (sem duplicação)
- Tipo válido (Simples, Duplo, Suíte)
- Capacidade > 0
- Preço > 0

### 4. Validação de Reservas
- Quarto deve existir
- Quarto deve estar disponível
- Período deve estar livre
- CPF válido
- Datas válidas

## ⚡ Complexidade Computacional

### Operações Principais:

| Operação | Complexidade | Justificativa |
|----------|--------------|---------------|
| Adicionar quarto | O(n) | Verifica duplicação |
| Buscar quarto | O(n) | Busca linear |
| Listar disponíveis | O(n) | Filtragem |
| Fazer reserva | O(n) | Verifica conflitos |
| Buscar reserva | O(n) | Busca linear |
| Verificar disponibilidade | O(m) | m = nº de reservas |
| Salvar dados | O(n+m) | Serializa tudo |
| Carregar dados | O(n+m) | Deserializa tudo |

**Otimizações Possíveis:**
- Usar dicionários para busca O(1) por número/ID
- Índice por data para consultas de disponibilidade
- Cache de quartos disponíveis

## 🧪 Testes Implementados

### Módulo `testes.py`

**Cobertura de Testes:**
1. **Gerenciamento de Quartos**
   - Adição de quartos
   - Prevenção de duplicação
   - Busca por número
   - Listagem e filtragem
   - Alteração de status

2. **Sistema de Reservas**
   - Criação de reservas
   - Cálculo de valores
   - Verificação de disponibilidade
   - Cancelamento
   - Check-in e check-out

3. **Relatórios**
   - Relatório de ocupação
   - Relatório de receita

4. **Persistência**
   - Salvamento em JSON
   - Carregamento de JSON
   - Integridade dos dados

**Executar Testes:**
```bash
python testes.py
```

## 📊 Métricas do Projeto

- **Linhas de Código:** ~1800 (comentários inclusos)
- **Módulos:** 5
- **Classes:** 6
- **Funções/Métodos:** ~80
- **Testes Automatizados:** 15+
- **Cobertura de Funcionalidades:** 100%

## 🔧 Requisitos Técnicos

**Python:** 3.7+

**Bibliotecas Utilizadas (todas padrão):**
- `datetime` - Manipulação de datas
- `json` - Serialização de dados
- `os` - Operações de sistema
- `re` - Expressões regulares (validação)

**Sem Dependências Externas** ✓

## 📝 Boas Práticas Aplicadas

1. **PEP 8** - Guia de estilo Python
2. **Docstrings** - Documentação em todas as funções
3. **Type Hints** - Comentários de tipo
4. **DRY** - Don't Repeat Yourself
5. **SOLID** - Princípios de OO
6. **Modularização** - Separação de responsabilidades
7. **Tratamento de Erros** - Validações robustas
8. **Persistência** - Salvamento automático

---

**Última Atualização:** Dezembro 2025
**Versão:** 1.0.0

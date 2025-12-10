# Documentacao Tecnica - Sistema Hotel Descanso Garantido

## Visao Geral

Sistema de gerenciamento hoteleiro desenvolvido em Python 3.12 usando programacao orientada a objetos. Usa apenas bibliotecas padrao do Python, sem necessidade de instalar pacotes externos.

## Arquitetura

O sistema e organizado em 5 modulos principais que se comunicam entre si. Cada modulo tem uma responsabilidade especifica.

### Estrutura de Pastas

```
TI---Fundamentos-AED/
├── main.py              (programa principal)
├── src/
│   ├── models/          (classes do sistema)
│   │   ├── hotel.py
│   │   ├── cliente.py
│   │   ├── funcionario.py
│   │   ├── quarto.py
│   │   └── estadia.py
│   ├── ui/              (interface do usuario)
│   │   └── menu.py
│   └── utils/           (funcoes auxiliares)
│       └── utils.py
├── data/                (dados salvos)
│   └── hotel_dados.bin
└── tests/               (testes)
    └── testes.py
```

### Como as Classes se Relacionam

A classe Hotel e a principal. Ela contem listas de clientes, funcionarios, quartos e estadias. Quando um cliente faz uma estadia, o sistema associa o cliente a um quarto especifico para um periodo de datas.

```
Hotel
  - tem varios clientes
  - tem varios funcionarios
  - tem varios quartos
  - tem varias estadias
  
Estadia
  - pertence a um cliente
  - ocupa um quarto
  - tem data de entrada e saida
```

## Descricao dos Modulos

## Descricao dos Modulos

### 1. cliente.py - Cadastro de Clientes

Gerencia informacoes dos clientes do hotel.

**Atributos:**
- codigo: numero unico gerado automaticamente
- nome: nome completo do cliente
- cpf: CPF com 11 digitos
- telefone: telefone de contato
- email: email do cliente
- pontos_fidelidade: pontos acumulados por estadias

**Funcoes principais:**
- Cadastra novo cliente com codigo automatico
- Busca cliente por codigo
- Adiciona pontos quando cliente faz checkout
- Lista todos os clientes

### 2. funcionario.py - Cadastro de Funcionarios

Gerencia dados dos funcionarios do hotel.

**Atributos:**
- codigo: numero unico gerado automaticamente
- nome: nome completo
- cpf: CPF com 11 digitos
- cargo: funcao do funcionario
- salario: valor do salario

**Funcoes principais:**
- Cadastra novo funcionario
- Busca por codigo
- Lista todos funcionarios

### 3. quarto.py - Gerenciamento de Quartos

Controla informacoes e status dos quartos.

**Atributos:**
- numero: numero do quarto (unico)
- tipo: Simples, Duplo ou Suite
- quantidade_hospedes: capacidade maxima
- preco_diaria: valor por dia
- status: Disponivel, Ocupado ou Manutencao

**Funcoes principais:**
- marcar_ocupado(): marca quarto como ocupado
- marcar_desocupado(): libera o quarto
- marcar_disponivel(): volta status para disponivel
- marcar_manutencao(): marca para manutencao
- esta_disponivel(): verifica se esta livre

### 4. estadia.py - Sistema de Estadias

Gerencia reservas e estadias dos clientes.

**Atributos:**
- codigo: numero unico da estadia
- codigo_cliente: codigo do cliente
- quarto: referencia ao quarto
- data_entrada: data de entrada
- data_saida: data de saida
- quantidade_diarias: numero de dias
- valor_total: preco total calculado
- status: Pendente, Confirmada, Cancelada ou Concluida

**Funcoes principais:**
- confirmar(): confirma a estadia
- cancelar(): cancela a estadia
- fazer_checkin(): realiza checkin e marca quarto ocupado
- fazer_checkout(data): realiza checkout e recalcula valor se necessario
- calcular_diarias(): calcula numero de dias

### 5. hotel.py - Modulo Central

Coordena todas as operacoes do hotel. E a classe principal que une tudo.

**Atributos:**
- nome: nome do hotel
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

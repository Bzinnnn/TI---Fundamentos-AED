# Sistema de Gerenciamento Hoteleiro

        VALLE PRADO RESORT 
---

## Sobre o Projeto

Este é um sistema de gerenciamento desenvolvido para a disciplina de Fundamentos da Engenharia de Software. 

O sistema foi implementado em **Python 3.12**, utilizando apenas as bibliotecas padrão da linguagem, sem frameworks externos. Isso permite focar nos conceitos fundamentais de programação e estruturas de dados.

---

### Executando os Testes

Para executar a bateria completa de 48 testes automatizados:

```bash
python tests/testes.py
```

**Saída esperada:**
```
...................................................
----------------------------------------------------------------------
Ran 48 tests in 0.013s

OK
```

Para executar os testes com saída detalhada (mostrando cada teste):

```bash
python tests/testes.py -v
```


## Como Executar o Sistema

### Requisitos

- Python 3.12 ou superior

Para verificar se o Python está instalado, abra o terminal e execute:
```bash
python --version
```

### Passos para Execução

1. Abra o terminal (CMD no Windows ou Terminal no Linux/macOS)

2. Navegue até o diretório do projeto:
```bash
cd caminho/para/TI---Fundamentos-AED
```

3. Execute o arquivo principal:
```bash
python main.py
```

### Executando os Testes

Para executar a bateria completa de 48 testes automatizados:

```bash
python tests/testes.py
```

**Saída esperada:**
```
...................................................
----------------------------------------------------------------------
Ran 48 tests in 0.013s

OK
```

Para executar os testes com saída detalhada (mostrando cada teste):

```bash
python tests/testes.py -v
```

---

## Persistência de Dados

O sistema utiliza a biblioteca **pickle** do Python para persistir os dados em arquivo binário. Todas as informações (clientes, funcionários, quartos e estadias) são automaticamente salvas no arquivo:

```
TI---Fundamentos-AED/
   └── data/
       └── hotel_dados.bin
```

**Funcionamento:**
- Ao iniciar o sistema, os dados são carregados do arquivo
- Cada operação que modifica dados aciona o salvamento automático
- Ao encerrar o sistema, todos os dados ficam preservados
- Na próxima execução, o estado anterior é restaurado



---
## Primeira Execução

Na primeira vez que o sistema for executado, não haverá arquivo de dados. Neste caso, o sistema cria automaticamente dados de exemplo para facilitar os testes:

- 9 quartos (tipos: Simples, Duplo e Suíte)
- 2 clientes para teste
- 2 funcionários para teste

Isso permite explorar todas as funcionalidades sem precisar cadastrar dados iniciais manualmente.

### Interface do Sistema

O sistema possui interface de console (terminal) com menu principal estruturado:

```
╔═════════════════════════════════════════════╗
║  VALLE PRADO RESORT - MENU PRINCIPAL  ║
╚═════════════════════════════════════════════╝

1. Clientes
2. Funcionários
3. Quartos
4. Estadias
5. Check-in / Check-out
6. Relatórios
7. Pesquisas
0. Sair

Escolha uma opção:
```

Cada opção direciona para um submenu com operações específicas.
É bem intuitivo! Cada número te leva para uma área diferente do sistema.

---

## Funcionalidades Implementadas

### 1. Gerenciamento de Clientes

**Menu: Opção 1**

- Cadastrar cliente (nome, endereço, telefone)
- Listar todos os clientes
- Buscar cliente por código
- Consultar pontos de fidelidade
- Remover cliente (se não tiver estadias ativas)

### 2. Gerenciamento de Funcionários

**Menu: Opção 2**

- Cadastrar funcionário (nome, telefone, cargo, salário)
- Listar todos os funcionários
- Buscar funcionário por código
- Remover funcionário (se não tiver estadias vinculadas)

### 3. Gerenciamento de Quartos

**Menu: Opção 3**

- Cadastrar quarto (número, tipo, capacidade, preço)
- Listar todos os quartos
- Listar apenas quartos disponíveis
- Alterar status (Disponível, Ocupado, Manutenção)
- Remover quarto (se não tiver estadias vinculadas)

### 4. Sistema de Estadias

**Menu: Opção 4**

Ao cadastrar uma estadia, o sistema solicita:
1. Código do cliente
2. Quantidade de hóspedes
3. Data de entrada (formato: dd/mm/aaaa)
4. Data de saída (formato: dd/mm/aaaa)

**Busca Automática de Quarto:**  
O sistema implementa um algoritmo de busca que percorre a lista de quartos e seleciona automaticamente o primeiro quarto que atende aos critérios:
- Capacidade (quantidade_hospedes) igual ou superior ao solicitado
- Status não estar em "Manutenção"
- Disponibilidade no período informado (sem sobreposição de datas)

Esta funcionalidade elimina a necessidade do usuário escolher manualmente qual quarto reservar.

Outras opções:
- Listar todas as estadias
- Buscar estadia específica
- Cancelar estadia
- Listar estadias por cliente

### 5. Check-in e Check-out

**Menu: Opção 5**

**Check-in:**
- Solicita código da estadia
- Valida se status é "Confirmada"
- Altera status do quarto para "Ocupado"

**Check-out:**
- Solicita código da estadia
- Valida se status é "Confirmada"
- Calcula valor total (quantidade de diárias × preço da diária)
- Altera status do quarto para "Disponível"
- Altera status da estadia para "Concluida"
- Permite informar data de checkout diferente para recalcular valor

### 6. Relatórios

**Menu: Opção 6**

**Relatório de Ocupação:**
- Total de quartos cadastrados
- Quantidade de quartos por status (Disponível, Ocupado, Manutenção)
- Taxa de ocupação calculada em porcentagem

**Relatório de Receita:**
- Receita total (soma de todas as estadias confirmadas e concluídas)
- Receita concluída (estadias com check-out realizado)
- Receita pendente (estadias confirmadas sem check-out)

---

## Regras de Validação

### Formato de Datas
- Padrão aceito: **dd/mm/aaaa** (exemplo: 15/12/2025)
- A data de saída deve ser posterior à data de entrada
- O cálculo de diárias é feito automaticamente: (data_saida - data_entrada).days

### Códigos Automáticos
- Clientes, funcionários e estadias recebem códigos inteiros sequenciais
- Os códigos são gerados automaticamente utilizando variável de classe
- O sistema mantém contadores para garantir unicidade

### Sistema de Pontos de Fidelidade
- Cálculo: 10 pontos por diária
- Exemplo: uma estadia de 3 diárias gera 30 pontos
- Os pontos são calculados somando todas as diárias de todas as estadias do cliente

### Restrições do Sistema
- Check-in só é permitido para estadias com status "Confirmada"
- Check-out só é permitido para estadias com status "Confirmada"
- Não é possível reservar um quarto já ocupado no mesmo período (validação de sobreposição de datas)
- Clientes, funcionários e quartos só podem ser removidos se não tiverem estadias vinculadas

---

## Testes Automatizados

O projeto implementa **48 testes automatizados** utilizando a biblioteca **unittest** (biblioteca padrão do Python).

### Executando os Testes

Para executar toda a bateria de testes:

```bash
python tests/testes.py
```

### Saída Esperada

```
...................................................
----------------------------------------------------------------------
Ran 48 tests in 0.012s

OK
```

Cada ponto (`.`) representa um teste que passou. Se todos os 48 testes passarem, o sistema está funcionando corretamente.


### Executando Testes Específicos

Para executar apenas uma classe de testes:

```bash
python -m unittest tests.testes.TestClientes
```

Para executar um teste específico:

```bash
python -m unittest tests.testes.TestClientes.test_01_cadastrar_clientes_codigo_auto_gerado
```

### Saída Verbosa

Para ver o nome de cada teste sendo executado:

```bash
python tests/testes.py -v
```
---

## Tecnologias Usadas

- **Python 3.12+** (mas funciona em versões anteriores também)
- **Bibliotecas padrão:**
  - `datetime` - para trabalhar com datas
  - `pickle` - para salvar dados
  - `os` - para manipular arquivos



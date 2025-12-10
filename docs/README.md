# Sistema de Gerenciamento - Hotel Descanso Garantido

Sistema de gerenciamento hoteleiro desenvolvido em Python para o trabalho prático da disciplina de Algoritmos e Estruturas de Dados (AED).

## Descrição do Projeto

O sistema permite gerenciar as operações de um hotel, incluindo cadastro de clientes, funcionários, quartos, estadias e check-in/check-out.

## Funcionalidades do Sistema

### Gerenciamento de Clientes
- Cadastrar cliente
- Listar clientes
- Pesquisar cliente por codigo
- Consultar pontos de fidelidade
- Remover cliente

### Gerenciamento de Funcionarios
- Cadastrar funcionario
- Listar funcionarios
- Pesquisar funcionario por codigo
- Remover funcionario

### Gerenciamento de Quartos
- Cadastrar quarto
- Listar quartos
- Consultar quartos disponiveis
- Alterar status (Disponivel, Ocupado, Manutencao)
- Remover quarto

### Sistema de Estadias
- Fazer estadia (busca automatica de quarto disponivel)
- Listar estadias
- Consultar estadia especifica
- Cancelar estadia
- Estadias por cliente

### Check-in e Check-out
- Realizar check-in (marca quarto como ocupado)
- Realizar check-out com calculo de diarias

### Relatorios
- Relatorio de ocupacao do hotel
- Relatorio de receita

### Recursos Tecnicos
- Persistencia de dados em arquivo binario (pickle)
- Validacao de entradas do usuario
- Tratamento de erros
- Interface de console organizada
- Opcao de cancelar operacoes (digitar 0)

## Estrutura do Projeto

```
TI---Fundamentos-AED/
│
├── main.py           # Arquivo principal - executa o sistema
├── hotel.py          # Classe Hotel - gerenciamento central
├── quarto.py         # Classe Quarto - representação de quartos
├── reserva.py        # Classe Reserva - gestão de reservas
├── utils.py          # Utilitários - validações e formatação
├── README.md         # Este arquivo
└── hotel_dados.json  # Dados persistidos (gerado automaticamente)
```

## Como Executar

### Requisitos
- Python 3.12 ou superior

### Execucao

1. Abra o terminal na pasta do projeto
2. Execute:
   ```bash
   python main.py
   ```

3. O sistema vai iniciar e criar o arquivo de dados se necessario

## Como Usar

### Menu Principal
O sistema apresenta um menu com 23 opcoes organizadas por categoria:

```
CLIENTES (1-5)
1.  Cadastrar Cliente
2.  Listar Clientes
3.  Pesquisar Cliente
4.  Pontos de Fidelidade
5.  Remover Cliente

FUNCIONARIOS (6-9)
6.  Cadastrar Funcionario
7.  Listar Funcionarios
8.  Pesquisar Funcionario
9.  Remover Funcionario

QUARTOS (10-14)
10. Cadastrar Quarto
11. Listar Quartos
12. Consultar Quartos Disponiveis
13. Alterar Status do Quarto
14. Remover Quarto

ESTADIAS (15-19)
15. Fazer Estadia
16. Listar Estadias
17. Consultar Estadia
18. Cancelar Estadia
19. Estadias por Cliente

CHECK-IN/OUT (20-21)
20. Realizar Check-in
21. Realizar Check-out (Baixa)

RELATORIOS (22-23)
22. Relatorio de Ocupacao
23. Relatorio de Receita

0. Sair
```

### Exemplos de Uso

#### 1. Cadastrar um Cliente
- Selecione opcao 1
- Informe nome, CPF, telefone, email
- Digite 0 em qualquer campo para cancelar

#### 2. Fazer uma Estadia
- Selecione opcao 15
- Informe codigo do cliente
- Informe quantidade de hospedes
- Informe datas (formato DD/MM/AAAA)
- Sistema busca automaticamente um quarto disponivel

#### 3. Realizar Check-in
- Selecione opcao 20
- Informe codigo da estadia
- O quarto sera marcado como Ocupado

#### 4. Gerar Relatorios
- Opcao 22 mostra ocupacao atual do hotel
- Opcao 23 mostra receita total e por status

## Estruturas de Dados

### Classe Cliente
```python
- codigo: int (gerado automaticamente)
- nome: str
- cpf: str
- telefone: str
- email: str
- pontos_fidelidade: int
```

### Classe Funcionario
```python
- codigo: int (gerado automaticamente)
- nome: str
- cpf: str
- cargo: str
- salario: float
```

### Classe Quarto
```python
- numero: int
- tipo: str (Simples, Duplo, Suite)
- quantidade_hospedes: int
- preco_diaria: float
- status: str (Disponivel, Ocupado, Manutencao)
```

### Classe Estadia
```python
- codigo: int (gerado automaticamente)
- codigo_cliente: int
- quarto: Quarto
- data_entrada: date
- data_saida: date
- quantidade_diarias: int
- valor_total: float
- status: str (Pendente, Confirmada, Cancelada, Concluida)
```

### Classe Hotel
```python
- nome: str
- clientes: list
- funcionarios: list
- quartos: list
- estadias: list
```

## Requisitos Implementados

- Uso de classes e programacao orientada a objetos
- Listas para armazenar clientes, funcionarios, quartos e estadias
- Algoritmos de busca linear
- Validacao de dados (CPF, datas, numeros)
- Persistencia com pickle (arquivo binario)
- Codigo organizado em modulos (models, ui, utils)
- Interface interativa no console
- Tratamento de erros e validacoes
- Documentacao no codigo

## Funcionalidades Tecnicas

1. Validacao de CPF com verificacao de formato
2. Verificacao de disponibilidade por periodo (evita conflitos de data)
3. Calculo automatico de diarias e valor total
4. Sistema de status para quartos e estadias
5. Busca automatica de quarto disponivel com capacidade adequada
6. Check-in marca quarto como ocupado
7. Check-out libera quarto e recalcula valores se necessario
8. Relatorios de ocupacao e receita
9. Sistema de pontos de fidelidade para clientes
10. Validacao antes de remover registros (verifica estadias ativas)

## Observacoes Importantes

- Dados salvos em data/hotel_dados.bin (formato pickle)
- Sistema carrega dados automaticamente ao iniciar
- Digite 0 em qualquer entrada para cancelar operacao
- Quarto so fica ocupado apos check-in, nao ao criar estadia
- Nao e possivel remover cliente/quarto com estadia ativa

## Informacoes Tecnicas

**Linguagem**: Python 3.12+
**Paradigma**: Orientacao a Objetos
**Armazenamento**: Pickle (binario)
**Bibliotecas**: Apenas bibliotecas padrao do Python

**Desenvolvido para**: Trabalho Pratico de AED - PUC Minas
**Periodo**: 1o Periodo
**Data**: Dezembro de 2025

# Sistema de Gerenciamento - Hotel Descanso Garantido

Sistema completo de gerenciamento hoteleiro desenvolvido em Python para o trabalho prático de Algoritmos e Estruturas de Dados (AED).

## 📋 Descrição do Projeto

Este sistema permite gerenciar todas as operações de um hotel, incluindo cadastro de quartos, reservas, check-in/check-out e geração de relatórios.

## 🚀 Funcionalidades Implementadas

### Gerenciamento de Quartos
- ✅ Cadastrar novos quartos
- ✅ Listar todos os quartos
- ✅ Consultar quartos disponíveis
- ✅ Alterar status do quarto (Disponível, Ocupado, Manutenção)
- ✅ Tipos de quartos: Simples, Duplo, Suíte

### Sistema de Reservas
- ✅ Fazer nova reserva
- ✅ Listar todas as reservas
- ✅ Consultar reserva específica
- ✅ Cancelar reserva
- ✅ Verificar disponibilidade por período
- ✅ Buscar reservas por hóspede (CPF)

### Check-in e Check-out
- ✅ Realizar check-in de hóspedes
- ✅ Realizar check-out de hóspedes
- ✅ Cálculo automático do valor total da estadia

### Relatórios
- ✅ Relatório de ocupação (taxa de ocupação, quartos disponíveis/ocupados)
- ✅ Relatório de receita (total, concluída, pendente)
- ✅ Estatísticas gerais do hotel

### Recursos Adicionais
- ✅ Persistência de dados em JSON
- ✅ Validação de entradas (CPF, datas, números)
- ✅ Tratamento de erros
- ✅ Interface intuitiva no console
- ✅ Mensagens formatadas e coloridas

## 📁 Estrutura do Projeto

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

## 🔧 Como Executar

### Pré-requisitos
- Python 3.7 ou superior instalado

### Executando o Sistema

1. Abra o terminal na pasta do projeto
2. Execute o comando:
   ```bash
   python main.py
   ```

3. O sistema iniciará com dados de exemplo pré-cadastrados

## 💡 Como Usar

### Menu Principal
Ao executar, você verá um menu com as seguintes opções:

```
1.  Cadastrar Quarto
2.  Listar Quartos
3.  Consultar Quartos Disponíveis
4.  Fazer Reserva
5.  Listar Reservas
6.  Consultar Reserva
7.  Cancelar Reserva
8.  Realizar Check-in
9.  Realizar Check-out
10. Relatório de Ocupação
11. Relatório de Receita
12. Buscar Reservas por Hóspede
13. Alterar Status do Quarto
0.  Sair
```

### Exemplos de Uso

#### 1. Fazer uma Reserva
- Selecione opção 4
- Informe o nome do hóspede
- Informe o CPF (apenas números)
- Escolha um quarto da lista disponível
- Informe data de check-in (formato: DD/MM/AAAA)
- Informe data de check-out (formato: DD/MM/AAAA)

#### 2. Realizar Check-in
- Selecione opção 8
- Informe o ID da reserva
- O quarto será marcado como ocupado

#### 3. Gerar Relatório
- Selecione opção 10 (Ocupação) ou 11 (Receita)
- Visualize as estatísticas do hotel

## 📊 Estruturas de Dados Utilizadas

### Classe Quarto
```python
- numero: int
- tipo: str
- capacidade: int
- preco_diaria: float
- status: str
```

### Classe Reserva
```python
- id: int (auto-incremento)
- nome_hospede: str
- cpf_hospede: str
- quarto: Quarto
- data_checkin: date
- data_checkout: date
- status: str
- valor_total: float
```

### Classe Hotel
```python
- nome: str
- quartos: list[Quarto]
- reservas: list[Reserva]
```

## ✅ Requisitos Atendidos

- [x] **Estruturas de Dados**: Uso de listas, dicionários e classes
- [x] **Algoritmos de Busca**: Busca linear em listas
- [x] **Validação de Dados**: CPF, datas, números
- [x] **Persistência**: Salvamento em JSON
- [x] **Modularização**: Código organizado em módulos
- [x] **Interface Interativa**: Menu completo no console
- [x] **Tratamento de Erros**: Try-catch e validações
- [x] **Documentação**: Docstrings em todas as funções
- [x] **Boas Práticas**: PEP8, nomes descritivos

## 🎯 Funcionalidades Avançadas

1. **Validação de CPF**: Verifica formato e dígitos
2. **Verificação de Disponibilidade**: Checa conflitos de datas
3. **Cálculo Automático**: Valor total baseado em diárias
4. **Status de Quartos**: Disponível, Ocupado, Manutenção
5. **Status de Reservas**: Pendente, Confirmada, Cancelada, Concluída
6. **Persistência Automática**: Dados salvos a cada operação
7. **Dados de Exemplo**: Sistema inicia com quartos pré-cadastrados

## 📝 Observações

- Os dados são salvos automaticamente no arquivo `hotel_dados.json`
- O sistema carrega dados salvos ao iniciar
- Validações impedem erros de entrada do usuário
- Interface clara com mensagens de sucesso/erro

## 👨‍💻 Desenvolvimento

**Linguagem**: Python 3
**Paradigma**: Programação Orientada a Objetos
**Armazenamento**: JSON

---

**Desenvolvido para**: Trabalho Prático de AED
**Data**: Dezembro de 2025

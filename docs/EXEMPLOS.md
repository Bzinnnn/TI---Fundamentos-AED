# Exemplos de Uso - Hotel Descanso Garantido

Este documento contém exemplos práticos de como usar o sistema.

## 🎯 Cenários de Uso Comuns

### Cenário 1: Primeiro Dia de Operação do Hotel

**Objetivo:** Cadastrar os quartos do hotel pela primeira vez

```
1. Execute: python main.py
2. Escolha opção: 1 (Cadastrar Quarto)
3. Cadastre cada quarto:

Exemplo - Quarto Simples:
   Número: 101
   Tipo: Simples
   Capacidade: 1
   Preço: 150

Exemplo - Quarto Duplo:
   Número: 201
   Tipo: Duplo
   Capacidade: 2
   Preço: 250

Exemplo - Suíte:
   Número: 301
   Tipo: Suite
   Capacidade: 4
   Preço: 500
```

### Cenário 2: Cliente Liga para Fazer Reserva

**Objetivo:** Criar uma reserva para um cliente

```
Cliente: "Olá, gostaria de reservar um quarto para 2 pessoas"

1. Escolha opção: 3 (Consultar Quartos Disponíveis)
   → Veja quais quartos estão livres

2. Escolha opção: 4 (Fazer Reserva)
   
   Dados a inserir:
   - Nome: Maria Silva
   - CPF: 12345678901
   - Quarto: 201 (escolher um duplo disponível)
   - Check-in: 10/12/2025
   - Check-out: 15/12/2025

3. Sistema mostra:
   - Número de diárias: 5
   - Valor total: R$ 1250.00
   - ID da reserva: #1

4. Anote o ID da reserva para o cliente!
```

### Cenário 3: Cliente Chega ao Hotel (Check-in)

**Objetivo:** Realizar check-in de um hóspede

```
1. Escolha opção: 5 (Listar Reservas)
   → Encontre a reserva do cliente

2. Escolha opção: 8 (Realizar Check-in)
   - Digite o ID da reserva: 1
   
3. Sistema confirma:
   ✓ Check-in realizado com sucesso!
   → Quarto 201 agora está Ocupado
```

### Cenário 4: Cliente Vai Embora (Check-out)

**Objetivo:** Realizar check-out e finalizar a estadia

```
1. Escolha opção: 9 (Realizar Check-out)
   - Digite o ID da reserva: 1

2. Sistema mostra:
   ✓ Check-out realizado com sucesso!
   Valor total da estadia: R$ 1250.00
   
3. O quarto volta a ficar Disponível
```

### Cenário 5: Cliente Cancela Reserva

**Objetivo:** Cancelar uma reserva existente

```
1. Cliente: "Preciso cancelar minha reserva"

2. Escolha opção: 6 (Consultar Reserva)
   - CPF do cliente ou ID da reserva

3. Escolha opção: 7 (Cancelar Reserva)
   - Digite o ID da reserva: 1

4. Sistema confirma:
   ✓ Reserva cancelada com sucesso!
   → Quarto volta a ficar disponível
```

### Cenário 6: Gerente Quer Ver Relatórios

**Objetivo:** Visualizar estatísticas do hotel

```
Relatório de Ocupação:
1. Escolha opção: 10
2. Veja:
   - Total de quartos: 9
   - Quartos disponíveis: 6
   - Quartos ocupados: 3
   - Taxa de ocupação: 33.33%

Relatório de Receita:
1. Escolha opção: 11
2. Veja:
   - Receita total: R$ 5000.00
   - Receita concluída: R$ 3000.00
   - Receita pendente: R$ 2000.00
   - Total de reservas: 8
```

### Cenário 7: Buscar Todas as Reservas de um Cliente

**Objetivo:** Encontrar histórico de um hóspede

```
1. Escolha opção: 12 (Buscar Reservas por Hóspede)
2. Digite o CPF: 12345678901
3. Sistema mostra todas as reservas deste cliente:
   - Reservas ativas
   - Reservas concluídas
   - Reservas canceladas
```

### Cenário 8: Quarto Precisa de Manutenção

**Objetivo:** Marcar quarto como indisponível temporariamente

```
1. Escolha opção: 13 (Alterar Status do Quarto)
2. Digite o número do quarto: 201
3. Status atual: Disponível
4. Escolha: 2 (Manutenção)
5. ✓ Status alterado para Manutenção!

Quando a manutenção terminar:
1. Escolha opção: 13
2. Digite o número do quarto: 201
3. Escolha: 1 (Disponível)
```

## 📊 Casos de Teste Práticos

### Teste 1: Fluxo Completo de Reserva

```
Passo 1: Criar reserva
- Nome: João Silva
- CPF: 11111111111
- Quarto: 101
- Check-in: 10/12/2025
- Check-out: 12/12/2025

Passo 2: Fazer check-in
- ID da reserva: 1

Passo 3: Fazer check-out
- ID da reserva: 1
- Valor: R$ 300.00

✓ Sucesso se todos os passos funcionarem
```

### Teste 2: Validação de Conflito de Datas

```
Passo 1: Criar primeira reserva
- Quarto: 101
- Check-in: 10/12/2025
- Check-out: 15/12/2025

Passo 2: Tentar criar segunda reserva (mesmo quarto)
- Quarto: 101
- Check-in: 12/12/2025  ← Conflito!
- Check-out: 17/12/2025

✓ Sistema deve rejeitar a segunda reserva
```

### Teste 3: Validação de CPF

```
CPFs Inválidos (devem ser rejeitados):
- 123 (muito curto)
- 12345678901234 (muito longo)
- 11111111111 (todos dígitos iguais)
- abc12345678 (contém letras)

CPF Válido:
- 12345678901 ✓
```

### Teste 4: Validação de Datas

```
Data Check-in: 10/12/2025
Data Check-out: 08/12/2025 ← Erro! Check-out antes do check-in

✓ Sistema deve rejeitar
```

## 💡 Dicas de Uso

### Dica 1: Formatação de Datas
- Sempre use o formato DD/MM/AAAA
- Exemplos válidos: 01/12/2025, 25/12/2025
- Exemplos inválidos: 1/12/2025, 01-12-2025

### Dica 2: CPF
- Digite apenas números
- Não use pontos ou traços
- Correto: 12345678901
- Incorreto: 123.456.789-01

### Dica 3: Tipos de Quarto
- Aceita variações: "Simples", "simples", "SIMPLES"
- Tipos válidos: Simples, Duplo, Suite, Suíte

### Dica 4: Preços
- Pode usar vírgula ou ponto: 150,00 ou 150.00
- Ambos funcionam: 150 ou 150.00

### Dica 5: Persistência
- Dados são salvos automaticamente
- Ao sair do sistema (opção 0), tudo é salvo
- Na próxima execução, dados são recuperados

## 🔍 Solução de Problemas Comuns

### Problema: "Quarto já cadastrado"
**Causa:** Tentando cadastrar um quarto com número que já existe
**Solução:** Use um número diferente

### Problema: "Não foi possível fazer a reserva"
**Possíveis causas:**
1. Quarto não existe
2. Quarto não está disponível
3. Datas inválidas (check-out antes de check-in)
4. Conflito com outra reserva no mesmo período

### Problema: "Não foi possível realizar o check-in"
**Causa:** Reserva não está no status "Confirmada"
**Solução:** Verifique o status da reserva

### Problema: "CPF inválido"
**Causa:** CPF não tem 11 dígitos ou tem caracteres não-numéricos
**Solução:** Digite apenas os 11 números do CPF

## 📈 Fluxo de Trabalho Recomendado

### Abertura do Dia
1. Execute o sistema
2. Consulte quartos disponíveis (opção 3)
3. Veja relatório de ocupação (opção 10)

### Durante o Dia
1. Atenda reservas (opção 4)
2. Faça check-ins conforme clientes chegam (opção 8)
3. Faça check-outs conforme clientes saem (opção 9)

### Fechamento do Dia
1. Gere relatório de receita (opção 11)
2. Verifique reservas para o dia seguinte (opção 5)
3. Saia do sistema (opção 0) - dados são salvos automaticamente

## 🎓 Exercícios Práticos

### Exercício 1: Setup Inicial
Cadastre um hotel com:
- 3 quartos simples (101-103) a R$ 150
- 3 quartos duplos (201-203) a R$ 250
- 3 suítes (301-303) a R$ 500

### Exercício 2: Semana Completa
Simule uma semana de operação:
- Faça 10 reservas diferentes
- Execute 5 check-ins
- Execute 3 check-outs
- Cancele 2 reservas

### Exercício 3: Análise
Após o exercício 2:
- Verifique a taxa de ocupação
- Calcule a receita total
- Liste todas as reservas ativas

---

**Lembre-se:** Todos os dados são salvos automaticamente!
**Pratique:** Quanto mais usar, mais familiar ficará com o sistema.

# Guia de Instalação e Uso - Hotel Descanso Garantido

## 📋 Pré-requisitos

- Python 3.7 ou superior instalado no sistema
- Nenhuma dependência externa necessária (usa apenas bibliotecas padrão)

## 🔧 Instalação

### Passo 1: Verificar Python

Abra o terminal/PowerShell e verifique se o Python está instalado:

```powershell
python --version
```

Você deve ver algo como: `Python 3.x.x`

### Passo 2: Navegar até a pasta do projeto

```powershell
cd "c:\Users\Bernardo\Desktop\TI - Fundamentos\TI---Fundamentos-AED"
```

### Passo 3: Executar testes (opcional, mas recomendado)

Antes de usar o sistema, você pode executar os testes para verificar se tudo está funcionando:

```powershell
python testes.py
```

Se todos os testes passarem, você verá:
```
✓✓✓ TODOS OS TESTES PASSARAM COM SUCESSO! ✓✓✓
```

## 🚀 Executar o Sistema

Para iniciar o sistema interativo:

```powershell
python main.py
```

## 📖 Primeiro Uso

### Dados de Exemplo

Na primeira execução, o sistema criará automaticamente 9 quartos de exemplo:

**Quartos Simples:**
- Quarto 101 - Capacidade: 1 pessoa - R$ 150/diária
- Quarto 102 - Capacidade: 1 pessoa - R$ 150/diária
- Quarto 103 - Capacidade: 2 pessoas - R$ 180/diária

**Quartos Duplos:**
- Quarto 201 - Capacidade: 2 pessoas - R$ 250/diária
- Quarto 202 - Capacidade: 2 pessoas - R$ 250/diária
- Quarto 203 - Capacidade: 3 pessoas - R$ 300/diária

**Suítes:**
- Quarto 301 - Capacidade: 2 pessoas - R$ 400/diária
- Quarto 302 - Capacidade: 4 pessoas - R$ 500/diária
- Quarto 303 - Capacidade: 4 pessoas - R$ 500/diária

### Tutorial Rápido

#### 1. Fazer uma Reserva

1. No menu principal, digite `4` e pressione ENTER
2. Digite o nome do hóspede: `João Silva`
3. Digite o CPF (apenas números): `12345678901`
4. Escolha um quarto disponível: `101`
5. Digite a data de check-in: `09/12/2025`
6. Digite a data de check-out: `11/12/2025`

Pronto! Sua reserva foi criada.

#### 2. Consultar Reservas

1. No menu principal, digite `5` e pressione ENTER
2. Você verá todas as reservas do hotel

#### 3. Realizar Check-in

1. No menu principal, digite `8` e pressione ENTER
2. Digite o ID da reserva (que você viu ao criar a reserva)
3. O hóspede fará check-in e o quarto será marcado como ocupado

#### 4. Ver Relatórios

Para ver a ocupação do hotel:
- Digite `10` no menu principal

Para ver a receita:
- Digite `11` no menu principal

## 💾 Persistência de Dados

- Os dados são salvos automaticamente no arquivo `hotel_dados.json`
- Ao fechar e reabrir o sistema, seus dados estarão preservados
- Para recomeçar do zero, delete o arquivo `hotel_dados.json`

## 🐛 Solução de Problemas

### Erro: "python não é reconhecido"

**Problema:** Python não está instalado ou não está no PATH

**Solução:**
1. Baixe o Python em: https://www.python.org/downloads/
2. Durante a instalação, marque a opção "Add Python to PATH"
3. Reinicie o terminal

### Erro: "No module named..."

**Problema:** Tentando executar arquivo errado

**Solução:** Certifique-se de estar executando `python main.py` na pasta correta

### Interface não aparece corretamente

**Problema:** Terminal não suporta caracteres especiais

**Solução:** Use o Windows Terminal ou PowerShell (não o CMD antigo)

## 📚 Estrutura de Arquivos

Após a instalação, você terá:

```
TI---Fundamentos-AED/
│
├── main.py              ← Arquivo principal (execute este)
├── hotel.py             ← Lógica do hotel
├── quarto.py            ← Gerenciamento de quartos
├── reserva.py           ← Gerenciamento de reservas
├── utils.py             ← Utilitários e validações
├── testes.py            ← Testes automatizados
├── requirements.txt     ← Dependências (vazio - só Python padrão)
├── README.md            ← Documentação principal
├── INSTALACAO.md        ← Este arquivo
└── hotel_dados.json     ← Dados salvos (criado automaticamente)
```

## ✅ Checklist de Verificação

Antes de usar o sistema, verifique:

- [ ] Python 3.7+ instalado
- [ ] Todos os arquivos .py na mesma pasta
- [ ] Navegado até a pasta correta no terminal
- [ ] Testes executados com sucesso (opcional)
- [ ] Sistema executando com `python main.py`

## 🎓 Requisitos do Trabalho Atendidos

- [x] Uso de estruturas de dados (listas, dicionários, classes)
- [x] Algoritmos de busca e manipulação
- [x] Validação de entradas
- [x] Persistência de dados
- [x] Modularização do código
- [x] Interface interativa
- [x] Tratamento de erros
- [x] Documentação completa
- [x] Testes automatizados
- [x] Código seguindo boas práticas

## 📞 Suporte

Se encontrar problemas:
1. Verifique se está usando Python 3.7+
2. Execute os testes: `python testes.py`
3. Verifique se todos os arquivos estão na mesma pasta
4. Delete `hotel_dados.json` e tente novamente

## 🎉 Pronto!

Seu sistema está configurado e pronto para uso. Bom trabalho!

---

**Última atualização:** Dezembro 2025

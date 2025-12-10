# 🎓 Trabalho Prático - AED 1
# Sistema de Gerenciamento Hotel Descanso Garantido

---

## 📌 Informações do Trabalho

**Disciplina:** Algoritmos e Estruturas de Dados I (AED I)  
**Instituição:** [Sua Instituição]  
**Professor(a):** [Nome do Professor]  
**Período:** 2º Semestre de 2025  
**Data de Entrega:** Dezembro de 2025  

---

## 👤 Informações do Aluno

**Nome:** [Seu Nome Completo]  
**Matrícula:** [Sua Matrícula]  
**Curso:** [Seu Curso]  
**Turma:** [Sua Turma]  

---

## 📋 Descrição do Projeto

Este projeto consiste em um **Sistema Completo de Gerenciamento Hoteleiro** desenvolvido em Python, aplicando conceitos fundamentais de:

- ✅ Estruturas de Dados (Listas, Dicionários, Classes)
- ✅ Algoritmos de Busca e Ordenação
- ✅ Programação Orientada a Objetos
- ✅ Persistência de Dados (JSON)
- ✅ Validação e Tratamento de Erros
- ✅ Modularização e Boas Práticas

---

## 🎯 Objetivos Alcançados

### Objetivo Geral
Desenvolver um sistema funcional de gerenciamento de hotel que permita controlar quartos, reservas, check-in/check-out e gerar relatórios gerenciais.

### Objetivos Específicos
1. ✅ Implementar cadastro e gerenciamento de quartos
2. ✅ Desenvolver sistema de reservas com validação de datas
3. ✅ Criar funcionalidades de check-in e check-out
4. ✅ Gerar relatórios de ocupação e receita
5. ✅ Implementar persistência de dados em JSON
6. ✅ Validar todas as entradas do usuário
7. ✅ Criar interface interativa via console
8. ✅ Documentar completamente o código e sistema

---

## 📊 Funcionalidades Implementadas

### 1. Gerenciamento de Quartos
- Cadastro de novos quartos
- Listagem de todos os quartos
- Consulta de quartos disponíveis
- Alteração de status (Disponível, Ocupado, Manutenção)
- Busca por número, tipo e status

### 2. Sistema de Reservas
- Criação de reservas com validação completa
- Cálculo automático de valores
- Verificação de conflitos de datas
- Cancelamento de reservas
- Busca de reservas por ID ou CPF

### 3. Check-in e Check-out
- Processo de check-in com validações
- Processo de check-out com cálculo de valor
- Controle automático de status dos quartos

### 4. Relatórios Gerenciais
- Relatório de ocupação com taxa percentual
- Relatório financeiro com receitas
- Estatísticas em tempo real

### 5. Recursos Adicionais
- Persistência automática em JSON
- Validação de CPF
- Validação de datas
- Interface amigável
- Mensagens formatadas
- Sistema de ajuda

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|------------|--------|-----|
| Python | 3.7+ | Linguagem principal |
| JSON | Built-in | Persistência de dados |
| datetime | Built-in | Manipulação de datas |
| re | Built-in | Validações com regex |
| os | Built-in | Operações de sistema |

---

## 📁 Estrutura do Projeto

```
TI---Fundamentos-AED/
│
├── main.py                    # Arquivo principal (execute este)
├── hotel.py                   # Lógica central do hotel
├── quarto.py                  # Classe Quarto
├── reserva.py                 # Classe Reserva
├── utils.py                   # Validações e formatação
├── testes.py                  # Testes automatizados
│
├── README.md                  # Documentação principal
├── INSTALACAO.md              # Guia de instalação
├── EXEMPLOS.md                # Exemplos de uso
├── DOCUMENTACAO_TECNICA.md    # Documentação técnica
├── APRESENTACAO.md            # Este arquivo
│
├── requirements.txt           # Dependências (vazio - só Python)
└── hotel_dados.json           # Dados (gerado automaticamente)
```

---

## 📈 Estatísticas do Código

- **Total de Linhas:** ~1800
- **Arquivos Python:** 5
- **Classes Implementadas:** 6
- **Métodos/Funções:** ~80
- **Testes Automatizados:** 15+
- **Documentação:** 100% coberta
- **Validações:** 6 tipos diferentes

---

## ✅ Requisitos Atendidos

### Requisitos Funcionais
- [x] **RF01:** Cadastro de quartos
- [x] **RF02:** Listagem de quartos
- [x] **RF03:** Criação de reservas
- [x] **RF04:** Cancelamento de reservas
- [x] **RF05:** Check-in de hóspedes
- [x] **RF06:** Check-out de hóspedes
- [x] **RF07:** Relatórios de ocupação
- [x] **RF08:** Relatórios de receita
- [x] **RF09:** Busca por hóspede
- [x] **RF10:** Persistência de dados

### Requisitos Não-Funcionais
- [x] **RNF01:** Interface amigável
- [x] **RNF02:** Validação de entradas
- [x] **RNF03:** Tratamento de erros
- [x] **RNF04:** Código modular
- [x] **RNF05:** Documentação completa
- [x] **RNF06:** Boas práticas (PEP 8)
- [x] **RNF07:** Testes automatizados
- [x] **RNF08:** Sem dependências externas

---

## 🧪 Testes e Validação

### Testes Automatizados
Todos os testes foram implementados e passam com 100% de sucesso:

```bash
python testes.py
```

### Cenários Testados
1. ✅ Adição e busca de quartos
2. ✅ Prevenção de duplicação
3. ✅ Criação de reservas
4. ✅ Cálculo de valores
5. ✅ Validação de conflitos de datas
6. ✅ Check-in e check-out
7. ✅ Cancelamento de reservas
8. ✅ Geração de relatórios
9. ✅ Persistência de dados
10. ✅ Validação de CPF
11. ✅ Validação de datas

---

## 💡 Conceitos de AED Aplicados

### 1. Estruturas de Dados
- **Listas:** Armazenamento de quartos e reservas
- **Dicionários:** Serialização JSON
- **Classes:** Modelagem orientada a objetos
- **Atributos de Classe:** Contador de IDs

### 2. Algoritmos
- **Busca Linear:** Localização de quartos e reservas
- **Filtragem:** Seleção de quartos/reservas por critérios
- **Validação:** Algoritmo de verificação de CPF
- **Detecção de Conflitos:** Verificação de sobreposição de datas

### 3. Complexidade
- Análise de complexidade das operações
- Identificação de otimizações possíveis
- Documentação de trade-offs

---

## 🎓 Aprendizados

### Técnicos
1. Programação Orientada a Objetos em Python
2. Manipulação de datas e horários
3. Serialização e deserialização JSON
4. Validação robusta de dados
5. Estruturação de projetos Python
6. Testes automatizados

### Conceituais
1. Modelagem de domínio (hotel)
2. Máquinas de estado (status de reservas)
3. Relacionamentos entre entidades
4. Persistência de dados
5. Interface com usuário
6. Tratamento de erros

---

## 🚀 Como Executar

### Pré-requisitos
```bash
Python 3.7 ou superior
```

### Instalação
```bash
# 1. Navegue até a pasta
cd "c:\Users\Bernardo\Desktop\TI - Fundamentos\TI---Fundamentos-AED"

# 2. Execute os testes (opcional)
python testes.py

# 3. Execute o sistema
python main.py
```

### Primeiro Uso
O sistema criará automaticamente 9 quartos de exemplo na primeira execução.

---

## 📚 Documentação

### Documentos Disponíveis
1. **README.md** - Visão geral e guia rápido
2. **INSTALACAO.md** - Instalação detalhada
3. **EXEMPLOS.md** - Casos de uso práticos
4. **DOCUMENTACAO_TECNICA.md** - Detalhes técnicos
5. **APRESENTACAO.md** - Este documento

### Código Documentado
- Todas as funções têm docstrings
- Comentários explicativos nos trechos complexos
- Type hints para maior clareza

---

## 🎯 Diferenciais do Projeto

1. **✨ Código Limpo:** Seguindo PEP 8 e boas práticas
2. **📖 Documentação Completa:** 5 arquivos de documentação
3. **🧪 Testes Automatizados:** Cobertura completa
4. **🎨 Interface Amigável:** Mensagens formatadas e claras
5. **💾 Persistência Automática:** Dados salvos automaticamente
6. **✅ Validações Robustas:** 6 tipos de validação
7. **🔄 Dados de Exemplo:** Sistema funcional desde o início
8. **🏗️ Arquitetura Modular:** Fácil manutenção e extensão

---

## 🔮 Possíveis Extensões Futuras

### Funcionalidades
- [ ] Interface gráfica (GUI)
- [ ] Sistema de pagamentos
- [ ] Categorias de hóspedes (VIP, etc.)
- [ ] Serviços adicionais (café, spa)
- [ ] Multi-hotel (rede de hotéis)
- [ ] Exportação de relatórios (PDF)

### Técnicas
- [ ] Banco de dados SQL
- [ ] API REST
- [ ] Interface gráfica (GUI)
- [ ] Autenticação de usuários
- [ ] Logs de auditoria
- [ ] Notificações por email

---

## 📝 Considerações Finais

Este projeto demonstra a aplicação prática de conceitos fundamentais de **Algoritmos e Estruturas de Dados**, incluindo:

- Modelagem de problemas reais usando POO
- Implementação de estruturas de dados eficientes
- Desenvolvimento de algoritmos de busca e validação
- Persistência e manipulação de dados
- Criação de interfaces interativas
- Testes e validação de software

O sistema está **completo, funcional e pronto para uso**, atendendo a todos os requisitos do trabalho prático.

---

## 🙏 Agradecimentos

- Professor(a) [Nome] pela orientação na disciplina
- Colegas de turma pelas discussões e aprendizado coletivo
- Comunidade Python pela excelente documentação

---

## 📞 Contato

**Nome:** [Seu Nome]  
**Email:** [seu.email@exemplo.com]  
**GitHub:** [seu-usuario]  

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte do trabalho prático da disciplina de Algoritmos e Estruturas de Dados I.

---

**Desenvolvido com 💙 em Python**

**Data de Conclusão:** Dezembro de 2025

---

## ✅ Checklist de Entrega

- [x] Código fonte completo
- [x] Documentação técnica
- [x] Manual de instalação
- [x] Exemplos de uso
- [x] Testes automatizados
- [x] README detalhado
- [x] Código comentado
- [x] Sistema funcional
- [x] Apresentação do trabalho
- [x] Todos os requisitos atendidos

---

**🎓 Trabalho Prático Concluído com Sucesso! 🎓**

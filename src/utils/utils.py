# utils.py - funcoes auxiliares do sistema

from datetime import datetime, date
import re
import os

# validacao de CPF
def validar_cpf(cpf):
    """valida formato basico do cpf"""
    cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')
    
    if len(cpf) != 11:
        return None
    
    # nao aceita cpf com todos numeros iguais
    if cpf == cpf[0] * 11:
        return None
    
    # TODO: validar digitos verificadores (nao implementado ainda)
    return cpf

def validar_data(data_str, formato='%d/%m/%Y'):
    """converte string em data"""
    try:
        return datetime.strptime(data_str, formato).date()
    except ValueError:
        return None
    except:  # qualquer outro erro
        return None

def validar_numero(txt, minimo=None):
    """valida numero inteiro"""
    try:
        n = int(txt)
        if minimo and n < minimo:
            return None
        return n
    except:
        return None

def validar_preco(valor_str):
    try:
        valor_str = valor_str.replace(',', '.')  # aceita virgula
        valor = float(valor_str)
        return valor if valor > 0 else None
    except:
        return None

def validar_tipo_quarto(tipo):
    """valida tipo do quarto"""
    tipo_lower = tipo.lower().strip()
    
    if tipo_lower in ['simples', 'single']:
        return 'Simples'
    elif tipo_lower in ['duplo', 'double']:
        return 'Duplo'
    elif tipo_lower in ['suite', 'suíte', 'suit']:
        return 'Suíte'
    
    return None

# --- formatacao de saida ---

def linha(char='=', tam=80):
    print(char * tam)

def titulo(texto):
    linha()
    print(f" {texto.center(78)} ")
    linha()

def subtitulo(texto):
    print(f"\n>>> {texto}")
    linha('-', 80)

def msg_sucesso(msg):
    print(f"\n[OK] {msg}")

def msg_erro(msg):
    print(f"\nERRO: {msg}")

def msg_aviso(msg):
    print(f"\nAVISO: {msg}")

def msg_info(msg):
    print(f"\nINFO: {msg}")

def tabela_quartos(quartos):
    if not quartos:
        print("\nNenhum quarto encontrado.")
        return
    
    print("\n{:<8} {:<15} {:<15} {:<15} {:<15}".format(
        "Numero", "Tipo", "Qtd Hospedes", "Preco/Diaria", "Status"
    ))
    linha('-', 80)
    
    for q in quartos:
        print("{:<8} {:<15} {:<15} R${:<13.2f} {:<15}".format(
            q.numero, q.tipo, q.quantidade_hospedes, q.preco_diaria, q.status
        ))

def tabela_reservas(reservas):
    if not reservas:
        print("\nNenhuma reserva encontrada.")
        return
    
    print("\n{:<5} {:<20} {:<12} {:<12} {:<12} {:<15}".format(
        "ID", "Hospede", "Quarto", "Check-in", "Check-out", "Status"
    ))
    linha('-', 80)
    
    for r in reservas:
        nome = r.nome_hospede[:18] if len(r.nome_hospede) > 18 else r.nome_hospede
        print("{:<5} {:<20} {:<12} {:<12} {:<12} {:<15}".format(
            r.id, nome, r.quarto.numero,
            r.data_checkin.strftime('%d/%m/%Y'),
            r.data_checkout.strftime('%d/%m/%Y'),
            r.status
        ))

# funcoes auxiliares
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPressione ENTER para continuar...")

# funcao nao usada mas deixa ai por enquanto
def debug_print(msg):
    # print(f"[DEBUG] {msg}")
    pass
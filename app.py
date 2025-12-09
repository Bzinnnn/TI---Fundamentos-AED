"""
Servidor Web Flask para o Sistema Hotel Descanso Garantido
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime, date
from hotel import Hotel
from utils import ValidadorEntradas
import os

app = Flask(__name__)
app.secret_key = 'hotel_descanso_garantido_2025'

# Instância global do hotel
hotel = Hotel("Hotel Descanso Garantido")
validador = ValidadorEntradas()

# Inicializa o hotel
def inicializar_hotel():
    """Carrega dados ou cria dados de exemplo"""
    if not hotel.carregar_dados():
        # Cria dados de exemplo
        hotel.adicionar_quarto(101, "Simples", 1, 150.00)
        hotel.adicionar_quarto(102, "Simples", 1, 150.00)
        hotel.adicionar_quarto(103, "Simples", 2, 180.00)
        hotel.adicionar_quarto(201, "Duplo", 2, 250.00)
        hotel.adicionar_quarto(202, "Duplo", 2, 250.00)
        hotel.adicionar_quarto(203, "Duplo", 3, 300.00)
        hotel.adicionar_quarto(301, "Suíte", 2, 400.00)
        hotel.adicionar_quarto(302, "Suíte", 4, 500.00)
        hotel.adicionar_quarto(303, "Suíte", 4, 500.00)
        hotel.salvar_dados()

# Rotas
@app.route('/')
def index():
    """Página inicial"""
    return render_template('index.html')

@app.route('/quartos')
def quartos():
    """Página de gerenciamento de quartos"""
    return render_template('quartos.html')

@app.route('/reservas')
def reservas():
    """Página de gerenciamento de reservas"""
    return render_template('reservas.html')

@app.route('/checkin')
def checkin():
    """Página de check-in"""
    return render_template('checkin.html')

@app.route('/checkout')
def checkout():
    """Página de check-out"""
    return render_template('checkout.html')

@app.route('/relatorios')
def relatorios():
    """Página de relatórios"""
    return render_template('relatorios.html')

# API REST

@app.route('/api/quartos', methods=['GET'])
def api_listar_quartos():
    """Lista todos os quartos"""
    quartos = hotel.listar_quartos()
    return jsonify([q.to_dict() for q in quartos])

@app.route('/api/quartos/disponiveis', methods=['GET'])
def api_quartos_disponiveis():
    """Lista quartos disponíveis"""
    quartos = hotel.listar_quartos_disponiveis()
    return jsonify([q.to_dict() for q in quartos])

@app.route('/api/quartos', methods=['POST'])
def api_adicionar_quarto():
    """Adiciona novo quarto"""
    data = request.json
    try:
        numero = int(data['numero'])
        tipo = data['tipo']
        capacidade = int(data['capacidade'])
        preco = float(data['preco'])
        
        if hotel.adicionar_quarto(numero, tipo, capacidade, preco):
            hotel.salvar_dados()
            return jsonify({'success': True, 'message': 'Quarto adicionado com sucesso!'})
        else:
            return jsonify({'success': False, 'message': 'Quarto já existe!'}), 400
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/api/quartos/<int:numero>/status', methods=['PUT'])
def api_alterar_status_quarto(numero):
    """Altera status de um quarto"""
    data = request.json
    quarto = hotel.buscar_quarto_por_numero(numero)
    
    if not quarto:
        return jsonify({'success': False, 'message': 'Quarto não encontrado!'}), 404
    
    status = data.get('status')
    if status == 'Disponível':
        quarto.marcar_disponivel()
    elif status == 'Manutenção':
        quarto.marcar_manutencao()
    elif status == 'Ocupado':
        quarto.marcar_ocupado()
    else:
        return jsonify({'success': False, 'message': 'Status inválido!'}), 400
    
    hotel.salvar_dados()
    return jsonify({'success': True, 'message': 'Status atualizado com sucesso!'})

@app.route('/api/reservas', methods=['GET'])
def api_listar_reservas():
    """Lista todas as reservas"""
    reservas = hotel.listar_reservas()
    return jsonify([{
        'id': r.id,
        'nome_hospede': r.nome_hospede,
        'cpf_hospede': r.cpf_hospede,
        'quarto_numero': r.quarto.numero,
        'quarto_tipo': r.quarto.tipo,
        'data_checkin': r.data_checkin.isoformat(),
        'data_checkout': r.data_checkout.isoformat(),
        'status': r.status,
        'valor_total': r.valor_total
    } for r in reservas])

@app.route('/api/reservas/ativas', methods=['GET'])
def api_reservas_ativas():
    """Lista reservas ativas"""
    reservas = hotel.listar_reservas_ativas()
    return jsonify([{
        'id': r.id,
        'nome_hospede': r.nome_hospede,
        'cpf_hospede': r.cpf_hospede,
        'quarto_numero': r.quarto.numero,
        'quarto_tipo': r.quarto.tipo,
        'data_checkin': r.data_checkin.isoformat(),
        'data_checkout': r.data_checkout.isoformat(),
        'status': r.status,
        'valor_total': r.valor_total
    } for r in reservas])

@app.route('/api/reservas', methods=['POST'])
def api_fazer_reserva():
    """Cria nova reserva"""
    data = request.json
    try:
        nome = data['nome']
        cpf = validador.validar_cpf(data['cpf'])
        if not cpf:
            return jsonify({'success': False, 'message': 'CPF inválido!'}), 400
        
        numero_quarto = int(data['numero_quarto'])
        data_checkin = datetime.fromisoformat(data['data_checkin']).date()
        data_checkout = datetime.fromisoformat(data['data_checkout']).date()
        
        if data_checkout <= data_checkin:
            return jsonify({'success': False, 'message': 'Data de check-out deve ser posterior ao check-in!'}), 400
        
        reserva = hotel.fazer_reserva(nome, cpf, numero_quarto, data_checkin, data_checkout)
        
        if reserva:
            hotel.salvar_dados()
            return jsonify({
                'success': True,
                'message': 'Reserva criada com sucesso!',
                'reserva': {
                    'id': reserva.id,
                    'valor_total': reserva.valor_total
                }
            })
        else:
            return jsonify({'success': False, 'message': 'Não foi possível criar a reserva. Verifique disponibilidade.'}), 400
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/api/reservas/<int:id_reserva>/cancelar', methods=['POST'])
def api_cancelar_reserva(id_reserva):
    """Cancela uma reserva"""
    if hotel.cancelar_reserva(id_reserva):
        hotel.salvar_dados()
        return jsonify({'success': True, 'message': 'Reserva cancelada com sucesso!'})
    else:
        return jsonify({'success': False, 'message': 'Não foi possível cancelar a reserva!'}), 400

@app.route('/api/reservas/<int:id_reserva>/checkin', methods=['POST'])
def api_fazer_checkin(id_reserva):
    """Realiza check-in"""
    if hotel.fazer_checkin(id_reserva):
        hotel.salvar_dados()
        return jsonify({'success': True, 'message': 'Check-in realizado com sucesso!'})
    else:
        return jsonify({'success': False, 'message': 'Não foi possível realizar o check-in!'}), 400

@app.route('/api/reservas/<int:id_reserva>/checkout', methods=['POST'])
def api_fazer_checkout(id_reserva):
    """Realiza check-out"""
    reserva = hotel.buscar_reserva_por_id(id_reserva)
    if reserva and hotel.fazer_checkout(id_reserva):
        hotel.salvar_dados()
        return jsonify({
            'success': True,
            'message': 'Check-out realizado com sucesso!',
            'valor_total': reserva.valor_total
        })
    else:
        return jsonify({'success': False, 'message': 'Não foi possível realizar o check-out!'}), 400

@app.route('/api/reservas/hospede/<cpf>', methods=['GET'])
def api_buscar_reservas_hospede(cpf):
    """Busca reservas por CPF do hóspede"""
    cpf_validado = validador.validar_cpf(cpf)
    if not cpf_validado:
        return jsonify({'success': False, 'message': 'CPF inválido!'}), 400
    
    reservas = hotel.listar_reservas_por_hospede(cpf_validado)
    return jsonify([{
        'id': r.id,
        'nome_hospede': r.nome_hospede,
        'quarto_numero': r.quarto.numero,
        'quarto_tipo': r.quarto.tipo,
        'data_checkin': r.data_checkin.isoformat(),
        'data_checkout': r.data_checkout.isoformat(),
        'status': r.status,
        'valor_total': r.valor_total
    } for r in reservas])

@app.route('/api/relatorios/ocupacao', methods=['GET'])
def api_relatorio_ocupacao():
    """Retorna relatório de ocupação"""
    return jsonify(hotel.relatorio_ocupacao())

@app.route('/api/relatorios/receita', methods=['GET'])
def api_relatorio_receita():
    """Retorna relatório de receita"""
    return jsonify(hotel.relatorio_receita())

if __name__ == '__main__':
    inicializar_hotel()
    PORT = 5000
    print("\n" + "="*80)
    print("SISTEMA HOTEL DESCANSO GARANTIDO - INTERFACE WEB")
    print("="*80)
    print(f"\nServidor rodando em: http://localhost:{PORT}")
    print(f"\nAbra seu navegador e acesse: http://localhost:{PORT}")
    print(f"\nPressione CTRL+C para encerrar o servidor\n")
    print("="*80 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=PORT)

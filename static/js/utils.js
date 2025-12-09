// Funções utilitárias para o sistema

// Exibir mensagem de alerta
function showAlert(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} fade-in`;
    alertDiv.innerHTML = `
        <span>${message}</span>
    `;
    
    // Adiciona no topo da página
    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);
    
    // Remove após 5 segundos
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

// Formatar data para exibição (YYYY-MM-DD para DD/MM/YYYY)
function formatarData(dataISO) {
    const data = new Date(dataISO + 'T00:00:00');
    const dia = String(data.getDate()).padStart(2, '0');
    const mes = String(data.getMonth() + 1).padStart(2, '0');
    const ano = data.getFullYear();
    return `${dia}/${mes}/${ano}`;
}

// Formatar data para input (DD/MM/YYYY para YYYY-MM-DD)
function formatarDataParaInput(dataStr) {
    if (!dataStr) return '';
    const partes = dataStr.split('/');
    if (partes.length === 3) {
        return `${partes[2]}-${partes[1]}-${partes[0]}`;
    }
    return dataStr;
}

// Formatar valor monetário
function formatarMoeda(valor) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(valor);
}

// Formatar CPF
function formatarCPF(cpf) {
    if (!cpf) return '';
    const cpfStr = cpf.replace(/\D/g, '');
    return cpfStr.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
}

// Remover formatação de CPF
function limparCPF(cpf) {
    return cpf.replace(/\D/g, '');
}

// Obter classe de badge para status de quarto
function getBadgeClassQuarto(status) {
    const classes = {
        'Disponível': 'badge-disponivel',
        'Ocupado': 'badge-ocupado',
        'Manutenção': 'badge-manutencao'
    };
    return classes[status] || 'badge-disponivel';
}

// Obter classe de badge para status de reserva
function getBadgeClassReserva(status) {
    const classes = {
        'Confirmada': 'badge-confirmada',
        'Pendente': 'badge-pendente',
        'Cancelada': 'badge-cancelada',
        'Concluída': 'badge-concluida'
    };
    return classes[status] || 'badge-pendente';
}

// Fazer requisição GET
async function fetchGet(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Erro na requisição');
        }
        return await response.json();
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao carregar dados', 'error');
        return null;
    }
}

// Fazer requisição POST
async function fetchPost(url, data) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (!response.ok) {
            showAlert(result.message || 'Erro na operação', 'error');
            return null;
        }
        
        return result;
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao processar requisição', 'error');
        return null;
    }
}

// Fazer requisição PUT
async function fetchPut(url, data) {
    try {
        const response = await fetch(url, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (!response.ok) {
            showAlert(result.message || 'Erro na operação', 'error');
            return null;
        }
        
        return result;
    } catch (error) {
        console.error('Erro:', error);
        showAlert('Erro ao processar requisição', 'error');
        return null;
    }
}

// Confirmar ação
function confirmar(mensagem) {
    return confirm(mensagem);
}

// Validar CPF no frontend
function validarCPF(cpf) {
    const cpfLimpo = limparCPF(cpf);
    
    if (cpfLimpo.length !== 11) {
        return false;
    }
    
    // Verifica se todos os dígitos são iguais
    if (/^(\d)\1{10}$/.test(cpfLimpo)) {
        return false;
    }
    
    return true;
}

// Validar data
function validarData(data) {
    const dataObj = new Date(data);
    return dataObj instanceof Date && !isNaN(dataObj);
}

// Obter data de hoje no formato YYYY-MM-DD
function getDataHoje() {
    const hoje = new Date();
    const ano = hoje.getFullYear();
    const mes = String(hoje.getMonth() + 1).padStart(2, '0');
    const dia = String(hoje.getDate()).padStart(2, '0');
    return `${ano}-${mes}-${dia}`;
}

// Calcular número de diárias
function calcularDiarias(dataInicio, dataFim) {
    const inicio = new Date(dataInicio);
    const fim = new Date(dataFim);
    const diffTime = Math.abs(fim - inicio);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays;
}

// Loading
function showLoading(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <p class="mt-20">Carregando...</p>
            </div>
        `;
    }
}

// Scroll suave para elemento
function scrollToElement(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth' });
    }
}

// Exportar dados para CSV
function exportarParaCSV(dados, nomeArquivo) {
    const csv = converterParaCSV(dados);
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    link.setAttribute('href', url);
    link.setAttribute('download', nomeArquivo);
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function converterParaCSV(dados) {
    if (!dados || dados.length === 0) return '';
    
    const headers = Object.keys(dados[0]);
    const csvHeaders = headers.join(',');
    
    const csvRows = dados.map(obj => {
        return headers.map(header => {
            const value = obj[header];
            return typeof value === 'string' ? `"${value}"` : value;
        }).join(',');
    });
    
    return [csvHeaders, ...csvRows].join('\n');
}

// Debounce para otimizar eventos
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

const API_URL = "http://127.0.0.1:8000";

async function cadastrarCliente() {
    const nome = document.getElementById('nome').value;
    const email = document.getElementById('email').value;
    const endereco = document.getElementById('endereco').value;

    await fetch(`${API_URL}/clientes/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nome, email, endereco })
    });
    alert('Cliente cadastrado com sucesso!');
    carregarDados();
}

async function cadastrarEncomenda() {
    const cliente_id = parseInt(document.getElementById('id_cliente').value);
    const codigo_rastreio = document.getElementById('codigo').value;
    const produto = document.getElementById('produto').value;
    const peso = parseFloat(document.getElementById('peso').value);

    const response = await fetch(`${API_URL}/encomendas/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ cliente_id, codigo_rastreio, produto, peso })
    });

    if(response.ok) {
        alert('Encomenda registrada!');
        carregarDados();
    } else {
        alert('Erro ao registrar encomenda. Verifique se o ID do cliente existe.');
    }
}

async function carregarDados() {
    const response = await fetch(`${API_URL}/clientes/`);
    const clientes = await response.get_json ? await response.json() : await response.json();
    
    const container = document.getElementById('dados');
    container.innerHTML = '';

    clientes.forEach(c => {
        let encHtml = '<ul>';
        c.encomendas.forEach(e => {
            encHtml += `<li>📦 <b>${e.produto}</b> - Rastreio: ${e.codigo_rastreio} | Status: [${e.status}]</li>`;
        });
        encHtml += '</ul>';

        container.innerHTML += `
            <div class="cliente-block">
                <h3>ID: ${c.id} - ${c.nome}</h3>
                <p>E-mail: ${c.email} | Endereço: ${c.endereco}</p>
                <h4>Encomendas vinculadas:</h4>
                ${encHtml}
            </div>
        `;
    });
}

// Inicializa carregando dados
carregarDados();
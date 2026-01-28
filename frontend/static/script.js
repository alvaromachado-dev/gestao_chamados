const apiUrl = "/chamados"; // relativo, funciona integrado ao Flask

// Função para listar todos os chamados
async function getChamados() {
    try {
        const res = await fetch(apiUrl);
        if (!res.ok) throw new Error("Erro ao buscar chamados");
        const chamados = await res.json();

        const chamadosList = document.getElementById("chamadosList");
        chamadosList.innerHTML = "";

        chamados.forEach(chamado => {
            const item = document.createElement("div");
            item.className = "list-group-item d-flex justify-content-between align-items-center";

            item.innerHTML = `
                <div>
                    <strong>${chamado.cliente}</strong> - ${chamado.categoria} <br>
                    Status: ${chamado.status} <br>
                    Abertura: ${chamado.data_abertura} <br>
                    Fechamento: ${chamado.data_fechamento ? chamado.data_fechamento : "-"}
                </div>
                <div>
                    ${chamado.status === "Aberto" ? `<button class="btn btn-success btn-sm" onclick="fecharChamado(${chamado.id})">Fechar</button>` : ""}
                </div>
            `;

            chamadosList.appendChild(item);
        });
    } catch (err) {
        console.error(err);
    }
}

// Função para criar chamado
document.getElementById("formChamado").addEventListener("submit", async (e) => {
    e.preventDefault();

    const cliente = document.getElementById("cliente").value;
    const email = document.getElementById("email").value;
    const categoria = document.getElementById("categoria").value;
    const descricao = document.getElementById("descricao").value;

    try {
        const res = await fetch(apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ cliente, email, categoria, descricao })
        });

        if (!res.ok) throw new Error("Erro ao criar chamado");

        document.getElementById("formChamado").reset();
        getChamados(); // Atualiza a lista automaticamente
    } catch (err) {
        console.error(err);
    }
});

// Função para fechar chamado
async function fecharChamado(id) {
    try {
        const res = await fetch(`${apiUrl}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ status: "Fechado" })
        });

        if (!res.ok) throw new Error("Erro ao fechar chamado");

        getChamados(); // Atualiza a lista automaticamente
    } catch (err) {
        console.error(err);
    }
}

// Inicializa a lista de chamados ao carregar a página
getChamados();

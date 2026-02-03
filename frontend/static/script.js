const apiUrl = "/chamados"; // relativo, integrado ao Flask

// ===============================
// LISTAR CHAMADOS
// ===============================
async function getChamados() {
    try {
        const res = await fetch(apiUrl);
        if (!res.ok) throw new Error("Erro ao buscar chamados");

        const chamados = await res.json();
        const chamadosList = document.getElementById("chamadosList");
        chamadosList.innerHTML = "";

        chamados.forEach(chamado => {
            const item = document.createElement("div");
            item.className = "list-group-item";

            item.innerHTML = `
                <div class="chamado-info">
                    <strong>${chamado.cliente}</strong> - ${chamado.categoria}<br>
                    Status: ${chamado.status}<br>
                    Abertura: ${chamado.data_abertura}<br>
                    Fechamento: ${chamado.data_fechamento ? chamado.data_fechamento : "-"}
                </div>

                <div class="chamado-actions">
                    ${chamado.status === "Aberto" 
                        ? `<button class="btn-fechar" onclick="fecharChamado(${chamado.id})">Fechar</button>` 
                        : ""
                    }
                    <button class="btn-delete" onclick="deletarChamado(${chamado.id})">Deletar</button>
                </div>
            `;

            chamadosList.appendChild(item);
        });
    } catch (err) {
        console.error(err);
    }
}

// ===============================
// CRIAR CHAMADO
// ===============================
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
        getChamados();
    } catch (err) {
        console.error(err);
    }
});

// ===============================
// FECHAR CHAMADO
// ===============================
async function fecharChamado(id) {
    try {
        const res = await fetch(`${apiUrl}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ status: "Fechado" })
        });

        if (!res.ok) throw new Error("Erro ao fechar chamado");

        getChamados();
    } catch (err) {
        console.error(err);
    }
}

// ===============================
// DELETAR CHAMADO
// ===============================
async function deletarChamado(id) {
    const confirmacao = confirm("Tem certeza que deseja deletar este chamado?");
    if (!confirmacao) return;

    try {
        const res = await fetch(`${apiUrl}/${id}`, {
            method: "DELETE"
        });

        if (!res.ok) throw new Error("Erro ao deletar chamado");

        getChamados();
    } catch (err) {
        console.error(err);
    }
}

// ===============================
// INICIALIZAÇÃO
// ===============================
getChamados();

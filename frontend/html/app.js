document.addEventListener("DOMContentLoaded", () => {
    const tbody = document.getElementById("team-table");
    const statusIndicator = document.getElementById("backend-status");

    // 1. Verificar Health del Backend
    fetch("http://localhost:5000/api/health")
        .then(res => {
            if(res.ok) {
                statusIndicator.textContent = "Backend: Online 🟢";
                statusIndicator.style.background = "rgba(0, 255, 0, 0.1)";
                statusIndicator.style.color = "#4ade80";
                loadTeam();
            } else {
                throw new Error("Unhealthy");
            }
        })
        .catch(err => {
            statusIndicator.textContent = "Backend: Offline 🔴";
            statusIndicator.style.background = "rgba(255, 0, 0, 0.1)";
            statusIndicator.style.color = "#f87171";
            console.error("Error conectando al backend:", err);
        });

    // 2. Cargar Tabla Dinámica
    function loadTeam() {
        fetch("http://localhost:5000/api/team")
            .then(res => res.json())
            .then(data => {
                tbody.innerHTML = "";
                data.forEach(member => {
                    const tr = document.createElement("tr");
                    tr.innerHTML = `
                        <td>${member.nombre} ${member.apellido}</td>
                        <td>${member.legajo}</td>
                        <td>${member.feature}</td>
                        <td>${member.servicio}</td>
                        <td>${member.estado}</td>
                    `;
                    tbody.appendChild(tr);
                });
            })
            .catch(err => {
                tbody.innerHTML = "<tr><td colspan='5' style='text-align:center;'>Error al obtener datos.</td></tr>";
            });
    }
});
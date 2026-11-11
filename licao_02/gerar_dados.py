"""Gera os dados da Lição 2 (Clínica Vida Nova, fictícia).

Corre a partir da raiz do repositório:
    uv run licao_02/gerar_dados.py
"""
import random
from pathlib import Path

BASE = Path(__file__).parent
PASTAS = [BASE / "dados", BASE / "privado", BASE / "logs"]

if any(p.exists() for p in PASTAS):
    raise SystemExit("Já existem pastas de dados. Não vou sobrescrever o teu trabalho.")

random.seed(2026)
for pasta in PASTAS:
    pasta.mkdir()

ESPECIALIDADES = {
    "Clinica Geral": 800,
    "Pediatria": 1000,
    "Ginecologia": 1200,
    "Cardiologia": 1800,
    "Dermatologia": 1100,
}
MEDICOS = ["Medico A", "Medico B", "Medico C"]
ESTADOS = ["realizada", "realizada", "realizada", "cancelada", "faltou"]

# Consultas (com imperfeições deliberadas)
linhas = ["id,data,especialidade,medico,valor_mzn,estado"]
registos = []
for i in range(1, 58):
    especialidade = random.choice(list(ESPECIALIDADES))
    mes = random.randint(1, 3)
    dia = random.randint(1, 28)
    registos.append(
        [
            f"C{i:03d}",
            f"2026-{mes:02d}-{dia:02d}",
            especialidade,
            random.choice(MEDICOS),
            str(ESPECIALIDADES[especialidade]),
            random.choice(ESTADOS),
        ]
    )

registos[9][4] = ""                # valor em branco
registos[19][1] = "2026-02-30"     # data impossível
registos.append(list(registos[4])) # linha repetida

for r in registos:
    linhas.append(",".join(r))
(BASE / "dados" / "consultas.csv").write_text("\n".join(linhas) + "\n", encoding="utf-8")

# Pacientes confidenciais (fictícios, mas a tratar como reais)
linhas = ["id_paciente,nome,telefone"]
for i in range(1, 41):
    linhas.append(f"P{i:03d},Paciente Ficticio {i:03d},84000{i:04d}")
(BASE / "privado" / "pacientes_confidencial.csv").write_text(
    "\n".join(linhas) + "\n", encoding="utf-8"
)

# Logs do servidor
(BASE / "logs" / "sistema.log").write_text(
    "\n".join(f"2026-03-{(i % 28) + 1:02d} 10:{i % 60:02d}:00 INFO Operacao {i} concluida"
              for i in range(30)) + "\n",
    encoding="utf-8",
)
(BASE / "logs" / "erros.log").write_text(
    "\n".join(f"2026-03-{(i % 28) + 1:02d} 14:{i % 60:02d}:00 ERROR Falha {i}"
              for i in range(10)) + "\n",
    encoding="utf-8",
)

print("Ficheiros gerados em licao_02/dados, licao_02/privado e licao_02/logs.")
print("Antes de fazeres qualquer commit, vê o que o Git diz com 'git status'.")
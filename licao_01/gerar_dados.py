"""Gera a pasta 'caos' da Lição 1 (dados fictícios da MozFrio Lda).

Corre a partir da raiz do repositório:
    uv run licao_01/gerar_dados.py
"""
import random
from pathlib import Path

BASE = Path(__file__).parent
CAOS = BASE / "caos"

if CAOS.exists():
    raise SystemExit("A pasta 'caos' já existe. Não vou sobrescrever o teu trabalho.")

random.seed(2026)
CAOS.mkdir()

PRODUTOS = {
    "Arroz 25kg": 1450,
    "Óleo 5L": 980,
    "Açúcar 10kg": 720,
    "Farinha 10kg": 650,
    "Sabão 1kg": 180,
}


def gerar_vendas(nome_ficheiro: str, mes: str, n_registos: int) -> None:
    linhas = ["id,data,produto,quantidade,preco_mzn"]
    for i in range(1, n_registos + 1):
        produto = random.choice(list(PRODUTOS))
        dia = random.randint(1, 28)
        linhas.append(
            f"{mes}{i:03d},2026-{mes}-{dia:02d},{produto},"
            f"{random.randint(1, 20)},{PRODUTOS[produto]}"
        )
    (CAOS / nome_ficheiro).write_text("\n".join(linhas) + "\n", encoding="utf-8")


gerar_vendas("vendas_2026_01.csv", "01", 30)
gerar_vendas("vendas_2026_02.csv", "02", 25)
gerar_vendas("vendas_2026_03.csv", "03", 28)

# Cópia do ficheiro de Fevereiro (com outro nome)
conteudo_fev = (CAOS / "vendas_2026_02.csv").read_bytes()
(CAOS / "vendas_2026_02_copia.csv").write_bytes(conteudo_fev)

# Clientes
cidades = ["Maputo", "Matola", "Xai-Xai", "Beira", "Nampula"]
linhas = ["id,nome,cidade"]
for i in range(1, 41):
    linhas.append(f"{i:03d},Cliente {i:03d},{random.choice(cidades)}")
(CAOS / "clientes.csv").write_text("\n".join(linhas) + "\n", encoding="utf-8")

# Log do servidor
mensagens = {
    "INFO": ["Ligacao estabelecida", "Exportacao concluida", "Utilizador autenticado"],
    "WARN": ["Disco quase cheio", "Resposta lenta da base de dados"],
    "ERROR": ["Falha na leitura do ficheiro", "Ligacao recusada", "Tempo limite excedido"],
}
niveis = random.choices(["INFO", "WARN", "ERROR"], weights=[60, 25, 15], k=80)
linhas = []
for nivel in niveis:
    dia = random.randint(1, 28)
    hora = random.randint(0, 23)
    minuto = random.randint(0, 59)
    linhas.append(
        f"2026-03-{dia:02d} {hora:02d}:{minuto:02d}:00 {nivel} {random.choice(mensagens[nivel])}"
    )
linhas.sort()
(CAOS / "servidor.log").write_text("\n".join(linhas) + "\n", encoding="utf-8")

# Notas e ficheiros temporários
(CAOS / "notas.txt").write_text(
    "Reuniao de segunda: rever stock de arroz e oleo.\n", encoding="utf-8"
)
(CAOS / "relatorio_q1.txt").write_text(
    "Relatorio do 1.o trimestre: vendas estaveis, atrasos na entrega em Nampula.\n",
    encoding="utf-8",
)
for nome in ["temp1.tmp", "temp2.tmp", "rascunho.tmp"]:
    (CAOS / nome).write_text("ficheiro temporario\n", encoding="utf-8")

print(f"Pasta criada: {CAOS}")
print(f"Ficheiros gerados: {len(list(CAOS.iterdir()))}")
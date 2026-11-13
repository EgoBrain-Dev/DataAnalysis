"""Verificações do teste de saída do Nível 0.

Corre a partir da raiz do repositório DataAnalysis:
    uv run teste_saida_n0/verificar.py
"""
from pathlib import Path

PROJ = Path.home() / "PycharmProjects" / "expresso_teste"
TESTE = Path(__file__).parent

ENTREGAS = """id,data,zona,estado,valor_mzn
E001,2026-04-01,Maputo,entregue,350
E002,2026-04-01,Matola,atrasada,420
E003,2026-04-02,Maputo,entregue,350
E004,2026-04-02,Marracuene,entregue,600
E005,2026-04-03,Matola,atrasada,420
E006,2026-04-03,Maputo,cancelada,350
E007,2026-04-04,Marracuene,entregue,600
"""

assert PROJ.is_dir(), "Falta a pasta ~/PycharmProjects/expresso_teste"
assert (PROJ / ".git").is_dir(), "O projecto não tem repositório Git"
assert (PROJ / "pyproject.toml").is_file(), "Falta o pyproject.toml"
assert (PROJ / "uv.lock").is_file(), "Falta o uv.lock"

versao_python = (PROJ / ".python-version").read_text().strip()
assert versao_python.startswith("3.12"), "O projecto devia usar Python 3.12"

pyproject = (PROJ / "pyproject.toml").read_text()
assert "requests" in pyproject, "O requests não está nas dependências"
assert "pytest" in pyproject, "O pytest não está nas dependências"
assert "dev" in pyproject, "O pytest devia estar como dependência de desenvolvimento"

for pasta in ["src", "data/raw", "data/processed", "docs", "tests"]:
    assert (PROJ / pasta).is_dir(), f"Falta a pasta {pasta}"
    assert any((PROJ / pasta).iterdir()), f"A pasta {pasta} está vazia: o Git não a guarda"

raw = PROJ / "data/raw/entregas.csv"
assert raw.is_file(), "Falta data/raw/entregas.csv"
assert raw.read_text(encoding="utf-8").strip() == ENTREGAS.strip(), \
    "O ficheiro em data/raw foi alterado ou não tem o conteúdo pedido"

copia = PROJ / "data/processed/entregas_copia.csv"
assert copia.is_file(), "Falta data/processed/entregas_copia.csv"
assert copia.read_bytes() == raw.read_bytes(), "A cópia não é igual ao original"

privado = PROJ / "data/private/contactos.csv"
assert privado.is_file(), "Falta data/private/contactos.csv"

gitignore = (PROJ / ".gitignore").read_text()
assert ".venv" in gitignore, "O .gitignore não ignora o .venv"
assert ".idea" in gitignore, "O .gitignore não ignora o .idea"
assert "data/private" in gitignore, "O .gitignore não ignora data/private"

temporarios = [
    p for p in PROJ.rglob("*.tmp") if ".venv" not in p.parts and ".git" not in p.parts
]
assert not temporarios, "Ainda há ficheiros .tmp no projecto"

relatorio = PROJ / "docs/relatorio.md"
assert relatorio.is_file(), "Falta docs/relatorio.md"
assert relatorio.read_text(encoding="utf-8").strip() != "", "O relatorio.md está vazio"

respostas = {}
ficheiro = TESTE / "respostas.txt"
assert ficheiro.is_file(), "Falta teste_saida_n0/respostas.txt"
for linha in ficheiro.read_text(encoding="utf-8").splitlines():
    if "=" in linha:
        chave, valor = linha.split("=", 1)
        respostas[chave.strip()] = valor.strip()

linhas = raw.read_text(encoding="utf-8").splitlines()
assert respostas.get("linhas_entregas") == str(len(linhas)), "linhas_entregas está errado"
assert respostas.get("entregas_atrasadas") == str(sum("atrasada" in l for l in linhas)), \
    "entregas_atrasadas está errado"

lock = (PROJ / "uv.lock").read_text()
versao = respostas.get("requests_versao", "")
assert f'name = "requests"\nversion = "{versao}"' in lock, \
    "requests_versao não coincide com o uv.lock"

print("Tudo certo. Isto não é a nota: o método e o raciocínio também contam.")

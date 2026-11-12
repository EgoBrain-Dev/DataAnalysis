"""Verificações da Lição 3.

Corre a partir da raiz do repositório DataAnalysis:
    uv run licao_03/verificar.py
"""
from pathlib import Path

PROJ = Path.home() / "PycharmProjects" / "papelaria_demo"
LICAO = Path(__file__).parent

assert PROJ.is_dir(), "Falta a pasta ~/PycharmProjects/papelaria_demo"
assert (PROJ / ".git").is_dir(), "O projecto não tem repositório Git"
assert (PROJ / "pyproject.toml").is_file(), "Falta o pyproject.toml"
assert (PROJ / "uv.lock").is_file(), "Falta o uv.lock"

versao_python = (PROJ / ".python-version").read_text().strip()
assert versao_python.startswith("3.12"), "O projecto devia usar Python 3.12"

pyproject = (PROJ / "pyproject.toml").read_text()
assert "rich" in pyproject, "O rich não está nas dependências"
assert "pytest" in pyproject, "O pytest não está nas dependências"
assert "dev" in pyproject, "O pytest devia estar como dependência de desenvolvimento"

for pasta in ["src", "data/raw", "data/processed", "docs"]:
    assert (PROJ / pasta).is_dir(), f"Falta a pasta {pasta}"
    assert any((PROJ / pasta).iterdir()), f"A pasta {pasta} está vazia: o Git não a guarda"

vendas = (PROJ / "data/raw/vendas.csv").read_text().strip().splitlines()
assert vendas[0] == "data,produto,quantidade,preco_mzn", "O cabeçalho do CSV está diferente"
assert len(vendas) == 6, "O CSV devia ter o cabeçalho e 5 linhas de vendas"

assert (PROJ / "src/hello.py").is_file(), "Falta o ficheiro src/hello.py"

gitignore = (PROJ / ".gitignore").read_text()
assert ".venv" in gitignore, "O .gitignore não ignora o .venv"
assert ".idea" in gitignore, "O .gitignore não ignora o .idea"

respostas = (LICAO / "respostas.txt").read_text().strip()
assert respostas.startswith("rich_versao="), "respostas.txt devia começar por rich_versao="
versao = respostas.split("=", 1)[1].strip()
lock = (PROJ / "uv.lock").read_text()
assert f'name = "rich"\nversion = "{versao}"' in lock, "A versão do rich não coincide com o uv.lock"

print("Tudo certo. Isto não é a nota: o método e o raciocínio também contam.")

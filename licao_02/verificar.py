"""Verificações automáticas da Lição 2.

Corre a partir da raiz do repositório:
    uv run licao_02/verificar.py
"""
import subprocess
from pathlib import Path

BASE = Path(__file__).parent
RAIZ = BASE.parent
resultados = []


def git(*args: str) -> tuple[int, str]:
    r = subprocess.run(
        ["git", "-C", str(RAIZ), *args], capture_output=True, text=True
    )
    return r.returncode, r.stdout.strip()


def verificar(descricao: str, condicao: bool) -> None:
    resultados.append(bool(condicao))
    print(("OK     " if condicao else "FALHA  ") + descricao)


def seguido(caminho: str) -> bool:
    return bool(git("ls-files", caminho)[1])


def ignorado(caminho: str) -> bool:
    return git("check-ignore", "-q", caminho)[0] == 0


# 1. Estado geral
verificar("Estás na branch master", git("rev-parse", "--abbrev-ref", "HEAD")[1] == "master")
verificar("Tudo o que é de licao_02 está guardado em commits (nada pendente)",
          git("status", "--porcelain", "licao_02")[1] == "")

# 2. .idea
verificar("O Git já não segue nenhum ficheiro de .idea", not seguido(".idea"))
verificar("O .idea está ignorado", ignorado(".idea/misc.xml"))
verificar("O .venv continua ignorado", ignorado(".venv/bin/python"))

# 3. Regras do .gitignore e dados
verificar("A pasta privado/ está ignorada", ignorado("licao_02/privado/pacientes_confidencial.csv"))
verificar("Nenhum ficheiro de privado/ está no Git", not seguido("licao_02/privado"))
verificar("Os .log estão ignorados", ignorado("licao_02/logs/sistema.log")
          and ignorado("licao_02/logs/erros.log"))
verificar("Nenhum .log está no Git", not seguido("licao_02/logs"))
verificar("consultas.csv está no Git", seguido("licao_02/dados/consultas.csv"))

# 4. Branch e junção
verificar("Existe a branch analise", git("show-ref", "--verify", "--quiet", "refs/heads/analise")[0] == 0)

merge_hash = ""
for linha in git("log", "--merges", "--format=%H\t%s")[1].splitlines():
    hash_, _, assunto = linha.partition("\t")
    if "analise" in assunto:
        merge_hash = hash_
        break
verificar("Existe um commit de junção da branch analise", bool(merge_hash))

if merge_hash:
    n_commits = int(git("rev-list", "--count", f"{merge_hash}^1..{merge_hash}^2")[1] or 0)
    mensagens = git("log", "--format=%s", f"{merge_hash}^1..{merge_hash}^2")[1].splitlines()
else:
    n_commits, mensagens = 0, []
verificar("A branch analise tinha pelo menos 2 commits", n_commits >= 2)
verificar("As mensagens desses commits têm pelo menos 12 caracteres",
          bool(mensagens) and all(len(m.strip()) >= 12 for m in mensagens))

# 5. resumo.txt
consultas = BASE / "dados" / "consultas.csv"
resumo = BASE / "resumo.txt"
esperado = (
    str(len(consultas.read_text(encoding="utf-8").splitlines()) - 1)
    if consultas.is_file() else None
)
conteudo = resumo.read_text(encoding="utf-8").strip() if resumo.is_file() else ""
verificar("resumo.txt tem consultas=<número> correcto",
          esperado is not None and conteudo == f"consultas={esperado}")
verificar("notas_analise.txt existe e não está vazio",
          (BASE / "notas_analise.txt").is_file()
          and (BASE / "notas_analise.txt").read_text(encoding="utf-8").strip() != "")

# 6. Respostas
respostas = {}
ficheiro = BASE / "respostas.txt"
if ficheiro.is_file():
    for linha in ficheiro.read_text(encoding="utf-8").splitlines():
        if "=" in linha:
            chave, valor = linha.split("=", 1)
            respostas[chave.strip()] = valor.strip()

verificar("Existe respostas.txt", ficheiro.is_file())
primeiro = git("rev-list", "--max-parents=0", "HEAD")[1].splitlines()
verificar("Resposta primeiro_commit correcta",
          bool(primeiro) and respostas.get("primeiro_commit") == primeiro[0][:7])
ignorados = git("ls-files", "--others", "--ignored", "--exclude-standard", "licao_02")[1]
n_ignorados = len(ignorados.splitlines()) if ignorados else 0
verificar("Resposta ficheiros_ignorados correcta",
          respostas.get("ficheiros_ignorados") == str(n_ignorados))

percentagem = round(100 * sum(resultados) / len(resultados))
print(f"\nVerificações passadas: {sum(resultados)}/{len(resultados)} ({percentagem}%)")
print("Nota: isto não é a nota da lição. O método e o raciocínio também contam.")
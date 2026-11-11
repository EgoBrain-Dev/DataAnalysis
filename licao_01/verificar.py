"""Verificações automáticas da Lição 1.

Corre a partir da raiz do repositório:
    uv run licao_01/verificar.py
"""
from pathlib import Path

BASE = Path(__file__).parent
CAOS = BASE / "caos"
EMPRESA = BASE / "empresa"
resultados = []


def verificar(descricao: str, condicao: bool) -> None:
    resultados.append(bool(condicao))
    print(("OK     " if condicao else "FALHA  ") + descricao)


def ficheiros(pasta: Path) -> list[str]:
    if not pasta.is_dir():
        return []
    return sorted(p.name for p in pasta.iterdir() if p.is_file())


# 1. Estrutura
for nome in ["dados", "logs", "relatorios", "arquivo"]:
    verificar(f"Existe a pasta empresa/{nome}", (EMPRESA / nome).is_dir())

# 2. Ficheiros nos sítios certos
verificar(
    "empresa/dados tem os 3 ficheiros de vendas e os clientes (e mais nada)",
    ficheiros(EMPRESA / "dados")
    == ["clientes.csv", "vendas_2026_01.csv", "vendas_2026_02.csv", "vendas_2026_03.csv"],
)
verificar("empresa/logs tem o log do servidor (e mais nada)",
          ficheiros(EMPRESA / "logs") == ["servidor.log"])
verificar("empresa/relatorios tem os 2 ficheiros .txt (e mais nada)",
          ficheiros(EMPRESA / "relatorios") == ["notas.txt", "relatorio_q1.txt"])
verificar("empresa/arquivo tem a cópia de Fevereiro e o backup dos clientes (e mais nada)",
          ficheiros(EMPRESA / "arquivo") == ["clientes_backup.csv", "vendas_2026_02_copia.csv"])

# 3. Backup igual ao original
original = EMPRESA / "dados" / "clientes.csv"
backup = EMPRESA / "arquivo" / "clientes_backup.csv"
verificar(
    "clientes_backup.csv é igual a clientes.csv (e o original continua em dados)",
    original.is_file() and backup.is_file() and original.read_bytes() == backup.read_bytes(),
)

# 4. caos vazia e sem temporários
verificar("A pasta caos ficou sem ficheiros", CAOS.is_dir() and ficheiros(CAOS) == [])
verificar("Não sobrou nenhum ficheiro .tmp em licao_01", not list(BASE.rglob("*.tmp")))

# 5. Respostas
respostas = {}
ficheiro_respostas = BASE / "respostas.txt"
if ficheiro_respostas.is_file():
    for linha in ficheiro_respostas.read_text(encoding="utf-8").splitlines():
        if "=" in linha:
            chave, valor = linha.split("=", 1)
            respostas[chave.strip()] = valor.strip()

verificar("Existe respostas.txt", ficheiro_respostas.is_file())

vendas_jan = EMPRESA / "dados" / "vendas_2026_01.csv"
esperado_jan = str(len(vendas_jan.read_text(encoding="utf-8").splitlines())) if vendas_jan.is_file() else None
verificar("Resposta 1 (linhas_vendas_janeiro) correcta",
          esperado_jan is not None and respostas.get("linhas_vendas_janeiro") == esperado_jan)

log = EMPRESA / "logs" / "servidor.log"
esperado_erros = (
    str(sum(1 for l in log.read_text(encoding="utf-8").splitlines() if " ERROR " in l))
    if log.is_file() else None
)
verificar("Resposta 2 (erros_no_log) correcta",
          esperado_erros is not None and respostas.get("erros_no_log") == esperado_erros)

fev = EMPRESA / "dados" / "vendas_2026_02.csv"
copia = EMPRESA / "arquivo" / "vendas_2026_02_copia.csv"
esperado_copia = "sim" if (fev.is_file() and copia.is_file() and fev.read_bytes() == copia.read_bytes()) else None
verificar("Resposta 3 (copia_identica) correcta",
          esperado_copia is not None and respostas.get("copia_identica") == esperado_copia)

percentagem = round(100 * sum(resultados) / len(resultados))
print(f"\nVerificações passadas: {sum(resultados)}/{len(resultados)} ({percentagem}%)")
print("Nota: isto não é a nota da lição. O método e o raciocínio também contam.")
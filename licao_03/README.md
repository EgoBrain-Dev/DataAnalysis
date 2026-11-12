# Lição 3: PyCharm, uv e estrutura de projectos

## Cenário
A **Papelaria Maputo Central** (fictícia) quer começar a analisar as suas vendas. Antes de
qualquer análise, precisa de um projecto bem montado: ambiente próprio, dependências
registadas, pastas organizadas e histórico de Git limpo. Vais montar esse esqueleto.

## Objectivos
- Criar um projecto com o uv e abri-lo no PyCharm com o interpretador certo.
- Adicionar dependências (normais e de desenvolvimento) e perceber o que o uv regista.
- Organizar as pastas de um projecto de dados.
- Fazer commits em inglês simples e ler uma mensagem de erro em inglês.

## Perguntas
1. O Python que o terminal usa no projecto é o mesmo que o PyCharm usa?
2. Que versão do `rich` ficou instalada?
3. Porque é que cada projecto tem o seu próprio ambiente?

## Regras
- Comandos de terminal a partir da pasta indicada em cada tarefa.
- O projecto `papelaria_demo` fica em `~/PycharmProjects/`, **fora** do `DataAnalysis`, com o
  seu próprio Git. Se o terminal mostrar `(dataanalysis)` e o uv avisar de que ignora esse
  ambiente, é normal.
- Mensagens de commit **em inglês simples**: verbo no imperativo + ideia completa
  (exemplo: `Add sample sales data`). Não é preciso inglês perfeito, mas tem de se perceber.
- Antes de cada commit, vê o que vais guardar (`git status --short`).

## Tarefas
1. Cria o projecto **`papelaria_demo`** em `~/PycharmProjects/`, com o uv, a usar **Python 3.12**.
   Vê que ficheiros e pastas o uv criou.
2. Abre-o no PyCharm (**File → Open**) e confirma, em **Settings → Project → Python
   Interpreter**, que o interpretador é o `.venv` do projecto e a versão é 3.12.
3. Adiciona a dependência **`rich`** (normal) e **`pytest`** (só de desenvolvimento). Vê como
   mudou o `pyproject.toml`.
4. Organiza o projecto com estas pastas: `src/`, `data/raw/`, `data/processed/`, `docs/`.
   Lembra-te do que aprendeste sobre pastas vazias no Git: cada pasta tem de ficar com pelo
   menos um ficheiro.
5. Cria `data/raw/vendas.csv` com **exactamente** este conteúdo:
   ```
   data,produto,quantidade,preco_mzn
   2026-03-02,Caderno A4,12,85
   2026-03-02,Caneta azul,40,15
   2026-03-03,Resma de papel,5,520
   2026-03-04,Marcador,18,35
   2026-03-05,Agrafador,9,110
   ```
6. Cria `src/hello.py` com o script abaixo. É uma ferramenta: **não** tens de o perceber linha
   a linha (aprendes isso no Nível 1). Lê só o ficheiro CSV e mostra-o numa tabela.
   ```python
   """Mostra as vendas da Papelaria Maputo Central numa tabela."""
   import csv
   from pathlib import Path

   from rich.console import Console
   from rich.table import Table

   ficheiro = Path(__file__).parent.parent / "data" / "raw" / "vendas.csv"

   tabela = Table(title="Papelaria Maputo Central: vendas")
   with ficheiro.open(encoding="utf-8") as f:
       leitor = csv.reader(f)
       cabecalho = next(leitor)
       for coluna in cabecalho:
           tabela.add_column(coluna)
       for linha in leitor:
           tabela.add_row(*linha)

   Console().print(tabela)
   ```
7. Corre o script **de duas maneiras**: no PyCharm (botão verde) e no terminal com o uv.
   O resultado tem de ser a mesma tabela.
8. **Ler um erro em inglês.** No terminal, corre `uv run python src/nao_existe.py` (o ficheiro
   não existe de propósito). Antes de me perguntares o que significa, escreve numa frase, em
   português, o que **tu** achas que o erro diz.
9. Garante que o `.gitignore` do projecto ignora `.venv` e `.idea`. Faz **pelo menos 3
   commits** pequenos, cada um com uma ideia e mensagem em inglês.
10. **Documentação (inglês técnico).** Abre a documentação do uv em `docs.astral.sh/uv` e lê o
    guia **"Working on projects"**, na parte sobre o ficheiro `uv.lock` (se a página mudou,
    pesquisa "uv lockfile" e diz-me). Responde, em português, em 2 frases: *para que serve o
    `uv.lock` e deve ir para o Git?*
11. Em `DataAnalysis/licao_03/respostas.txt`, escreve **pelo terminal** uma linha:
    `rich_versao=<versão que o uv instalou>`
    Descobre a versão com um comando (`uv pip list` ou `uv tree`), não de memória.
12. A partir da raiz do `DataAnalysis`, corre `uv run licao_03/verificar.py`, corrige o que
    falhar, faz commit dos ficheiros de `licao_03` (mensagem em inglês) e o push.

## Critérios de avaliação
- Resultado (projecto e respostas correctos): 50%
- Método (commits pequenos e claros, em inglês simples; ver antes de guardar): 20%
- Explicação do raciocínio (pergunta final): 20%
- Autonomia (quantas pistas pediste): 10%
O inglês não tem nota própria: conta no método e no raciocínio.

## O que colar no chat (tudo, à primeira)
1. `find ~/PycharmProjects/papelaria_demo -not -path '*/.git/*' -not -path '*/.venv/*' | sort`
2. `cat ~/PycharmProjects/papelaria_demo/pyproject.toml`
3. O que o PyCharm mostra em Python Interpreter (texto ou captura)
4. O output do `uv run src/hello.py` no terminal
5. O output do erro da Tarefa 8, **e a tua frase** a dizer o que ele significa
6. `git --no-pager log --oneline` (dentro de `papelaria_demo`)
7. A tua resposta da Tarefa 10
8. O output completo de `uv run licao_03/verificar.py` e o `cat licao_03/respostas.txt`
9. Os comandos que usaste, copiados do terminal: `history | tail -60`
10. Em 2 ou 3 frases: *porque é que o `papelaria_demo` tem o seu próprio `.venv` em vez de
    instalares o `rich` globalmente no computador?*

# Teoria: Lição 3 (glossário PT / EN)

**IDE / Integrated Development Environment (ambiente de desenvolvimento integrado)**:
editor + terminal + execução + Git num só programa (o PyCharm). Porquê: menos trocas de
janela. Erro comum: achar que o PyCharm é o Python. Não é: é só a ferramenta que o usa.

**Interpreter (interpretador)**: o programa Python que corre o teu código. Cada projecto
escolhe o seu. Erro comum: o terminal e o PyCharm usarem Pythons diferentes. Confirma com
`which python3` no terminal e em Settings → Python Interpreter no PyCharm.

**Virtual environment, `.venv` (ambiente virtual)**: pasta com o Python e os pacotes de um
só projecto. Porquê: projectos diferentes não se estragam uns aos outros. Nunca vai para o Git.

**Dependency (dependência)**: pacote externo de que o projecto precisa. Exemplo:
`uv add rich`. Fica registado no `pyproject.toml`.

**Dev dependency (dependência de desenvolvimento)**: pacote só necessário para desenvolver
(testes), não para correr o projecto. Exemplo: `uv add --dev pytest`.

**`pyproject.toml`**: ficheiro com o nome do projecto, a versão do Python e as dependências.
É a "identidade" do projecto. Vai para o Git.

**Lockfile, `uv.lock`**: lista as versões **exactas** de tudo o que foi instalado, para que o
ambiente se recrie igual noutro computador. Vai para o Git. Erro comum: editá-lo à mão.

**`uv init`**: cria um projecto novo. Exemplo: `uv init papelaria_demo --python 3.12`.

**`uv add` / `uv remove`**: adiciona ou remove uma dependência e actualiza `pyproject.toml`
e `uv.lock`. Exemplo: `uv add rich`.

**`uv sync`**: cria ou actualiza o `.venv` a partir do `pyproject.toml`/`uv.lock`. Porquê:
é como se recria o ambiente depois de clonar um repositório.

**`uv run`**: corre um comando ou script dentro do ambiente do projecto.
Exemplo: `uv run src/hello.py`.

**Project structure (estrutura de projecto)**: pastas com função clara. Neste curso:
`src/` (código), `data/raw/` (dados originais, nunca alterados), `data/processed/` (dados
tratados), `docs/` (documentação). Porquê: qualquer pessoa percebe onde está cada coisa.

**`.gitkeep`**: ficheiro vazio, por convenção, só para o Git guardar uma pasta que ficaria
vazia. Lembra-te: o Git não guarda pastas vazias.

**Run (executar)** no PyCharm: botão verde ao lado do ficheiro. Usa o interpretador do
projecto. Erro comum: correr com um interpretador diferente do do terminal.

**Commit message em inglês**: verbo no imperativo + ideia completa. Verbos úteis: *Add*
(adicionar), *Fix* (corrigir), *Remove* (remover), *Update* (actualizar), *Rename*
(renomear), *Move* (mover). Exemplos: `Add sample sales data`, `Fix typo in README`.
Erro comum: mensagens vagas (`changes`, `update`) ou frases a meio.

**Reading errors (ler erros)**: lê de baixo para cima. A última linha costuma dizer o que
falhou. Palavras úteis: *No such file or directory* (ficheiro ou pasta não existe),
*can't open file* (não consigo abrir o ficheiro), *not found* (não encontrado),
*permission denied* (sem permissão).

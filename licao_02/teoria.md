# Teoria: Lição 2 (glossário)

**Working tree (pasta de trabalho)**: os ficheiros tal como os vês no disco. Porquê: é onde
editas; o Git só regista o que mandares. Exemplo: `git status`.

**Staging area (índice)**: a "caixa de embalagem" onde escolhes o que vai no próximo commit.
Porquê: permite commits pequenos, com uma ideia só. Exemplo: `git add ficheiro.txt`, `git diff --staged`.

**Commit**: uma fotografia do projecto, com autor, data e mensagem. Porquê: é o que podes
consultar e recuperar. Erro comum: mensagens vagas ("alterações", "teste").
Exemplo: `git commit -m "Adicionar resumo das consultas"`.

**Hash**: o identificador único de um commit (`6bb687f` é a forma curta). Porquê: é como se
refere um commit. Exemplo: `git show 6bb687f`.

**HEAD**: o commit em que estás neste momento. Exemplo: `git log --oneline` mostra `HEAD ->`.

**`git diff` / `git diff --staged`**: mostram o que mudou (ainda não em staging / já em
staging). Erro comum: fazer commit sem rever. Exemplo: `git diff`.

**`git log`**: o histórico. `--oneline` compacta, `--graph` desenha as branches, `--all` mostra
todas. Exemplo: `git log --oneline --graph --all`.

**`git show`**: mostra o que um commit alterou. `--stat` resume os ficheiros. Exemplo:
`git show --stat HEAD`.

**`.gitignore`**: ficheiro com padrões de ficheiros que o Git deve ignorar. Porquê: protege
dados privados e evita lixo (ambientes, logs). Exemplos de padrões: `*.log` (todos os .log),
`pasta/` (uma pasta inteira).
Erro comum: achar que o `.gitignore` também afecta ficheiros **que o Git já seguia**. Não afecta.

**`git rm --cached`**: faz o Git deixar de seguir um ficheiro **sem o apagar do disco**
(`-r` para pastas). Porquê: o par certo do `.gitignore` quando algo foi guardado por engano.
Exemplo: `git rm -r --cached pasta/`.

**`git check-ignore -v`**: diz que regra de que ficheiro está a ignorar um caminho. Porquê:
testar antes de confiar. Exemplo: `git check-ignore -v caminho/ficheiro`.

**Branch**: uma linha de commits paralela. Porquê: experimentas sem mexer na `master`.
Exemplos: `git switch -c analise` (cria e muda), `git switch master` (volta).

**Merge**: junta uma branch à actual. Com `--no-ff` fica sempre um commit de junção visível
no histórico, mesmo quando não era necessário. Erro comum: fazer merge estando na branch
errada. Exemplo: `git switch master` e depois `git merge --no-ff analise`.

**Remote / `origin` / push**: `origin` é o nome do repositório no GitHub; `push` envia os
commits para lá. Porquê: só o que fizeres `push` aparece no GitHub.

**O histórico guarda tudo.** Apagar um ficheiro num commit novo não o remove dos commits
anteriores. Quem clonar o repositório pode recuperá-lo. Porquê importa: dados privados que
entraram uma vez no Git já estão comprometidos.
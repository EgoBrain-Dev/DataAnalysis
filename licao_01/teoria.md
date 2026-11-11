# Teoria — Lição 1 (glossário)

**Terminal / shell (bash)**: programa onde escreves comandos de texto. Porquê: é mais rápido
e automatizável que clicar, e é a base de scripts e servidores. Exemplo: `echo olá`.

**Caminho absoluto vs relativo**: absoluto começa em `/` (ou `~` = a tua pasta pessoal);
relativo parte da pasta onde estás. Porquê: a maioria dos erros de iniciantes é estar na pasta
errada. Exemplo: `cd licao_01` (relativo), `cd ~/PycharmProjects` (absoluto).

**`pwd`**: mostra a pasta actual. Erro comum: executar comandos sem saber onde estás.

**`ls`**: lista ficheiros. `-l` dá detalhe, `-a` mostra os ocultos. Exemplo: `ls -la`.

**`cd`**: muda de pasta. `cd ..` sobe um nível. Exemplo: `cd licao_01/caos`.

**`mkdir`**: cria pastas. `-p` cria também as pastas-mãe em falta. Exemplo: `mkdir -p a/b/c`.

**`cp`**: copia (o original fica). Exemplo: `cp origem.txt destino.txt`.

**`mv`**: move ou muda o nome (o original deixa de existir no sítio antigo).
Exemplo: `mv ficheiro.txt pasta/`.

**`rm`**: apaga **sem reciclagem**: não há como desfazer. Erro comum: apagar com um padrão
(`*`) sem antes ver o que ele apanha. Exemplo: `ls *.tmp` primeiro, `rm *.tmp` depois.

**`cat`, `head`, `tail`**: mostram o conteúdo de um ficheiro, o início ou o fim.
Exemplo: `head -n 5 ficheiro.csv`.

**`wc -l`**: conta linhas. Exemplo: `wc -l ficheiro.csv`.

**`grep`**: procura texto dentro de ficheiros. `-c` conta as linhas que coincidem.
Erro comum: esquecer que distingue maiúsculas de minúsculas. Exemplo: `grep -c ERRO log.txt`.

**`cmp` / `diff`**: comparam ficheiros. Sem output do `cmp`, os ficheiros são idênticos.
Exemplo: `cmp a.txt b.txt`.

**Redirecção `>` e `>>`**: guarda o output de um comando num ficheiro. `>` substitui o
conteúdo, `>>` acrescenta no fim. Erro comum: usar `>` e apagar o que já lá estava.
Exemplo: `echo "x=1" >> notas.txt`.

**`find`**: procura ficheiros por nome/tipo. Exemplo: `find . -name "*.csv"`.

**`Tab` e seta para cima**: `Tab` completa nomes; a seta para cima recupera comandos
anteriores. Porquê: menos erros de escrita.

**`man comando` e `comando --help`**: documentação do próprio comando (inglês técnico).
Exemplo: `grep --help`. Sai do `man` com a tecla `q`.
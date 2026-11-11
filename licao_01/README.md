# Lição 1 — Terminal Linux básico

## Cenário
A **MozFrio Lda** é uma distribuidora fictícia de produtos alimentares e de limpeza, com sede
em Maputo. O responsável de operações exportou ficheiros do sistema para uma pasta e ficou tudo
misturado: vendas de três meses, clientes, um log do servidor, notas soltas, ficheiros
temporários e uma cópia suspeita de um ficheiro de vendas.

Foste contratado para arrumar tudo **usando apenas o terminal** e responder a 3 perguntas.

## Objectivos
- Navegar entre pastas e ler o que lá está.
- Criar, copiar, mover e apagar ficheiros com segurança.
- Inspeccionar ficheiros de dados sem os abrir num editor.

## Perguntas de negócio
1. Quantas linhas tem o ficheiro de vendas de Janeiro (cabeçalho incluído)?
2. Quantos erros (nível ERROR) registou o servidor?
3. O ficheiro `vendas_2026_02_copia.csv` é mesmo uma cópia exacta do de Fevereiro?

## Regras
- Trabalha **só no terminal**. Nada de gestor de ficheiros nem PyCharm para mover ficheiros.
- Os comandos correm a partir de `~/PycharmProjects/DataAnalysis`.
- Antes de apagar seja o que for, confirma o que vais apagar.

## Tarefas
1. Entra na pasta `licao_01/caos`, confirma onde estás e lista o conteúdo com detalhe
   (tamanho e datas).
2. Em `licao_01`, cria a estrutura `empresa/` com quatro subpastas: `dados`, `logs`,
   `relatorios`, `arquivo`.
3. Responde às 3 perguntas de negócio **antes de mover os ficheiros**, usando comandos de
   leitura. Escreve as respostas no ficheiro `licao_01/respostas.txt` **pelo terminal**,
   neste formato exacto (uma por linha, sem espaços à volta do `=`):
   `linhas_vendas_janeiro=<número>`
   `erros_no_log=<número>`
   `copia_identica=<sim ou nao>`
4. Arruma os ficheiros de `caos`:
   - vendas (Janeiro, Fevereiro, Março) e `clientes.csv` → `empresa/dados`
   - o log → `empresa/logs`
   - ficheiros `.txt` → `empresa/relatorios`
   - a cópia do ficheiro de Fevereiro → `empresa/arquivo`
   - ficheiros temporários (`.tmp`) → apagados
5. Faz uma cópia de segurança de `clientes.csv` para `empresa/arquivo`, com o nome
   `clientes_backup.csv` (o original continua em `dados`).
6. No fim, a pasta `caos` não pode ter ficheiros.
7. Corre `uv run licao_01/verificar.py`, corrige o que falhar e faz commit.

## Critérios de avaliação
- Resultado (estrutura e respostas correctas): 50%
- Método (usaste leitura antes de mover/apagar; sem apagar nada a mais): 20%
- Explicação do raciocínio (pergunta abaixo): 20%
- Autonomia (quantas pistas pediste): 10%

## O que colar no chat
1. O output completo de: `find licao_01/empresa licao_01/caos | sort`
2. O output de: `cat licao_01/respostas.txt`
3. O output completo de `uv run licao_01/verificar.py`
4. O output de `git log --oneline`
5. A tua resposta, em 2 ou 3 frases, a esta pergunta: *porque é que, no terminal, apagar
   com `rm` é mais perigoso do que apagar num gestor de ficheiros, e o que fizeste para
   te proteger?*
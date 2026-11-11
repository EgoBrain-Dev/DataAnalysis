# Lição 2: Git e GitHub a fundo

## Cenário
A **Clínica Vida Nova** (fictícia, Matola) exporta do seu sistema as consultas realizadas, os
pacientes e os logs do servidor. Foste contratado para pôr este material sob controlo de versões
num repositório que, no futuro, a equipa vai partilhar no GitHub.

Há um risco: entre os ficheiros exportados está uma lista **confidencial** de pacientes. Quem
trabalha com dados de saúde não pode deixar que isto chegue a um repositório partilhado, mesmo que
os dados deste exercício sejam fictícios. Trata-os como se fossem reais.

## Objectivos
- Perceber as três zonas do Git: pasta de trabalho, staging e histórico.
- Fazer commits pequenos, com uma ideia cada e mensagens claras.
- Controlar o que entra no repositório com `.gitignore`.
- Trabalhar numa branch e juntá-la à `master`.
- Ler o histórico para responder a perguntas.

## Perguntas de negócio
1. Que ficheiros do repositório **nunca** devem ser partilhados e porquê?
2. Qual foi o primeiro commit deste repositório?
3. Quantos ficheiros da pasta `licao_02` o Git está a ignorar?

## Regras
- Trabalha no terminal. O PyCharm serve para criar e editar ficheiros; o GitHub Desktop só para o
  `push` final.
- Corre os comandos a partir de `~/PycharmProjects/DataAnalysis`.
- **Um commit, uma ideia.** Não uses `git add .` às cegas: vê sempre antes o que vais guardar.
- Mensagens de commit em português, sem gralhas (ficam no histórico público) e com pelo menos
  12 caracteres.

## Tarefas
1. **Ponto de partida.** Confirma em que branch estás e vê o histórico actual com a árvore
   (`--graph`). Cola esse output na submissão.
2. **Corrigir o `.idea`.** A pasta `.idea` (configurações pessoais do PyCharm) está no Git. Faz
   com que o Git deixe de a seguir **sem a apagar do teu computador**, e com que passe a ignorá-la.
   Isto são 2 coisas e um commit.
3. **Gerar os dados, sem commit ainda.** Corre o `gerar_dados.py` e observa o que o `git status`
   diz. Depois escreve no `.gitignore` as regras para que o Git ignore:
   - toda a pasta `licao_02/privado/`
   - todos os ficheiros `.log`
   Confirma que as regras funcionam **antes** de fazeres commit (há um comando do Git que te
   diz qual a regra que está a ignorar um ficheiro). Faz commit só das regras.
4. **Guardar a lição.** Faz um commit com os ficheiros da lição e os dados em `licao_02/dados`.
   Antes do commit, vê o que está em staging.
5. **Branch de análise.** Cria e muda para uma branch chamada `analise`. Nela:
   - cria `licao_02/resumo.txt` com **uma linha**, `consultas=<número>`, onde o número é a
     quantidade de registos de `consultas.csv` (sem contar o cabeçalho). Escreve o ficheiro
     pelo terminal. Commit.
   - cria `licao_02/notas_analise.txt` com uma frase tua sobre a qualidade dos dados que viste
     ao abrir o `consultas.csv` (no terminal, com `head`, `tail` ou `cat`). Commit.
   Tens de ter, no mínimo, **2 commits** na branch.
6. **Juntar.** Volta à `master` e junta a `analise` de forma a **ficar um commit de junção
   visível** no histórico (a teoria explica a opção).
7. **Perguntas de histórico.** Escreve `licao_02/respostas.txt` **pelo terminal**, neste formato
   exacto (uma por linha, sem espaços à volta do `=`):
   `primeiro_commit=<os primeiros 7 caracteres do hash>`
   `ficheiros_ignorados=<número>`
   Descobre os valores com comandos do Git.
8. **Fechar.** Corre `uv run licao_02/verificar.py`, corrige o que falhar, faz commit do
   `respostas.txt` na `master` e faz o push no GitHub Desktop.

## Critérios de avaliação
- Resultado (estado final do repositório e respostas): 50%
- Método (commits pequenos e claros; verificar antes de guardar; sem dados privados no histórico): 20%
- Explicação do raciocínio (pergunta abaixo): 20%
- Autonomia (quantas pistas pediste): 10%

## O que colar no chat
1. O output completo de `git status --short` e de `git log --oneline --graph --all`
2. O output de `cat licao_02/respostas.txt`
3. O output de `git check-ignore -v licao_02/privado/pacientes_confidencial.csv`
4. O output completo de `uv run licao_02/verificar.py`
5. **A lista, por ordem, dos comandos que usaste** nas tarefas 2 a 6 (só eu a posso avaliar se a
   escreveres; lembra-te do que aconteceu na Lição 1)
6. A tua resposta, em 2 ou 3 frases: *porque é que o ficheiro de pacientes confidenciais nunca
   deve ir para o GitHub, mesmo que depois o apagues num commit seguinte?*
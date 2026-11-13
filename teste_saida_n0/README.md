# Teste de saída: Nível 0 (Preparação)

## Cenário
A **Expresso do Índico** (fictícia) é uma empresa de entregas em Maputo. Quer um projecto
organizado para começar a analisar as entregas, com um ficheiro de dados, um ambiente próprio
e histórico de Git limpo. Tens de o montar sozinho, do zero.

## Regras
- **Sem ajuda.** Nada de pistas minhas. Permitido: `--help`, `man`, documentação oficial,
  as tuas notas.
- O projecto chama-se **`expresso_teste`** e fica em `~/PycharmProjects/`, **fora** do
  `DataAnalysis`, com o seu próprio Git.
- Mensagens de commit em inglês simples (verbo no imperativo + ideia completa).
- Antes de apagar ou guardar, confirma o que vais apagar ou guardar.
- Os comandos não estão no enunciado: escolhe-os tu.
- Se encravares, não peças pistas: regista onde encravaste e submete o que tens.

## Dados (`data/raw/entregas.csv`, com exactamente este conteúdo)
```
id,data,zona,estado,valor_mzn
E001,2026-04-01,Maputo,entregue,350
E002,2026-04-01,Matola,atrasada,420
E003,2026-04-02,Maputo,entregue,350
E004,2026-04-02,Marracuene,entregue,600
E005,2026-04-03,Matola,atrasada,420
E006,2026-04-03,Maputo,cancelada,350
E007,2026-04-04,Marracuene,entregue,600
```

## Tarefas
1. Cria o projecto `expresso_teste` com o uv, a usar **Python 3.12**.
2. Abre-o no PyCharm e confirma que o interpretador é o do projecto.
3. Adiciona as dependências **`requests`** (normal) e **`pytest`** (só desenvolvimento).
4. Estrutura: `src/`, `data/raw/`, `data/processed/`, `docs/`, `tests/`.
   Todas têm de ficar guardadas no Git.
5. Cria `data/raw/entregas.csv` com o conteúdo acima. **Os dados em `raw` nunca se alteram.**
6. Faz uma cópia dos dados originais para `data/processed/entregas_copia.csv`.
7. Cria `data/private/contactos.csv` com 2 contactos fictícios (cabeçalho
   `id,nome,telefone`). Este ficheiro é confidencial: **não pode ficar no Git nem no histórico**.
8. Garante que o Git ignora `.venv`, `.idea` e `data/private/`.
9. Cria 3 ficheiros temporários `.tmp` em `data/processed/` e **limpa-os** com segurança.
10. Numa branch chamada `relatorio`, com pelo menos 2 commits, cria `docs/relatorio.md`
    (um título e uma frase tua). Junta-a à `master` com commit de junção visível.
11. Pelo menos **6 commits** no total, pequenos e com mensagens claras em inglês.
12. No terminal, responde com comandos (não de memória) e escreve em
    `DataAnalysis/teste_saida_n0/respostas.txt`, uma linha por pergunta, formato exacto:
    `linhas_entregas=<número de linhas do ficheiro, cabeçalho incluído>`
    `entregas_atrasadas=<número de entregas atrasadas>`
    `requests_versao=<versão que o uv instalou>`
13. **Ler erros em inglês.** Para cada mensagem, diz em português o que significa e o que
    farias a seguir:
    - `fatal: not a git repository (or any of the parent directories): .git`
    - `error: pathspec 'entregas.csv' did not match any file(s) known to git`
14. **Documentação.** Na documentação oficial do uv (`docs.astral.sh/uv`), encontra o que
    faz o comando `uv sync` e explica numa frase.
15. A partir da raiz do `DataAnalysis`: `uv run teste_saida_n0/verificar.py`. Faz commit dos
    ficheiros de `teste_saida_n0` (mensagem em inglês) e o push.

## Critérios de avaliação
- Resultado (estado do projecto e respostas correctas): 50%
- Método (commits pequenos e claros, ver antes de guardar/apagar, sem dados privados no
  histórico): 20%
- Explicação do raciocínio (pergunta final e tarefas 13 e 14): 20%
- Autonomia (10% só se fizeres tudo sem pedir pistas): 10%
- Aprovação: 70% no total e 60% em cada componente. Se reprovares, faço um reforço com um
  novo cenário (não repetes o mesmo).

## O que colar no chat (tudo, à primeira)
1. `find ~/PycharmProjects/expresso_teste -not -path '*/.git/*' -not -path '*/.venv/*' | sort`
2. `cat ~/PycharmProjects/expresso_teste/pyproject.toml`
3. O que o PyCharm mostra em Python Interpreter (texto ou captura)
4. `git --no-pager log --oneline --graph --all` (dentro de `expresso_teste`)
5. `git --no-pager log --all --oneline -- data/private` (se não aparecer nada, diz que ficou
   vazio: é o resultado certo)
6. `git --no-pager ls-files` (dentro de `expresso_teste`)
7. O output completo de `uv run teste_saida_n0/verificar.py` e o `cat teste_saida_n0/respostas.txt`
8. As tuas respostas das tarefas 13 e 14, em português, com as tuas palavras
9. O `history | tail -80` copiado **de cada janela do terminal** onde trabalhaste
10. Em 3 respostas curtas, com as tuas palavras: (a) porque é que os dados em `raw` nunca
    se alteram; (b) porque é que o `.gitignore` tem de estar guardado **antes** dos dados
    privados; (c) a diferença entre `pyproject.toml` e `uv.lock`.

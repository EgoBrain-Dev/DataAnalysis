git branch --show-current                  # em que branch estou
git --no-pager log --oneline --graph --all # histórico, sem paginador

git rm -r --cached .idea                   # deixa de seguir, NÃO apaga do disco
echo ".idea/" >> .gitignore                # >> acrescenta; > apagava o ficheiro todo
git status --short                         # rever antes de guardar
git commit -m "Remover .idea do controlo de versões"

uv run licao_02/gerar_dados.py             # gera dados; ainda sem commit
echo "licao_02/privado/" >> .gitignore
echo "*.log" >> .gitignore
git check-ignore -v licao_02/privado/pacientes_confidencial.csv   # testar a regra
git add .gitignore && git commit -m "Ignorar pasta privada e ficheiros de log"

git status --short                         # ver o que vai entrar
git add licao_02/ && git diff --staged --stat   # ver em staging antes de guardar
git commit -m "Guardar ficheiros da lição 2"

git switch -c analise                      # cria e muda
echo "consultas=57" > licao_02/resumo.txt  # (o número vem de wc -l, menos o cabeçalho)
git add licao_02/resumo.txt && git commit -m "Criar resumo das consultas"
# ...segundo commit, com as notas de análise...

git switch master
git merge --no-ff analise                  # força o commit de junção

git rev-list --max-parents=0 HEAD          # primeiro commit (o sem pais)
git ls-files --others --ignored --exclude-standard licao_02   # ficheiros ignorados
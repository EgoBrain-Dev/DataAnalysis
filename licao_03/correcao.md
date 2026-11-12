cd ~/PycharmProjects
uv init papelaria_demo --python 3.12      # cria o projecto com o uv
cd papelaria_demo
uv add rich                               # dependência normal
uv add --dev pytest                       # só de desenvolvimento (grupo dev)
mkdir -p data/raw data/processed docs
touch data/processed/.gitkeep docs/.gitkeep   # ficheiro vazio para o Git guardar a pasta
uv run src/hello.py                       # corre dentro do ambiente do projecto
uv run python src/nao_existe.py           # erro de propósito: ler a última linha
git commit -m "Add initial project files"
git commit -m "Add sample sales data and hello script"
git commit -m "Add .gitkeep to track empty folders"

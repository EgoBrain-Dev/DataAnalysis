cd ~/PycharmProjects/DataAnalysis/licao_01/caos
pwd                                   # onde estou?
ls -la                                # o que há aqui, com detalhe

cd ..
mkdir -p empresa/dados empresa/logs empresa/relatorios empresa/arquivo

# Perguntas, ANTES de mover
wc -l caos/vendas_2026_01.csv         # 1) linhas (cabeçalho incluído)
grep -c " ERROR " caos/servidor.log   # 2) erros; os espaços evitam apanhar outras palavras
cmp caos/vendas_2026_02.csv caos/vendas_2026_02_copia.csv && echo sim   # 3) sem output = idênticos

echo "linhas_vendas_janeiro=31" > respostas.txt     # > cria/substitui
echo "erros_no_log=13" >> respostas.txt             # >> acrescenta
echo "copia_identica=sim" >> respostas.txt

# Arrumar
mv caos/vendas_2026_0[123].csv caos/clientes.csv empresa/dados/
mv caos/servidor.log empresa/logs/
mv caos/*.txt empresa/relatorios/
mv caos/vendas_2026_02_copia.csv empresa/arquivo/
cp empresa/dados/clientes.csv empresa/arquivo/clientes_backup.csv

# Apagar com cuidado: ver primeiro, apagar depois
ls caos/*.tmp
rm caos/*.tmp
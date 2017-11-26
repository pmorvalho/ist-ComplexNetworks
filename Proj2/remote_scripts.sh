#!/bin/bash

# isto serve para:
# 	1. mexer os ficheiros no cluster pro sitio certo, 
#	2. sacar pra maquina local so os novos 
#	3. e separar os dados por linguagens muito fast (#allcoreslife)
# estimativa para 100% dos dados: max 5Gb probably

echo "Moving files in inesc machine to specific directory"
ssh redes@mem.inesc-id.pt "cd twitter; mv full_data* full_parsed/; rm full_parsed.zip; zip -r full_parsed.zip full_parsed"


# # explicaçao: tirando permissao de escrita aos ficheiros locais, os ficheiros remotes nao conseguem dar overwrite
# echo "Changing permissions of already downloaded files..."
# chmod a-w parsed_data/*

echo "Downloading only new files"
scp redes@mem.inesc-id.pt:twitter/full_parsed.zip parsed_data.zip

unzip parsed_data.zip

rm -r parsed_data

mv full_parsed parsed_data

echo "Splitting files by language"
mkdir en_data
mkdir es_data
mkdir pt_data
python split_by_language.py
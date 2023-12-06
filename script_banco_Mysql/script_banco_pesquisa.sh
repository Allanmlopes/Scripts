#!/bin/bash

database="Pesquisa_URA"

# Obtendo a data atual
current_date=$(date +"%Y-%m-%d")
current_month=$(date +"%Y-%m-01")

# Calculando o primeiro dia e o último dia do mês atual
start_date="${current_month} 00:00:00"
end_date=$(date -d "$current_month +1 month -1 second" +"%Y-%m-%d %H:%M:%S")

# Criando um nome de arquivo com a data do mês
output_filename="./Pesquisa/Pesquisa_$(date +"%Y-%m").csv"

# Executando o comando MySQL e redirecione a saída para o arquivo:
mysql --defaults-file=mysql_options.cnf -D "$database" -e "SELECT id, data, id_pesquisa, id_service, id_resposta, nota_resposta, CONCAT('Ramal ', operador) AS operador FROM pesquisa WHERE data BETWEEN '$start_date' AND '$end_date';" > "$output_filename"

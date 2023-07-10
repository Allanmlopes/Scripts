#!/usr/bin/python

import platform
import subprocess
import distro
import re

php_version_output = subprocess.check_output(['php', '--version']).decode('utf-8').strip()
match = re.search(r'PHP (\S+)', php_version_output)
php_version = match.group(1)
db_version = subprocess.check_output(['mysql', '--version']).decode('utf-8').strip()
apache_version = subprocess.check_output(['apache2ctl', '-v']).decode('utf-8').strip()
mem_info = subprocess.check_output(['free', '-h']).decode('utf-8').strip()
df_output = subprocess.check_output(['df', '-h']).decode('utf-8').strip()
#distribution_info = distro.linux_distribution(full_distribution_name=False)
distribution_id = distro.id()
distribution_version = distro.version()

p1 = subprocess.Popen(['lscpu'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['egrep', 'Nome do modelo'], stdin=p1.stdout, stdout=subprocess.PIPE)
process_name = p2.communicate()[0].decode('utf-8')


print("Nome da Maquina..........:", platform.node())
print("Arquitetura..............:", platform.architecture())
print("Sistema Operacional......:", platform.system())
print("Versão do S.O............:", platform.release())
#print("Distribuição Linux.......:", distribution_info[0])
#print("Versão...................:", distribution_info[1])
#print("ID.......................:", distribution_info[2])
print("ID.......................:", distribution_id)
print("Versão...................:", distribution_version)
print("Veresão do Python........:", platform.python_version())
print("Versão do Banco de Dados.:", db_version)
print("Versão do Apache.........:", apache_version)
print("Versão do PHP............:", php_version)
print("Processador..............:", process_name)
print("Quantidade de Memória....:\n", mem_info)
print("Listagem de Disco........:", df_output)

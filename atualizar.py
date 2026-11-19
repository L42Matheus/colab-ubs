"""Extrai o recorte municipal do ZIP oficial do Ministério da Saúde."""
import csv
import sys
import zipfile
import xml.etree.ElementTree as ET

with zipfile.ZipFile(sys.argv[1]) as arquivo:
    raiz = ET.fromstring(arquivo.read(arquivo.namelist()[0]))
campos = ['CNES', 'NOME', 'BAIRRO', 'LATITUDE', 'LONGITUDE']
with open('dados/ubs.csv', 'w', newline='', encoding='utf8') as destino:
    tabela = csv.DictWriter(destino, campos)
    tabela.writeheader()
    for unidade in raiz:
        if unidade.findtext('IBGE') == '250400':
            tabela.writerow({campo: unidade.findtext(campo) for campo in campos})

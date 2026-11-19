# Acesso às UBS de Campina Grande

Leia o [artigo com resultados e referências](ARTIGO.md) ou consulte as [coordenadas das UBS](dados/ubs.csv) e os [cenários calculados](cenarios.csv).

O notebook da disciplina foi preservado com as saídas removidas para publicação. Sua etapa original de importação depende de um CSV local do CNES. Para reproduzir o estudo atualizado, use os arquivos em dados/ e rode na raiz do repositório:

```sh
python -m pip install numpy scipy shapely pyproj
python simular.py
```

Em simular.py, a primeira parte converte os polígonos em pontos internos e as coordenadas em metros. A matriz de distâncias permite identificar os setores além de 2 km da rede. A última parte testa um novo ponto em cada setor e escolhe aquele que alcança mais moradores ainda fora do raio. O arquivo cenarios.csv registra o ganho de cada escolha.

Para atualizar o cadastro, baixe o [ZIP XML do Ministério da Saúde](https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/CNES/Unidades_Basicas_Saude-UBS_xml.zip), execute `python atualizar.py caminho/do/arquivo.zip` e depois `python simular.py`. A atualização substitui o recorte municipal e os resultados da simulação. O artigo descreve a extração de 19/11/2026.

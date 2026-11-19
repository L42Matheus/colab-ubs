# Acesso às UBS de Campina Grande

Leia o [artigo com resultados e referências](ARTIGO.md) ou consulte as [coordenadas das UBS](dados/ubs.csv) e os [cenários calculados](cenarios.csv).

[Abra o notebook da disciplina no Colab](https://colab.research.google.com/github/L42Matheus/colab-ubs/blob/main/Sensoriamento_Inteligente_UBS_Campina_Grande.ipynb) e escolha “Executar tudo” para gerar indicadores, agrupamentos, mapas e cenários. A [versão original da disciplina, com K-Means](https://github.com/L42Matheus/colab-ubs/blob/1fbaeda/Sensoriamento_Inteligente_UBS_Campina_Grande.ipynb), continua disponível. Para reproduzir a simulação pelo terminal, rode na raiz do repositório:

```sh
python -m pip install numpy scipy shapely pyproj
python simular.py
```

Em simular.py, a primeira parte converte os polígonos em pontos internos e as coordenadas em metros. A matriz de distâncias permite identificar os setores além de 2 km da rede. A última parte testa um novo ponto em cada setor e escolhe aquele que alcança mais moradores ainda fora do raio. O arquivo cenarios.csv registra o ganho de cada escolha.

Para atualizar o cadastro, baixe o [ZIP XML do Ministério da Saúde](https://s3.sa-east-1.amazonaws.com/ckan.saude.gov.br/CNES/Unidades_Basicas_Saude-UBS_xml.zip), execute `python atualizar.py caminho/do/arquivo.zip` e depois `python simular.py`. A atualização substitui o recorte municipal e os resultados da simulação. O artigo descreve a extração de 19/11/2026.

"""Compara a rede cadastrada com até três novos pontos de atendimento."""
import csv
import json
import numpy as np
from pyproj import Transformer
from shapely.geometry import Point, shape
from shapely.ops import transform, unary_union
from scipy.spatial.distance import cdist

projetar = Transformer.from_crs(4326, 31985, always_xy=True).transform
inverter = Transformer.from_crs(31985, 4326, always_xy=True).transform
with open('dados/setores.geojson') as arquivo:
    setores = sorted(json.load(arquivo)['features'], key=lambda f: f['properties']['CD_SETOR'])
areas = [transform(projetar, shape(s['geometry'])) for s in setores]
limite = unary_union(areas)
pontos = [a.representative_point().coords[0] for a in areas]
pop = np.array([s['properties']['populacao'] for s in setores], dtype=int)
with open('dados/ubs.csv') as arquivo:
    unidades = list(csv.DictReader(arquivo))
rede = {}
for u in unidades:
    try:
        xy = projetar(float(u['LONGITUDE']), float(u['LATITUDE']))
    except (ValueError, TypeError):
        continue
    if limite.covers(Point(xy)):
        rede[u['CNES']] = xy
distancia = cdist(pontos, list(rede.values())).min(axis=1)
vizinhos = cdist(pontos, pontos) <= 2000
fora = distancia > 2000
print('Cadastros, CNES válidos, coordenadas distintas:', len(unidades), len(rede), len(set(rede.values())))
print('Setores, população, mediana em metros:', len(pop), pop.sum(), round(np.median(distancia), 1))
with open('cenarios.csv', 'w', newline='') as arquivo:
    tabela = csv.writer(arquivo)
    tabela.writerow(['adicoes','setor_candidato','longitude','latitude','ganho_pessoas','setores_fora','pessoas_fora'])
    tabela.writerow([0,'','','',0,fora.sum(),pop[fora].sum()])
    for etapa in range(1, 4):
        ganhos = vizinhos @ (pop * fora)
        melhor = int(ganhos.argmax())
        if ganhos[melhor] == 0:
            break
        fora &= ~vizinhos[melhor]
        tabela.writerow([etapa,setores[melhor]['properties']['CD_SETOR'],*inverter(*pontos[melhor]),ganhos[melhor],fora.sum(),pop[fora].sum()])

# Acessibilidade geográfica às UBS em Campina Grande (PB): diagnóstico por setor censitário e cenários de expansão

**Resumo.** Quantos moradores de Campina Grande vivem em setores cujo ponto representativo fica a mais de 2 km de uma unidade básica de saúde? Cruzamos a população do Censo 2022 com o cadastro público de UBS consultado em 19 de novembro de 2026. Entre 791 setores, 36 ficaram além do limiar, somando 9.868 pessoas. Uma simulação sequencial com três pontos adicionais reduziu esse total para 7.359. A medida descreve proximidade espacial potencial e permite selecionar territórios para investigação de campo.

## Introdução

A Política Nacional de Atenção Básica orienta a organização da rede pela territorialização, pela população adscrita e pela continuidade do cuidado [1]. Uma família pode morar perto de uma UBS e pertencer ao território de outra equipe. A distância até a unidade mais próxima mede uma dimensão do acesso que pode ser confrontada com as áreas de atuação das equipes. O diagnóstico participativo do Plano Diretor municipal, por exemplo, apresenta um mapa com áreas de abrangência de 800 m no distrito sede [2]. Neste estudo, 2 km é uma hipótese experimental de alcance entre população e serviço. Não identificamos na PNAB consultada obrigação de espaçar UBS a cada 2 km.

## Dados e método

Recuperamos os polígonos e a população de 791 setores do mapa incorporado ao notebook da disciplina, construído com a malha censitária e os agregados básicos do IBGE [3]. O recorte soma 419.379 habitantes em 2022. Extraímos da relação pública de UBS do Ministério da Saúde [4] os registros de código municipal 250400 e conservamos um ponto por código CNES com coordenadas válidas dentro da malha municipal. Dos 103 registros, 101 entraram na análise. A data da extração identifica a versão consultada. A presença no cadastro requer confirmação local de funcionamento.

Projetamos as geometrias em SIRGAS 2000 / UTM 25S e atribuímos a população de cada setor a um ponto interno. Calculamos em metros a distância em linha reta desse ponto à UBS mais próxima. Para simular expansão, consideramos os 791 pontos internos como locais candidatos. Em cada rodada escolhemos o candidato que alcançava a maior soma de população ainda fora do raio. Após cada escolha, retiramos os setores recém-alcançados do cálculo de ganho. Empates favorecem o menor código de setor. Essa busca sequencial produz uma solução reproduzível sem garantir o ótimo global.

## Resultados

A distância mediana dos pontos setoriais à rede cadastrada foi de 408,8 m. A mediana descreve um setor típico, enquanto o indicador populacional pondera cada setor pelo número de moradores.

| Novos pontos acumulados | Setor acrescentado | Latitude, longitude | Ganho marginal estimado | Setores além de 2 km | Pessoas além de 2 km |
|---:|---|---|---:|---:|---:|
| 0 | — | — | — | 36 | 9.868 |
| 1 | 250400905000855 | −7,25088; −35,97116 | 916 | 33 | 8.952 |
| 2 | 250400920000019 | −7,27507; −35,80852 | 897 | 30 | 8.055 |
| 3 | 250400915000010 | −7,31812; −36,05561 | 696 | 26 | 7.359 |

Os três pontos alcançaram dez setores adicionais, com 2.509 habitantes. A parcela estimada além de 2 km caiu de 2,35% para 1,75% do total municipal, uma redução relativa de 25,4% no grupo inicialmente distante.

O experimento original da disciplina usou 91 pontos e registrou mediana de 439,7 m. Comparou K-Means com K igual a 2, 3 e 4 sobre distância, densidade e número de unidades em 2 km, após padronização. Os valores de Silhouette foram 0,425, 0,320 e 0,352. O critério selecionou dois perfis. Davies–Bouldin favoreceu quatro grupos (0,908 contra 1,038 para dois), mostrando que a escolha depende do critério. Esses valores pertencem à execução salva do notebook original. A diferença entre os inventários não permite inferir quantas unidades abriram.

## Discussão e conclusão

Os ganhos marginais diminuíram de 916 para 696 pessoas entre a primeira e a terceira escolha. Mesmo com as três adições, 26 setores permaneceriam além do limiar. Favorecer o maior ganho populacional pode deixar territórios pouco povoados para o fim. Para avaliar equidade, a gestão municipal pode confrontar esses setores com vulnerabilidade, transporte e presença de equipes itinerantes.

As estimativas são sensíveis à distribuição dos domicílios dentro de cada setor, particularmente na zona rural. O modelo usa a população de 2022 com a rede cadastrada em 2026, desconsidera atendimento além da divisa municipal e não mede tempo de caminhada, capacidade, horários ou vínculo com a equipe. Coordenadas distintas também podem identificar equipes no mesmo imóvel. Antes de propor uma obra, seria necessário validar endereços, barreiras viárias, disponibilidade de terrenos e territórios adscritos com a Secretaria Municipal de Saúde. Os três setores oferecem uma ordem inicial para essa verificação.

## Referências

1. Brasil. Ministério da Saúde. Política Nacional de Atenção Básica. [Portaria de Consolidação GM/MS nº 2/2017, Anexo XXII](https://bvsms.saude.gov.br/bvs/saudelegis/gm/2017/prc0002_03_10_2017.html).
2. Campina Grande. Revisão do Plano Diretor. [Diagnóstico participativo, 2024](https://planodiretor.campinagrande.pb.gov.br/wp-content/uploads/2024/05/DIAGNOSTICO-PARTICIPATIVO.pdf).
3. IBGE. Censo Demográfico 2022. [Agregados por setores censitários](https://ftp.ibge.gov.br/Censos/Censo_Demografico_2022/Agregados_por_Setores_Censitarios/) e [malhas de setores](https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_de_setores_censitarios__divisoes_intramunicipais/censo_2022/).
4. Brasil. Ministério da Saúde. [Unidades Básicas de Saúde cadastradas no CNES](https://dadosabertos.saude.gov.br/dataset/unidades-basicas-de-saude-ubs). Extração em 19/11/2026.

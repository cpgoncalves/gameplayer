"""
Análise de jogo EUA vs União Europeia com matriz de jogo produzida pelo
ChatGPT em relação ao problema da Gronelândia. O resultado da análise
é gravado em ficheiro Synthesis.xlsx.

O jogo, a abordagem e os resultados são cobertos pelo artigo:
    
    Gonçalves e Rouco (2026) Aplicação de I.A. Generativa à 
    Cenarização Estratégica com Recurso à Teoria dos Jogos -
    Caso da Gronelândia. 
    https://www.academia.edu/156990887/Aplica%C3%A7%C3%A3o_de_I_A_Generativa_%C3%A0_Cenariza%C3%A7%C3%A3o_Estrat%C3%A9gica_com_Recurso_%C3%A0_Teoria_dos_Jogos_Caso_da_Gronel%C3%A2ndia

    
O webinar de base que explica a metodologia e cobre o caso encontra-se
disponível na Playlist do YouTube: 
 https://youtube.com/playlist?list=PLmLUR-kyF1qWvL8J0gEt5gknFpbnwScP7&si=3I9Z2X2122gt3_Td
    
@autores: Carlos Pedro Gonçalves e Carlos Rouco
@institution: Universidade Lusófona
@school: Escola de Ciências Económicas e das Organizações (ECEO)
@department: Departamento de Gestão da Aviação Civil e Aeroportos

"""

import twoplayer as tp

X = tp.read_file("Gronelândia.xlsx")


tp.analyze_matrix(X)




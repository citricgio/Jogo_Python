# Tsunami Rush

Nossa implementação do jogo Tsunami Rush.
A proposta de jogo é um estilo endless run que deverá envolver algum tipo de desastre natural (escolhemos o tsunami), o jogo se assemelha a mecânica de outros jogos famosos, como por exemplo chrome dino, onde o jogador deve desviar dos obstaculos e recolhers as recompensas.
A condição de fim é dada quando o jogador colidir com algum dos obstáculos.



## Bônus
### GameIA



Optamos por implementar um segundo personagem no jogo que fosse contralado por uma máquina, esse segundo personagem terá o papel de um auxiliar no jogo.
Na implementação do segundo personagem utilizamos o framework pytorch, para o uso de algoritmos de aprendizado de reforço. O algoritmo escolhido foi o Q-learning, esse algoritmo busca encontrar a melhor ação a ser tomada, dado o estado atual.


### Prévia do treinamento
https://github.com/citricgio/Jogo_Python/assets/103596102/a2647594-c9dd-457f-9abb-686d4d0b22b2



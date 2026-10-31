# Caminho das Cinzas

**Caminho das Cinzas** é um jogo desenvolvido em Python utilizando a biblioteca PgZero, no estilo Roguelike com visão superior (*Top-Down*).

O jogador precisa atravessar um ambiente de obstáculos e inimigos, evitando colisões e administrando suas vidas até alcançar a saída.

## Objetivo do jogo

Explore o mapa, desvie dos inimigos e encontre o portal de saída para escapar das ruínas.

Durante a jornada:

- Atravesse o mapa utilizando movimentação em grade.
- Evite os inimigos que patrulham determinadas áreas.
- Preserve suas três vidas.
- Alcance a saída para concluir a missão.

O jogador perde quando suas vidas chegam a zero.

## Controles

| Tecla | Ação |
|---|---|
| `W` ou `↑` | Mover para cima |
| `S` ou `↓` | Mover para baixo |
| `A` ou `←` | Mover para a esquerda |
| `D` ou `→` | Mover para a direita |

O jogo também possui:
- Menu inicial.
- Controle de áudio.
- Menu de pausa.
- Tela de vitória.
- Tela de Game Over.

## Tecnologias utilizadas

- **Python 3:** linguagem de programação.
- **PgZero:** biblioteca utilizada para desenvolvimento do jogo.
- **Pygame Rect:** utilização da classe `Rect` para operações com retângulos e colisões.
- **Math:** cálculos matemáticos utilizados na movimentação dos personagens.

## Estrutura do projeto

```text
meu-game/
│
├── game.py
├── player.py
├── enemy.py
├── game_map.py
│
├── images/
│   ├── sprites do jogador
│   └── sprites dos inimigos
│
├── sounds/
│   └── efeitos sonoros
│
└── music/
    └── musica de fundo
```

## Como executar

### 1. Requisitos

- Python 3 instalado.
- PgZero instalado.

### 2. Instalação do PgZero

No terminal, execute:

```bash
pip install pgzero
```

### 3. Executar o jogo

Entre na pasta do projeto e execute:

```bash
pgzrun game.py
```

## Organização do código

O projeto foi dividido em módulos para facilitar a organização e manutenção:

- **game.py:** controla o fluxo principal, menu, áudio, colisões e estados do jogo.
- **player.py:** implementa o personagem principal, movimentação, animações e sistema de vidas.
- **enemy.py:** implementa os inimigos, movimentação de patrulha e animações.
- **game_map.py:** define o mapa, obstáculos, saída e verificação de áreas caminháveis.

## Sobre o desenvolvimento

O projeto foi desenvolvido como atividade prática de programação, com foco na aplicação de conceitos de orientação a objetos, lógica de programação, movimentação em grade, animações, colisões e organização modular do código.

---

**Caminho das Cinzas**  
*Explore. Sobreviva. Encontre a saída.*

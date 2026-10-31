
from player import Player
from game_map import GameMap
from enemy import Enemy
from pygame import Rect

WIDTH = 800
HEIGHT = 600
TITLE = "Caminho das Cinzas"

game_over = False
game_won = False
game_started = False
game_paused = False
sound_enabled = True

player = Player()
game_map = GameMap()

enemies = [
    Enemy(240, 120, patrol_distance=2),
    Enemy(480, 280, patrol_distance=2),
    Enemy(640, 440, patrol_distance=2)
]

music.set_volume(0.4)


def draw():
    screen.clear()

    if not game_started:
        screen.fill((15, 23, 42))

        screen.draw.text(
            "CAMINHO DAS CINZAS",
            center=(400, 180),
            fontsize=45,
            color="white"
        )

        screen.draw.filled_rect(
            Rect(300, 250, 200, 50), (0, 118, 110)
        )
        screen.draw.text("START", center=(400, 275), color="white")

        screen.draw.filled_rect(
            Rect(300, 320, 200, 50), (51, 65, 85)
        )
        screen.draw.text(
            "SOUND ON" if sound_enabled else "SOUND OFF",
            center=(400, 345),
            color="white"
        )

        screen.draw.filled_rect(
            Rect(300, 390, 200, 50), (130, 45, 45)
        )
        screen.draw.text("EXIT", center=(400, 415), color="white")
        return

    screen.fill((15, 23, 42))
    game_map.draw(screen)
    player.draw()

    for enemy in enemies:
        enemy.draw()

    screen.draw.text(
        f"Vidas: {player.health}",
        (20, 20),
        color="white"
    )

    if not game_paused and not game_over:
        screen.draw.filled_rect(
            Rect(660, 60, 100, 40), (51, 65, 85)
        )
        screen.draw.text(
            "PAUSE", center=(710, 80), color="white"
        )

    if game_paused:
        screen.draw.filled_rect(
            Rect(250, 180, 300, 240), (15, 23, 42)
        )

        screen.draw.text(
            "PAUSED",
            center=(400, 215),
            fontsize=40,
            color="white"
        )

        screen.draw.filled_rect(
            Rect(300, 250, 200, 40), (0, 118, 110)
        )
        screen.draw.text(
            "CONTINUE", center=(400, 270), color="white"
        )

        screen.draw.filled_rect(
            Rect(300, 305, 200, 40), (51, 65, 85)
        )
        screen.draw.text(
            "SOUND ON" if sound_enabled else "SOUND OFF",
            center=(400, 325),
            color="white"
        )

        screen.draw.filled_rect(
            Rect(300, 360, 200, 40), (130, 45, 45)
        )
        screen.draw.text(
            "EXIT", center=(400, 380), color="white"
        )

    if game_over:
        screen.draw.text(
            "GAME OVER",
            center=(400, 300),
            fontsize=60,
            color="red"
        )
    if game_won:
        screen.draw.filled_rect(
            Rect(150, 230, 500, 140),
            (15, 23, 42)
        )

        screen.draw.text(
            "YOU WIN!",
            center=(400, 280),
            fontsize=45,
            color="green"
        )

def on_mouse_down(pos):
    global game_started, sound_enabled, game_paused

    if not game_started:
        if Rect(300, 250, 200, 50).collidepoint(pos):
            game_started = True
            if sound_enabled:
                music.play("musica")

        elif Rect(300, 320, 200, 50).collidepoint(pos):
            sound_enabled = not sound_enabled

        elif Rect(300, 390, 200, 50).collidepoint(pos):
            exit()

        return

    if game_over:
        return

    if game_paused:
        if Rect(300, 250, 200, 40).collidepoint(pos):
            game_paused = False

        elif Rect(300, 305, 200, 40).collidepoint(pos):
            sound_enabled = not sound_enabled

            if sound_enabled:
                music.play("musica")
            else:
                music.stop()

        elif Rect(300, 360, 200, 40).collidepoint(pos):
            exit()

        return

    if Rect(660, 60, 100, 40).collidepoint(pos):
        game_paused = True


def update(dt):
    global game_over, game_won

    if not game_started or game_over or game_paused or game_won:
        return

    player.update(dt)

    if player.actor.colliderect(game_map.exit_rect):
        game_won = True
        music.stop()
        return

    for enemy in enemies:
        enemy.update(game_map, dt)

        if player.actor.colliderect(enemy.actor):
            if player.damage_timer <= 0:
                player.health -= 1
                player.damage_timer = 1.0

                if sound_enabled:
                    sounds.damage.play()

                player.actor.pos = (80, 80)
                player.target_x = 80
                player.target_y = 80
                player.moving = False

                if player.health <= 0:
                    game_over = True

                    if sound_enabled:
                        sounds.gameover.play()

                    music.stop()

                break


def on_key_down(key):
    if not game_started or game_over or game_paused or game_won:
        return

    if key == keys.RIGHT or key == keys.D:
        player.move(1, 0, game_map)

    elif key == keys.LEFT or key == keys.A:
        player.move(-1, 0, game_map)

    elif key == keys.UP or key == keys.W:
        player.move(0, -1, game_map)

    elif key == keys.DOWN or key == keys.S:
        player.move(0, 1, game_map)

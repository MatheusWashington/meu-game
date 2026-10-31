
from pgzero.actor import Actor
from math import hypot


class Player:
    def __init__(self):
        self.actor = Actor("player_idle_0", (80, 80))

        self.health = 3
        self.tile_size = 40
        self.speed = 4
        self.damage_timer = 0

        self.target_x = self.actor.x
        self.target_y = self.actor.y
        self.moving = False

        self.idle_frames = ["player_idle_0", "player_idle_1"]
        self.move_frames = ["player_move_0", "player_move_1"]

        self.animation_index = 0
        self.animation_timer = 0
        self.animation_speed = 0.15
        self.animation_state = "idle"

    def move(self, dx, dy, game_map):
        if self.moving:
            return

        new_x = self.target_x + dx * self.tile_size
        new_y = self.target_y + dy * self.tile_size

        if not game_map.is_walkable(new_x, new_y):
            return

        if new_x < 20 or new_x > 780:
            return

        if new_y < 20 or new_y > 580:
            return

        self.target_x = new_x
        self.target_y = new_y
        self.moving = True

    def update(self, dt):
        self.damage_timer = max(0, self.damage_timer - dt)

        if self.moving:
            dx = self.target_x - self.actor.x
            dy = self.target_y - self.actor.y
            distance = hypot(dx, dy)

            if distance <= self.speed:
                self.actor.x = self.target_x
                self.actor.y = self.target_y
                self.moving = False
            else:
                self.actor.x += (dx / distance) * self.speed
                self.actor.y += (dy / distance) * self.speed

        self.animate(dt)

    def draw(self):
        self.actor.draw()

    def animate(self, dt):
        current_state = "move" if self.moving else "idle"

        if current_state != self.animation_state:
            self.animation_state = current_state
            self.animation_index = 0
            self.animation_timer = 0

        self.animation_timer += dt

        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0

            frames = (
                self.idle_frames
                if self.animation_state == "idle"
                else self.move_frames
            )

            self.animation_index = (
                self.animation_index + 1
            ) % len(frames)

            self.actor.image = frames[self.animation_index]

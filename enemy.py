
from pgzero.actor import Actor
from math import hypot


class Enemy:
    def __init__(self, x, y, patrol_distance=3):
        self.actor = Actor("enemy_idle_0", (x, y))

        self.tile_size = 40
        self.speed = 2

        self.start_x = x
        self.start_y = y

        self.patrol_distance = patrol_distance
        self.direction = 1

        self.target_x = x
        self.target_y = y
        self.moving = False

        self.idle_frames = ["enemy_idle_0", "enemy_idle_1"]
        self.move_frames = ["enemy_move_0", "enemy_move_1"]

        self.animation_index = 0
        self.animation_timer = 0
        self.animation_speed = 0.15
        self.animation_state = "idle"

    def choose_target(self, game_map):
        next_x = self.target_x + self.direction * self.tile_size
        next_y = self.target_y

        distance = abs(next_x - self.start_x)

        if (
            not game_map.is_walkable(next_x, next_y)
            or distance > self.patrol_distance * self.tile_size
        ):
            self.direction *= -1
            return

        self.target_x = next_x
        self.target_y = next_y
        self.moving = True

    def update(self, game_map, dt):
        if not self.moving:
            self.choose_target(game_map)

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

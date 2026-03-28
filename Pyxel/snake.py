# Create a blank screen
import pyxel

class Game:
    def __init__(self):
        pyxel.init(160, 120, title="Snake")
        self.x = 75
        self.y = 55
        # Fruit
        self.apple_x = 5
        self.apple_y = 5
        self.generate_apple()
        self.vx = 2
        self.vy = 0
        self.speed = 2
        self.size = 5
        pyxel.run(self.update, self.draw)

    def generate_apple(self):
        # Ensure apple is within boundaries and matches grid
        self.apple_x = pyxel.rndi(0, (160 // 5) - 1) * 5
        self.apple_y = pyxel.rndi(0, (120 // 5) - 1) * 5

    def snake_increase(self):
        self.size += 1

    def update(self):
        # Game over if hit the corner (close game)
        if self.x >= pyxel.width or self.x <= 0:
            pyxel.quit()

        if self.y >= pyxel.height or self.y <= 0:
            pyxel.quit()

        # Movement to all sides when arrow keys pressed
        if pyxel.btn(pyxel.KEY_DOWN):
            self.vx, self.vy = 0, self.speed

        if pyxel.btn(pyxel.KEY_UP):
            self.vx, self.vy = 0, -self.speed

        if pyxel.btn(pyxel.KEY_LEFT):
            self.vx, self.vy = -self.speed, 0

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.vx, self.vy = self.speed, 0

        self.x += self.vx
        self.y += self.vy

        # collision with snake and apple must spawn randomly
        if self.x <= self.apple_x and self.y <= self.apple_y:
            self.size += 1
            self.generate_apple()

    def draw(self):
        pyxel.cls(0)

        # Create an object(snake head)
        pyxel.rect(self.x, self.y, 5, self.size, 11)

        # Create apple
        pyxel.rect(self.apple_x, self.apple_y, 5, 5, 8)

Game()
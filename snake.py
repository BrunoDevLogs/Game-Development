# Create a blank screen
import pyxel

class Game:
    def __init__(self):
        pyxel.init(160, 120, title="Snake")
        self.x = 75
        self.y = 55
        self.vx = 2
        self.vy = 0
        self.speed = 2
        self.size = 5
        pyxel.run(self.update, self.draw)

    def update(self):
        # Game over if hit the corner( close game)
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

    def draw(self):
        pyxel.cls(0)

        # Create an object(snake head)
        pyxel.rect(self.x, self.y, self.size, self.size, 11)

Game()

# Create fruit
# Fruit must spawn randomly
# If snake touches fruit it increases in length
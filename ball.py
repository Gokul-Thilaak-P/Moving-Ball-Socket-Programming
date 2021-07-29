
class Ball:
    def __init__(self, x, y, color):
        self.centre_x = x
        self.centre_y = y
        self.color = color
        self.radius = 25
        self.velocity = 25
        self.isjumping = False
        self.jump_pos = 10

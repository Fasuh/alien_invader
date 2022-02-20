from models.hitbox import Hitbox

class GameObject:
    def __init__(self, height, width, posX, posY) -> None:
        self.height = height
        self.width = width
        self.posX = posX
        self.posY = posY

    def getHitbox(self) -> Hitbox:
        rx = self.posX + self.width
        ry = self.posY + self.height

        return Hitbox(lx=self.posX, ly=self.posY, rx=rx, ry=ry)
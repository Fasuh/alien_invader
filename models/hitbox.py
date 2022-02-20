class Hitbox:
    def __init__(self, lx:float,ly:float,rx:float,ry:float,) -> None:
        self.topLeft = self.lx, self.ly = lx, ly
        self.bottomRight = self.rx, self.ry = rx, ry

    
    def collidesWithOther(self, other) -> bool:
        if (self.lx>=other.rx) or (self.rx <= other.lx) or (self.ry<=other.ly) or (self.ly>=other.ry):
            return False
        else:
            return True
        if (self.lx == self.rx or self.ly == self.ry or other.lx == other.rx
            or other.ly == other.ry):
            return False
    
        if (self.lx >= other.rx or other.lx >= self.rx):
            return False
    
        if (self.ry >= other.ly or other.ry >= self.ly):
            return False
    
        return True
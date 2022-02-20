import math
import random

from typing import List

from controllers.bullets_controller import BulletsController
from decorators.debounce import Debounce
from models.alien import Alien
from models.bounds import Bounds
from models.game_result import GameResult
from models.movement import Movement
from models.tick import Tick


class AlienController:
    def __init__(self, bulletController: BulletsController, bounds: Bounds) -> None:
        self.aliens: List[Alien] = list()
        self.padding = 10
        self.alienBounds = 5
        self.alienWidth = 20
        self.alienHeight = 20
        self.bulletController = bulletController
        self.movement = Movement.RIGHT
        self.movementSpeed = 0.05
        self.bounds = bounds

    def generateAliens(self, numberOfRows: int, bounds: Bounds):
        aliensPerRow = ((bounds.width - (2*self.alienBounds)) /
                        ((self.alienWidth + self.padding)))
        aliensFreeSpace = (aliensPerRow % 1)*(self.alienWidth+self.padding)
        aliensPerRowRealistic = math.floor(aliensPerRow)

        self.aliens = [Alien(position=x, height=self.alienHeight,
                             width=self.alienWidth) for x in range(numberOfRows * aliensPerRowRealistic)]

        for alien in self.aliens:
            specificRow = alien.position//aliensPerRowRealistic if alien.position > 0 else 0
            specificSpot = alien.position % aliensPerRowRealistic

            alien.posX = self.alienBounds + \
                (aliensFreeSpace/2)+(specificSpot*(alien.width+self.padding))
            alien.posY = self.alienBounds + \
                (aliensFreeSpace/2)+(specificRow*(alien.height+self.padding))

    @Debounce(0.5)
    def shoot(self):
        if self.aliens:
            randomAlien = random.choice(self.aliens)
            self.bulletController.registerEnemyBullet(alien=randomAlien)

    def alienTick(self, tick: Tick):
        if self.aliens:
            furthestLeftAlien = min(alien.posX for alien in self.aliens)
            furthestRightAlien = max(alien.posX for alien in self.aliens)

            distance = self.movementSpeed*tick.delta*self.movement.value

            realisticDistance = min(max(self.alienBounds - furthestLeftAlien, distance),
                                    self.bounds.width - (furthestRightAlien+self.alienWidth) - self.alienBounds)

            if realisticDistance != distance:
                self.flipMovement()

            self.move(realisticDistance)

    def move(self, distance: float):
        for alien in self.aliens:
            alien.posX += distance

    def flipMovement(self):
        if self.movement == Movement.RIGHT:
            self.movement = Movement.LEFT
        elif self.movement == Movement.LEFT:
            self.movement = Movement.RIGHT

    def notyfyHit(self, alien: Alien) -> GameResult:
        self.aliens.remove(alien)

        if not self.aliens:
            return GameResult.WIN

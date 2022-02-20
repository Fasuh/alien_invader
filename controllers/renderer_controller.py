from turtle import screensize
from typing import List
import pygame
from pygame.locals import *

from pygame.surface import Surface
from models.alien import Alien
from models.bullet import Bullet
from models.game_result import GameResult
from models.player import Player
from controllers.game_controller import GameController

class RendererController:
    def __init__(self):
        pass

    def render(self, screen:Surface, round:GameController):
        screen.fill((0, 0, 0))
        self.renderPlayer(screen, player=round.player)
        self.renderAliens(screen, aliens=round.aliens)
        self.renderBullets(screen, bullets=round.bulletsController.bullets)
        if round.result is not None:
            self.drawResult(screen, round.result)


    def renderPlayer(self, screen:Surface, player:Player):
        playerRect = (player.posX, player.posY, player.width, player.height)
        pygame.draw.rect(screen, player.color, playerRect)

    def renderAliens(self, screen:Surface, aliens:List[Alien]):
        for alien in aliens:
            alienRect = (alien.posX, alien.posY, alien.width, alien.height)
            pygame.draw.rect(screen, alien.color, alienRect)

    def renderBullets(self, screen:Surface, bullets:List[Bullet]):
        for bullet in bullets:
            bulletRect = (bullet.posX, bullet.posY, bullet.width, bullet.height)
            pygame.draw.rect(screen, bullet.color, bulletRect)

    def drawResult(self, screen:Surface, result:GameResult):
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        if result == GameResult.WIN:
            textsurface = myfont.render('YOU WIN', False, (255, 255, 255))
            center = textsurface.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
            screen.blit(textsurface, center)

        elif result == GameResult.LOSS:
            textsurface = myfont.render('YOU LOST', False, (255, 255, 255))
            center = textsurface.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
            screen.blit(textsurface, center)

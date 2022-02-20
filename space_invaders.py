import pygame
from pygame.locals import *

from controllers.time_controller import TimeController
from models.bounds import Bounds
from controllers.game_controller import GameController
from controllers.renderer_controller import RendererController
from models.tick import Tick
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.bounds = Bounds(width=640, height=400)
        self.size = self.width, self.height = self.bounds.width, self.bounds.height
        self.round = GameController(bounds=self.bounds)
        self.rendererController = RendererController()
        self.timeController = TimeController()
 
    def on_init(self):
        pygame.init()
        pygame.font.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Space Invaders')
        self._running = True
 
    def on_event(self, events, tick:Tick):
        if events:
            for event in events:
                if event.type == pygame.QUIT:
                    self._running = False

        self.round.playerTick(events, tick=tick)

    def on_loop(self, tick:Tick):
        self.round.roundTick(tick=tick)

    def on_render(self):
        self.rendererController.render(screen=self._display_surf, round=self.round)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            tick = self.timeController.tick()
            events = pygame.event.get()
            self.on_event(events, tick=tick)
            self.on_loop(tick=tick)
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
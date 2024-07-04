import pygame
import sys
from settings import *
from map import Map
from player import Player
from raycasting import RayCasting
from object_renderer import ObjectRenderer
from object_handler import ObjectHandler
from weapon import Weapon
from sound import Sound



class PixelGibs:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_RES[0], WINDOW_RES[1]), pygame.RESIZABLE)
        self.render_surface = pygame.Surface(RES)
        self.clock = pygame.time.Clock()
        self.running = True
        self.delta_time = 1
        self.new_game()
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(False)
        self.object_renderer = ObjectRenderer(self)
        self.object_handler = ObjectHandler(self)
        self.map.add_npcs()
        self.raycasting = RayCasting(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        pygame.mixer.music.load("resources/music/QEAN - Left Behinds - 09 Sunday Morning.ogg")

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        self.delta_time = self.clock.tick()  # limits FPS to 60
        pygame.display.set_caption(f"{self.clock.get_fps() : .1f}")

    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            self.player.single_fire_event(event)

    def run(self):
        pygame.mixer.music.play()
        while self.running:
            self.check_events()
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = PixelGibs()
    game.run()

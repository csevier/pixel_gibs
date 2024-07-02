import pygame
class Sound:
    def __init__(self, game):
        self.game = game
        pygame.mixer.init()
        self.path = 'resources/sfx/'
        self.lazer = pygame.mixer.Sound(self.path + 'Laser-Ricochet3.ogg')
        self.npc_pain = pygame.mixer.Sound(self.path + 'npc_pain.ogg')
        # self.npc_death = pygame.mixer.Sound(self.path + 'npc_pain.ogg')
        # self.npc_shot = pygame.mixer.Sound(self.path + 'npc_pain.ogg')
        # self.player_pain = pygame.mixer.Sound(self.path + 'npc_pain.ogg')
        # self.theme = pygame.mixer.Sound(self.path + 'npc_pain.ogg')

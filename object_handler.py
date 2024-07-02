from sprite_object import SpriteObject, AnimatedSprite
from npc import NPC
from settings import PLAYER_POS

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.animated_sprite_path = 'resources/sprites/animated_sprites/'

        self.add_sprite(SpriteObject(game))
        self.add_sprite(AnimatedSprite(game,scale=2))
        self.add_npc(NPC(game))
        self.add_npc(NPC(game, pos=PLAYER_POS))
        self.add_npc(NPC(game, pos=PLAYER_POS))
        self.add_npc(NPC(game, pos=PLAYER_POS))


    def update(self):
        for sprite in self.sprite_list:
            sprite.update()
        for npc in self.npc_list:
            npc.update()

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self, npc):
        self.npc_list.append(npc)

import pygame
from settings import PLAYER_POS
import dungeon_gen as dg
from random import randint
from npc import NPC
from sprite_object import SpriteObject, AnimatedSprite


_ = False
mini_map = []
# mini_map = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, _, 3, 3, 3, 3, _, _, _, 2, 2, 2, _, _, 1],
#     [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
#     [1, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, 1],
#     [1, _, _, 3, 3, 3, 3, _, _, _, _, _, _, _, _, 1],
#     [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, _, _, 4, _, _, _, 4, _, _, _, _, _, _, 1],
#     [1, 1, 1, 3, 1, 3, 1, _, 1, 3, 3, 3, 3, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
#     [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
#     [3, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
#     [1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    
# ]

# mini_map = [
#     [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
#     [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
#     [_, _, _, 3, 3, 3, 3, _, _, _, 2, 2, 2, _, _, _],
#     [_, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, _],
#     [_, _, _, _, _, _, 4, _, _, _, _, _, 2, _, _, _],
#     [_, _, _, 3, 3, 3, 3, _, _, _, _, _, _, _, _, _],
#     [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
#     [_, _, _, _, 4, _, _, _, 4, _, _, _, _, _, _, _],
#     [_, 1, 1, 3, 1, 3, 1, _, 1, 3, 3, 3, 3, 1, 1, _],
#     [_, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _],
#     [_, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _],
#     [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
#     [_, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _],
#     [_, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _],
#     [_, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _],
#     [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
#     [_, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _],
#     [_, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _],
#     [_, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _],
#     [_, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _],
#     [_, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _],
#     [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
#     [_, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _],
#     [_, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _],
#     [_, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _],
#     [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    
# ]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.generate()
        self.world_map = {}
        self.get_map()
        self.generate()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        for pos in self.world_map:
            pygame.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)

    def add_npcs(self):
        self.game.object_handler.add_sprite(SpriteObject(self.game))
        self.game.object_handler.add_sprite(AnimatedSprite(self.game,scale=2))
        for i in range(randint(4,12)):
            # find empty space come hell or high water!
            while True:
                new_pos = self.d.findEmptySpace(randint(1,10))
                if new_pos != (None, None):
                    break
            print(new_pos)
            self.game.object_handler.add_npc(NPC(self.game, pos=new_pos))

    def generate(self):
        tileSize = 1
        levelSize = 40
        self.d = dg.dungeonGenerator(levelSize, levelSize)
        #d.placeRoom(2, 2, 4, 0)
        self.d.placeRandomRooms(5, 11, 2, 4, 500)
        self.d.generateCorridors()
        self.d.connectAllRooms(30)
        self.d.pruneDeadends(20)
        self.d.placeWalls()
        PLAYER_POS = self.d.findEmptySpace(1)
        for x in range(levelSize):
            for y in range(levelSize):
                if x == 0 or y == 0 or x == levelSize-1 or y == levelSize-1:
                    self.d.grid[x][y] = dg.WALL


        self.mini_map = self.d.grid

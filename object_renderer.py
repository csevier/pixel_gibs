import os
import pygame
from settings import *
import numpy as np
import random

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.render_surface = game.render_surface
        self.wall_textures = self.load_wall_textures()
        self.sky = pygame.Surface((WIDTH, HEIGHT / 2))
        self.sky.fill("black")

        self.floor = pygame.Surface((WIDTH, HEIGHT / 2))
        #self.floor.fill("grey47")
        self.floor.fill("grey27")

    def draw(self):
        self.draw_background()
        self.render_game_object()
        pygame.transform.scale(self.render_surface,
                               (self.screen.get_width(),
                               self.screen.get_height()),
                               dest_surface=self.screen)

    def draw_background(self):
        self.render_surface.blit(self.sky, (0, 0))
        self.render_surface.blit(self.floor, (0, HEIGHT / 2))

    def render_game_object(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.render_surface.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def draw_floor(self):
        posx, posy = self.game.player.x, self.game.player.y
        
        for i in range(self.hres):
            x, y = posx, posy
            rot_i = self.game.player.angle + np.deg2rad(i/self.mod -30)
            sin, cos = np.sin(rot_i), np.cos(rot_i)
            
            for j in range(self.halfvres):
                n = self.halfvres / (self.halfvres-j)
                x, y, = posx + cos*n, posy + sin*n
                #shade = 0.2 + 0.8 * (1-j/HALF_HEIGHT)
                if int(x) % 2 == int(y)%2:
                    self.frame[i][self.halfvres*2-j-1]= [0,0,0]
                else:
                    self.frame[i][self.halfvres*2-j-1]= [1,1,1]

    def load_wall_textures(self):
        dir_path = './resources/textures'
        # to load a specific wall texture
        # comment the line below
        # uncomment the following line and change to match your textures file name
        textures = [dir_path+'/'+f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and 'blood' not in f]
        # textures = ['./resource/textures/mytesttexture.png']
        return {
            1: self.get_texture(random.choice(textures)),
            2: self.get_texture(random.choice(textures)),
            3: self.get_texture(random.choice(textures)),
            4: self.get_texture(random.choice(textures)),
            5: self.get_texture(random.choice(textures)),
        }
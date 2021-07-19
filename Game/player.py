import pygame
from pygame.math import Vector2
from sprite_sheet import SpriteSheet

class Player(pygame.sprite.Sprite):

    def __init__(self, dungeonhero, pos):
        super().__init__()
        self.game_area = dungeonhero.game_area
        self.texture1 = pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 2, 14, 15), (14*2, 15*2))
        self.rect = self.texture1.get_rect(center=pos)
        self.up_textures = [
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2)),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(43, 67, 15, 14), (14*2, 15*2)),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2)),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2)),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2)),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2)),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2)),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2))
        ]
        self.up_textures_rect = [
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2)).get_rect(center=pos),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(43, 67, 15, 14), (14*2, 15*2)).get_rect(center=pos),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2)).get_rect(center=pos),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2)).get_rect(center=pos),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2)).get_rect(center=pos),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2)).get_rect(center=pos),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2)).get_rect(center=pos),
            pygame.transform.scale(SpriteSheet("Assets/CharAni-Sheet4.png").get_image(11, 66, 15, 15), (14*2, 15*2)).get_rect(center=pos)
        ]
        self.pos = Vector2(pos)
        self.velocity = Vector2(0, 2)
        self.x = 400
        self.y = 300


    def load_player(self):
        self.game_area.blit(self.texture1, self.rect)

    def update(self):
        if pygame.key.get_pressed()[pygame.K_w]:
            for i in range(len(self.up_textures_rect)):
                self.pos -= self.velocity
                self.rect.center = self.pos
                self.kill()
            self.game_area.blit(self.texture1, self.rect)


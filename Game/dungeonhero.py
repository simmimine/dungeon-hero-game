import pygame
from Events.quitevent import quitscreen
from player import Player



class DungeonHero:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.game_area = pygame.Rect(60, 60, 520, 360)
        self.clock = pygame.time.Clock()

    def game_loop(self):
        all_sprites = pygame.sprite.Group(Player(self, self.game_area.center))
        Player(self, (400,300)).load_player()
        while True:
            quitscreen()
            self._update_screen()
            all_sprites.add(Player(self.game_area, self.game_area.center))
            all_sprites.update()

    def _update_screen(self):
        pygame.display.update()
        self.clock.tick(60)



if __name__ == "__main__":
    dungeon_hero = DungeonHero()
    dungeon_hero.game_loop()
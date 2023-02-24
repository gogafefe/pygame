import os
import random
import pygame


if __name__ == '__main__':
    pygame.init()

    bg = pygame.image.load('bg.png')
    box = pygame.image.load('data/wall.png')
    wall = pygame.transform.scale(box, (50, 50))
    screen = pygame.display.set_mode((bg.get_width(), bg.get_height()))
    pygame.display.set_caption('Марио')

    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    players = pygame.sprite.Group()
    player = pygame.sprite.Sprite()
    player_image = load_image('sprite.png')
    player.image = pygame.transform.scale(player_image, (50, 70))
    player.rect = player.image.get_rect()
    players.add(player)
    player.rect.x = 50
    player.rect.y = 380

    y = 380

    speed = 4
    is_jump = False
    yspeed = 0

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()

        if is_jump:
            y -= yspeed
            yspeed -= 2
        elif keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            is_jump = True
            yspeed = 24
        if y > 380:
            is_jump = False
            yspeed = 0
            y = 380

        screen.blit(bg, (0, 0))
        players.draw(screen)
        player.rect.y = y
        pygame.display.update()
    pygame.quit()

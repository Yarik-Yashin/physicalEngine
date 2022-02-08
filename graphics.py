import pygame
from main import Vector, Solid

G = 1 * 10 ** -2
DEBUG = False
GRAPHIC_DEBUG = False
simulation_time_in_tics = 30000
if __name__ == '__main__':
    W = 1500
    H = 1000
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.font.SysFont('arial', 36)
    f1 = pygame.font.Font(None, 36)

    clock = pygame.time.Clock()
    objects = [Solid(750, 400, 200, 'Earth', (0, 255, 0), speed=Vector(0.2, 0)),
               Solid(750, 500, 40000, 'Sun', (255, 255, 0), speed=Vector(0.0, 0.0)),
               Solid(750, 650, 20, 'Mars', (255, 0, 0), speed=Vector(-0.15, 0)),
               Solid(750, 570, 80, 'Venus', (255, 0, 0), speed=Vector(-0.23, 0)),
               Solid(750, 1020, 3180, 'Jupiter', (200, 100, 10), speed=Vector(-0.09, 0)),
               ]
    coordinates = list()
    for i in range(simulation_time_in_tics):
        coords = list()
        for j in objects:
            j.update(1 / 100, objects, G)
            coords.append((j.position, j.color))
        coordinates.append(coords)
    for i in range(simulation_time_in_tics):
        if GRAPHIC_DEBUG:
            text1 = f1.render(f'Time in tics:{i} tics.', True, (0, 255, 0))
            text1Rect = text1.get_rect()
            screen.blit(text1, (100, 50))
            text2 = f1.render(f'Final time in tics:{simulation_time_in_tics}.', True, (0, 255, 0))
            text1Rect = text1.get_rect()
            screen.blit(text2, (100, 100))
            if i - 2000 < 0:
                b = 0
            else:
                b = i - 2000
            for k in coordinates[b:i]:
                for j in k:
                    pygame.draw.circle(screen, j[1], (j[0].x, j[0].y), 1)
        for k in coordinates[i]:
            pygame.draw.circle(screen, k[1], (k[0].x, k[0].y), 10)
        clock.tick(1000)
        pygame.display.update()
        screen.fill((0, 0, 0))
    '''while True:
        for i in objects:

            i.update(1 / 100, objects, G)
            if DEBUG:
                f = open("demofile2.txt", "a")
                f.write(str(i))
                f.close()
            if GRAPHIC_DEBUG:
                coordinates.append((i.position, i.color))
                for j in coordinates:
                    pygame.draw.circle(screen, j[1], (j[0].x, j[0].y), 1)
            pygame.draw.circle(screen, i.color, (i.position.x, i.position.y), 20)

        clock.tick(1000)
        pygame.display.flip()
        screen.fill((0, 0, 0))
        '''

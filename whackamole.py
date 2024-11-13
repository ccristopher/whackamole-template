import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        location = 0, 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    position = x // 32, y // 32
                    if position == location:
                        location = random.randrange(0, 20), random.randrange(0, 16)

            # draw bg
            screen.fill("light green")

            #draw grid
            for i in range(1, 16):
                pygame.draw.line(
                    screen,
                    "black",
                    (0, i * 32),
                    (640, i * 32)
                )
            for i in range(1, 20):
                pygame.draw.line(
                    screen,
                    "black",
                    (i * 32, 0),
                    (i * 32, 512)
                )

            #draw mole
            pixel_location = location[0] * 32, location[1] * 32
            screen.blit(mole_image, mole_image.get_rect(topleft=pixel_location))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
import pygame

width = 500
height = 500
color = ((0,255,0))

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(this, x, y, width, height, color) -> None:
        this.x = x
        this.y = y
        this.width = width
        this.height = height
        this.color = color
        this.rect = (x,y,width,height)
        this.vel = 3

    def draw(this, screen):
        pygame.draw.rect(screen, this.color, this.rect)

    def move(this):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            this.x -= this.vel
        if keys[pygame.K_RIGHT]:
            this.x += this.vel
        if keys[pygame.K_UP]:
            this.y -= this.vel
        if keys[pygame.K_DOWN]:
            this.y += this.vel

        this.rect = (this.x, this.y, this.width, this.height)


def redrawWindow(screen, player):
    screen.fill((255,255,255))
    player.draw(screen)
    pygame.display.update()

def main():
    run = True
    p = Player(50, 50, 100, 100, color)
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(screen, p)

main()

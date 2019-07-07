import pygame, sys, random
from pygame.locals import *

class FlappyBird:
        def __init__(self):
            self.screen = pygame.display.set_mode((400, 720))
            self.bird = pygame.Rect(65, 50, 50, 50)
            self.background = pygame.image.load("assets/background.png").convert()
            self.birdSprites = [pygame.image.load("assets/1.png").convert_alpha(), pygame.image.load("assets/2.png").convert_alpha(), pygame.image.load("assets/dead.png")]
            self.wallUp = pygame.image.load("assets/bottom.png").convert_alpha()
            self.wallDown = pygame.image.load("assets/top.png").convert_alpha()
            self.gap = 150
            self.wallX = 400
            self.birdY = 350
            self.jump = 0
            self.jumpspeed = 10
            self.gravity = 5
            self.dead = False
            self.sprite = 0
            self.counter = 0
            self.offset = random.randint(-110, 110)

        def updateWalls(self):
            self.wallX -= 2
            if self.wallX < -80:
                self.wallX = 400
                self.counter += 1
                self.offset = random.randint(-110, 110)

        def birdUpdate(self):
            if self.jump:
                self.jumpspeed -= 1
                self.birdY -= self.jumpspeed
                self.jump -= 1
            else:
                self.birdY += self.gravity
                self.gravity += 0.1
            
            self.bird[1] = self.birdY
            downRect = pygame.Rect(self.wallX, 0 - self.gap - self.offset, self.wallDown.get_width(), self.wallDown.get_height())
            upRect = pygame.Rect(self.wallX, 360 + self.gap - self.offset, self.wallUp.get_width(), self.wallUp.get_height())

            if upRect.colliderect(self.bird):
                self.dead = True
            if downRect.colliderect(self.bird):
                self.dead = True
            if not 0 < self.bird[1] < 720:
                self.bird[1] = 50
                self.birdY = 50
                self.dead = False
                self.counter = 0
                self.wallX = 400
                self.offset = random.randint(-110, 110)
                self.gravity = 5
        
        def run(self): 
            clock = pygame.time.Clock()
            pygame.display.set_caption('Flappy Bird')
            pygame.font.init()
            font = pygame.font.SysFont("Arial", 50)
            while True:
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if (event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead:
                        self.jump = 17
                        self.gravity = 5
                        self.jumpspeed = 10

                self.screen.fill((255, 255, 255))
                self.screen.blit(self.background, (0, 0))
                self.screen.blit(self.wallUp, (self.wallX, 360 + self.gap - self.offset))
                self.screen.blit(self.wallDown, (self.wallX, 0 - self.gap - self.offset))
                self.screen.blit(font.render(str(self.counter), -1, (255, 255, 255)), (200, 50))
                
                if self.dead:
                    self.sprite = 2
                elif self.jump:
                    self.sprite = 1

                self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))

                if not self.dead:
                    self.sprite = 0
                self.updateWalls()
                self.birdUpdate()
                pygame.display.update()

if __name__ == "__main__":
    FlappyBird().run()

from pygame import *
# clock = time.Clock()
main = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
class Game_Sprite(sprite.Sprite):
    def __init__(self, name_picture, speed, x1, y1, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(name_picture), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
    def blit1(self):
        main.blit(self.image, (self.rect.x, self.rect.y))
class Player(sprite.Sprite):
    def __init__(self, color_fill, speed, x1, y1, size_x, size_y):       
        self.image = Surface((size_x, size_y))
        self.image.fill((color_fill[0], color_fill[1], color_fill[2]))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
    def blit1(self):
        main.blit(self.image, (self.rect.x, self.rect.y))
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] == True and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] == True and self.rect.y < 400:
            self.rect.y += self.speed
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_o] == True and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_l] == True and self.rect.y < 400:
            self.rect.y += self.speed
rocket1 = Player([255, 255, 255], 3, 10, 200, 20, 100)
rocket2 = Player([255, 255, 255], 3, 670, 200, 20, 100)
ball = Game_Sprite('asteroid.png', 5, 325, 225, 50, 50)
flag = True
flag2 = True
while flag != False:
    if flag2 == True:
        main.fill((99, 184, 255))
        ball.blit1()
        rocket1.update_left()
        rocket1.blit1()
        rocket2.update_right()
        rocket2.blit1()


    for ev in event.get():
        if ev.type == QUIT:
            flag = False
    clock.tick(60)
    display.update()

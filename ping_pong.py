from pygame import *
font.init()

#Створюємо вікно та фон
window = display.set_mode((500,500))
BG = transform.scale(image.load("BG.jpg"),(500,500))


#Клас для платформи
class Platform():
    def __init__(self,uids,height,x,y,platform_emage,speed,points):
        self.emage = image.load(platform_emage)
        self.rect = Rect(x,y,uids,height)
        self.speed = speed
        self.points = points
    def draw(self,window):
        window.blit(self.emage,(self.rect.x,self.rect.y))

#Клас для м'яча
class Ball():
    def __init__(self,uids,height,x,y,platform_emage,speed_x,speed_y):
        self.emage = image.load(platform_emage)
        self.rect = Rect(x,y,uids,height)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def draw(self,window):
        window.blit(self.emage,(self.rect.x,self.rect.y))


#створення спрайтів
platform_1 = Platform(15,75,0,300,"platform.png",6,0)
platform_2 = Platform(15,75,490,300,"platform.png",6,0)
ball = Ball(50,50,255,255,"ball.png",4,4)
def pause():
    pause = font.Font(None, 60).render("PAUSE", True, (0,0,0))
    while True:
        for i in event.get():
            if i.type == KEYDOWN:
                if i.key == K_SPACE:
                    return
        window.blit(pause, (180,220))
        display.update()
win_1 = font.Font(None, 50).render("Player 1 Win", True, (255,0,0))
win_2 = font.Font(None, 50).render("Player 2 Win", True, (255,0,0))

#Ігровий цикл
game = True
finish = False
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        #коли кнопка натиснута 
        if e.type == KEYDOWN:
            #якщо це була кнопка "W" чи нопка "S", то рухаємо першу платформу 
            if e.key == K_s:
                platform_1.speed = 6
            if e.key == K_w:
                platform_1.speed = -6
            #якщо це була стрілка вверхи чи стрілка вниз, то рухаємо другу платформу 
            if e.key == K_DOWN:
                platform_2.speed = 6
            if e.key == K_UP:
                platform_2.speed = -6

            if e.key == K_SPACE:
                pause()
    if not finish:
        window.blit(BG,(0,0))
        #задаємо визначене вище прискорення платформам
        platform_1.rect.y += platform_1.speed
        platform_2.rect.y += platform_2.speed

        #задаємо визначене вище прискорення м'ячу
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y

        #додаємо текстові лічильники (зробимо на уроці)
        score1_font = font.Font(None,50).render("Рахунок 1:" + str(platform_2.points), True, (0,0,0))
        score2_font = font.Font(None,50).render("Рахунок 2:" + str(platform_1.points), True, (0,0,0))

        #перевіряємо зіткнення м'яча з верхом та низом екрану
        if ball.rect.y > 465:
           ball.speed_y *= -1
        if ball.rect.y < 0:
          #тут швидкість ball.speed_y треба поміняти на протилежну
           ball.speed_y *= -1

    
         #перевіряємо якщо м'яч вилітає за праву чи ліву сторони екрану
        if ball.rect.x > 500:     
            display.update()
            platform_2.points += 1
            ball.rect.x = 250
            ball.rect.y = 200
        if ball.rect.x < 0:      
            display.update()
            platform_1.points += 1
            ball.rect.x = 250
            ball.rect.y = 200
        #так само як в поередній перевірці, тільки бали додаємо першій платформі

        #перевіряємо зіткнення наших платформ з м'ячем
        if ball.rect.colliderect(platform_1.rect):
            ball.speed_y *= -1
            ball.speed_x *= -1
        if ball.rect.colliderect(platform_2.rect):
            ball.speed_y *= -1
            ball.speed_x *= -1


        #перевіряємо зіткнення платформ з верхом та низом екрану
        #Для першої платформи
        if platform_1.rect.y > 425:
            platform_1.speed *= -1
        if platform_1.rect.y < 0:
            platform_1.speed *= -1
    
        #Для другої платформи
        if platform_2.rect.y > 425:
            platform_2.speed *= -1
        if platform_2.rect.y < 0:
            platform_2.speed *= -1

        if platform_1.points >= 10:
            finish = True
            window.blit(win_1, (160,230))
    
        if platform_2.points >= 10:
            finish = True
            window.blit(win_2, (160,230))

        platform_1.draw(window)
        platform_2.draw(window)
        ball.draw(window)
        window.blit(score1_font, (10,2))
        window.blit(score2_font, (260,2))
    display.update()
    clock.tick(40)

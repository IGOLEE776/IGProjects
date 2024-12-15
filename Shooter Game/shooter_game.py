#Create your own shooter

from pygame import *
from random import *
from time import time as timer
#game scrn
l = 700
t = 500

img_bg = 'galaxy.jpg' #bg
img_rocket = 'rocket.png' #player
img_ufo = 'ufo.png' #enemy
img_bullet = 'bullet.png' #pew
display.set_caption('Game shootee')
win = display.set_mode((l,t))
bg = transform.scale(image.load(img_bg), (l,t))
img_rock = 'asteroid.png' #DE RACK

#bg sauna soundy susssssssssssssssssssssssssss
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('Camera Click (6).mp3')
miss = mixer.Sound('missed.ogg')
boom = mixer.Sound('Explosion (28).mp3')
wrong = mixer.Sound('wrong-lie-incorrect-buzzer.mp3')
shipboom = mixer.Sound('Explosion (4).mp3')
shipboom2 = mixer.Sound('Explosion.mp3')


#font and the lebel
font.init()
font1 = font.SysFont('Verdana', 35)
font2 = font.SysFont('Verdana', 75)
font3 = font.SysFont('Verdana', 70)
font4 = font.SysFont('Verdana', 18)
lose = font4.render('THE CHEAP UFOS JUST HIT EARTH AAAAAAAAAAAAAAAAAA', True, (255,0,0))
losecrash = font1.render('YOU CRASHED A UFO AAAAAAAAAA', True, (255,0,0))
losecrash2 = font1.render('YOU CRASHED A ROCK AAAAAAAAA', True, (255,50,50))
losecrashed = font1.render('YOU DIES', True, (255,50,50))
winer = font1.render('ufos dies', True, (0,255,30))

score = 0 #>:)
missed = 0 #I MISSED.
death = 10 #ono
winner = 10000 #YOU WIN

#what class are u in?
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_w, size_h, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_w, size_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

#play clac
class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys [K_d] and self.rect.x < l - 70:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < t - 30:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx - 15, self.rect.top - 20, 30, 40, -30)
        bullets.add(bullet)

#why is there a ufo?
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global missed
        if self.rect.y > t:
            missed += 1
            self.rect.x = randint(30, l-30)
            self.rect.y = 0
            self.speed = randint(3,7)
            miss.play()

#DE ROUK
class Rock(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global missed
        if self.rect.y > t:
            self.rect.x = randint(30, l-30)
            self.rect.y = 0
            self.speed = randint(1,4)

#IM A BULLET
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        #dies after the top bc ye
        if self.rect.y < 0:
            self.kill()

#objec
rocket = Player(img_rocket, l/2.2 , t-50, 70, 30, 15)
#ufo is in group chat
ufos = sprite.Group()
#group of raining balats
bullets = sprite.Group()

#REWIND TIME
def reset_game():
    global score, missed, finish, ufos, bullets, reload, num_fire, life
    score = 0
    missed = 0
    finish = False
    reload = False
    num_fire = 50
    life = 3
    ufos.empty()
    bullets.empty()
    rocks.empty()
    for i in range(1,6):
        ufo = Enemy(img_ufo, randint(30, t-30), -40, 50, 50, randint(3,7))
        ufos.add(ufo)
    for i in range(1,4):
        rock = Rock(img_rock, randint(30, t-30), -40, 50, 50, randint(1,4))
        rocks.add(rock)
    rocket.rect.x = l/2.2
    rocket.rect.y = t-50
    mixer.music.play()

#lopgaming
finish = False
run = True
for i in range(1,6):
    ufo = Enemy(img_ufo, randint(30, t-30), -40, 50, 50, randint(3,7))
    ufos.add(ufo)

rocks = sprite.Group()
for i in range(1,4):
    rock = Rock(img_rock, randint(30, t-30), -40, 50, 50, randint(1,4))
    rocks.add(rock)

reload = False
num_fire = 50
life = 3

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        #pew from [_]
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if not finish:
                    if num_fire > 0 and reload == False:
                        num_fire -= 1
                        rocket.fire()
                        fire_sound.play()

                    if num_fire <= 0 and reload == False:
                        last_time = timer()
                        reload = True
            elif e.key == K_r and finish:
                reset_game()
            elif e.key == K_q:
                run = False
    if not finish:
        win.blit(bg, (0, 0))
        rocket.draw()
        rocket.move()
        ufos.update()
        ufos.draw(win)
        bullets.update()
        bullets.draw(win)
        rocks.update()
        rocks.draw(win)

        #make the loadr i g
        if reload == True:
            now_time = timer()
            if now_time - last_time < 3:
                reloadt = font1.render(str(now_time - last_time) + ' --', True, (255,255,255))
                win.blit(reloadt, (10,400))
            else:
                num_fire = 50
                reload = False
        #draw the letters lol
        tscore = font3.render(str(score), 1, (255,255,255))
        win.blit(tscore, (10,0))
        tmiss = font1.render('Misses: ' + str(missed) + '/' + str(death), 1, (255,100,100))
        win.blit(tmiss, (10,70))
        bulletsleft = font1.render(str(num_fire) + ' ---', 1, (100,100,100))
        win.blit(bulletsleft, (10,450))
        livest = font3.render(str(life), 1, (100,100,100))
        win.blit(livest, (640,0))

        #BULLET AND UFO DIES
        COLLIDES = sprite.groupcollide(ufos, bullets, True, True)
        for c in COLLIDES:
            score += randint(50,150)
            boom.play()
            ufo = Enemy(img_ufo, randint(30, l-30), -40, 50, 50, randint(3,7))
            ufos.add(ufo)

        #BULLET AND UFO DIES
        COLLIDES2 = sprite.groupcollide(rocks, bullets, True, True)
        for c in COLLIDES2:
            score += randint(20,50)
            boom.play()
            rock = Rock(img_rock, randint(30, l-30), -40, 50, 50, randint(1,4))
            rocks.add(rock)

        #To much UFOS AAAAAAAAAAAAA hit the PALMNET
        if missed >= death:
            finish = True
            win.blit(lose, (70,250))
            wrong.play()
            mixer.music.stop()

        '''#YOU HIT THE UFO CREEPER
        if sprite.spritecollide(rocket, ufos, False):
            finish = True
            win.blit(losecrash, (35,250))
            shipboom.play()
            mixer.music.stop()

        #YOU HIT THE RUOK CREEPER
        if sprite.spritecollide(rocket, rocks, False):
            finish = True
            win.blit(losecrash2, (35,250))
            shipboom.play()
            mixer.music.stop()''' #its just yes
        
        if sprite.spritecollide(rocket, rocks, False):
            sprite.spritecollide(rocket, rocks, True)
            life -= 1
            shipboom2.play()
            rock = Rock(img_rock, randint(30, l-30), -40, 50, 50, randint(1,4))
            rocks.add(rock)
        
        if sprite.spritecollide(rocket, ufos, False):
            sprite.spritecollide(rocket, ufos, True)
            life -= 1
            shipboom2.play()
            ufo = Enemy(img_ufo, randint(30, l-30), -40, 50, 50, randint(3,7))
            ufos.add(ufo)

        if life <= 0:
            finish = True
            win.blit(losecrashed, (250,250))
            shipboom.play()
            mixer.music.stop()


        '''#ufo dies and wiiner
        if score >= winner:
            finish = True
            win.blit(winer, (70,250))
            mixer.music.stop()''' #no no winner but infinite tho
    
    else:
        #if r clicker means reset ur character
        reset_quit_label = font4.render('Click R to reset or Q to GET OUT', True, (255,255,255))
        win.blit(reset_quit_label, (190, 300))

    display.update()
    time.delay(60)
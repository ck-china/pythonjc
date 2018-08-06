import pygame
import random
import time
class Plane(object):
    def __init__(self,path,screen,x,y):
        self.x=x
        self.y=y
        self.w=100
        self.h=124
        self.screen=screen
        self.path=path
        self.plane=pygame.image.load(self.path)
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.bullet_lis=[]
        self.hit=False
        self.lis=[]
        self._zha()
        self.num=0
        self.ind=0
    def display(self):
        self.screen.blit(self.plane,self.rect)
        for i in self.bullet_lis:
            if i.xiaoshi():
                self.bullet_lis.remove(i)
            i.display()
            i.fashe()
        if self.hit == True:
            self.screen.blit(self.lis[self.ind],self.rect)
            self.num+=1
            if self.num == 10:
                self.ind+=1
                self.num =0
            if self.ind >3:
                time.sleep(1)
                exit()
    def bom(self):
        self.hit=True
class zidan(object):
    def __init__(self,path,screen,x,y):
        self.screen=screen
        self.x=x
        self.y=y
        self.h=22
        self.w=22
        self.path=path
        self.zidan=pygame.image.load(self.path)#子弹图片的路径
        self.rect=pygame.Rect(self.x,self.y,self.h,self.w)
    def display(self):
        self.screen.blit(self.zidan,(self.x,self.y))
    def fashe(self):
        self.y-=5
    def xiaoshi(self):
        if self.y <=0:
            return True
        else:
            return False
class Hero(Plane):
    def __init__(self,path,screen):
        Plane.__init__(self,path,screen,(400-100)/2,550)
    def fire(self):
        self.bullet_lis.append(zidan('./images/bullet.png',self.screen,self.rect.x+40,self.rect.y-20))
    def _zha(self):
        self.lis.append(pygame.image.load('./images/hero_blowup_n1.png'))
        self.lis.append(pygame.image.load('./images/hero_blowup_n2.png'))
        self.lis.append(pygame.image.load('./images/hero_blowup_n3.png'))
        self.lis.append(pygame.image.load('./images/hero_blowup_n4.png'))

class Di(Plane):
    def __init__(self,path,screen):
        Plane.__init__(self,path,screen,0,0)
        self.flag='right'
    def _zha(self):
        self.lis.append(pygame.image.load('./images/enemy1_down1.png'))
        self.lis.append(pygame.image.load('./images/enemy1_down2.png'))
        self.lis.append(pygame.image.load('./images/enemy1_down3.png'))
        self.lis.append(pygame.image.load('./images/enemy1_down4.png'))
    def move(self):
        if self.flag == 'right':
            self.rect.x +=2
            if self.rect.x == 410:
                self.flag = 'left'
        else:
            self.rect.x -=2
            if self.rect.x <= 0:
                self.flag = 'right'
        self.rect.y +=1
    def fire(self):
        self.bullet_lis.append(Dizidan('./images/bullet1.png',self.screen,self.rect.x+30,self.rect.y+80))
class Dizidan(object):
    def __init__(self,path,screen,x,y):
        self.screen=screen
        self.x=x
        self.y=y
        self.h=22
        self.w=22
        self.path=path
        self.zidan=pygame.image.load(self.path)#子弹图片的路径
        self.rect=pygame.Rect(self.x,self.y,self.h,self.w)
    def display(self):
        self.screen.blit(self.zidan,(self.x,self.y))
    def fashe(self):
        self.y+=5
    def xiaoshi(self):
        if self.y >700:
            return True
        else:
            return False

def move(hero,buchang,di):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print('break!')
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            '''
            if event.key == pygame.K_UP:
                hero.rect.y -= buchang
            elif event.key == pygame.K_DOWN:
                hero.rect.y += buchang
            elif event.key == pygame.K_LEFT:
                hero.rect.x -= buchang
            elif event.key == pygame.K_RIGHT:
                hero.rect.x += buchang
            '''
            if event.key == pygame.K_SPACE:
                hero.fire()
            if event.key == pygame.K_b:
                #hero.bom()
                di.bom()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        if hero.rect.x == 380:
            hero.rect.x = 380
        else:
            hero.rect.x += buchang

    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        if hero.rect.x == 0:
            hero.rect.x = 0
        else:
            hero.rect.x -= buchang
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        if hero.rect.y < 0:
            hero.rect.y = hero.rect.y
        else:
            hero.rect.y -= buchang
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        if hero.rect.y > 578:
            hero.rect.y = hero.rect.y
        else:
            hero.rect.y += buchang
    #if keys_pressed[pygame.K_SPACE]:
        #hero.fire()
def lose(hero,di):
    for i in di.bullet_lis:
        if (i.x >= hero.rect.x and i.x <= hero.rect.x+100)and (i.y >= hero.rect.y and i.y <= hero.rect.y+122):
            hero.bom()
    for i in hero.bullet_lis:
        if (i.x >= di.rect.x and i.x <=di.rect.x+69)and (i.y <= di.rect.y+93 and i.y >=di.rect.y):
            di.bom()

def main():
    #用pygame.display.set_mode拉来初始化屏幕的大小

    screen=pygame.display.set_mode((480,700),0,32)

    #用pygame.image.load来初始化背景图片，赋值给background
    background=pygame.image.load('./images/background.png')

    #同理获得英雄飞机的图片，赋值给feiji
    hero=Hero('./images/hero2.png',screen)
    di=Di('./images/enemy1.png',screen)

    #rect=pygame.Rect((480-100)/2,700-122,100,122)

    clock=pygame.time.Clock() #获得时间控制器
    while True:
        #把背景图片覆盖到屏幕上
        screen.blit(background,(0,0))
        #把英雄飞机的图片覆盖到屏幕上
        hero.display()
        di.display()
        #刷新屏幕
        move(hero,10,di)
        lose(hero,di)
        di.move()
        if di.rect.x %50  == 0:
            di.fire()
        pygame.display.update()
        clock.tick(60) #时钟控制
if __name__ == '__main__':
    main()

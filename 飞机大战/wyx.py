import pygame
import time
import random
class Plane(object):#飞机的父类
    def __init__(self,lujing,screen,x,y):

        self.lujing=lujing
        self.screen=screen
        self.x=x
        self.y=y
        self.width=22
        self.height=22
        self.feiji1=pygame.image.load(self.lujing)
        self.rect=pygame.Rect(self.x,self.y,self.width,self.height)
        self.flag="right"
        self.bulletlist=[]
    def display(self):
        self.screen.blit(self.feiji1,self.rect)
        for i in self.bulletlist:
            if i.xiaoshi():
                self.bulletlist.remove(i)

            i.display()
            i.mv()
        self.panzha()


class Zidan(object):#子弹的父类
    def __init__(self,lujing,screen,x,y):
        self.lujing=lujing
        self.screen=screen
        self.x=x+34
        self.y=y
        self.bullet=pygame.image.load(self.lujing)
    def display(self):
        self.screen.blit(self.bullet,(self.x,self.y))

class HeroPlane(Plane):#英雄的飞机
    def __init__(self,lujing,screen,x,y):
        Plane.__init__(self,lujing,screen,x,y)
        self.baolist=[]
        self.baotian()
        self.a=0
        self.b=0

        self.shifoubao=False
    def fire(self):
        self.bulletlist.append( Bullet("./xiazai/plane.png",self.screen,self.rect.x,self.rect.y))
    def baotian(self):
        self.baolist.append(pygame.image.load("./xiazai/hero_blowup_n1.png"))
        self.baolist.append(pygame.image.load("./xiazai/hero_blowup_n2.png"))
        self.baolist.append(pygame.image.load("./xiazai/hero_blowup_n3.png"))
        self.baolist.append(pygame.image.load("./xiazai/hero_blowup_n4.png"))
    def baozha(self):
        self.shifoubao=True

    def panzha(self):
        if self.shifoubao==True:
            self.screen.blit(self.baolist[self.a],self.rect)
            self.b+=1
            if self.b==10:
                self.a+=1
                self.b=0
            if self.a>3:
                self.a=0
                self.rect.x=100
                self.rect.y=378

        #else:
         #self.screen.blit(self.lujing,self.rect)

class EnemyPlane(Plane):    #敌人的飞机
    def __init__(self,lujing,screen,x,y):
        Plane.__init__(self,lujing,screen,x,y)
        self.baolist=[]

        self.shifoubao=False
        self.baotian()
        self.a=0
        self.b=0


    #def duojiao(self):
     #   self.screen.
    def fire(self):
        if self.rect.y>=-50:
            self.bulletlist.append(dBullet("./xiazai/bullet1.png",self.screen,self.rect.x,self.rect.y+80))

    def baotian(self):
        self.baolist.append(pygame.image.load("./xiazai/enemy1_down1.png"))
        self.baolist.append(pygame.image.load("./xiazai/enemy1_down2.png"))
        self.baolist.append(pygame.image.load("./xiazai/enemy1_down3.png"))
        self.baolist.append(pygame.image.load("./xiazai/enemy1_down4.png"))
    def panzha(self):
        if self.shifoubao==True:
            self.screen.blit(self.baolist[self.b],self.rect)
            self.a+=1
            if self.a==10:
                self.b+=1
                self.a=0
            if self.b>3:
                self.b=0
                self.rect.x=0
                self.rect.y=-60
    def baozha(self):
        self.shifoubao=True

    def move1(self):
        if self.flag=="right":
            self.rect.x+=1

        else :
            self.rect.x-=1
        if self.rect.x>320:
            if self.rect.y<=0:
                self.rect.y+=20
            else:
                self.rect.y+=5
            self.flag="left"
        elif self.rect.x<0:
            if self.rect.y<=0:
                self.rect.y+=21
            else:
                self.rect.y+=5
            self.flag="right"
class Bullet(Zidan):#英雄的子弹
    def __init__(self,lujing,screen,x,y):
        Zidan.__init__(self,lujing,screen,x,y)

    def mv(self):
        self.y-=5
    def xiaoshi(self):
        if self.y<0:
            return True
        else:
            return False

class dBullet(Zidan):#敌人的子弹
    def __init__(self,lujing,screen,x,y):
        Zidan.__init__(self,lujing,screen,x,y)
    def mv(self):
        self.y+=5
    def xiaoshi(self):
        if self.y>500:
            return True
        else:
            return False
class EnemyPlane2(Plane):
    def __init__(self,lujing,screen,x,y):
        Plane.__init__(self,lujing,screen,x,y)
        self.baolist=[]

        self.shifoubao=False
        self.baotian()
        self.a=0
        self.b=0


    #def duojiao(self):
     #   self.screen.
    def fire(self):
        if self.rect.y>=-20:
            self.bulletlist.append(dBullet("./xiazai/bullet2.png",self.screen,self.rect.x,self.rect.y+80))

    def baotian(self):
        self.baolist.append(pygame.image.load("./xiazai/enemy0_down1.png"))
        self.baolist.append(pygame.image.load("./xiazai/enemy0_down2.png"))
        self.baolist.append(pygame.image.load("./xiazai/enemy0_down3.png"))
        self.baolist.append(pygame.image.load("./xiazai/enemy0_down4.png"))
    def panzha(self):
        if self.shifoubao==True:
            self.screen.blit(self.baolist[self.b],self.rect)
            self.a+=1
            if self.a==10:
                self.b+=1
                self.a=0
            if self.b>3:
                self.b=0
                self.rect.x=0
                self.rect.y=-30
    def baozha(self):
        self.shifoubao=True

    def move1(self):
        if self.flag=="right":
            self.rect.x+=1

        else :
            self.rect.x-=1
        if self.rect.x>320:
            if self.rect.y<=0:
                self.rect.y+=20
            else:
                self.rect.y+=5
            self.flag="left"
        elif self.rect.x<0:
            if self.rect.y<=0:
                self.rect.y+=21
            else:
                self.rect.y+=5
            self.flag="right"

def jiluo(fa,zhui,a,b):
    for i in fa.bulletlist:
        if (i.x >= zhui.rect.x and i.x <= zhui.rect.x+a) and (i.y >= zhui.rect.y and i.y <= zhui.rect.y+b):
            zhui.baozha()

#def jihui(hero,enemy):
 #   for i in enemy.bulletlist:
  #      if (i.x >= hero.rect.x and i.x <= hero.rect.x+100) and (i.y >= hero.rect.y and i.y <= hero.rect.y+124):
   #         hero.baozha()
    #for i in hero.bulletlist:
     #   if (i.x >= enemy.rect.x and i.x <= enemy.rect.x+69) and (i.y >= enemy.y and i.y <= enemy.rect.y+89):
#      enemy.baozha()
def move(move_step,hero,enemy):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_q]:
        hero.baozha()
        enemy.baozha()
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        if hero.rect.x<300:
            hero.rect.x += move_step
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        if hero.rect.x>0:
            hero.rect.x -= move_step
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
        if hero.rect.y>0:
            hero.rect.y -= move_step
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        if hero.rect.y<376:
            hero.rect.y += move_step

def main():
    screen=pygame.display.set_mode((400,500),0,32)

    background=pygame.image.load("./xiazai/bg.png")
    hero=HeroPlane("./xiazai/hero1.png",screen,(400-100)/2,376)# 创建对象hero
    enemy=EnemyPlane("./xiazai/enemy1_hit.png",screen,(400-69)/2,0)
    enemy2=EnemyPlane2("./xiazai/enemy0.png",screen,(400-200)/2,0)
    while True:
        move_step=10
        aa=random.randint(1,30)

        screen.blit(background,(0,0))
        hero.display()#调用方法
        enemy.display()
        enemy2.display()
        enemy.move1()
        enemy2.move1()
        clock=pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("退出了")
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hero.fire()
        if aa%27==0:
            enemy.fire()
        move(move_step,hero,enemy)
        enemy.shifoubao=False
        hero.shifoubao=False
        enemy2.shifoubao=False

        jiluo(hero,enemy,69,89)
        jiluo(enemy,hero,100,124)
        jiluo(hero,enemy,51,39)

        pygame.display.update()
        clock.tick(60)

if __name__=="__main__":

    main()


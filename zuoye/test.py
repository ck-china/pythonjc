import pygame
def main():
    screen=pygame.display.set_mode((690,660),0,32)
    clock = pygame.time.Clock() #获得游戏时钟 控制器
    a=1
    while True :
        background=pygame.image.load('./images/%d.jpg'%a)
        screen.blit(background,(0,0))

        a+=1
        clock.tick(1)
        pygame.display.update()
        if a > 9:
            a=1
        for event in pygame.event.get():
            print('event.type = ', event.type)
            print('event = ', event)
            if event.type == pygame.QUIT:#退出游戏
                print('游戏退出')
                pygame.quit()
                exit() #退出程序
main()

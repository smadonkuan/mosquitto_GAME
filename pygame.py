import sys, time
import random
import pygame
from pygame.locals import Color, QUIT, MOUSEBUTTONDOWN, USEREVENT, USEREVENT

a=0
global b,bug,tool
b=0
bug=tool=1
    
#更改圖片路徑

class Menu:
    def start(self):
        global b
        display_width = 950
        display_height = 550

        WHITE = (255, 255, 255)
        RED = (255, 0, 0)
        bg_location = './開始背景.jpg'

        pygame.init()
        class Button(object):
            def __init__(self, text, color, x=None, y=None, **kwargs):
                self.surface = font.render(text, True, color)
                self.WIDTH = self.surface.get_width()
                self.HEIGHT = self.surface.get_height()

                if 'centered_x' in kwargs and kwargs['centered_x']:
                    self.x = display_width // 2 - self.WIDTH // 2
                else:
                    self.x = x

                if 'centered_y' in kwargs and kwargs['cenntered_y']:
                    self.y = display_height // 2 - self.HEIGHT // 2
                else:
                    self.y = y

            def display(self):
                screen.blit(self.surface, (self.x, self.y))

            def check_click(self, position):
                x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
                y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

                if x_match and y_match:
                    return True
                else:
                    return False
        def starting_screen():
            global b
            screen.blit(bg, (0,0))

            game_title = font.render('Killing   Bugs', True, WHITE)
            #game_title = pygame.font.Font('C:/PYTHON/pygame/蟲系剋星.ttf',3)
            screen.blit(game_title, (display_width//2 - game_title.get_width()//2, 150))

            start_button = Button('START', RED, None, 300, centered_x=True)
            set_button = Button('SET', RED, None, 350, centered_x=True)
            exit_button = Button('EXIT', WHITE, None, 400, centered_x=True)
            
            start_button.display()
            set_button.display()
            exit_button.display()

            pygame.display.update()

            while True:
                if start_button.check_click(pygame.mouse.get_pos()):
                    start_button = Button('START', RED, None, 300, centered_x=True)
                else:
                    start_button = Button('START', WHITE, None, 300, centered_x=True)

                if set_button.check_click(pygame.mouse.get_pos()):
                    set_button = Button('SET', RED, None, 350, centered_x=True)
                else:
                    set_button = Button('SET', WHITE, None, 350, centered_x=True)

                if exit_button.check_click(pygame.mouse.get_pos()):
                    exit_button = Button('EXIT', RED, None, 400, centered_x=True)
                else:
                    exit_button = Button('EXIT', WHITE, None, 400, centered_x=True)

                start_button.display()
                set_button.display()
                exit_button.display()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        raise SystemExit
                if pygame.mouse.get_pressed()[0]:
                    if start_button.check_click(pygame.mouse.get_pos()):
                        b=1
                        break
                        ##可設連接
                    if set_button.check_click(pygame.mouse.get_pos()):
                        b=2
                        break
                    if exit_button.check_click(pygame.mouse.get_pos()):
                        pygame.quit()
                        raise SystemExit
                        break

        screen = pygame.display.set_mode((display_width, display_height))
        bg = pygame.image.load(bg_location)
        font_addr = pygame.font.get_default_font()
        font = pygame.font.Font(font_addr, 36)

        starting_screen()


    def choose1(self):
        global b,bug
        SCREEN_HEIGHT = 550
        SCREEN_WIDTH = 900

        backgroud = "./選單畫面.jpg"
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('選單')


        class Button():
            def __init__(self, x, y, image, scale):
                width = image.get_width()
                height = image.get_height()
                self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False

            def draw(self, surface):
                action = False
                #get mouse position
                pos = pygame.mouse.get_pos()

                #check mouseover and clicked conditions
                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        self.clicked = True
                        action = True

                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False

                #draw button on screen
                surface.blit(self.image, (self.rect.x, self.rect.y))

                return action

        first_img = pygame.image.load('./工具列按鈕拼圖1.png').convert_alpha()
        first_img = pygame.transform.scale(first_img,(200,70))

        second_img = pygame.image.load('./工具列按鈕拼圖2.png').convert_alpha()
        second_img = pygame.transform.scale(second_img,(200,70))

        third_img = pygame.image.load('./工具列按鈕拼圖3.png').convert_alpha()
        third_img = pygame.transform.scale(third_img,(200,70))

        four_img = pygame.image.load('./蚊子拼圖.jpg').convert_alpha()
        four_img = pygame.transform.scale(four_img,(150,150))

        five_img = pygame.image.load('./蒼蠅拼圖.jpg').convert_alpha()
        five_img = pygame.transform.scale(five_img,(150,150))

        six_img = pygame.image.load('./蜻蜓拼圖.jpg').convert_alpha()
        six_img = pygame.transform.scale(six_img,(150,150))

        seven_img = pygame.image.load('./蝴蝶拼圖.jpg').convert_alpha()
        seven_img = pygame.transform.scale(seven_img,(150,150))

        eight_img = pygame.image.load('./蟑螂拼圖.jpg').convert_alpha()
        eight_img = pygame.transform.scale(eight_img,(150,150))

        nine_img = pygame.image.load('./瓢蟲拼圖.jpg').convert_alpha()
        nine_img = pygame.transform.scale(nine_img,(150,150))
        #create button instances
        one_button = Button(5, 70, first_img, 0.8)
        two_button = Button(5, 140, second_img, 0.8)
        three_button = Button(5, 210, third_img, 0.8)
        mos_button = Button(250, 100, four_img, 0.8)
        pufly_button = Button(400, 100, five_img, 0.8)
        drafly_button = Button(550, 100, six_img, 0.8)
        butter_button = Button(250, 275, seven_img, 0.8)
        #cock_button = Button(400, 275, eight_img, 0.8)
        cock_button = Button(700, 100, eight_img, 0.8)
        butfly_button = Button(550, 275, nine_img, 0.8)
        #game loop

        run = True
        while run:
            bg = pygame.image.load(backgroud)
            bg = pygame.transform.scale(bg,(900,550))
            #screen.fill((202, 228, 241))
            screen.blit(bg,(0,0))
            #screen.blit(bg,(0,0))
            if one_button.draw(screen):
                print('他是昆蟲按鈕')
            if two_button.draw(screen):
                print('他是工具按鈕')
                b=4
                break
            if three_button.draw(screen):
                print('點擊進入排行榜')
                b=3
                break
            if mos_button.draw(screen):
                print('蚊子讓人很癢')
                b=4
                bug=1
                break
            if pufly_button.draw(screen):
                print('吃屎蒼蠅')
                b=4
                bug=2
                break
            if drafly_button.draw(screen):
                print('蜻蜓雨神')
                b=4
                bug=3
                break
            if butter_button.draw(screen):
                print('蝴蝶真的好美麗')
                b=4
                bug=4
                break
            if cock_button.draw(screen):
                print('蟑螂天敵是拖鞋')
                b=4
                bug=5
                break
            if butfly_button.draw(screen):
                print('點點蟲')
                b=4
                bug=6
                break

            #event handler
            for event in pygame.event.get():
                #quit game
                if event.type == pygame.QUIT:
                    run = False


            pygame.display.update()


        pygame.quit()


    def choose2(self):
        global b,tool
        SCREEN_HEIGHT = 550
        SCREEN_WIDTH = 950

        backgroud = "./選單畫面.jpg"
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('選單')




        class Button():
            def __init__(self, x, y, image, scale):
                width = image.get_width()
                height = image.get_height()
                self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False

            def draw(self, surface):
                action = False
                #get mouse position
                pos = pygame.mouse.get_pos()

                #check mouseover and clicked conditions
                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        self.clicked = True
                        action = True

                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False

                #draw button on screen
                surface.blit(self.image, (self.rect.x, self.rect.y))

                return action

        first_img = pygame.image.load('./工具列按鈕拼圖1.png').convert_alpha()
        first_img = pygame.transform.scale(first_img,(200,70))

        second_img = pygame.image.load('./工具列按鈕拼圖2.png').convert_alpha()
        second_img = pygame.transform.scale(second_img,(200,70))

        third_img = pygame.image.load('./工具列按鈕拼圖3.png').convert_alpha()
        third_img = pygame.transform.scale(third_img,(200,70))

        four_img = pygame.image.load('./滅蚊拍拼圖.jpg').convert_alpha()
        four_img = pygame.transform.scale(four_img,(150,150))

        five_img = pygame.image.load('./捕蟲網拼圖.jpg').convert_alpha()
        five_img = pygame.transform.scale(five_img,(150,150))


        #create button instances
        one_button = Button(5, 70, first_img, 0.8)
        two_button = Button(5, 140, second_img, 0.8)
        three_button = Button(5, 210, third_img, 0.8)
        kill = Button(250, 100, four_img, 0.8)
        kill_2_button = Button(400, 100, five_img, 0.8)

        #game loop

        run = True
        while run:
            bg = pygame.image.load(backgroud)
            bg = pygame.transform.scale(bg,(950,550))
            #screen.fill((202, 228, 241))
            screen.blit(bg,(0,0))
            #screen.blit(bg,(0,0))
            if one_button.draw(screen):
                print('他是昆蟲按鈕')
                b=2
                break
            if two_button.draw(screen):
                print('他是工具按鈕')
            if three_button.draw(screen):
                print('點擊進入排行榜')
                b=3
                break
            if kill.draw(screen):
                print('這是滅蚊拍')
                b=1
                tool=1
                break
            if kill_2_button.draw(screen):
                print('這是捕蟲網')
                b=1
                tool=2
                break


            #event handler
            for event in pygame.event.get():
                #quit game
                if event.type == pygame.QUIT:
                    run = False


            pygame.display.update()

        pygame.quit()

    def game(self):
        global bug,tool
        window_width = 950
        window_height = 550
        image_width = 80
        image_height = 50
        FPS = 60


        def get_random_position(window_width, window_height, image_width, image_height):
            random_x = random.randint(image_width, window_width - image_width)
            random_y = random.randint(image_height, window_height - image_height)
            return random_x, random_y

        # init mosquito random position
        class Mosquito(pygame.sprite.Sprite):
            def __init__(self, width, height, random_x, random_y, window_width, window_height):
                global bug
                super().__init__()
                                     
                if bug==1:
                    self.raw_image = pygame.image.load("./蚊子去背.png").convert_alpha()
                elif bug==2:
                    self.raw_image = pygame.image.load("./蒼蠅去背.png").convert_alpha()
                elif bug==3:
                    self.raw_image = pygame.image.load("./蜻蜓去背.png").convert_alpha()
                elif bug==4:
                    self.raw_image = pygame.image.load("./蝴蝶去背.png").convert_alpha()
                elif bug==5:
                    self.raw_image = pygame.image.load("./蟑螂去背.png").convert_alpha()
                elif bug==6:
                    self.raw_image = pygame.image.load("./瓢蟲去背.png").convert_alpha()
                
                #self.raw_image = pygame.image.load('C:/PYTHON/pygame/蚊子.png').convert_alpha()
                self.image = pygame.transform.scale(self.raw_image, (width, height))
                self.rect = self.image.get_rect()
                self.rect.topleft = (random_x, random_y)
                self.width = width
                self.height = height
                self.window_width = window_width
                self.window_height = window_height

        def main():
            global tool
            time=0
            pygame.init()
            
            window = pygame.display.set_mode((window_width, window_height))
            pygame.display.set_caption('KillingBugs_GameWindow')
            bg_img = pygame.image.load("./遊戲背景.jpg").convert()
            
           # pygame.display.flip()
            
            random_x, random_y = get_random_position(window_width, window_height, image_width, image_height)
            mosquito = Mosquito(image_width, image_height, random_x, random_y, window_width, window_height)
            reload_mosquito_event = USEREVENT + 1
            pygame.time.set_timer(reload_mosquito_event,700)
            points = 0
            times=100
            
            my_font = pygame.font.SysFont(None, 30)
            my_hit_font = pygame.font.SysFont(None, 75)
            hit_text_surface = None
            main_clock = pygame.time.Clock()


            while True:
                # 偵測事件
                for event in pygame.event.get():
                    
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == reload_mosquito_event:
                        # 偵測到重新整理事件，固定時間移除蚊子，換新位置
                        time+=1
                        times-=1
                        if time<=100:
                            mosquito.kill()
                            # 蚊子新位置
                        else:
                            pygame.quit()
                            sys.exit()
                            #time超過就跳出來
                        
                        random_x, random_y = get_random_position(window_width, window_height, image_width, image_height)
                        mosquito = Mosquito(image_width, image_height, random_x, random_y, window_width, window_height)
                    elif event.type == MOUSEBUTTONDOWN:
                        # 當使用者點擊滑鼠時，檢查是否滑鼠位置 x, y 有在蚊子圖片上
                        if random_x < pygame.mouse.get_pos()[0] < random_x + image_width and random_y < pygame.mouse.get_pos()[1] < random_y + image_height:
                            mosquito.kill()
                            random_x, random_y = get_random_position(window_width, window_height, image_width, image_height)
                            mosquito = Mosquito(image_width, image_height, random_x, random_y, window_width, window_height)
                            hit_text_surface = my_hit_font.render('Hit!!', True, (0, 0, 0))
                            points += 5
                            
               
                # 背景顏色，清除畫面
                #window_surface.fill(WHITE)
                window.blit(bg_img, [0, 0])
                
                if tool==1:
                    mouse ="./滅蚊拍去背.png"
                elif tool==2:
                    mouse ="./捕蟲網去背.png"
                mouse_img = mouse
                
                #mouse_img = 'C:/PYTHON/pygame/滅蚊拍去背.png'
                mouse_cursor = pygame.image.load(mouse_img).convert_alpha()
                mouse_cursor = pygame.transform.scale(mouse_cursor,(175,150))

                    #滑鼠的x,y座標
                x, y = pygame.mouse.get_pos()
                    #隱藏滑鼠
                pygame.mouse.set_visible(False)
                x -= mouse_cursor.get_width() /2
                y -= mouse_cursor.get_height()/125
                    #用其他圖形代替滑鼠
                window.blit(mouse_cursor, (x, y))
               # pygame.display.update()####閃現

                # 遊戲分數儀表板
                text_surface = my_font.render('Points: {}'.format(points), True, (0, 0, 0))
                point_surface = my_font.render('Times: {}'.format(times), True, (0, 0, 0))
                # 渲染物件
                window.blit(mosquito.image, mosquito.rect)
                window.blit(text_surface, (10, 0))
                window.blit(point_surface, (150, 0))
                # 顯示打中提示文字
                if hit_text_surface:
                    window.blit(hit_text_surface, (10, 0))
                    hit_text_surface = None

                pygame.display.update()
                # 控制遊戲迴圈迭代速率
                main_clock.tick(FPS)

        if __name__ == '__main__':    
            main()
      def rank(self):
        #create display window
        SCREEN_HEIGHT = 550
        SCREEN_WIDTH = 900

        backgroud ="./排行榜.jpg"
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('排行榜')




        class Button():
            def __init__(self, x, y, image, scale):
                width = image.get_width()
                height = image.get_height()
                self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False


            def draw(self, surface):
                action = False
                #get mouse position
                pos = pygame.mouse.get_pos()

                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        self.clicked = True
                        action = True

                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False

                #draw button on screen
                surface.blit(self.image, (self.rect.x, self.rect.y))


                return action
        return_button = pygame.image.load('./返回.png').convert_alpha()
        return_button = pygame.transform.scale(return_button,(200,50))


        #create button instances
        firstbutton = Button(630,500 , return_button, 0.8)

        #game loop


        run = True
        while run:
            bg = pygame.image.load(backgroud)
            bg = pygame.transform.scale(bg,(900,550))

            #screen.fill((202, 228, 241))
            screen.blit(bg,(0,0))
            #screen.blit(bg,(0,0))
            if firstbutton.draw(screen):
                print('返回按鈕')
                break

            #event handler
            for event in pygame.event.get():
                #quit game
                if event.type == pygame.QUIT:
                    run = False


            pygame.display.update()

        pygame.quit()
        




m=Menu()
while(True):
    
    if b==0:
        m.start()
    elif b==1:
        m.game()
        b=3
    elif b==2:
        m.choose1()
        
    elif b==3:
        m.rank()
        b=0
    elif b==4:
        m.choose2()

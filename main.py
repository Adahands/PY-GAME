import pygame
import random

# --------------------------------------------------------------------------------------------------------

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# -------------------------------------------------------------------------------------------------------

pygame.mixer.music.load("Kevin MacLeod The Builder.mp3")

# -------------------------------------------------------------------------------------------------------

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("猜拳遊戲")

# --------------------------------------------------------------------------------------------------------

background_image = pygame.image.load('zhigraiiiiiiu.png')
font = pygame.font.Font('mingliu.TTF', 33)
play_message = font.render("      來玩猜拳吧!", True, (255, 235, 193))
play_message2 = font.render("請選擇 石頭 布 或 剪刀", True, (255, 235, 193))

# --------------------------------------------------------------------------------------------------------

score_font = pygame.font.Font('mingliu.TTF', 45)
user_score_message = score_font.render("你", True, (255, 235, 200))
comp_score_message = score_font.render("  電腦", True, (255, 235, 200))
tie_message = font.render(" 平手", True, (255, 235, 193))
won_message = font.render("你贏了", True, (124, 252, 0))
lost_message = font.render("你輸了", True, (255, 0, 0))

# --------------------------------------------------------------------------------------------------------

button_rock = pygame.image.load('button_rock.png')
button_paper = pygame.image.load('button_paper.png')
button_scissor = pygame.image.load('button_scissor.png')

# --------------------------------------------------------------------------------------------------------

rock_rect = button_rock.get_rect(topleft=(25, 330))
paper_rect = button_rock.get_rect(topleft=(225, 330))
scissor_rect = button_rock.get_rect(topleft=(425, 330))

# --------------------------------------------------------------------------------------------------------

rock = pygame.image.load('rock.png')
paper = pygame.image.load('paper.png')
scissor = pygame.image.load('scissor.png')
weapon_choices = [rock, paper, scissor]

# --------------------------------------------------------------------------------------------------------

is_start = False
user_weapon = None
comp_weapon = None
is_user_weapon = False
is_show_weapon = False
user_weapon_text = None
comp_weapon_text = None
result_message = None


# --------------------------------------------------------------------------------------------------------

def pick_weapon(user_weapon_index):
    global is_start, user_weapon, comp_weapon, is_user_weapon, is_show_weapon, user_weapon_text, comp_weapon_text
    is_start = True
    user_weapon = weapon_choices[user_weapon_index]
    is_user_weapon = True
    is_show_weapon = False
    comp_weapon_index = random.randint(0, 2)
    comp_weapon = weapon_choices[comp_weapon_index]


# --------------------------------------------------------------------------------------------------------

# def pick_weapon(user_weapon_index):
#    global is_start, user_weapon, comp_weapon, is_user_weapon, is_show_weapon
#    is_start = True
#    user_weapon = weapon_choices[user_weapon_index]
#    is_user_weapon = True
#    is_show_weapon = False
#    comp_weapon_index = random.randint(0, 2)
#    comp_weapon = weapon_choices[comp_weapon_index]

# --------------------------------------------------------------------------------------------------------

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rock_rect.collidepoint(event.pos):
                # is_start = True
                # user_weapon = weapon_choices[0]
                # is_user_weapon = True
                # index =random.randint(0, 2)
                # comp_weapon =weapon_choices
                pick_weapon(0)
                # print("rock")

            elif paper_rect.collidepoint(event.pos):
                # is_start = True
                # user_weapon = weapon_choices[1]
                # is_user_weapon = True
                # index = random.randint(0, 2)
                # comp_weapon = weapon_choices
                pick_weapon(1)
                # print('paper')

            elif scissor_rect.collidepoint(event.pos):
                # is_start = True
                # user_weapon = weapon_choices[2]
                # is_user_weapon = True
                # index = random.randint(0, 2)
                # comp_weapon = weapon_choices
                pick_weapon(2)
                # print("scissor")

    screen.blit(background_image, (0, 0))
    screen.blit(user_score_message, (50, 20))
    screen.blit(comp_score_message, (420, 20))

    if is_start is False:
        screen.blit(play_message, (100, 170))
        screen.blit(play_message2, (120, 200))
        pygame.mixer.music.play(-1)

    if is_show_weapon:
        screen.blit(user_weapon, (60, 70))
        screen.blit(comp_weapon, (350, 70))
        screen.blit(result_message, (250, 20))
        is_user_weapon = False

    if is_user_weapon:
        is_show_weapon = True
        if user_weapon == comp_weapon:
            result_message = tie_message

        elif user_weapon == rock and comp_weapon == scissor:
            result_message = won_message

        elif user_weapon == rock and comp_weapon == paper:
            result_message = lost_message

        elif user_weapon == scissor and comp_weapon == rock:
            result_message = lost_message

        elif user_weapon == scissor and comp_weapon == paper:
            result_message = won_message

        elif user_weapon == paper and comp_weapon == rock:
            result_message = won_message

        elif user_weapon == paper and comp_weapon == scissor:
            result_message = lost_message

    screen.blit(button_rock, rock_rect)
    screen.blit(button_paper, paper_rect)
    screen.blit(button_scissor, scissor_rect)

    pygame.display.update()
    clock.tick(20)

# ---------------------------------------------------------------------------------------------------------

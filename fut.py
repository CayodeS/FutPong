import pygame

pygame.init()

janela = pygame.display.set_mode([1280,720])
titulo = pygame.display.set_caption('Fut Pong')

vitoria = pygame.image.load("assets/win.png")

placar1 = 0
placar1_img = pygame.image.load('assets/score/0.png')
placar2 = 0
placar2_img = pygame.image.load('assets/score/0.png')

campo = pygame.image.load('assets/field.png')

player = pygame.image.load('assets/player1.png')
player_y = 310
player_movecima = False
player_movebaixo = False

player2 = pygame.image.load('assets/player2.png')
player2_y = 310

bola = pygame.image.load('assets/ball.png')
bola_x = 617
bola_y = 337
bola_dire = -5
bola_diry = 1


def move_player():
    global player_y

    if player_movecima:
        player_y -= 5
    else:
        player_y += 0

    if player_movebaixo:
        player_y += 5
    else:
        player_y -= 0

    if player_y <= 0:
        player_y = 0
    elif player_y >= 575:
        player_y = 575


def move_player2():
    global  player2_y

    player2_y = bola_y

def move_bola():
    global bola_x
    global bola_y
    global bola_dire
    global bola_diry
    global placar1
    global placar2
    global placar1_img
    global placar2_img

    bola_x += bola_dire
    bola_y += bola_diry

    if bola_x <= 120:
        if player_y <= bola_y + 23:
            if player_y + 146 >= bola_y:
                bola_dire *= -1

    if bola_x > 1100:
        if player2_y <= bola_y + 23:
            if player2_y + 146 >= bola_y:
                bola_dire *= -1

    if bola_y >= 665:
        bola_diry *= -1
    elif bola_y <= 0:
        bola_diry *= -1

    if bola_x <= -50:
        bola_x = 617
        bola_y = 337
        bola_dire *= -1
        bola_diry *= -1
        placar2 += 1
        placar2_img = pygame.image.load(f'assets/score/{placar2}.png')

    elif bola_x >= 1320:
        bola_x = 617
        bola_y = 337
        bola_dire *= -1
        bola_diry *= -1
        placar1 += 1
        placar1_img = pygame.image.load(f'assets/score/{placar1}.png')


def desenho():
    if placar1 or placar2 < 3:
        janela.blit(campo, (0, 0))
        janela.blit(player, (50, player_y))
        janela.blit(player2, (1150, player2_y))
        janela.blit(bola, (bola_x, bola_y))
        janela.blit(placar1_img, (500, 50 ))
        janela.blit(placar2_img, (710, 50))
        move_bola()
        move_player()
        move_player2()
    else:
        janela.blit(vitoria, (300,330))

loop = True
while loop:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop=False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                player_movecima = True
            elif evento.key == pygame.K_s:
                player_movebaixo = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w:
                player_movecima = False
            elif evento.key == pygame.K_s:
                player_movebaixo = False
    desenho()
    pygame.display.update()
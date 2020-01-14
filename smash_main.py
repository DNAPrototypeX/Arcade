# Paul Moore
def smash_main():
    import pygame
    from TitleScreen import TitleScreen
    from smash_Platform import Platform
    from smash_Player import Player
    import time
    import sys

    pygame.init()
    size = (1050, 650)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Epic Smash Siblings Omega")
    clock = pygame.time.Clock()

    # Colours
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (255, 0, 255)

    # Vars
    done = False
    timer = 0

    def character_select(ID):
        p1_choose = TitleScreen(74, screen, 250, 100, "Player 1 Choose Colour.")
        p2_choose = TitleScreen(74, screen, 250, 100, "Player 2 Choose Colour")

        r = 255
        g = 0
        b = 0
        RGB = (r, g, b)
        colour_rects = [pygame.Rect(400, 200, 20, 20),
                        pygame.Rect(450, 200, 20, 20),
                        pygame.Rect(500, 200, 20, 20),
                        pygame.Rect(550, 200, 20, 20),
                        pygame.Rect(600, 200, 20, 20),
                        pygame.Rect(500, 240, 20, 20)]
        colour_list = [RED, BLUE, GREEN, YELLOW, PURPLE, RGB]
        done = False
        while not done:
            if r > 0 and b == 0:
                r -= 5
                g += 5
                colour_list[5] = (r, g, b)
            elif g > 0 and r == 0:
                g -= 5
                b += 5
                colour_list[5] = (r, g, b)
            elif b > 0 and g == 0:
                r += 5
                b -= 5
                colour_list[5] = (r, g, b)
            if ID == 0:
                p1_choose.drawText()
            else:
                screen.blit(title_image, (0, 0))
                p2_choose.drawText()
            pygame.draw.rect(screen, BLACK, (390, 190, 240, 40))
            pygame.draw.rect(screen, BLACK, (490, 230, 40, 40))
            for i in range(len(colour_rects)):
                if colour_rects[i].width == 40:
                    pygame.draw.rect(screen, colour_list[i], colour_rects[i].move(-10, -10))
                else:
                    pygame.draw.rect(screen, colour_list[i], colour_rects[i])

            pygame.display.update()
            m_pos = pygame.mouse.get_pos()
            for colour in colour_rects:
                if pygame.Rect(colour).collidepoint(m_pos[0], m_pos[1]):
                    colour.width = 40
                    colour.height = 40
                else:
                    colour.width = 20
                    colour.height = 20

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if ID == 0:
                        if pygame.Rect(colour_rects[0]).collidepoint(m_pos[0], m_pos[1]):
                            players[0].colour = RED
                            click_sound.play()
                            return
                        elif pygame.Rect(colour_rects[1]).collidepoint(m_pos[0], m_pos[1]):
                            players[0].colour = BLUE
                            click_sound.play()
                            return
                        elif pygame.Rect(colour_rects[2]).collidepoint(m_pos[0], m_pos[1]):
                            players[0].colour = GREEN
                            click_sound.play()
                            return
                        elif pygame.Rect(colour_rects[3]).collidepoint(m_pos[0], m_pos[1]):
                            players[0].colour = YELLOW
                            click_sound.play()
                            return
                        elif pygame.Rect(colour_rects[4]).collidepoint(m_pos[0], m_pos[1]):
                            players[0].colour = PURPLE
                            click_sound.play()
                            return
                        elif pygame.Rect(colour_rects[5]).collidepoint(m_pos[0], m_pos[1]):
                            players[0].is_RGB = True
                            click_sound.play()
                            return
                    elif ID == 1:
                        if pygame.Rect(colour_rects[0]).collidepoint(m_pos[0], m_pos[1]):
                            players[1].colour = RED
                            click_sound.play()
                            return
                        elif pygame.Rect(colour_rects[1]).collidepoint(m_pos[0], m_pos[1]):
                            players[1].colour = BLUE
                            click_sound.play()
                            return
                        elif pygame.Rect(colour_rects[2]).collidepoint(m_pos[0], m_pos[1]):
                            players[1].colour = GREEN
                            click_sound.play()
                            return
                        elif pygame.Rect(colour_rects[3]).collidepoint(m_pos[0], m_pos[1]):
                            players[1].colour = YELLOW
                            click_sound.play()
                            return
                        elif pygame.Rect(colour_rects[4]).collidepoint(m_pos[0], m_pos[1]):
                            players[1].colour = PURPLE
                            click_sound.play()
                            return
                        elif pygame.Rect(colour_rects[5]).collidepoint(m_pos[0], m_pos[1]):
                            players[1].is_RGB = True
                            click_sound.play()
                            return

    def restart():
        player_1_wins = TitleScreen(74, screen, 350, 250, "Player 1 Wins!")
        player_2_wins = TitleScreen(74, screen, 350, 250, "Player 2 Wins!")
        player_1_wins.colour = (255, 0, 0)
        player_2_wins.colour = (255, 0, 0)
        screen.blit(git_gud, (0, 0))

        if players[1].stock_remaining == 0:
            player_1_wins.drawText()
        elif players[0].stock_remaining == 0:
            player_2_wins.drawText()
        pygame.display.update()
        time.sleep(2)
        while True:
            pygame.init()
            screen.blit(git_gud, (0, 0))
            restart_text = TitleScreen(74, screen, 350, 250, "Play again? Y/N")
            restart_text.drawText()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        smash_main()
                    elif event.key == pygame.K_n:
                        return

    # Platforms
    platforms = [Platform(screen, BLACK, 275, 450, 500, 40),
                 Platform(screen, BLACK, 325, 350, 125, 10),
                 Platform(screen, BLACK, 465, 250, 125, 10),
                 Platform(screen, BLACK, 600, 350, 125, 10)]

    # Main background image
    background_image = pygame.image.load('smash_main_background.jpeg').convert()

    # Players
    players = [Player(screen, RED, 300, 400, 20, 40, platforms, 0),
               Player(screen, GREEN, 725, 400, 20, 40, platforms, 1)]
    player_1_text = TitleScreen(24, screen, 160, 600, "Player 1's stock:")
    player_2_text = TitleScreen(24, screen, 460, 600, "Player 2's stock:")
    player_1_health = TitleScreen(24, screen, 160, 550, "Player 1's Health:")
    player_2_health = TitleScreen(24, screen, 460, 550, "Player 2's Health:")
    player_info = [player_1_text, player_1_health, player_2_text, player_2_health]

    # Title screen
    click_sound = pygame.mixer.Sound("smash_select_noise.wav")
    pygame.mixer.music.load('smash_title_screen_theme.wav')
    pygame.mixer.music.play(-1, 0.0)
    title_image = pygame.image.load('smash_cover.jpg').convert()
    title_image.set_colorkey(WHITE)
    play_button = TitleScreen(48, screen, 350, 575, "Press any key to play!")
    play_button.colour = BLACK
    git_gud = pygame.image.load('smash_git gud.png').convert()

    screen.fill(WHITE)
    screen.blit(title_image, (0, 0))
    pygame.display.update()
    character_select(0)
    character_select(1)
    play_button.drawText()
    pygame.display.update()
    play_button.waitForPlayerToPressKey()
    click_sound.play()

    pygame.mixer.music.stop()
    pygame.mixer.music.load('smash_playing_theme.wav')
    pygame.mixer.music.play(-1, 0.0)

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        # --- All events are detected here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    players[0].x_speed = -3
                    players[0].direction = "LEFT"
                if event.key == pygame.K_d:
                    players[0].x_speed = 3
                    players[0].direction = "RIGHT"
                if event.key == pygame.K_w:
                    if players[0].jumps_available > 0:
                        players[0].jumping = True
                if event.key == pygame.K_SPACE:
                    players[0].attacking = True
                if event.key == pygame.K_LEFT:
                    players[1].x_speed = -3
                    players[1]. direction = "LEFT"
                if event.key == pygame.K_RIGHT:
                    players[1].x_speed = 3
                    players[1].direction = "RIGHT"
                if event.key == pygame.K_UP:
                    if players[1].jumps_available > 0:
                        players[1].jumping = True
                if event.key == pygame.K_KP_ENTER:
                    players[1].attacking = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    players[0].x_speed = 0
                if event.key == pygame.K_d:
                    players[0].x_speed = 0
                if event.key == pygame.K_SPACE:
                    players[0].attacking = False
                if event.key == pygame.K_LEFT:
                    players[1].x_speed = 0
                if event.key == pygame.K_RIGHT:
                    players[1].x_speed = 0
                if event.key == pygame.K_KP_ENTER:
                    players[1].attacking = False

        # --- Game logic should go here

        for player in players:
            player.Move()

            if player == players[0]:
                player.die(300)
            else:
                player.die(725)

            if player.stock_remaining == 0:
                done = True

        # --- Screen-clearing code goes here
        screen.fill(WHITE)

        # --- Drawing code should go here
        # Background
        screen.blit(background_image, (0, 0))
        # Platforms
        for platform in platforms:
            platform.draw_platform()

        # Players
        for player in players:
            player.draw()
            player.attack(players)

        # Stocks
        for text in player_info:
            text.drawText()
        players[0].draw_health_bar(300)
        players[1].draw_health_bar(600)
        for player in players:
            for i in range(player.stock_remaining):
                if player == players[0]:
                    pygame.draw.rect(screen, player.colour, (300 + (30 * i), 600, 20, 20))
                else:
                    pygame.draw.rect(screen, player.colour, (600 + (30 * i), 600, 20, 20))

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Game over
    restart()
    from menu import menu_main
    menu_main()


smash_main()

# Paul Moore
def menu_main():
    import pygame
    import sys
    # Define some colors, you may want to add more
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Menu")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # setup
    font = pygame.font.SysFont('Calibri', 45, True, False)
    font2 = pygame.font.SysFont('Calibri', 36, True, False)
    title = font.render('Paul\'s Arcade! Pick a game!', True, WHITE)
    pong_button = font2.render('Pong', True, BLACK)
    pong_button_rect = pygame.Rect(50, 125, 200, 50)
    fship_button = font2.render('Flappy Ship', True, BLACK)
    fship_button_rect = pygame.Rect(50, 260, 200, 50)
    smash_button = font2.render('ESSO', True, BLACK)
    smash_button_rect = pygame.Rect(50, 385, 200, 50)
    pygame.mixer.music.load('menu_music.wav')
    pygame.mixer.music.play(-1, 0.0)
    # -------- Main Program Loop -----------
    while not done:
        mpos = pygame.mouse.get_pos()
        # --- Main event loop

        # --- All events are detected here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pong_button_rect.collidepoint(mpos[0], mpos[1]):
                    from pong_main import pong_main
                    pong_main()
                elif fship_button_rect.collidepoint(mpos[0], mpos[1]):
                    from fs_main import fs_main
                    fs_main()
                elif smash_button_rect.collidepoint(mpos[0], mpos[1]):
                    from smash_main import smash_main
                    smash_main()

        # --- Game logic should go here
        size = (700, 500)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Menu")
        # --- Screen-clearing code goes here
        #  Here, we clear the screen to white.
        screen.fill(BLACK)

        # --- Drawing code should go here
        screen.blit(title, (100, 35))
        for i in range(1, 4):
            pygame.draw.rect(screen, WHITE, (50, i * 125, 200, 50))
        screen.blit(pong_button, (110, 135))
        screen.blit(fship_button, (65, 260))
        screen.blit(smash_button, (110, 385))
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    sys.exit()


menu_main()

import sys

import pygame

from pygame.sprite import Group
from Settings import Settings

from ship import Ship
from button import Button

import game_functions as gf
from game_stats import GameStats


def run_game():

    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption('Alien Invasion')

    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)


    #Создание корабля
    ship = Ship(ai_settings, screen)

    # Создание пуль
    bullets = Group()

    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update_ship()
            gf.update_bullets(aliens, bullets)

            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
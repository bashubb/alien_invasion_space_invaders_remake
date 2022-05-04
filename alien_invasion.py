import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from game_stats import GameStats
from alien import Alien
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """The Class which manages main function of the game"""

    def __init__(self):
        """Initialization of the game itself and its resources"""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Inwazja obcych")
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, 'Gra')


    def run_game(self):
        """Initialization of main loop of the game """
        while True:
        #wait for action from keyboard\
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """Start new game after 'click' button GAME"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()
            self.settings.initialize_dynamic_settings()
            self.sb.prep_level()
            self.sb.prep_ships()

    def _start_game(self):
        # reset the statistic data
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        # reset the alien list and the bullet list
        self.aliens.empty()
        self.bullets.empty()
        # create a new fleet and centering the spaceship
        self._create_fleet()
        self.ship.center_ship()
        pygame.mouse.set_visible(False)


    def _check_keydown_events(self, event):
        """reaction to pressing the button"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_g:
            self._start_game()


    def _check_keyup_events(self, event):
        """reaction to the release the button"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """Update bullet's position and removing bullet's no longer seen on the screen"""
        #updaate bullet's position
        self.bullets.update()
        # remove bullet's which are not longer on the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        #check if a bullet hit an alien
        #if True remove the bullet and the alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increse_speed()
            self.stats.level += 1
            self.sb.prep_level()
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points *len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

    def _ship_hit(self):
        """Reaction for a hit between an alien and the ship"""
        if self.stats.ships_left > 0 :
            #reduction of the ships_left number
            self.stats.ships_left -=1
            self.sb.prep_ships()

            #Remove the alien list and the bullet list
            self.aliens.empty()
            self.bullets.empty()

            #Create a new fleet and put new spaceship in the middle of the screen
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any alien reached bottom edge of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break


    def _update_aliens(self):
        """Check if fleet is near the screen's edge then
        update every single alien's position in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        #check if any contact between an alien and the spaceship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #check, if any aliens reached the bottom of the screen
        self._check_aliens_bottom()


    def _fire_bullet(self):
        """create new bullet and adding it to the group """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _create_fleet(self):
        """Create of the alien fleet"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # how many rows fits into a screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _check_fleet_edges(self):
        """Reaction if an alien would arrive to the edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move the alien fleet down and change direction of movment"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1



    def _create_alien(self, alien_number, row_number):
        """create alien and placement it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _update_screen(self):
        """screen refresh"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # display score information
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        #display the last modified screen
        pygame.display.flip()

if __name__ =='__main__':
    # creation an instance of the game and running it

    ai = AlienInvasion()
    ai.run_game()
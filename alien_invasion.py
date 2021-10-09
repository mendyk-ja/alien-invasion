import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Main class intended for managing resources and the way of working of the game."""

    def __init__(self):
        """Game initialization and creating their resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1200, 800))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien invasion")

        # Creating object, which storage game's statistics data
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Creating the Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Starting main loop of the game"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Reaction on events generated by keyword and mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_play_button(self, mouse_pos):
        """Starting a new game after pressing Play button"""
        if self.play_button.rect.collidepoint(mouse_pos):
            # Resetting game statistic data.
            self.stats.reset_stats()
            self.stats.game_active = True

            # Removing contents of  aliens and bullets lists.
            self.aliens.empty()
            self.bullets.empty()

            # Creating a new fleet and center the spaceship
            self._create_fleet()
            self.ship.center_ship()

    def _check_keydown_events(self, event):
        """Reaction for pressing a button"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Reaction for releasing the  button"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _create_fleet(self):
        """Creating complete alien fleet"""
        # Creating an alien and determination number of aliens, which can fit in a row.
        # Distance between each alien is equal to width of alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determination  how many rows can fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Creating full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # Creating alien and putting it into a row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Proper reaction, when alien would come to the edge of the screen."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Mowing the all fleet to the bottom and changing direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _fire_bullet(self):
        """Creating new bullet and adding it to the bullet group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Updating localization of bullet and removing unseeable ones"""
        # Updating localization of bullet
        self.bullets.update()

        # Removing bullets, which are located beyond the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Checking if any bullet hits the an alien.
        # If it's true, then removing the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Removing existed bullets and creating a new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """
        Checking if fleet in on the edge of the screen and then
        actualization of all aliens location
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Detection of collision between alien and spaceship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Searching for aliens, which are going to reach the bottom of the screen
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Checking if, any alien reached to the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # The same as in the case of hotting the spaceship
                self._ship_hit()
                break

    def _ship_hit(self):
        """ Reaction after an alien hits the spaceship"""
        if self.stats.ships_left > 0:
            # decreasing value storage in ship_left
            self.stats.ships_left -= 1

            # Removing contents from lists aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Creating a new fleet and center the spaceship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_screen(self):
        """Updating images on the screen and switching to new screen."""
        # Refreshing the screen during every loop iteration.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Displaying the button only  when the game is disabled
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Displaying recently modified screen
        pygame.display.flip()


if __name__ == '__main__':
    #  Creating game object and starting it
    ai = AlienInvasion()
    ai.run_game()

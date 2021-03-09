# This class contains the settings for the Alien Invasion Game

class Settings:
    def __init__(self):
        # Screen Settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230,230, 230)

        # Ship Settings
        self.ship_speed = 2.5

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 = moves to the right, -1 = moves to the left
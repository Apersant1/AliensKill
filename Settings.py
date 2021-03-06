class Settings():
    '''Настройка параметров'''

    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 100 # 10
        self.fleet_direction = 1 # 1-right , -1-lelt

        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

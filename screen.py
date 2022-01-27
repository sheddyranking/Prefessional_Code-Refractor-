from color import Color

class Screen: #screen vasuals
    def __init__(self, width = 800, height = 600, background_color = Color.BLACK, font_type ="monospace", font_size =30, clock_tick = 30):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.screen = pygame.display.set_mode((width, height))
        self.myFont = pygame.font.SysFont(font_type, font_size)
        self.clock = pygame.time.Clock()
        self.clock_tick = clock_tick

    
    

        

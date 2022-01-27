import random

from player1 import Enemy
class Game:
    def __init__(self, speed, score, enemy_list, max_enemies = 10, delay = 0.1 ):
        self.speed = speed
        self.score = score
        self.enemy_list = enemy_list
        self.max_enemies = max_enemies
        self.delay = delay
        

        self.enemy_list = []

    def drop_enemies(self, screen_width):
        delay = random.random() 
        if len(self.enemy_list) < self.max_enemies  and delay < self.delay:
            random_x = random.randint(0, screen_width)
            y_pos = 0
            enemy = Enemy(random_x, y_pos)
            self.enemy_list.append(enemy)

    def updating_enemy_position(self, screen_height):
        new_enemy_list = []
        for enemy in self.enemy_list:
            if enemy.y >= 0 and enemy.y <= screen_height:
                enemy.y += self.speed
                new_enemy_list.append(enemy)
        else:
            self.score += 1 
        self.enemy_list = new_enemy_list
    


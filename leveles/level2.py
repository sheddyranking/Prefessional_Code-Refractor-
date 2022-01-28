import sys
sys.path.insert(0, '.../')
import pygame
from player1 import HumanPlayer, Player
from screen import Screen
from game import Game
from main import play_game



if __name__ == "__main__":
    pygame.init()

    screen  = Screen()
    player = HumanPlayer(screen.width/2, screen.height-100)
    game = Game()

play_game(screen, player, game)

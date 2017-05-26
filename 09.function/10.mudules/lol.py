import sys
from functions.shop import buy_item, title as shop_title
from functions.game import play_game, title as game_title
title = 'main module'

if __name__ == '__main__':
    game.play_game()
    buy_item()
    print(title)
    print(shop_title)
    print(game_title)
    play_game()
    buy_item()

from player import Player
from gamecontroller import GameController


def main():
    p1 = Player("Marco Farina", 100, 15, 8)
    p2 = Player()

    controller = GameController(p1, p2)

    controller.start_game_loop()


if __name__ == "__main__":
    main()
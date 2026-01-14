from player import Player
from potion import Potion
from weapon import Weapon
import view

class GameController:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def start_game_loop(self):
        view.show_welcome()
        view.show_initial_stats(self.player1.get_state_dict(), self.player2.get_state_dict())

        try:
            weapon1 = Weapon("Spada Lunga", 5, 12, "melee")
        except ValueError as e:
            view.show_validation_error("Weapon", e)
            return 1
        try:
            weapon2 = Weapon("Balestra pesante", 4, 12, "Ranged")
        except ValueError as e:
            view.show_validation_error("Weapon", e)
            return 1

        try:
            self.player1.weapon = weapon1
        except TypeError as e:
            view.show_validation_error("Equip Weapon", e)
            self.player1.weapon = None
        try:
            self.player2.weapon = weapon2
        except TypeError as e:
            view.show_validation_error("Equip Weapon", e)
            self.player2.weapon = None

        self.setup_potions(self.player1)
        self.setup_potions(self.player2)

        view.show_weapon_equip(self.player1.name, weapon1)
        view.show_weapon_equip(self.player2.name, weapon2)

        turns = 0
        while True:
            self.handle_turns(turns)
            try:
                player1_alive = self.player1.is_alive()
            except Exception as e:
                view.show_action_failure(self.player1.name, "Status", "Failure in checking Player Status")
                player1_alive = False
            try:
                player2_alive = self.player2.is_alive()
            except Exception as e:
                view.show_action_failure(self.player2.name, "Status", "Failure in checking Player Status")
                player2_alive = False

            if player1_alive and not player2_alive:
                view.show_winner(self.player1)
                break
            elif player2_alive and not player1_alive:
                view.show_winner(self.player2)
                break
            else:
                view.show_draw()
                break

    def handle_turns(self, turns):
        turns += 1
        view.show_turn_header(turns)
        try:
            potion = p1.should_use_potion()
        except (ValueError, TypeError) as e:
            print(f"{p1.name} tenta usare {potion}, ma si verifica un errore: {str(e)}")
        if potion is not None:
            print(f"{p1.name} usa {potion}")

        try:
            damage1 = p1.attack(p2)
        except (ValueError, TypeError) as e:
            print(f"Errore durante l'attacco di {p1.name}: {str(e)}")
            damage1 = 0
        action(p1, p2, damage1)

        if not p2.is_alive():
            break

        try:
            potion = p2.should_use_potion()
        except (ValueError, TypeError) as e:
            print(f"{p2.name} tenta usare {potion}, ma si verifica un errore: {str(e)}")
        if potion is not None:
            print(f"{p2.name} usa {potion}")

        try:
            damage2 = p2.attack(p1)
        except (ValueError, TypeError) as e:
            print(f"Errore durante l'attacco di {p2.name}: {str(e)}")
            damage2 = 0
        action(p2, p1, damage2)

        p1.tick_buffs()
        p2.tick_buffs()

    def setup_potions(self, player: Player) -> None:
        player.potions.append(Potion("Healing Draught", "heal", 10, 0))
        player.potions.append(Potion("Healing Draught", "heal", 10, 0))

        if player.strength >= player.dexterity:

            player.potions.append(Potion("Ogre Tonic", "buff_str", 2, 3))
        else:
            player.potions.append(Potion("Cat's Grace", "buff_dex", 2, 3))
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

        self.handle_turns(turns)

    def handle_turns(self, turns):
        while True:
            turns += 1
            view.show_turn_header(turns)
            try:
                potion1 = self.player1.should_use_potion()
            except (ValueError, TypeError) as e:
                view.show_action_failure(self.player1.name, "Using a Potion", e)
            if potion1 is not None:
                view.show_potion_success(potion1.get_state_dict(), self.player1.get_state_dict())

            try:
                damage1 = self.player1.attack(self.player2)
            except (ValueError, TypeError) as e:
                view.show_action_failure(self.player1.name, "Attack", e)
                damage1 = 0
            view.show_attack_result(self.player1.get_state_dict(), self.player2.get_state_dict(), damage1)

            if not self.player2.is_alive():
                break

            try:
                potion2 = self.player1.should_use_potion()
            except (ValueError, TypeError) as e:
                view.show_action_failure(self.player2.name, "Using a Potion", e)
            if potion2 is not None:
                view.show_potion_success(potion2.get_state_dict(), self.player2.get_state_dict())

            try:
                damage2 = self.player2.attack(self.player1)
            except (ValueError, TypeError) as e:
                view.show_action_failure(self.player2.name, "Attack", e)
                damage2 = 0
            view.show_attack_result(self.player2.get_state_dict(), self.player1.get_state_dict(), damage2)

            self.player1.tick_buffs()
            self.player2.tick_buffs()

            if not self.player1.is_alive() or not self.player2.is_alive():
                break

        try:
            player1_alive = self.player1.is_alive()
        except ValueError as e:
            view.show_action_failure(self.player1.name, "Checking Player Status", e)
            player1_alive = False
        try:
            player2_alive = self.player2.is_alive()
        except ValueError as e:
            view.show_action_failure(self.player2.name, "Checking Player Status", e)
            player2_alive = False
        if player1_alive and not player2_alive:
            view.show_winner(self.player1.name)
        elif player2_alive and not player1_alive:
            view.show_winner(self.player2.name)
        else:
            view.show_draw()


    def setup_potions(self, player: Player) -> None:
        player.potions.append(Potion("Healing Draught", "heal", 10, 0))
        player.potions.append(Potion("Healing Draught", "heal", 10, 0))

        if player.strength >= player.dexterity:

            player.potions.append(Potion("Ogre Tonic", "buff_str", 2, 3))
        else:
            player.potions.append(Potion("Cat's Grace", "buff_dex", 2, 3))


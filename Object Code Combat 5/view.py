from colorama import Fore, Style, init

init(autoreset=True)


def show_welcome():
    print(f"📢 {Style.BRIGHT}{Fore.YELLOW}Inizio Combattimento 📢")


def show_validation_error(component: str, message):
    print(f"Si è verificato un errore con '{component}': {Fore.RED}{message}")


def show_default_weapon(player_name: str, default_weapon_name: str):
    print(f"⚔️ {player_name} usa: {Fore.LIGHTBLUE_EX}{default_weapon_name}{Fore.RESET}.")


def show_initial_stats(p1_stats: dict, p2_stats: dict):
    print(
        f"{p1_stats["name"]} {Fore.LIGHTBLUE_EX}(HP: {p1_stats["health"]}/{p1_stats["max_health"]}, STR: {p1_stats["strength"]}, DEX: {p1_stats["dexterity"]})\n"
        f"{Fore.RESET}{p2_stats["name"]} {Fore.LIGHTBLUE_EX}(HP: {p2_stats["health"]}/{p2_stats["max_health"]}, STR: {p2_stats["strength"]}, DEX: {p2_stats["dexterity"]})\n")


def show_weapon_equip(player_name: str, weapon):
    print(f"⚔️ {player_name} equipaggia: {Fore.YELLOW}{weapon} {Fore.RESET}⚔️")


def show_turn_header(turn_number: int):
    print(f"{Style.BRIGHT}{Fore.YELLOW}--- Turno {turn_number} ---")


def show_potion_decision(player_name: str, potion_name: str):
    print(f"{player_name} decide di usare {Fore.LIGHTBLUE_EX}{potion_name}{Fore.RESET}.")


def show_action_failure(player_name: str, action_name, reason: str):
    print(f"‼️ Errore: {Fore.LIGHTRED_EX}{action_name}"
          f"{Fore.RESET}. Giocatore: {Fore.LIGHTRED_EX}{player_name}"
          f"{Fore.RESET}. Motivo: {Fore.LIGHTRED_EX}{reason}")


def show_potion_success(potion: dict, player_stats: dict):
    if potion["effect"] == "heal":
        print(
            f"✨ {player_stats["name"]} usa la pozione: {Fore.LIGHTYELLOW_EX}{potion["effect"]}{Fore.RESET} -> {player_stats["name"]} HP: {Fore.LIGHTYELLOW_EX}{player_stats["health"]}")
    elif potion["effect"] == "buff_dex":
        print(
            f"✨ {player_stats["name"]} usa la pozione: {Fore.LIGHTYELLOW_EX}{potion["effect"]}{Fore.RESET} -> {player_stats["name"]} Destrezza: {Fore.LIGHTYELLOW_EX}{player_stats["dexterity"]}")
    elif potion["effect"] == "buff_dex":
        print(
            f"✨ {player_stats["name"]} usa la pozione: {Fore.LIGHTYELLOW_EX}{potion["effect"]}{Fore.RESET} -> {player_stats["name"]} Fora: {Fore.LIGHTYELLOW_EX}{player_stats["strength"]}")


def show_attack_result(attacker_name: str, defender_name: str, damage: int, defender_health: int):
    print(f"⚔️ {Fore.RED}{attacker_name}{Fore.RESET} colpisce {Fore.GREEN}{defender_name}{Fore.RESET} "
          f"infliggendo {damage} danni. Vita di {defender_name} rimasta: {defender_health}")


def show_winner(winner_name: str):
    print(f"🏆 {Style.BRIGHT}{Fore.YELLOW}Combattimento finito! Il vincitore è... {winner_name}!!! 🏆")


def show_draw():
    print(f"👏 {Style.BRIGHT}{Fore.LIGHTWHITE_EX}Combattimento finito! C'è stato un pareggio!! 👏")

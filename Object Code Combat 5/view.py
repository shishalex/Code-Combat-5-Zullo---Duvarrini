from colorama import Fore, Style, init

init(autoreset=True)


def show_welcome():
    print(f"📢 {Style.BRIGHT}{Fore.YELLOW}Inizio Combattimento 📢")


def show_validation_error(component, message):
    print(f"Si è verificato un errore con '{component}': {Fore.RED}{message}")


def show_default_weapon(player_name, default_weapon_name):
    print(f"⚔️ {player_name} usa: {Fore.LIGHTBLUE_EX}{default_weapon_name}{Fore.RESET}.")


def show_initial_stats(p1_stats: dict, p2_stats: dict):
    print(
        f"{p1_stats["name"]} {Fore.LIGHTBLUE_EX}(HP: {p1_stats["health"]}/{p1_stats["max_health"]}, STR: {p1_stats["strength"]}, DEX: {p1_stats["dexterity"]})\n"
        f"{Fore.RESET}{p2_stats["name"]} {Fore.LIGHTBLUE_EX}(HP: {p2_stats["health"]}/{p2_stats["max_health"]}, STR: {p2_stats["strength"]}, DEX: {p2_stats["dexterity"]})\n")


def show_weapon_equip(player_name, weapon):
    print(f"⚔️ {player_name} equipaggia: {Fore.YELLOW}{weapon} {Fore.RESET}⚔️")


def show_turn_header(turn_number):
    print(f"{Style.BRIGHT}{Fore.YELLOW}--- Turno {turn_number} ---")


def show_potion_decision(player_name, potion_name):
    print(f"{player_name} decide di usare {Fore.LIGHTBLUE_EX}{potion_name}{Fore.RESET}.")


def show_action_failure(player_name, action_name, reason):
    print(f"‼️ Errore: {Fore.LIGHTRED_EX}{action_name}"
          f"{Fore.RESET}. Giocatore: {Fore.LIGHTRED_EX}{player_name}"
          f"{Fore.RESET}. Motivo: {Fore.LIGHTRED_EX}{reason}")


def show_potion_success(player_name, effect_desc, current_hp_msg):
    print(
        f"✨ {player_name} usa la pozione: {Fore.LIGHTYELLOW_EX}{effect_desc}{Fore.RESET} -> {player_name} HP: {Fore.LIGHTYELLOW_EX}{current_hp_msg}")


def show_attack_result(attacker_name, defender_name, damage, eff_stat):
    print(f"⚔️ {Fore.RED}{attacker_name}{Fore.RESET} colpisce {Fore.GREEN}{defender_name}{Fore.RESET} "
          f"infliggendo {damage} danni. {eff_stat}")


def show_winner(winner_name):
    print(f"🏆 {Style.BRIGHT}{Fore.YELLOW}Combattimento finito! Il vincitore è... {winner_name}!!! 🏆")


def show_draw():
    print(f"👏 {Style.BRIGHT}{Fore.LIGHTWHITE_EX}Combattimento finito! C'è stato un pareggio!! 👏")

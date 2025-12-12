from colorama import Fore, Style, init

init(autoreset=True)


def show_welcome():
    print(f"📢 {Style.BRIGHT}{Fore.YELLOW}Inizio Combattimento 📢")


def show_validation_error(component, message):
    print(f"Creazione '{component}' fallita: {Fore.RED}{message}")

def show_default_weapon(player_name, default_weapon_name):
    print(f"⚔️ {player_name} usa: {Fore.LIGHTBLUE_EX}{default_weapon_name}{Fore.RESET}.")

def show_initial_stats(p1_name, p2_name, p1_hp, p2_hp, p1_max_hp, p2_max_hp, p1_str, p2_str, p1_dex, p2_dex):
    print(f"{p1_name} {Fore.LIGHTBLUE_EX}(HP: {p1_hp}/{p1_max_hp}, STR: {p1_str}, DEX: {p1_dex})\n"
          f"{Fore.RESET}{p2_name} {Fore.LIGHTBLUE_EX}(HP: {p2_hp}/{p2_max_hp}, STR: {p2_str}, DEX: {p2_dex})")

def show_turn_header(turn_number):
    print(f"{Style.BRIGHT}{Fore.YELLOW}--- Turno {turn_number} ---")


def show_potion_decision(player_name, potion_name):
    print(f"{player_name} decide di usare {Fore.LIGHTBLUE_EX}{potion_name}{Fore.RESET}.")


def show_action_failure(player_name, action_name, reason):
    print(f"‼️ Errore: {Fore.LIGHTRED_EX}{action_name}"
          f"{Fore.RESET}. Giocatore: {Fore.LIGHTRED_EX}{player_name}"
          f"{Fore.RESET}. Motivo: {Fore.LIGHTRED_EX}{reason}")


def show_potion_success(player_name, effect_desc, current_hp_msg):
    print(f"✨ {player_name} usa la pozione: {Fore.LIGHTYELLOW_EX}{effect_desc}{Fore.RESET} -> {player_name} HP: {Fore.LIGHTYELLOW_EX}{current_hp_msg}")


def show_attack_result(attacker_name, defender_name, damage, eff_stat):
    print(f"⚔️ {Fore.RED}{attacker_name}{Fore.RESET} colpisce {Fore.GREEN}{defender_name}{Fore.RESET} "
          f"infliggendo {damage} danni. {eff_stat}")


def show_winner(winner_name):
    print(f"🏆 {Style.BRIGHT}{Fore.YELLOW}Combattimento finito! Il vincitore è... {winner_name}!!! 🏆")
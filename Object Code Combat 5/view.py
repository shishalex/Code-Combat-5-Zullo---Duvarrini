from colorama import Fore, Style, init

init(autoreset=True)


def show_welcome():
    print("📢 " + Style.BRIGHT + Fore.YELLOW + "Inizio Combattimento" + " 📢")


def show_validation_error(component, message):
    print(f"Creazione {component} fallita. " + Fore.RED + f"({message})")


def show_default_weapon(player_name, default_weapon_name):
    print(f"⚔️ {player_name} usa: " + Fore.LIGHTBLUE_EX + f"{default_weapon_name}" + Fore.RESET + ".")


def show_initial_stats(p1_name, p2_name, p1_hp, p2_hp, p1_max_hp, p2_max_hp, p1_str, p2_str, p1_dex, p2_dex):
    print(f"{p1_name} " + Fore.LIGHTBLUE_EX + f"(HP: {p1_hp}/{p1_max_hp}, STR: {p1_str}, DEX: {p1_dex}\n"
          + Fore.RESET + f"{p2_name} " + Fore.LIGHTBLUE_EX + f"(HP: {p2_hp}/{p2_max_hp}, STR: {p2_str}, DEX: {p2_dex})")


def show_turn_header(turn_number):
    print(Style.BRIGHT + Fore.YELLOW + f"--- Turno {turn_number} ---")


def show_potion_decision(player_name, potion_name):
    print(f"{player_name} decide di usare " + Fore.LIGHTBLUE_EX + f"{potion_name}" + Fore.RESET + ".")


def show_action_failure(player_name, action_name, reason):
    print(f"{action_name} fallita:" + Fore.RED + f"{player_name} {reason}.")


def show_potion_success(player_name, effect_desc, current_hp_msg):
    print(f"✨ {player_name} usa la pozione: {effect_desc} -> {player_name} {current_hp_msg}")


def show_attack_result(attacker_name, defender_name, damage, eff_stat):
    print(
        "⚔️ " + Fore.RED + f"{attacker_name}" + "colpisce" + Fore.GREEN + f"{defender_name}" +
        f"infliggendo {damage} danni. {eff_stat}")


def show_winner(winner_name):
    print("🏆 " + Style.BRIGHT + Fore.YELLOW + f"Combattimento finito! Il vincitore è... {winner_name}!!" + "🏆")

def show_welcome():
    print("==="
          " SIMULAZIONE COMBATTIMENTO "
          "===")


def show_validation_error(component, message):
    print(f"Creazione {component} fallita." + message)


def show_default_weapon(player_name, default_weapon_name):
    print(f"⚔️ {player_name} usa: {default_weapon_name}.")


def show_initial_stats(p1_name, p2_name, p1_hp, p2_hp, p1_max_hp, p2_max_hp, p1_str, p2_str, p1_dex, p2_dex):
    print(f"{p1_name} (HP: {p1_hp}/{p1_max_hp}, STR: {p1_str}, DEX: {p1_dex}"
          f"{p2_name} (HP: {p2_hp}/{p2_max_hp}, STR: {p2_str}, DEX: {p2_dex})")


def show_turn_header(turn_number):
    print(f"---"
          f" Turno {turn_number} "
          f"---")


def show_potion_decision(player_name, potion_name):
    print(f"{player_name} decide di usare {potion_name}.")


def show_action_failure(player_name, action_name, reason):
    print(f"{action_name} fallita: {player_name} {reason}.")


def show_potion_success(player_name, effect_desc, current_hp_msg):
    print(f"{player_name} usa la pozione: {effect_desc} -> {player_name} {current_hp_msg}")


def show_attack_result(attacker_name, defender_name, damage, eff_stat):
    print(f"⚔️ {attacker_name} colpisce {defender_name} infliggendo {damage} danni. {eff_stat}")


def show_winner(winner_name):
    print(f"Combattimento finito! Il vincitore è... {winner_name}!!")

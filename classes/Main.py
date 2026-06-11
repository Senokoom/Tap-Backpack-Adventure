# console_test.py
import sys
from PyQt6.QtWidgets import QApplication


from classes.Entities.Player import Player
from classes.System.Calculator import Calculator
from classes.System.EnemyGenerator import EnemyGenerator
from classes.System.ItemGenerator import ItemGenerator
from classes.Inventory.ActiveInventory import ActiveInventory
from classes.Inventory.BackpackInventory import BackpackInventory
from classes.GameState import GameState
from ui.run_ui_test import BattleWindow


def main():
    calculator = Calculator()
    item_gen = ItemGenerator()
    enemy_gen = EnemyGenerator()


    player = Player(
        id=1,
        name="TestHero",
        xppoints=0,
        gold=0,
        level=1,
        skill_point=0,
        ActiveInventory=ActiveInventory(6, 6),
        BackpackInventory=BackpackInventory(6, 6),
        last_time_online=0
    )

    state = GameState(
        player=player,
        calculator=calculator,
        itemgenerator=item_gen,
        enemygenerator=enemy_gen,
        current_enemy=None,
        progression=1
    )


    while True:
        cmd = input("\n>>> ")
        if cmd.lower() == 'exit':
            break

        state.handle_tap()

        enemy = state.current_enemy
        print(f"[Уровень {state.progression}] Враг: {enemy.name} | HP: {enemy.current_hp:.0f}/{calculator.get_max_hp_scaled(enemy):.0f}")
        print(f"Золото: {state.player.gold} | XP: {state.player.xppoints}")

        if state.pending_loot:
            print(f"!!! ЛУТ: {len(state.pending_loot)} предметов ожидает !!!")


def start_game():

    app = QApplication(sys.argv)

    calculator = Calculator()
    item_gen = ItemGenerator()
    enemy_gen = EnemyGenerator()

    player = Player(
        id=1,
        name="TestHero",
        xppoints=0,
        gold=0,
        level=1,
        skill_point=0,
        ActiveInventory=ActiveInventory(6, 6),
        BackpackInventory=BackpackInventory(6, 6),
        last_time_online=0
    )

    state = GameState(
        player=player,
        calculator=calculator,
        itemgenerator=item_gen,
        enemygenerator=enemy_gen,
        current_enemy=None,
        progression=1
    )

    window = BattleWindow()
    update_ui(window, state)

    window.show()
    sys.exit(app.exec())

def on_tap(state, ui):
    state.handle_tap()
    update_ui(ui, state)

def update_ui(ui, state):
    ui.label_gold.setTexxt(f"Gold: {str(state.player.gold)}")
    ui.label_enemy_hp.setText(f"Enemy Health: {state.current_enemy.current_hp} HP")
    ui.label_enemy_name.setText(f"Enemy Name {state.current_enemy.name}")
    ui.label_dps.setText(f"Damage dealt: {state.last_damage}")


if __name__ == "__main__":
    try:
        main()
        # start_game()
    except Exception as e:
        print(f"ОШИБКА: {e}")
        import traceback

        traceback.print_exc()
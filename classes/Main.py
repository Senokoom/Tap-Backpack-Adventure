# console_test.py
import sys
import os

from classes.Inventory.ActiveInventory import ActiveInventory
from classes.Inventory.BackpackInventory import BackpackInventory

# Добавляем корень проекта в путь, чтобы импорты работали
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from classes.Entities.Player import Player
from classes.System.Calculator import Calculator
from classes.System.EnemyGenerator import EnemyGenerator
from classes.System.ItemGenerator import ItemGenerator
from classes.System.settings import Config
from classes.GameState import GameState  # Твой файл с GameState


def main():
    print("--- ЗАПУСК КОНСОЛЬНОГО ТЕСТА ---")

    # 1. Инициализация зависимостей
    calculator = Calculator()
    item_gen = ItemGenerator()
    enemy_gen = EnemyGenerator()  # Убедись, что он умеет создавать врагов без UI

    # 2. Создаем игрока (заглушка данных)
    # Тут подставь реальные аргументы твоего конструктора Player
    player = Player(
        id=1,
        name="TestHero",
        xppoints=0,
        gold=0,
        level=1,
        skill_point=0,
        ActiveInventory=ActiveInventory(6, 6),  # Или пустой инвентарь
        BackpackInventory=BackpackInventory(6, 6),  # Или пустой инвентарь
        last_time_online=0
    )

    # 3. Создаем GameState
    # current_enemy пока None, он заспавнится при первом тапе
    state = GameState(
        player=player,
        calculator=calculator,
        itemgenerator=item_gen,
        enemygenerator=enemy_gen,
        current_enemy=None,
        progression=1
    )

    print(f"Игрок создан. Золото: {state.player.gold}")
    print("Нажми Enter, чтобы нанести удар. Напиши 'exit' для выхода.")

    # 4. Игровой цикл
    while True:
        cmd = input("\n>>> ")
        if cmd.lower() == 'exit':
            break

        # Выполняем тап
        state.handle_tap()

        # Выводим состояние
        enemy = state.current_enemy
        print(f"[Уровень {state.progression}] Враг: {enemy.name} | HP: {enemy.current_hp:.0f}/{calculator.get_max_hp_scaled(enemy):.0f}")
        print(f"Золото: {state.player.gold} | XP: {state.player.xppoints}")

        # Если есть лут, показываем
        if state.pending_loot:
            print(f"!!! ЛУТ: {len(state.pending_loot)} предметов ожидает !!!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ОШИБКА: {e}")
        import traceback

        traceback.print_exc()
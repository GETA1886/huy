import random
import time

def print_slow(text, delay=0.05):
    """Печатает текст с задержкой."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def start_game():
    """Начало игры."""

    print_slow("Добро пожаловать в мир приключений!")
    print_slow("Вы - храбрый путешественник, который отправляется в опасное путешествие.")
    print_slow("Ваша цель - найти легендарный артефакт, спрятанный в древнем храме.")

    name = input("Как вас зовут? ")
    print_slow(f"Отлично, {name}! Ваше приключение начинается...")

    # Создание персонажа
    player = {
        "name": name,
        "health": 100,
        "attack": 15,
        "defense": 5,
        "inventory": []
    }

    # Начало путешествия
    travel(player)

def travel(player):
    """Функция для путешествия."""

    print_slow("\nВы стоите на развилке дорог. Куда вы хотите пойти?")
    print_slow("1. В лес")
    print_slow("2. В горы")
    print_slow("3. К реке")

    choice = input("Введите номер направления: ")

    if choice == "1":
        forest(player)
    elif choice == "2":
        mountains(player)
    elif choice == "3":
        river(player)
    else:
        print_slow("Неверное направление. Попробуйте еще раз.")
        travel(player)

def forest(player):
    """Функция для леса."""

    print_slow("\nВы зашли в густой лес. Воздух наполнен ароматом сосны и мха.")
    print_slow("Внезапно вы слышите шум.")
    print_slow("1. Попытаться скрыться.")
    print_slow("2. Пройти вперед.")

    choice = input("Введите номер действия: ")

    if choice == "1":
        print_slow("Вы пытаетесь скрыться за деревьями, но шум становится все громче.")
        print_slow("Из кустов выпрыгивает огромный волк!")
        fight(player, "волк", 25, 10, 5)
    elif choice == "2":
        print_slow("Вы решаете идти вперед и вскоре видите...")
        print_slow("Загадочный храм! Вход в него охраняет огромный грифон.")
        fight(player, "грифон", 40, 15, 10)
    else:
        print_slow("Неверное действие. Попробуйте еще раз.")
        forest(player)

def mountains(player):
    """Функция для гор."""

    print_slow("\nВы начинаете подъем в горы. Воздух становится тонким, а вершины скрываются в облаках.")
    print_slow("На пути вам встречается пещера.")
    print_slow("1. Зайти в пещеру.")
    print_slow("2. Обойти пещеру.")

    choice = input("Введите номер действия: ")

    if choice == "1":
        print_slow("Внутри пещеры вы находите древний сундук.")
        print_slow("1. Открыть сундук.")
        print_slow("2. Оставить сундук.")

        choice = input("Введите номер действия: ")
        if choice == "1":
            treasure = random.choice(["золото", "эликсир", "меч"])
            player["inventory"].append(treasure)
            print_slow(f"В сундуке вы нашли {treasure}!")
        else:
            print_slow("Вы решаете оставить сундук.")
    elif choice == "2":
        print_slow("Вы обходите пещеру и продолжаете путь.")
        mountains(player)
    else:
        print_slow("Неверное действие. Попробуйте еще раз.")
        mountains(player)

def river(player):
    """Функция для реки."""

    print_slow("\nВы подходите к бурной реке. На другом берегу виднеется древний храм.")
    print_slow("1. Попытаться переплыть реку.")
    print_slow("2. Поиск моста.")

    choice = input("Введите номер действия: ")

    if choice == "1":
        print_slow("Вы пытаетесь переплыть реку, но течение слишком сильное.")
        print_slow("Вы теряете немного здоровья.")
        player["health"] -= 10
        print_slow(f"Ваше здоровье: {player['health']}")
        travel(player)
    elif choice == "2":
        print_slow("Вы отправляетесь на поиски моста. Вскоре вы находите его, но...")
        print_slow("На мосту стоит страж, который требует от вас пройти испытание.")
        fight(player, "страж", 30, 12, 8)
    else:
        print_slow("Неверное действие. Попробуйте еще раз.")
        river(player)

def fight(player, enemy_name, enemy_health, enemy_attack, enemy_defense):
    """Функция для боя."""

    print_slow(f"\nВы вступили в бой с {enemy_name}!")

    while player["health"] > 0 and enemy_health > 0:
        print_slow(f"\nВаше здоровье: {player['health']}")
        print_slow(f"Здоровье {enemy_name}: {enemy_health}")

        print_slow("1. Атаковать")
        print_slow("2. Защищаться")

        choice = input("Введите номер действия: ")

        if choice == "1":
            damage = player["attack"] - enemy_defense
            if damage < 0:
                damage = 0
            enemy_health -= damage
            print_slow(f"Вы атаковали {enemy_name} и нанесли {damage} урона!")
        elif choice == "2":
            print_slow("Вы защищаетесь.")
        else:
            print_slow("Неверное действие. Попробуйте еще раз.")
            continue

        if enemy_health > 0:
            # Ход врага
            damage = enemy_attack - player["defense"]
            if damage < 0:
                damage = 0
            player["health"] -= damage
            print_slow(f"{enemy_name} атаковал вас и нанес {damage} урона!")

    if player["health"] <= 0:
        print_slow(f"К сожалению, вы проиграли бой. {enemy_name} победил!")
        print_slow("Игра окончена.")
        exit()
    else:
        print_slow(f"Вы победили {enemy_name}!")

        # Победа
        print_slow(f"Вы получили {enemy_health // 2} очков здоровья.")
        player["health"] += enemy_health // 2
        if player["health"] > 100:
            player["health"] = 100
        print_slow(f"Ваше здоровье: {player['health']}")

        # Продолжение путешествия
        travel(player)

if __name__ == "__main__":
    start_game()
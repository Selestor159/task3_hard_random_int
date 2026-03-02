import random


def guess_the_number():
    print("=" * 50)
    print("Добро пожаловать в игру 'Угадай число'!")
    print("=" * 50)
    print("Правила игры:")
    print("- Компьютер загадывает случайное число в заданном диапазоне")
    print("- Вам нужно угадать это число за ограниченное количество попыток")
    print("- После каждой попытки вы получите подсказку: больше или меньше ваше число")
    print("- Когда у вас останется меньше половины попыток, игра автоматически")
    print("  покажет примерный диапазон загаданного числа (плюс-минус 5)")
    print()

    # Выбор уровня сложности
    print("Выберите уровень сложности:")
    print("0 - Число от 1 до 100 (легкий)")
    print("1 - Число от 1 до 125 (средний)")
    print("2 - Число от 1 до 150 (сложный)")

    while True:
        try:
            difficulty = int(input("Ваш выбор (0, 1, 2): "))
            if difficulty in [0, 1, 2]:
                break
            else:
                print("Пожалуйста, введите 0, 1 или 2.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

    # Устанавливаем диапазон чисел в зависимости от уровня сложности
    if difficulty == 0:
        max_number = 100
        max_attempts = 8
        print("Вы выбрали легкий уровень (числа от 1 до 100)")
    elif difficulty == 1:
        max_number = 125
        max_attempts = 10
        print("Вы выбрали средний уровень (числа от 1 до 125)")
    else:
        max_number = 150
        max_attempts = 12
        print("Вы выбрали сложный уровень (числа от 1 до 150)")

    # Компьютер загадывает случайное число
    secret_number = random.randint(1, max_number)
    attempts = 0  # счетчик попыток
    hint_threshold = max_attempts // 2  # порог для подсказки (половина попыток)
    hint_shown = False  # флаг, была ли уже показана подсказка

    print(f"Я загадал число от 1 до {max_number}. У вас {max_attempts} попыток.")
    print(f"Подсказка с диапазоном появится автоматически, когда останется меньше {hint_threshold} попыток!")
    print("-" * 50)

    while attempts < max_attempts:
        attempts += 1
        remaining_attempts = max_attempts - attempts

        # Получаем предположение игрока
        while True:
            try:
                guess = int(input(f"Попытка {attempts}. Ваше предположение: "))
                # Проверяем, что число в допустимом диапазоне
                if 1 <= guess <= max_number:
                    break
                else:
                    print(f"Пожалуйста, введите число от 1 до {max_number}.")
            except ValueError:
                print("Пожалуйста, введите целое число.")

        # Проверяем угадал или нет
        if guess < secret_number:
            print("Введенное число маленькое. Загаданное число больше.")
        elif guess > secret_number:
            print("Введенное число большое. Загаданное число меньше.")
        else:
            print(f"\nПоздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
            print("Спасибо за игру!")
            return

        # Показываем оставшиеся попытки
        if remaining_attempts > 0:
            print(f"Осталось попыток: {remaining_attempts}")

            # Автоматически показываем подсказку, если осталось меньше половины попыток
            if remaining_attempts < hint_threshold and not hint_shown:
                min_hint = max(1, secret_number - 5)
                max_hint = min(max_number, secret_number + 5)
                print(f"ПОДСКАЗКА: Загаданное число где-то между {min_hint} и {max_hint}!")
                hint_shown = True
        print("-" * 30)

    print(f"\n К сожалению, попытки закончились. Загаданное число было: {secret_number}")
    print("Спасибо за игру!")


# Запускаем игру
if __name__ == "__main__":
    guess_the_number()

    # Хочет ли игрок сыграть еще раз
    while True:
        play_again = input("\nХотите сыграть еще раз? (да/нет): ").strip().lower()
        if play_again == "да":
            print("\n" * 2)
            guess_the_number()
        elif play_again == "нет":
            print(" До свидания!")
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")
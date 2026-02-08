import random

def print_board(board):
    """"Выводит игровое поле"""
    print("   1   2   3")
    for i, row in enumerate(board, 1):
        print(f"{i}  {row[0]} | {row[1]} | {row[2]}")
        if i < 3:
            print("  -----------")

def check_winner(board, player):
    """Проверка победы игрока, перебирая все выигрышные комбинации"""
    win_combinations = [
        # Строки
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Столбцы
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Диагонали
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for combo in win_combinations:
        if all(board[r][c] == player for r, c in combo):
            return True
    return False

def is_full(board):
    """Проверка заполнения поля, перебирая все клетки"""
    for row in board:
        for cell in row:
            if cell == ' ':
                return False  # Пустая клетка — поле не заполнено
    return True  # Все клетки заняты

def get_move(player, board):
    """Запрашивает у игрока ход и проверяет корректность ввода"""
    while True:
        try:
            move = input(f"Ваш ход ({player}), введите строку и столбец через пробел (например, 1 2): ").split()
            if len(move) != 2:
                print("Введите два числа через пробел.")
                continue
            row, col = int(move[0]) - 1, int(move[1]) - 1
            if row not in range(3) or col not in range(3):
                print("Числа должны быть от 1 до 3.")
                continue
            if board[row][col] != ' ':
                print("Эта клетка уже занята!")
                continue
            return row, col
        except ValueError:
            print("Введите два целых числа.")

def get_computer_move(board):
    """Делает случайный свободный ход для компьютера (O)."""
    free_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(free_cells)

def main():
    # Инициализируем пустое поле 3x3
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'  # Игрок X, компьютер O

    print("Добро пожаловать в Крестики‑нолики!")
    print("Вы играете за X, компьютер за O.")
    print_board(board)

    while True:
        if current_player == 'X':
            # Ход игрока
            row, col = get_move(current_player, board)
        else:
            # Ход компьютера
            print("Ход компьютера (O)...")
            row, col = get_computer_move(board)

        # Делаем ход
        board[row][col] = current_player

        # Выводим обновлённое поле
        print_board(board)

        # Проверяем победу
        if check_winner(board, current_player):
            if current_player == 'X':
                print("Вы победили! Поздравляю!")
            else:
                print("Компьютер победил! Попробуйте ещё раз.")
            break

        # Проверяем ничью
        if is_full(board):
            print("Ничья! Поле заполнено.")
            break

        # Передаём ход
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
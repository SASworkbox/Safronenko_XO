playing_field = list(range(1, 10))
winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    """Функция рисует игровое поле ввода"""
    print('~' * 13)
    for i in range(3):
        print('|', playing_field[0 + i * 3], '|', playing_field[1 + i * 3], '|', playing_field[2 + i * 3], '|')
        print('~' * 13)


def take_input(player_turn):
    """Функция ожидающая ввода( Х или О ) от пользователя"""
    while True:
        value = input('Ходит игрок %s:  \n' % player_turn)
        if not (value in '123456789'):
            print('Ошибочный ввод. Повторите')
            continue
        value = int(value)
        if str(playing_field[value - 1]) in 'XO':
            print('Эта клетка уже занята')
            continue
        playing_field[value - 1] = player_turn
        break


def start_game():
    """Функция запускающая игру"""
    player_step = 0
    while True:
        draw_board()
        if player_step % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if player_step > 3:
            winner = victory_check()
            if winner:
                draw_board()
                print(winner, 'Выиграл!')
                break
        player_step += 1
        if player_step > 8:
            draw_board()
            print('Ничья!')
            break


def victory_check():
    """Функция проверяющая выигрышные комбинации на игровом поле"""
    for each in winning_combinations:
        if playing_field[each[0] - 1] == playing_field[each[1] - 1] == playing_field[each[2] - 1]:
            return playing_field[each[1] - 1]
    else:
        return False


start_game()

import Operation
import Ui


def run():
    command = ''
    while command != '7':
        Ui.menu()
        command = input().strip()
        if command == '1':
            Operation.show('all')
        elif command == '2':
            Operation.add()
        elif command == '3':
            Operation.show('id')
            Operation.id_delete()
        elif command == '4':
            Operation.show('id')
            Operation.id_rewrite()
        elif command == '5':
            Operation.show('date')
            Operation.date_show()
        elif command == '6':
            Operation.show('id')
            Operation.id_show()
        elif command == '7':
            bye()
            break
        else:
            print('Команды не существует. '
                  'Проверьте правильность ввода!')


def bye():
    print('Завершено!')

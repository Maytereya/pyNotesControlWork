import Note


def create_note(min_size):
    name = check_len_text(input('Введите имя заметки: '), min_size)
    content = input('Введите текст заметки: ')
    return (Note.
            Note(name=name, content=content))


def check_len_text(text, min_size):
    while len(text) <= min_size:
        print(f'Текст не должен содержать меньше {min_size} символов!')
        text = input('\n Введите текст: \n')
    else:
        return text

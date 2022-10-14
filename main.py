from datetime import datetime
import requests
import logging

def logger(some_function):
    def new_function(*args, **kwargs):
        date = datetime.now()
        result = some_function(*args, **kwargs)
        with open('text.txt', 'w', encoding='utf-8') as file:
            file.write(f'Дата и время: {date}\n'
            f'Имя функции: {some_function}\n'
            f'Аргументы функции: {args} и {kwargs}\n'
            f'Возвращаемое значение: {result}')
        return result
    return new_function


@logger
def get_status(*args, **kwargs):
    a = ''
    b = ''
    return

if __name__ == '__main__':
    get_status()
import datetime

def log_cash(rezhim, result):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{rezhim} = {result}.Время запроса: {datetime.datetime.now()}\n' )


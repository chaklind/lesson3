"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    import datetime as DT, calendar
    from datetime import timedelta
    now = DT.datetime.now(DT.timezone.utc).astimezone()
    today = now
    yesterday = now - timedelta(days=1)
    now_month = calendar.monthrange(now.year, now.month)[1]
    now -= timedelta(days = now_month)
    time_format = "%Y-%m-%d %H:%M:%S"
    print(f"Сегоднящняя дата: {today:{time_format}}\nВчерашняя дата: {yesterday:{time_format}}\nДата месяц назад: {now:{time_format}}")
   
    
def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    input(string)
    from datetime import datetime
    format = '%d/%m/%y %H:%M:%S.%f'
    datetime.strptime(string, format)
    

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
    





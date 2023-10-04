import pandas as pd
from datetime import date
import random
def find_name_by_weekday(excel_file):
    # Загрузка данных из Excel файла
    df = pd.read_excel(excel_file)

    # Получение текущего месяца и дня
    current_date = date.today()
    current_week = current_date.month  # Текущий месяц
    current_day = current_date.day  # Текущий день


    # Функция для извлечения номера недели и дня недели из даты в столбце "ДАТА"
    def extract_weekday(row):
        date_in_column = row['ДАТА']
        date_week = date_in_column.month
        date_day = date_in_column.day
        return date_week, date_day

    # Применение функции extract_weekday к каждой строке и создание новых столбцов 'Месяц' и 'День'
    df[['Месяц', 'День']] = df.apply(extract_weekday, axis=1, result_type='expand')

    # Поиск строки, в которой неделя и день недели совпадают с текущей неделей и днем недели
    matching_row = df[(df['Месяц'] == current_week) & (df['День'] == current_day)]

    # Проверка, найдена ли соответствующая строка
    if not matching_row.empty:
        # Извлечение имени из соответствующей строки
        name = matching_row.iloc[0]['ФИО']  # Замените 'Имя' на название соответствующего столбца
        random_cng = random.choice(df["ПОЗДРАВЛЕНИЕ"])
        cng = f'{name} {random_cng}'
        nam = f'Сегодня день рождения у {name}'
        return cng, nam
    else:
        a = f'Сегодня никто не празднует день рождения'
        return a # Если совпадение не найдено






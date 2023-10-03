import pandas as pd
from datetime import datetime

def find_name_by_weekday(excel_file):
    # Загрузка данных из Excel файла
    df = pd.read_excel(excel_file)

    # Получение текущей недели и дня недели
    current_date = datetime.now().date()
    current_week = current_date.isocalendar()[1]  # Текущая неделя
    current_day = current_date.weekday()  # Текущий день недели (0 - понедельник, 6 - воскресенье)

    # Функция для извлечения номера недели и дня недели из даты в столбце "ДАТА"
    def extract_weekday(row):
        date_in_column = row['ДАТА']
        date_week = date_in_column.isocalendar()[1]
        date_day = date_in_column.weekday()
        return date_week, date_day

    # Применение функции extract_weekday к каждой строке и создание новых столбцов 'Неделя' и 'День'
    df[['Неделя', 'День']] = df.apply(extract_weekday, axis=1, result_type='expand')

    # Поиск строки, в которой неделя и день недели совпадают с текущей неделей и днем недели
    matching_row = df[(df['Неделя'] == current_week) & (df['День'] == current_day)]

    # Проверка, найдена ли соответствующая строка
    if not matching_row.empty:
        # Извлечение имени из соответствующей строки
        name = matching_row.iloc[0]['ФИО']  # Замените 'Имя' на название соответствующего столбца
        return name
    else:
        a = f'Совпадение не найдено'
        return a # Если совпадение не найдено





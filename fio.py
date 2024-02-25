def format_fio(fio_list):
    formatted_fio_list = []
    for name in fio_list:
# Разделение строки по пробелам и получение списка частей
        parts = name.split()
# Фамилия - первая часть
        last_name = parts[1]
# Инициалы - остальные части объединенные без пробелов
        initials = ''.join(parts[2:])
# Слияние фамилии и инициалов вместе
        formatted_name = last_name + initials
# Добавление отформатированного ФИО в новый список
        formatted_fio_list.append(formatted_name)
    return formatted_fio_list
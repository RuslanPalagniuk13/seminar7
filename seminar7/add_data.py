
# накидал что нашел в интернете для создания кода

from export_data import export_data
from import_data import import_data
from search_data import search_data

# открытие файла, чтение, закрытие
with open("phone.csv", "r", encoding='utf-8') as f:
    data = f.readlines()

# удаление строк, для которых выполнено условие
data = filter(lambda line: "стоп_слово" not in line, data)

# более сложные условия редактирования стоит вынести в отдельную функцию   
def transformation(line):
    if "слово_маркер" in line:
        return "замещающая строка\n"
    return line.replace("что_заменить", "на_что")

# редактирование строк файла
data = map(transformation, data)

# открытие, запись и закрытие файла
with open("phone.csv", "w", encoding='utf-8') as f:
    f.write("".join(data))
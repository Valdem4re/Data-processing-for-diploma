import mysql.connector
import re

from CifFile import ReadCif

cf = ReadCif("P23.cif")
print(cf['csd_cif_jufwuc'])

# conn = mysql.connector.connect(host='localhost', user='user', password='12345', database='NNCDB')
# cursor = conn.cursor()

# cursor.execute('SELECT ID FROM REFCODES WHERE REFCOD_CCDC = "BEQBEH";')
# result = cursor.fetchone()
# cif_file = ""
# if result:
#     id = result[0]  # Получаем ID из результата запроса
#     cursor.execute("SELECT CIF_FILE FROM CIFS WHERE ID = %s;", (id,))
#     cif_file_result = cursor.fetchone()

#     if cif_file_result:
#         cif_file = cif_file_result[0]  # Получаем CIF_FILE из результата запроса
#         pattern = r"^\s*\d+\s+\S+,\S+,\S+\s*$"

#         # Извлечение строк с позициями
#         positions = re.findall(pattern, cif_file, re.MULTILINE)

#         # Преобразование строк с позициями в список координат
#         coordinates = []
#         for pos in positions:
#             coord = pos.strip().split()[1]  # Отделяем координаты и разбиваем по запятым
#             coordinates.append(coord)
#         print(coordinates)
#         res = substitute_coordinates([0.5,0.5,0.5], coordinates)
#         print(res)
#     else:
#         print("Не удалось найти запись в таблице CIFS для ID:", id)
# else:
#     print("Не удалось найти запись в таблице REFCODES")



# Закрытие курсора и соединения
# cursor.close()
# conn.close()
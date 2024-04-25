from pprint import pprint
import csv
import re
from operator import itemgetter

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

for c in contacts_list[1:]:
    
    # приводим ФИО к виду Ф,И,О
    
    fio = ' '.join(c[:2]).strip().split(' ')
    for i in range(0,3):
        c[i] = (fio[i] if i < len(fio) else '')

    # приводим телефоны к виду  +7(999)999-99-99 доп. 9999

    fulltel = re.split('доб', c[5])
    tel = re.sub('\D','', fulltel[0])
    doptel = (re.sub('\D', '', fulltel[1]) if len(fulltel) > 1 else '')
    c[5] = ('+7(' + tel[-10:-7] + ')' 
            + tel[-7:-4] + '-' + tel[-4:-2] + '-' + tel[-2:]
            + (' доп. ' + doptel if doptel !='' else '') if tel != '' else '') 

# убираем дубли

headers = contacts_list[0]
contacts_list.pop(0)
contacts_list.sort(key=itemgetter(0,1,2))

temp = []*2
i = 0
while i < len(contacts_list):
    if contacts_list[i][:2] == temp:
        for j in range(len(contacts_list[i])):
            if contacts_list[i-1][j] == '':
                contacts_list[i-1][j] = contacts_list[i][j]  
        contacts_list.pop(i)
    temp = contacts_list[i][:2]
    i += 1

contacts_list.insert(0,headers)
pprint(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)

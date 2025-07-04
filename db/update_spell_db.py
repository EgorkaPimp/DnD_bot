import json
import logging
#Для Windows
import os

from db.DB_connection import db_con

directory_path = "Q:\\my_pet_projact\\Pars_DnD\\data_json\\spells"

def open_json(name_json):
    with open(f'{directory_path}\\{name_json}', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def spell_data_for_db():
  try:
    contents = os.listdir(directory_path)
    for number in range(len(contents)):
        name_en = contents[number].split('.')[0].replace(" ", "_")
        data = open_json(contents[number])
        name_ru = data['name_ru'].replace(' ', '_')
        url_spell = data['url']
        if check_spell(name_en):
            continue
        else:
            #logging.INFO(f'Add spell: {number}-{name_en}-{name_ru}')
            update_spell(name_en, name_ru, url_spell)

  except FileNotFoundError:
    print(f"Ошибка: Директория '{directory_path}' не найдена.")
  except PermissionError:
    print(f"Ошибка: Нет доступа к директории '{directory_path}'.")
  except Exception as e:
    print(f"Произошла ошибка: {e}")

def update_spell(name_en, name_ru, url_spell):
    conn, cursor = db_con()
    cursor.execute(
        "INSERT INTO spell (spell_en, spell_ru, url)"
                           "VALUES (?, ?, ?)",
                           (name_en, name_ru, url_spell)
    )
    conn.commit()


def check_spell(name_spell):
    conn, cursor = db_con()
    cursor.execute("SELECT 1 FROM spell WHERE spell_en = ?",
                    (name_spell,))
    value = cursor.fetchone() is not None
    conn.close()
    return value

#Для Linux
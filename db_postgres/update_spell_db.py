import json
import logging
#Для Windows
import os

directory_path = "Q:\\my_pet_projact\\Pars_DnD\\data_json\\spells"

async def open_json(name_json):
    with open(f'{directory_path}\\{name_json}', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

async def spell_data_for_db(conn):
  try:
    contents = os.listdir(directory_path)
    for number in range(len(contents)):
        name_en = contents[number].split('.')[0].replace(" ", "_")
        data = await open_json(contents[number])
        name_ru = data['name_ru'].replace(' ', '_')
        url_spell = data['url']
        if await check_spell(conn, name_en):
            continue
        else:
            await update_spell(conn, name_en, name_ru, url_spell)

  except FileNotFoundError:
    print(f"Ошибка: Директория '{directory_path}' не найдена.")
  except PermissionError:
    print(f"Ошибка: Нет доступа к директории '{directory_path}'.")
  except Exception as e:
    print(f"Произошла ошибка: {e}")

async def update_spell(conn, name_en, name_ru, url_spell):
    await conn.execute("""
        INSERT INTO spell(spell_en, spell_ru, url) VALUES($1, $2, $3)
        """, name_en, name_ru, url_spell
    )


async def check_spell(conn, name_spell):
    value = await conn.fetchval("""
            SELECT EXISTS (
                SELECT 1
                FROM spell
                WHERE spell_en = $1
        )
            """, name_spell)
    return value

#Для Linux
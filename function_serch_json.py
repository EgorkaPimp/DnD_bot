import asyncio
import json
import os


directory_path = "Q:\\my_pet_projact\\Pars_DnD\\data_json\\class"

async def open_json(name_json):
    with open(f'{directory_path}\\{name_json}', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

async def search_name_class():
    contents = os.listdir(directory_path)
    for i in contents:
        data = await open_json(i)
        if data['book'] == "Player's Handbook":
            name_class = data['name_ru']
            print(name_class)

asyncio.run(search_name_class())
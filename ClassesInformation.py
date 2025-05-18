import os
import json
import re

class JsonClassClass:
    def __init__(self):
        self.classes = {}
        self.path_classes = os.path.join('data', 'class')

    def _load_classes(self):
        for filename in os.listdir(self.path_classes):
            if filename.endswith(".json"):
                with open(os.path.join(self.path_classes, filename), "r", encoding="utf-8") as file:
                    class_data = json.load(file)
                    self.classes[class_data["name"].lower()] = class_data

                    # for subrace in race_data.get("subraces", []):
                    #     key = f"{race_data['name'].lower()}:{subrace['name'].lower()}"
                    #     self.classes[key] = subrace

        return self.classes


    def _connection_json(self, class_name:str):
        classes = self._load_classes()
        class_j = classes.get(class_name.lower())
        if not class_j:
            print(f'Ошибка подключение к {class_name}')
        return class_j

    def classes_description(self, class_name:str):
        class_j = self._connection_json(class_name)
        class_description = class_j["description"]
        return class_description

    def classes_ability_score(self, class_name:str):
        class_j = self._connection_json(class_name)
        class_ability_score = class_j["ability_score"]
        return class_ability_score

    def classes_background(self, class_name:str):
        class_j = self._connection_json(class_name)
        class_background = class_j["background"]
        return class_background

    def classes_hits_dise(self, class_name:str):
        class_j = self._connection_json(class_name)
        class_hits = class_j["hits"]
        return class_hits

    def classes_armor(self, class_name:str):
        class_j = self._connection_json(class_name)
        class_armor = class_j["armor"]
        return class_armor

    def classes_weapons(self, class_name:str):
        class_j = self._connection_json(class_name)
        class_weapons = class_j["weapons"]
        return class_weapons

    def classes_instruments(self, class_name:str):
        class_j = self._connection_json(class_name)
        class_instruments = class_j["instruments"]
        return class_instruments

    def classes_saving_throws(self, class_name:str):
        class_j = self._connection_json(class_name)
        class_saving_throws = class_j["saving_throws"]
        return class_saving_throws

    def classes_skills(self, class_name:str):
        class_j = self._connection_json(class_name)
        class_skills = class_j["skills"]
        return class_skills

    def classes_equipment(self, class_name:str):
        class_j = self._connection_json(class_name)
        class_equipment = class_j["equipment"]
        return class_equipment
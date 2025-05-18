import os
import json
import re


class JsonClassRace:
    def __init__(self):
        self.races = {}
        self.races_dir = os.path.join("data", "races")

        self._default_attributes = {'Intelligence': 0,
        "Dexterity": 0,
        "Wisdom": 0,
        "Charisma": 0,
        "Constitution": 0,
        "Strength": 0}
        self._default_traits = {}
        self._default_data_subrace = []

        self.data_subrace = self._default_data_subrace.copy()
        self.data_state = self._default_attributes.copy()
        self.traits = self._default_traits.copy()


    def _load_races(self):
        for filename in os.listdir(self.races_dir):
            if filename.endswith(".json"):
                with open(os.path.join(self.races_dir, filename), "r", encoding="utf-8") as file:
                    race_data = json.load(file)
                    self.races[race_data["name"].lower()] = race_data

                    for subrace in race_data.get("subraces", []):
                        key = f"{race_data['name'].lower()}:{subrace['name'].lower()}"
                        self.races[key] = subrace

        return self.races

    def _connection_json(self, race_name:str):
        races = self._load_races()
        race = races.get(race_name.lower())
        if not race:
            print(f'Ошибка подключение к {race_name}')
        return race

    """Возвращает TXT с кратким описанием расы"""
    def racial_description(self, race_name: str):
        race = self._connection_json(race_name)
        race_desc = race["description"]
        return race_desc

    """Возвращает TXT с кратким описанием возроста"""
    def racial_age(self, race_name: str):
        race = self._connection_json(race_name)
        race_age = race["age"]
        return race_age

    """Возвращает МАПУ с характеристиками только от расы"""
    def racial_bonuses(self, race_name: str):
        try:
            race = self._connection_json(race_name)
            for stat, bonus in race["ability_score_increase"].items():
                self.data_state[stat] += bonus
            return self.data_state
        finally:
            self._reset_state()

    """Возвращает МАПУ с способностями только от расы"""
    def racial_trait(self, race_name: str):
        try:
            race = self._connection_json(race_name)

            for trait in race["traits"]:
                self.traits[trait['name']] = trait['description']
            return self.traits
        finally:
            self._reset_state()

    """Возвращает INT с значением скорости"""
    def racial_speed(self, race_name: str):
        race = self._connection_json(race_name)
        speed = race['speed']
        return speed

    """Возвращает МАПУ с ключами text - текстовой формат размера,
                                 min - минимальный размер из книги,
                                 max - максимальный размер из книги"""
    def racial_size(self, race_name: str):
        race = self._connection_json(race_name)
        result_size = re.split(r'[/.]', race['size'])
        size_map = {'text': result_size[0],
                    'min': result_size[1],
                    'max': result_size[2]}
        return size_map

    """Возвращает МАСИВ с языками"""
    def racial_language(self, race_name: str):
        race = self._connection_json(race_name)
        languages = race['languages']
        return languages

    """Возвращает МАСИВ с подкласами"""
    def racial_subrace(self, race_name: str):
        try:
            race = self._connection_json(race_name)
            subraces = race['subraces']
            for subrace in subraces:
                self.data_subrace.append(subrace["name"])
            return self.data_subrace
        finally:
            self._reset_state()


    """Возвращает МАПУ с характеристиками только от подрасы"""
    def subracial_bonuses(self, subraces_name: str):
        try:
            if subraces_name is None:
                return {}
            else:
                race_name = (subraces_name.split(" ")[-1])
                all_races = self._connection_json(f"{race_name.lower()}:{subraces_name.lower()}")

                for stat, bonus in all_races["ability_score_increase"].items():
                    self.data_state[stat] += bonus
                return self.data_state
        finally:
            self._reset_state()

    """Возвращает МАПУ с характеристиками только от подрасы"""
    def subracial_trait(self, subraces_name: str):
        try:
            if subraces_name is None:
                return {}
            else:
                race_name = (subraces_name.split(" ")[-1])
                all_races = self._connection_json(f"{race_name.lower()}:{subraces_name.lower()}")

                for trait in all_races["traits"]:
                    self.traits[trait['name']] = trait['description']
                return self.traits
        finally:
            self._reset_state()


    def _reset_state(self):
        self.data_state = self._default_attributes.copy()
        self.traits = self._default_traits.copy()
        self.data_subrace = self._default_data_subrace.copy()

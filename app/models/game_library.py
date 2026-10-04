from app.utils import resource_path
import json

# path to the data file, resolved relative to this file's location
DATA_FILE = resource_path("data/games.json")

class GameLibrary:

    # initialization function for the class
    def __init__(self):
        self._data = self._load()

    # internal use function
    # returns a dictionary
    def _load(self) -> dict:

        with open(DATA_FILE, "r", encoding="utf-8") as f:
            # parses the JSON file into a Python dictionary
            return json.load(f)

    def save(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=4, ensure_ascii=False)

    # series functions

    def get_series_names(self) -> list[str]:
        return [s["name"] for s in self._data["series"]]

    def get_games_for_series(self, series_name: str) -> list[str]:
        for s in self._data["series"]:
            if s["name"] == series_name:
                return s["games"]
        return[]

    def add_series(self, series_name:str):
        if series_name not in self.get_series_names():
            self._data["series"].append({"name": series_name, "games": []})
            self.save()

    def add_game_to_series(self, series_name: str, game_title: str):
        for s in self._data["series"]:
            if s["name"] == series_name:
                if game_title not in s["games"]:
                    s["games"].append(game_title)
                    self.save()
                return

    # game functions

    def get_standalone_games(self) -> list[str]:
        return self._data["standalone_games"]

    def add_standalone_game(self, game_title: str):
        if game_title not in self._data["standalone_games"]:
            self._data["standalone_games"].append(game_title)
            self.save()

    # console functions

    def get_consoles(self) -> list[str]:
        return self._data["consoles"]

    def add_console(self, console_name: str):
        if console_name not in self._data["consoles"]:
            self._data["consoles"].append(console_name)
            self.save()
import json
import os

# It seems the os is another "Python class" we call..
# And thus, we get OS related stuff like pathnames from it.
# __file__ is a Python variable which holds a path... to where?
# Clearly, the file where the line is written!
# Path to the data file, resolved relative to this file's location
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "data", "games.json")

class GameLibrary:
    # The GameLibrary class is our subject who is authorized.
    # This might not work. We might need more space. Let's try it: the GameLibrary class is our subject who is...
    # Not enough. He's authorized to talk about Games. He's the one the UI will ask for info on Games. Our intermediary.
    # An Intermerdiary.

    # Our initialization function for the class. We've seen this before.
    def __init__(self):
        self._data = self._load()

    # Our loading and saving "cuntions" come next.

    # The "_" means: "Please don't call this from outside of the class! It's for internal use only, thanks."
    # Python doesn't enforce this, it's purpose is to help the coder.
    # More interesting however, is the "dict" keyword...
    # Apparently it means the function returns a dictionary.
    # Python does not give a shit about this keyword, it's just for the IDE and the coder.
    def _load(self) -> dict:
        # normpath "normalizes" our path, making it absolute and easier to manipualte.
        path = os.path.normpath(DATA_FILE)
        # we can tell that this line opens a file with a path
        # the "r" stands for "read"
        with open(path, "r", encoding="utf-8") as f:
            # now this line parses the JSON file into a Python dictionary
            # let's remember a Python dictionary is basically the same thing as a JSON object...
            return json.load(f)

    def save(self):
        path = os.path.normpath(DATA_FILE)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=4, ensure_ascii=False)

    # now for series related functions...

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

    # now standalone games...

    def get_standalone_games(self) -> list[str]:
        return self._data["standalone_games"]

    def add_standalone_game(self, game_title: str):
        if game_title not in self._data["standalone_games"]:
            self._data["standalone_games"].append(game_title)
            self.save()

    # finally, consoles...

    def get_consoles(self) -> list[str]:
        return self._data["consoles"]

    def add_console(self, console_name: str):
        if console_name not in self._data["consoles"]:
            self._data["consoles"].append(console_name)
            self.save()
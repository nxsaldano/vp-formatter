from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QLineEdit,
    QPushButton,
)
from PyQt6.QtCore import pyqtSignal
 
from app.models.game_library import GameLibrary

class CaptionForm(QWidget):

    # holds a signal (it seems)
    caption_generated = pyqtSignal(str)

    def __init__(self, library: GameLibrary):
        super().__init__()
        self.library = library
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        # series
        layout.addWidget(QLabel("Series"))
        self.series_combo = QComboBox()
        self.series_combo.setEditable(True)
        self.series_combo.addItem("")

        self.series_combo.addItems(self.library.get_series_names())
        self.series_combo.currentTextChanged.connect(self._on_series_changed)
        layout.addWidget(self.series_combo)

        # game
        layout.addWidget(QLabel("Game"))
        self.game_combo = QComboBox()
        self.game_combo.setEditable(True)
        self._populate_games()
        layout.addWidget(self.game_combo)

        # console
        layout.addWidget(QLabel("Console"))
        self.console_combo = QComboBox()
        self.console_combo.setEditable(True)
        self.console_combo.addItems(self.library.get_consoles())
        layout.addWidget(self.console_combo)

        # decade
        layout.addWidget(QLabel("Decade"))
        self.decade_combo = QComboBox()
        self.decade_combo.setEditable(True)
        self.decade_combo.addItems(self._generate_decades())
        layout.addWidget(self.decade_combo)

        # generate button
        layout.addSpacing(8)
        self.generate_btn = QPushButton("Generate")
        self.generate_btn.clicked.connect(self._on_generate)
        layout.addWidget(self.generate_btn)

        layout.addStretch()


    # slots

    def _on_series_changed(self, series_name: str):
        self._populate_games(series_name)

    def _on_generate(self):
        series = self.series_combo.currentText().strip().lower().replace(" ", "")
        game = self.game_combo.currentText().strip().lower().replace(" ", "")
        console = self.console_combo.currentText().strip().lower().replace(" ", "")
        decade = self.decade_combo.currentText().strip().lower().replace(" ", "")

        if not game or not console or not decade:
            return 
        
        lines = []
        if series: 
            lines.append(f"#{series} #{game}")
        else:
            lines.append(f"#{game}")
        lines.append(f"#{console}")
        lines.append(f"#{decade}")
        lines.append("#virtualphotography")

        print("\n".join(lines))

        self.caption_generated.emit("\n".join(lines))

    # helpers
    def _populate_games(self, series_name: str = ""):

        self.game_combo.clear()
        if series_name:
            games = self.library.get_games_for_series(series_name)
        else:
            games = self.library.get_standalone_games()
        self.game_combo.addItems(games)
    
    def _generate_decades(self) -> list[str]:
        return ["1980s", "1990s", "2000s", "2010s", "2020s"]

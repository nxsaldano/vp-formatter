from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from app.utils import resource_path 
from app.models.game_library import GameLibrary
from app.views.caption_form import CaptionForm
from app.views.output_panel import OutputPanel

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("vp-formatter v1.0")
        self.setMinimumSize(800, 600)

        self.library = GameLibrary()

        self._init_ui()

    def _init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(16)

        self.caption_form = CaptionForm(self.library)
        self.output_panel = OutputPanel()

        main_layout.addWidget(self.caption_form)
        main_layout.addWidget(self.output_panel)

        self.caption_form.caption_generated.connect(self.output_panel.set_caption)

        central_widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(resource_path("assets/icon.png")))

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap(resource_path("assets/background.jpg"))
        painter.drawPixmap(0, 0, pixmap)






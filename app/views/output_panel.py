from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
)
from PyQt6.QtGui import QClipboard
from PyQt6.QtWidgets import QApplication

# self evident, but oh well. this is where the generated text shows up
class OutputPanel(QWidget):

    def __init__(self):
        super().__init__()
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(12)

        layout.addWidget(QLabel("Generated Caption"))

        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        layout.addWidget(self.text_display)

        self.copy_btn = QPushButton("Copy to Clipboard")
        self.copy_btn.clicked.connect(self._on_copy)
        layout.addWidget(self.copy_btn)

    # public interface

    def set_caption(self, caption: str):
        self.text_display.setPlainText(caption)

    # slots
    def _on_copy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.text_display.toPlainText())
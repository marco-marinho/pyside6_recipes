from __future__ import annotations

import sys

from mainwindow import Ui_MainWindow
from PySide6.QtCore import QAbstractItemModel, QModelIndex, QPersistentModelIndex, Qt
from PySide6.QtWidgets import QApplication, QComboBox, QLineEdit, QMainWindow


# Implement the model here
class DataModel(QAbstractItemModel):
    def __init__(self, buffer=None):
        super().__init__()
        self.buffer = buffer or []

    # Method for acquiring data from the model, must be implemented and follow this signature
    def data(self, index: QModelIndex | QPersistentModelIndex, role: Qt.ItemDataRole):
        if role == Qt.ItemDataRole.DisplayRole:
            text = self.buffer[index.row()]
            return text

    # Checks if a requrest index is valid and return it wrapped in a QModelIndex object
    def index(self, row: int, column: int, _: QModelIndex):
        if row >= len(self.buffer):
            return QModelIndex()
        return self.createIndex(row, column)

    # Method for acquiring the number of rows in the model, must be implemented and follow this signature
    def rowCount(self, _: QModelIndex):
        return len(self.buffer)

    # Method for acquiring the number of columns in the model, must be implemented and follow this signature
    def columnCount(self, _: QModelIndex) -> int:
        return 1

    # Method for acquiring the parent index of a given index, must be implemented and follow this signature
    def parent(self, _: QModelIndex):
        return QModelIndex()

    # Custom method for adding data to the model and emitting changes to layout
    def add(self, text):
        self.buffer.append(text)
        self.layoutChanged.emit()

    # Custom method for removing data from the model and emitting changes to layout
    def remove(self, index):
        self.buffer.pop(index)
        self.layoutChanged.emit()


def add_func(input: QLineEdit, model: DataModel):
    text = input.text()
    model.add(text)
    input.clear()


def remove_func(combo: QComboBox, model: DataModel):
    model.remove(combo.currentIndex())


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, model: DataModel):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.comboBox.setModel(model)
        self.addButton.clicked.connect(lambda: add_func(window.lineEdit, model))
        self.removeButton.clicked.connect(lambda: remove_func(window.comboBox, model))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = DataModel(["item1", "item2", "item3"])
    window = MainWindow(model)
    window.show()

    sys.exit(app.exec())

import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
# Add the current directory to the import path so that the QML engine can find the module
engine.addImportPath('.')

engine.load('main.qml')

sys.exit(app.exec())
from __future__ import annotations

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtQml import QmlElement

# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
QML_IMPORT_NAME = "io.pyside.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


# This decorator is used to register the class as a QML element
@QmlElement
class Bridge(QObject):
    # This signal will be emitted when the color changes and caught from QML
    colorChanged = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.flag = True

    # This method will be called from QML, the slot decorator can be used to define a method as a slot
    # and handle dynamic dispatching of signals and slots.
    @Slot(result=str)
    def getColor(self):
        if self.flag:
            self.flag = not self.flag
            self.colorChanged.emit()
            return "blue"
        else:
            self.colorChanged.emit()
            self.flag = not self.flag
            return "red"

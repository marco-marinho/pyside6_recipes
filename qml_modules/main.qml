import QtQuick 2.0
import my_components 1.0

Window {
    height: 640
    width: 480
    visible: true
    title: qsTr("Hello RCC")
    Row {
        MButton {
            text: "Rato Alado"
            onButtonClicked: {
                console.log("Rato Alado");
            }
        }
        anchors.centerIn: parent
    }
}

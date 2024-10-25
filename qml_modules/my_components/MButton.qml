import QtQuick

Item {
    id: rootId
    width: rectangleId.width
    height: rectangleId.height
    property alias text: textId.text
    signal buttonClicked
    Rectangle {
        id: rectangleId
        width: textId.implicitWidth + 20
        height: textId.implicitHeight + 20
        color: "red"
        Text {
            id: textId
            text: "Hello World"
            anchors.centerIn: parent
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                rootId.buttonClicked;
            }
        }
    }
}

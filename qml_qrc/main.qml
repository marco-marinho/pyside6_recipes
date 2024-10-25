import QtQuick 2.0

Window{
    height: 1000
    width: 1800
    visible: true
    title: qsTr("Hello RCC")
    Row{
    Image {
        source: "qrc:/images/image1.png"
    }
    Image {
        source: "qrc:/images/image2.png"
    }
    Image {
        source: "qrc:/images/image3.png"
    }
    anchors.centerIn: parent
    }

}
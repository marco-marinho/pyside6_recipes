import QtQuick 2.0 
import QtQuick.Controls 2.1
import QtQuick.Window 2.1
import QtQuick.Controls.Material 2.1

import io.pyside.textproperties 1.0 

ApplicationWindow {
    id: page
    width: 800
    height: 400
    visible: true

    // This components comes from Python in the bridge.py file
    Bridge { // qmllint disable
        id: bridge
        // This is the signal that will be emitted from Python, notice that the name here 
        // is not exactly the same with the "on" prepended to the camel case.
        onColorChanged: {
            console.log("Color changed.")
        }
    }

    Rectangle{
        id: rect
        width: 300
        height: 300
        color: "red"

        MouseArea {
            anchors.fill: parent
            onClicked: {
                // This is the method that will be called in Python
                rect.color = bridge.getColor()
            }
        }

    }

    Component.onCompleted: {
        // Signals can also be connected manually using the same name they have in python 
        bridge.colorChanged.connect(function(){
            console.log("Color changed custom connection.")
        })
    }

}
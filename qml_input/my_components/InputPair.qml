import QtQuick
import QtQuick.Controls

Item{

    property alias color: rectId.color
    property alias labelText: labelId.text
    property alias placeholderText: inputId.placeholderText
    height: rowId.implicitHeight 
    width: rowId.implicitWidth

    Row{

        id: rowId
        spacing: 10

        Rectangle{

            id: rectId
            width: labelId.implicitWidth + 10
            height: inputId.implicitHeight
            color: "grey"

            Text{
                id: labelId
                text: "First name"
                anchors.centerIn: parent
                font.pointSize: inputId.font.pointSize
            }

        }

        Rectangle{
            
            height: inputId.implicitHeight
            width: inputId.width
            color: rectId.color

            TextField{
                id: inputId
                placeholderText: "Enter first name"
                width: 300
                onEditingFinished: {
                    console.log("Editing finished with value: " + text)
                }
            }

        }

    }
}
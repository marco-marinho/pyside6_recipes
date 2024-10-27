import QtQuick
import QtQuick.Controls
import my_components

Window {

    width: 800
    height: 600
    visible: true
    id: root

    Column{
        x: 20
        y: 20
        spacing: 10

        InputPair{
            id: firstNameId
            color: "grey"
            labelText: "First name"
            placeholderText: "Enter first name"
        }


        InputPair{
            id: lastNameId
            color: "grey"
            labelText: "Last name"
            placeholderText: "Enter last name"
        }

    }
    




}
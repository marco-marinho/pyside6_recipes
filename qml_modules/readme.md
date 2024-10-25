### QML Modules

To create a module, you can create a folder or a folder structure that will contain you .qml files.
For each folder that will act as a module there must be a qmldir file that declares the name of the module,
and, for each component, there must exist a declaration with the name of the component, its version and the file 
that contains it. 

For importing, the name of the imported module must follow a Java like logic, where the file tree appears as part of the
import path: 
```
import app.modules.buttons 1.0
```

The root path to where the modules can be loaded can be added to the QQmlApplicationEngine using addImportPath.
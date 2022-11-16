from PySide2.QtWidgets import QApplication
from controllers.main_windows import  Form


if __name__ == "_main_":
    app = QApplication()
    window = Form
    window.show()

    app.exec_()
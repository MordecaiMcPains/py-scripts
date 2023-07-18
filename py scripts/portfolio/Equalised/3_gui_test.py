from PyQt5.QtWidgets import *

def main():

    admin_name = "Neba"
    app = QApplication([])
    window = QWidget()

    window.setFixedSize(1000, 500)  #  this makes the screen fixed and the maximuse is disabled
    window.setWindowTitle(admin_name)
    window.show()

    app.exec()

if __name__ == '__main__':
    main()
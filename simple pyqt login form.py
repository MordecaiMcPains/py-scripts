import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPalette, QColor

# Global variables
window_title = "Login"

class LoginWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # window set up
        self.setWindowTitle(window_title)
        self.setGeometry(500, 300, 300, 200)

        # Set the background color using a QPalette
        palette = self.palette()
        palette.setColor(QPalette.Background, QColor("#3E4B5C"))
        self.setPalette(palette)

        self.username_label = QLabel(self)
        self.username_label.setText("Username:")
        # self.user_plc_text = QLineEdit()    # user place holder text
        # self.user_plc_text.setPlaceholderText("name")
        self.username_label.move(50, 30)

        self.username_input = QLineEdit(self)
        self.username_input.move(120, 30)

        self.password_label = QLabel(self)
        self.password_label.setText("Password:")
        self.password_label.move(50, 70)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.move(120, 70)

        self.login_button = QPushButton(self)
        self.login_button.setText("Login")
        self.login_button.move(120, 110)
        self.login_button.clicked.connect(self.login)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "admin" and password == "password":
            LoginSuccess()
        else:
            InvalidUsername()

def LoginSuccess():
    msg = QMessageBox()

    msg.setText("Login successful!")
    msg.exec_()
    print("Login successful!")
    sys.exit(app.exec_())   #exits after login
    
def InvalidUsername():
    msg = QMessageBox()
    error = "error"

    msg.setText("Invalid username and password")
    msg.setWindowTitle(error)
    msg.exec_()
    print("Invalid username and password")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
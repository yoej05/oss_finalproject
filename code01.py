import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget, QComboBox)
import json

# 사용자 데이터 저장 파일
USER_DATA_FILE = "users.json"

def load_users():
    try:
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

class RoommateApp(QWidget):
    def __init__(self):
        super().__init__()
        self.users = load_users()
        self.user_data = {}  # 회원가입 데이터를 저장하는 딕셔너리
        self.initUI()

    def initUI(self):
        self.setWindowTitle("룸메이트 매칭 앱")
        self.layout = QVBoxLayout()

        # 로그인 영역
        self.create_login_ui()

        # 매칭 리스트 영역
        self.matching_list = QListWidget()
        self.matching_list.hide()
        self.layout.addWidget(self.matching_list)

        self.setLayout(self.layout)

    def create_login_ui(self):
        self.clear_layout()

        self.add_label("로그인 또는 회원가입")
        self.username_input = self.add_line_edit("아이디를 입력하세요")
        self.password_input = self.add_line_edit("비밀번호를 입력하세요", password=True)

        self.login_button = self.add_button("로그인", self.login)
        self.register_button = self.add_button("회원가입", self.show_registration_step1)

    def add_label(self, text):
        label = QLabel(text)
        self.layout.addWidget(label)

    def add_line_edit(self, placeholder, password=False):
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholder)
        if password:
            line_edit.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(line_edit)
        return line_edit

    def add_button(self, text, handler):
        button = QPushButton(text)
        button.clicked.connect(handler)
        self.layout.addWidget(button)
        return button

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in self.users and self.users[username]['password'] == password:
            QMessageBox.information(self, "성공", f"{username}님, 환영합니다!")
            self.show_matching_list()
        else:
            QMessageBox.warning(self, "오류", "아이디 또는 비밀번호가 잘못되었습니다!")

    def show_registration_step1(self):
        self.clear_layout()

        self.add_label("성별을 선택하세요:")
        self.gender_combo = self.add_combo_box(["여자", "남자"])
        self.next_button = self.add_button("다음", self.save_gender_and_proceed)

    def add_combo_box(self, items):
        combo = QComboBox()
        combo.addItems(items)
        self.layout.addWidget(combo)
        return combo

    def save_gender_and_proceed(self):
        self.user_data['gender'] = self.gender_combo.currentText()
        self.show_registration_step2()

    def show_registration_step2(self):
        self.clear_layout()

        self.add_label("신청한 기숙사를 선택하세요:")
        dorm_items = ["예지1동", "명덕1동", "명덕2동", "명덕3동"] if self.user_data['gender'] == "여자" else ["예지2동", "예지3동"]
        self.dorm_combo = self.add_combo_box(dorm_items)
        self.next_button = self.add_button("다음", self.save_dorm_and_proceed)

    def save_dorm_and_proceed(self):
        self.user_data['dorm'] = self.dorm_combo.currentText()
        self.show_registration_step3()

    def show_registration_step3(self):
        self.clear_layout()

        self.add_label("출생년도를 선택하세요:")
        self.birth_year_combo = self.add_combo_box([str(year) for year in range(1997, 2007)])

        self.add_label("학번을 선택하세요:")
        self.student_id_combo = self.add_combo_box([str(year) for year in range(16, 26)])

        self.add_label("소속 대학을 선택하세요:")
        self.college_combo = self.add_combo_box(["생명공학대학", "공과대학", "예술공학대학", "예술대학", "체육대학"])

        self.next_button = self.add_button("다음", self.save_details_and_proceed)

    def save_details_and_proceed(self):
        self.user_data['birth_year'] = self.birth_year_combo.currentText()
        self.user_data['student_id'] = self.student_id_combo.currentText()
        self.user_data['college'] = self.college_combo.currentText()
        self.show_registration_step4()

    def show_registration_step4(self):
        self.clear_layout()

        self.add_label("아이디를 입력하세요:")
        self.username_input = self.add_line_edit("")
        self.add_label("비밀번호를 입력하세요:")
        self.password_input = self.add_line_edit("", password=True)

        self.register_button = self.add_button("회원가입 완료", self.register)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in self.users:
            QMessageBox.warning(self, "오류", "이미 존재하는 아이디입니다!")
        elif not username or not password:
            QMessageBox.warning(self, "오류", "모든 항목을 입력하세요!")
        else:
            self.user_data['username'] = username
            self.user_data['password'] = password

            self.users[username] = self.user_data
            save_users(self.users)

            QMessageBox.information(self, "성공", "회원가입이 완료되었습니다!")

    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RoommateApp()
    window.show()
    sys.exit(app.exec_())

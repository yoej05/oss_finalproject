from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QDial, QPushButton, QComboBox, QCheckBox, QRadioButton, QSlider, QHBoxLayout,  QMessageBox
from PyQt5.QtCore import Qt

class DailyRoutineSelector(QWidget):
    def __init__(self):
        super().__init__()

        self.dial_sleep = None
        self.dial_wakeup = None
        self.selected_sleep_time = None
        self.selected_wakeup_time = None
        self.teeth_grind_checkbox = None
        self.snore_checkbox = None
        self.sleep_talk_checkbox = None
        self.no_habit_checkbox = None
        self.sleep_alarm = None
        self.moderate_alarm = None
        self.awake_alarm = None
        self.smoking_combobox = None
        self.drinking_slider = None
        self.bug_combobox = None
        self.phone_combobox = None
        self.eating_combobox = None
        self.submit_button = None
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("개인 성향 설정")

        self.layout = QVBoxLayout()

        # 1. 취침시간 설정
        self.sleep_time_label = QLabel("취침시간을 선택하세요:")
        self.layout.addWidget(self.sleep_time_label)

        self.dial_sleep = QDial()
        self.dial_sleep.setMinimum(0)
        self.dial_sleep.setMaximum(11)
        self.dial_sleep.setSingleStep(1)
        self.dial_sleep.setNotchesVisible(True)
        self.dial_sleep.setWrapping(False)
        self.dial_sleep.valueChanged.connect(self.update_sleep_time)
        self.layout.addWidget(self.dial_sleep)

        self.selected_sleep_time = QLabel("선택된 취침시간: 12시")
        self.layout.addWidget(self.selected_sleep_time)

        # 2. 기상시간 설정
        self.wakeup_time_label = QLabel("기상시간을 선택하세요:")
        self.layout.addWidget(self.wakeup_time_label)

        self.dial_wakeup = QDial()
        self.dial_wakeup.setMinimum(0)
        self.dial_wakeup.setMaximum(11)
        self.dial_wakeup.setSingleStep(1)
        self.dial_wakeup.setNotchesVisible(True)
        self.dial_wakeup.setWrapping(False)
        self.dial_wakeup.valueChanged.connect(self.update_wakeup_time)
        self.layout.addWidget(self.dial_wakeup)

        self.selected_wakeup_time = QLabel("선택된 기상시간: 12시")
        self.layout.addWidget(self.selected_wakeup_time)

        # 3. 샤워시간 설정 (아침/저녁/유동적)
        self.shower_label = QLabel("샤워시간을 선택하세요:")
        self.layout.addWidget(self.shower_label)

        self.shower_combobox = QComboBox()
        self.shower_combobox.addItem("아침")
        self.shower_combobox.addItem("저녁")
        self.shower_combobox.addItem("유동적")
        self.layout.addWidget(self.shower_combobox)

        # 4. 잠버릇 설정
        self.habit_label = QLabel("잠버릇을 선택하세요:")
        self.layout.addWidget(self.habit_label)

        self.teeth_grind_checkbox = QCheckBox("이갈이")
        self.snore_checkbox = QCheckBox("코골이")
        self.sleep_talk_checkbox = QCheckBox("잠꼬대")
        self.no_habit_checkbox = QCheckBox("없어요")

        self.layout.addWidget(self.teeth_grind_checkbox)
        self.layout.addWidget(self.snore_checkbox)
        self.layout.addWidget(self.sleep_talk_checkbox)
        self.layout.addWidget(self.no_habit_checkbox)

        self.no_habit_checkbox.stateChanged.connect(self.update_habits)

        # 5. 알람 설정
        self.alarm_label = QLabel("알람 설정:")
        self.layout.addWidget(self.alarm_label)

        self.alarm_buttons = QHBoxLayout()
        self.sleep_alarm = QRadioButton("잠만보에요")
        self.moderate_alarm = QRadioButton("적당히 잘 일어나요")
        self.awake_alarm = QRadioButton("잘 일어나요")

        self.alarm_buttons.addWidget(self.sleep_alarm)
        self.alarm_buttons.addWidget(self.moderate_alarm)
        self.alarm_buttons.addWidget(self.awake_alarm)

        self.layout.addLayout(self.alarm_buttons)

        # 6. 흡연여부 설정
        self.smoking_label = QLabel("흡연여부:")
        self.layout.addWidget(self.smoking_label)

        self.smoking_combobox = QComboBox()
        self.smoking_combobox.addItem("연초")
        self.smoking_combobox.addItem("전자담배")
        self.smoking_combobox.addItem("안 펴요")
        self.layout.addWidget(self.smoking_combobox)

        # 7. 음주 빈도 설정 (슬라이더로 수평선 설정)
        self.drinking_label = QLabel("음주 빈도:")
        self.layout.addWidget(self.drinking_label)

        self.drinking_slider = QSlider(Qt.Horizontal)
        self.drinking_slider.setRange(0, 100)
        self.drinking_slider.setValue(50)
        self.layout.addWidget(self.drinking_slider)

        self.drinking_text = QLabel("안마신다 <--> 매일 마신다")
        self.layout.addWidget(self.drinking_text)

        # 8. 벌레 잡는 능력 설정
        self.bug_label = QLabel("벌레 잡는 능력:")
        self.layout.addWidget(self.bug_label)

        self.bug_combobox = QComboBox()
        self.bug_combobox.addItem("그냥 아예 못잡아요")
        self.bug_combobox.addItem("작은거는 잡아요")
        self.bug_combobox.addItem("다 잘잡아요")
        self.layout.addWidget(self.bug_combobox)

        # 9. 전화 통화 설정
        self.phone_label = QLabel("전화 통화 가능 여부:")
        self.layout.addWidget(self.phone_label)

        self.phone_combobox = QComboBox()
        self.phone_combobox.addItem("무조건 가능해요")
        self.phone_combobox.addItem("간단한 통화만 가능해요")
        self.phone_combobox.addItem("밖에서 해주세요")
        self.layout.addWidget(self.phone_combobox)

        # 10. 실내취식 설정
        self.eating_label = QLabel("실내취식 여부:")
        self.layout.addWidget(self.eating_label)

        self.eating_combobox = QComboBox()
        self.eating_combobox.addItem("무조건 가능해요(저도 한입만)")
        self.eating_combobox.addItem("바로 치우고 환기하면 가능해요")
        self.eating_combobox.addItem("밖에서 취식해주세요")
        self.layout.addWidget(self.eating_combobox)

        # 버튼 추가
        self.submit_button = QPushButton("확인")
        self.submit_button.clicked.connect(self.submit)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    # 각 선택 항목을 업데이트하는 메서드들
    def update_sleep_time(self):
        time = self.dial_sleep.value() + 1
        self.selected_sleep_time.setText(f"선택된 취침시간: {time}시")

    def update_wakeup_time(self):
        time = self.dial_wakeup.value() + 1
        self.selected_wakeup_time.setText(f"선택된 기상시간: {time}시")

    def update_habits(self):
        if self.no_habit_checkbox.isChecked():
            self.teeth_grind_checkbox.setChecked(False)
            self.snore_checkbox.setChecked(False)
            self.sleep_talk_checkbox.setChecked(False)

    def submit(self):
        sleep_time = self.dial_sleep.value() + 1
        wakeup_time = self.dial_wakeup.value() + 1
        shower_time = self.shower_combobox.currentText()
        habits = []
        if self.teeth_grind_checkbox.isChecked():
            habits.append("이갈이")
        if self.snore_checkbox.isChecked():
            habits.append("코골이")
        if self.sleep_talk_checkbox.isChecked():
            habits.append("잠꼬대")
        alarm = "잠만보에요" if self.sleep_alarm.isChecked() else "적당히 잘 일어나요" if self.moderate_alarm.isChecked() else "잘 일어나요"
        smoking = self.smoking_combobox.currentText()
        drinking = self.drinking_slider.value()
        bug = self.bug_combobox.currentText()
        phone = self.phone_combobox.currentText()
        eating = self.eating_combobox.currentText()

        # 결과 출력
        print(f"취침시간: {sleep_time}시, 기상시간: {wakeup_time}시, 샤워시간: {shower_time}")
        print(f"잠버릇: {', '.join(habits) if habits else '없어요'}, 알람: {alarm}, 흡연여부: {smoking}")
        print(f"음주 빈도: {drinking}, 벌레 잡는 능력: {bug}, 전화 통화 가능 여부: {phone}, 실내취식 여부: {eating}")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("제출 완료")
        msg.setText("당신의 정보는 성공적으로 제출되었습니다. 성향이 맞는 최고의 룸메를 찾아 연락드릴게요! 이용해주셔서 감사합니다.")
        msg.exec_()

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    ex = DailyRoutineSelector()
    ex.show()
    sys.exit(app.exec_())

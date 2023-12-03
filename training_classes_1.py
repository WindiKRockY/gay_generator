from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app=QApplication([]) #створюємо коментарі

win=QWidget()#створюємо вікно
win.resize(400,200)

win.setWindowTitle("Хто тут гей(тролейбус)")

winner = QLabel('Вітаю!!!!Ти гей!!!!')
result = QLabel('А хто тут?)')

gen_button = QPushButton('Визначити')

v_line = QVBoxLayout()
v_line.addWidget(winner,alignment=Qt.AlignCenter)
v_line.addWidget(result,alignment=Qt.AlignCenter)
v_line.addWidget(gen_button,alignment=Qt.AlignCenter)

win.setLayout(v_line)



win.show()#показує вікно
app.exec_()#запускаємо додаток
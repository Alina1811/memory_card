from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

app = QApplication([])
main_ans = QWidget()
main_ans.setWindowTitle('Memory Card')

question = QLabel('Готов?')
RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')
ans = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

button_check = QPushButton('Нажми, чтобы начать')

main_ans.score = 0
main_ans.total = 0

RadioGroupBox_res = QGroupBox('Результат')
right_false = QLabel('Правильно/Неправильно')
RadioGroupBox_res.hide()

class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

quest_list = [Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Испанский', 'Английский'), 
              Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты'),
              Question('Fe - это символ какого химического элемента?', 'Железо', 'Азот', 'Сера', 'Фтор'),
              Question('Сколько клавиш у стандартного современного пианино?', '88', '79', '92', '56'),]

def ask(q: Question):
    shuffle(ans)
    ans[0].setText(q.right_ans)
    ans[1].setText(q.wrong1)
    ans[2].setText(q.wrong2)
    ans[3].setText(q.wrong3)

    ans_true.setText(q.right_ans)
    question.setText(q.question)
    show_quest()

def show_res():
    RadioGroupBox.hide()
    RadioGroupBox_res.show()
    button_check.setText('Следующий вопрос')

def show_quest():
    RadioGroupBox_res.hide()
    RadioGroupBox.show()
    button_check.setText('Ответить')

    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def check_ans():
    if ans[0].isChecked():
        show_correct('Правильно')
        main_ans.score += 1
    else:
        if ans[1].isChecked() or ans[2].isChecked() or ans[3].isChecked():
            show_correct('Неправильно')

def show_correct(res):
    right_false.setText(res)
    show_res()

def next_quest():
    
    '''if main_ans.cur_quest == len(ans):
        main_ans.cur_quest = 0'''

    if len(quest_list) > 0:
        cur_quest = randint(0, len(quest_list)-1)
        q = quest_list[cur_quest]

        q1 = quest_list[cur_quest]
        ask(q1)
        quest_list.remove(q1)

        main_ans.total += 1

    print('Статистика')
    print('Всего вопросов:', main_ans.total)
    print('Правильных ответов:', main_ans.score)

    if main_ans.total > 0:
        print('Рейтинг:', ((main_ans.score/main_ans.total)*100), '%')


def click_ok():
    if button_check.text() == 'Ответить':
        check_ans()
    else:
        next_quest()

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_main = QVBoxLayout()
layout_main.setSpacing(5)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

ans_true = QLabel('Правильный ответ')

layout_res = QVBoxLayout()

layout_res.addWidget(right_false, alignment=(Qt.AlignLeft))
layout_res.addWidget(ans_true, alignment=(Qt.AlignCenter))
RadioGroupBox_res.setLayout(layout_res)

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
RadioGroupBox.setLayout(layout_ans1)
layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(button_check, stretch = 2)
layout_line3.addStretch(1)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
layout_main.addLayout(layout_line1)
layout_main.addLayout(layout_line2)
layout_main.addLayout(layout_line3)

layout_line2.addWidget(RadioGroupBox_res)
layout_line3.addWidget(button_check, stretch = 2)

button_check.clicked.connect(click_ok)

main_ans.setLayout(layout_main)
main_ans.show()
app.exec_()
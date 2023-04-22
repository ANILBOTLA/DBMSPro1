from PyQt5.QtWidgets import *
import sys
import mysql.connector
import random

my_database = mysql.connector.connect(host="localhost", user="root", password="Aa0!Aa0!", database="bussinessmanagementsystem")

application = QApplication(sys.argv)

widget = QWidget()
widget.resize(980, 580)
widget.setWindowTitle("Bussiness Management System")

spotarea = QPlainTextEdit(widget)
spotarea.move(450, 40)
spotarea.resize(515, 515)
spotarea.show()

def click_btn1():
	mycusor = my_database.cursor()
	mycusor.execute("select * from worker")
	mydata = mycusor.fetchall()
	output = "id\tprofile_id\tduty_id\tcompany_id\tcode\tstatus\n"
	for x in mydata:
		for y in x:
			output += str(y) + "\t"
		output += "\n"
	spotarea.setPlainText(output)

def click_btn2():
	mycusor = my_database.cursor()
	mycusor.execute("select * from profile")
	mydata = mycusor.fetchall()
	output = "id\tfirstName\tlastName\tintro\t\tprofile\n"
	for x in mydata:
		for y in x:
			output += str(y) + "\t"
		output += "\n"
	spotarea.setPlainText(output)

def click_btn3():
	mycusor = my_database.cursor()
	mycusor.execute("select * from duty")
	mydata = mycusor.fetchall()
	output = "id\ttitle\t\tslug\tdescription\n"
	for x in mydata:
		for y in x:
			output += str(y) + "\t"
		output += "\n"
	spotarea.setPlainText(output)

def click_btn4():
	mycusor = my_database.cursor()
	mycusor.execute("select * from company")
	mydata = mycusor.fetchall()
	output = "id\ttitle\tsummary\t\tstatus\n"
	for x in mydata:
		for y in x:
			output += str(y) + "\t"
		output += "\n"
	spotarea.setPlainText(output)

def click_btn5():
	mycusor = my_database.cursor()
	query = "insert into worker (profile_id, duty_id, company_id, code, status) values (%s, %s, %s, %s, %s)"
	val = (random.randint(1,6), random.randint(1,6), random.randint(1,6), "Another", random.randint(1,10))
	mycusor.execute(query, val)
	my_database.commit()

	mycusor = my_database.cursor()
	mycusor.execute("select * from worker")
	mydata = mycusor.fetchall()
	output = "id\tprofile_id\tduty_id\tcompany_id\tcode\tstatus\n"
	for x in mydata:
		for y in x:
			output += str(y) + "\t"
		output += "\n"
	spotarea.setPlainText(output)

def click_btn6():
	mycusor = my_database.cursor()
	query = "insert into profile (firstName, lastName, intro, profile) values (%s, %s, %s, %s)"
	val = ("Mary", "Crown", "This is Mary Crown", "Graduate")
	mycusor.execute(query, val)
	my_database.commit()

	mycusor = my_database.cursor()
	mycusor.execute("select * from profile")
	mydata = mycusor.fetchall()
	output = "id\tfirstName\tlastName\tintro\t\tprofile\n"
	for x in mydata:
		for y in x:
			output += str(y) + "\t"
		output += "\n"
	spotarea.setPlainText(output)

def click_btn7():
	mycusor = my_database.cursor()
	query = "insert into duty (title, slug, description) values (%s, %s, %s)"
	val = ("Manager", "man", "This is another manager")
	mycusor.execute(query, val)
	my_database.commit()

	mycusor = my_database.cursor()
	mycusor.execute("select * from duty")
	mydata = mycusor.fetchall()
	output = "id\ttitle\t\tslug\tdescription\n"
	for x in mydata:
		for y in x:
			output += str(y) + "\t"
		output += "\n"
	spotarea.setPlainText(output)

def click_btn8():
	mycusor = my_database.cursor()
	query = "insert into company (title, summary, status) values (%s, %s, %s)"
	val = ("G Company", "This is G Company", random.randint(1, 10))
	mycusor.execute(query, val)
	my_database.commit()

	mycusor = my_database.cursor()
	mycusor.execute("select * from company")
	mydata = mycusor.fetchall()
	output = "id\ttitle\tsummary\t\tstatus\n"
	for x in mydata:
		for y in x:
			output += str(y) + "\t"
		output += "\n"
	spotarea.setPlainText(output)

def click_btn9():
	mycusor = my_database.cursor()
	query = "delete from worker where code='Another'"
	mycusor.execute(query)
	my_database.commit()

	mycusor = my_database.cursor()
	mycusor.execute("select * from worker")
	mydata = mycusor.fetchall()
	output = "id\tprofile_id\tduty_id\tcompany_id\tcode\tstatus\n"
	for x in mydata:
		for y in x:
			output += str(y) + "\t"
		output += "\n"
	spotarea.setPlainText(output)

def click_btn10():
	mycusor = my_database.cursor()
	query = "delete from profile where lastName='Crown'"
	mycusor.execute(query)
	my_database.commit()

	mycusor = my_database.cursor()
	mycusor.execute("select * from profile")
	mydata = mycusor.fetchall()
	output = "id\tfirstName\tlastName\tintro\t\tprofile\n"
	for x in mydata:
		for y in x:
			output += str(y) + "\t"
		output += "\n"
	spotarea.setPlainText(output)

def click_btn11():
	mycusor = my_database.cursor()
	query = "delete from duty where description='This is another manager'"
	mycusor.execute(query)
	my_database.commit()

	mycusor = my_database.cursor()
	mycusor.execute("select * from duty")
	mydata = mycusor.fetchall()
	output = "id\ttitle\t\tslug\tdescription\n"
	for x in mydata:
		for y in x:
			output += str(y) + "\t"
		output += "\n"
	spotarea.setPlainText(output)

def click_btn12():
	mycusor = my_database.cursor()
	query = "delete from company where title='G Company'"
	mycusor.execute(query)
	my_database.commit()

	mycusor = my_database.cursor()
	mycusor.execute("select * from company")
	mydata = mycusor.fetchall()
	output = "id\ttitle\tsummary\t\tstatus\n"
	for x in mydata:
		for y in x:
			output += str(y) + "\t"
		output += "\n"
	spotarea.setPlainText(output)

def click_btn13():
	mycusor = my_database.cursor()
	query = "update profile set firstName='Oxen' where firstName='James'"
	mycusor.execute(query)
	my_database.commit()

	mycusor = my_database.cursor()
	mycusor.execute("select * from profile")
	mydata = mycusor.fetchall()
	output = "id\tfirstName\tlastName\tintro\t\tprofile\n"
	for x in mydata:
		for y in x:
			output += str(y) + "\t"
		output += "\n"
	spotarea.setPlainText(output)

lbl1 = QLabel(widget)
lbl1.setText('Read worker Table')
lbl1.move(20, 20)
lbl1.show()

button1 = QPushButton(widget)
button1.setText('Click')
button1.move(190, 17)
button1.show()

lbl2 = QLabel(widget)
lbl2.setText('Read profile Table')
lbl2.move(20, 48)
lbl2.show()

button2 = QPushButton(widget)
button2.setText('Click')
button2.move(190, 45)
button2.show()

lbl3 = QLabel(widget)
lbl3.setText('Read duty Table')
lbl3.move(20, 76)
lbl3.show()

button3 = QPushButton(widget)
button3.setText('Click')
button3.move(190, 73)
button3.show()

lbl4 = QLabel(widget)
lbl4.setText('Read company Table')
lbl4.move(20, 104)
lbl4.show()

button4 = QPushButton(widget)
button4.setText('Click')
button4.move(190, 101)
button4.show()

lbl5 = QLabel(widget)
lbl5.setText('Insert 1 column in worker table')
lbl5.setWordWrap(True)
lbl5.move(20, 132)
lbl5.show()

button5 = QPushButton(widget)
button5.setText('Click')
button5.move(190, 129)
button5.show()

lbl6 = QLabel(widget)
lbl6.setText('Insert 1 column in profile table')
lbl6.setWordWrap(True)
lbl6.move(20, 165)
lbl6.show()

button6 = QPushButton(widget)
button6.setText('Click')
button6.move(190, 162)
button6.show()

lbl7 = QLabel(widget)
lbl7.setText('Insert 1 column in duty table')
lbl7.setWordWrap(True)
lbl7.move(20, 198)
lbl7.show()

button7 = QPushButton(widget)
button7.setText('Click')
button7.move(190, 195)
button7.show()

lbl8 = QLabel(widget)
lbl8.setText('Insert 1 column in company table')
lbl8.setWordWrap(True)
lbl8.move(20, 231)
lbl8.show()

button8 = QPushButton(widget)
button8.setText('Click')
button8.move(190, 228)
button8.show()

lbl9 = QLabel(widget)
lbl9.setText('Delete 1 column in worker table')
lbl9.setWordWrap(True)
lbl9.move(20, 265)
lbl9.show()

button9 = QPushButton(widget)
button9.setText('Click')
button9.move(190, 262)
button9.show()

lbl10 = QLabel(widget)
lbl10.setText('Delete 1 column in profile table')
lbl10.setWordWrap(True)
lbl10.move(20, 297)
lbl10.show()

button10 = QPushButton(widget)
button10.setText('Click')
button10.move(190, 294)
button10.show()

lbl11 = QLabel(widget)
lbl11.setText('Delete 1 column in duty table')
lbl11.setWordWrap(True)
lbl11.move(20, 330)
lbl11.show()

button11 = QPushButton(widget)
button11.setText('Click')
button11.move(190, 327)
button11.show()

lbl12 = QLabel(widget)
lbl12.setText('Delete 1 column in company table')
lbl12.setWordWrap(True)
lbl12.move(20, 363)
lbl12.show()

button12 = QPushButton(widget)
button12.setText('Click')
button12.move(190, 360)
button12.show()

lbl13 = QLabel(widget)
lbl13.setText('Update firstName "James" to "Oxen" in profile table')
lbl13.setWordWrap(True)
lbl13.move(20, 395)
lbl13.resize(100, 35)
lbl13.show()

button13 = QPushButton(widget)
button13.setText('Click')
button13.move(190, 392)
button13.show()

button1.clicked.connect(click_btn1)
button2.clicked.connect(click_btn2)
button3.clicked.connect(click_btn3)
button4.clicked.connect(click_btn4)
button5.clicked.connect(click_btn5)
button6.clicked.connect(click_btn6)
button7.clicked.connect(click_btn7)
button8.clicked.connect(click_btn8)
button9.clicked.connect(click_btn9)
button10.clicked.connect(click_btn10)
button11.clicked.connect(click_btn11)
button12.clicked.connect(click_btn12)
button13.clicked.connect(click_btn13)

widget.show()

application.exec_()
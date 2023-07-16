from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QLabel,QPushButton,QLabel
import sys  
app=QApplication(sys.argv)
MainWindow=QMainWindow()
MainWindow.setWindowTitle("Calclator")
MainWindow.setWindowIcon(QtGui.QIcon('cal.ico'))
MainWindow.setGeometry(700,100,400,500)
MainWindow.setStyleSheet("background-color:#e9e9f8;border-radius: 26px;")
############################################################################
def click(mark):
    text=labl.text()
    if mark == "0" or mark == "1" or mark == "2" or mark == "2" or mark == "3" or mark == "5" or mark == "6" or mark == "7" or mark == "8" or mark == "9" :
        labl.setText(f"{labl.text()}{mark}")
    elif mark=="C":
        labl.setText("")
    elif mark=="<<<":
        list_of_clear=labl.text()
        labl.setText(list_of_clear[:-1])  
    else:
        labl.setText(text+mark) 
############################################################################     
def math():
    scor=labl.text()
    an=eval(scor)
    labl.setText(str(an))
############################################################################
def pashbutton(num,x,y,w,h):
    pashbutton0=QPushButton(num,MainWindow)
    pashbutton0.setStyleSheet(f"background-color:#89bbfc;font-size: 30px;border-radius: 10px;border:1px solid #e60d0d;color:#ffffffd2;")
    pashbutton0.setGeometry(x,y,w,h)
    pashbutton0.clicked.connect(lambda:click(num))
############################################################################
def pashbutton_operation(op,x,y,w,h):
    pashbutton=QPushButton(op,MainWindow)
    pashbutton.setStyleSheet("background-color:#89bbfc;font-size: 30px;border-radius: 10px;border:1px solid #e60d0d;color:#ffffffd2;")
    if op == "=":
        pashbutton.setGeometry(x,y,w,h)
        pashbutton.clicked.connect(math)
    elif op == "+":
        pashbutton.setGeometry(x,y,w,h)
        pashbutton.clicked.connect(lambda:click(op))
    elif op == "-":
        pashbutton.setGeometry(x,y,w,h)
        pashbutton.clicked.connect(lambda:click(op))
    elif op =="X":
        pashbutton.setGeometry(x,y,w,h)
        pashbutton.clicked.connect(lambda:click('*'))
    elif op =="/":
        pashbutton.setGeometry(x,y,w,h)
        pashbutton.clicked.connect(lambda:click(op))
    elif op == ".":
        pashbutton.setGeometry(x,y,w,h)
        pashbutton.clicked.connect(lambda:click(op))
    elif op =="C":
        pashbutton.setGeometry(x,y,w,h)
        pashbutton.clicked.connect(lambda:click(op))
    elif op == "<<<":
        pashbutton.setGeometry(x,y,w,h)
        pashbutton.clicked.connect(lambda:click(op))
        pass
############################################################################
labl=QLabel("",MainWindow)
labl.move(10,20)
labl.setStyleSheet("font-size: 20px;border:1px solid rgb(34, 13, 230);border-radius: 10px;")
labl.resize(380,50)
#################################################################
pashbutton("0",10,400,180,90)
pashbutton("1",10,300,90,90)
pashbutton("2",105,300,90,90)
pashbutton("3",200,300,90,90)
pashbutton("4",10,200,90,90)
pashbutton("5",105,200,90,90)
pashbutton("6",200,200,90,90)
pashbutton("7",10,100,90,90)
pashbutton("8",105,100,90,90)
pashbutton("9",200,100,90,90)
#################################################################
pashbutton_operation('+',298,375,90,50)
pashbutton_operation('-',298,320,90,50)
pashbutton_operation('/',298,210,90,50)
pashbutton_operation('X',298,265,90,50)
pashbutton_operation('=',295,430,100,60)
pashbutton_operation('.',198,400,90,90)
pashbutton_operation('C',298,155,90,50)
pashbutton_operation('<<<',298,100,90,50)
#################################################################
MainWindow.show()
app.exec()

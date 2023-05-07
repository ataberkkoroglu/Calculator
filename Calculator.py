from PyQt5.QtWidgets import QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit,QLabel,QApplication,QMainWindow,QWidget
from PyQt5.QtGui import QFont,QIcon,QPixmap

import sys,numpy as np,math
class Calculator(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.program()
        self.expression=" "*self.text.width()
        self.Shift_state=0
        self.brackets_state=0
        self.plus_minus_state=0
        self.function_bracket=False
        
    def program(self):
        
        self.windows=QWidget()
        self.windows.setWindowTitle("Calculator")
        self.windows.setStyleSheet("background: black")
        self.text=QLineEdit()
        self.text.setFixedHeight(50)
        self.text.setFont(QFont("Arial",20,4))
        self.text.setStyleSheet("color: White")
       
        self.backspace=QPushButton("<")
        self.backspace.setFont(QFont("Arial",20,4))
        self.backspace.setStyleSheet("background: Red;color:white")
       
        
        self.shift=QPushButton("Shift")
        self.shift.setStyleSheet("background: gray;color:blue")
        self.Rad=QPushButton("Rad")
        self.Rad.setStyleSheet("background: gray;color:lightblue")
        self.Sqrt=QPushButton("Square Root")
        self.Sqrt.setStyleSheet("background: gray;color:lightblue")
        self.sin=QPushButton("Sin")
        self.sin.setStyleSheet("background: gray;color:lightblue")
        self.cos=QPushButton("Cos")
        self.cos.setStyleSheet("background: gray;color:lightblue")
        self.tan=QPushButton("Tan")
        self.tan.setStyleSheet("background: gray;color:lightblue")
        self.In=QPushButton("In")
        self.In.setStyleSheet("background: gray;color:lightblue")
        self.log=QPushButton("Log")
        self.log.setStyleSheet("background: gray;color:lightblue")
        self.measure=QPushButton("1/x")
        self.measure.setStyleSheet("background: gray;color:lightblue")
        self.e_power=QPushButton("e^x")
        self.e_power.setStyleSheet("background: gray;color:lightblue")
        self.power=QPushButton("x^2")
        self.power.setStyleSheet("background: gray;color:lightblue")
        self.power2=QPushButton("x^y")
        
        self.power2.setStyleSheet("background: gray;color:lightblue")
        self.abs=QPushButton("|x|")
        self.abs.setStyleSheet("background: gray;color:lightblue")
        self.pi=QPushButton("pi")
        self.pi.setStyleSheet("background: gray;color:lightblue")
        self.e=QPushButton("e")
        self.e.setStyleSheet("background: gray;color:lightblue")
        self.plus_minus=QPushButton("+/-")
        self.plus_minus.setStyleSheet("background: gray;color:lightblue")
        self.plus_minus.setFont(QFont("Arial",20,4))
        self.point=QPushButton(".")
        self.point.setStyleSheet("background: gray;color:lightblue")
        self.point.setFont(QFont("Arial",20,4))
        
        self.clear=QPushButton("C")
        self.clear.setStyleSheet("background: gray;color:red")
        self.brackets=QPushButton("()")
        self.brackets.setStyleSheet("background: gray;color:purple")
        self.mod=QPushButton("%")
        self.mod.setStyleSheet("background: gray;color:purple")
        self.div=QPushButton("/")
        self.div.setStyleSheet("background: gray;color:purple")
        self.mul=QPushButton("x")
        self.mul.setStyleSheet("background: gray;color:purple")
        self.minus=QPushButton("-")
        self.minus.setStyleSheet("background: gray;color:purple")
        self.plus=QPushButton("+")
        self.plus.setStyleSheet("background: gray;color:purple")
        self.equal=QPushButton("=")
        self.equal.setStyleSheet("background: purple ;color: white")
        
        self.Zero=QPushButton('0')
        self.Zero.setFont(QFont("Arial",20,4))
        self.Zero.setStyleSheet("background: gray;color: lightblue")
        self.One=QPushButton('1')
        self.One.setStyleSheet("background: gray;color: lightblue")
        self.Two=QPushButton('2')
        self.Two.setStyleSheet("background: gray;color: lightblue")
        self.Three=QPushButton('3')
        self.Three.setStyleSheet("background: gray;color: lightblue")
        self.Four=QPushButton('4')
        self.Four.setStyleSheet("background: gray;color: lightblue")
        self.Five=QPushButton('5')
        self.Five.setStyleSheet("background: gray;color: lightblue")
        self.Six=QPushButton('6')
        self.Six.setStyleSheet("background: gray;color: lightblue")
        self.Seven=QPushButton('7')
        self.Seven.setStyleSheet("background: gray;color: lightblue")
        self.Eight=QPushButton('8')
        self.Eight.setStyleSheet("background: gray;color: lightblue")
        self.Nine=QPushButton('9')
        self.Nine.setStyleSheet("background: gray;color: lightblue")
        
        self.shift.setFont(QFont("Arial",20,4))
        self.Rad.setFont(QFont("Arial",20,4))
        self.Sqrt.setFont(QFont("Arial",20,4))
        self.sin.setFont(QFont("Arial",20,4))
        self.cos.setFont(QFont("Arial",20,4))
        self.tan.setFont(QFont("Arial",20,4))
        self.In.setFont(QFont("Arial",20,4))
        self.log.setFont(QFont("Arial",20,4))
        self.measure.setFont(QFont("Arial",20,4))
        self.e_power.setFont(QFont("Arial",20,4))
        self.power.setFont(QFont("Arial",20,4))
        self.power2.setFont(QFont("Arial",20,4))
        self.abs.setFont(QFont("Arial",20,4))
        self.pi.setFont(QFont("Arial",20,4))
        self.e.setFont(QFont("Arial",20,4))
        self.clear.setFont(QFont("Arial",20,4))
        self.brackets.setFont(QFont("Arial",20,4))
        self.mod.setFont(QFont("Arial",20,4))
        self.div.setFont(QFont("Arial",20,4))
        self.mul.setFont(QFont("Arial",20,4))
        self.minus.setFont(QFont("Arial",20,4))
        self.plus.setFont(QFont("Arial",20,4))
        self.equal.setFont(QFont("Arial",20,4))  
        self.One.setFont(QFont("Arial",20,4))
        self.Two.setFont(QFont("Arial",20,4))
        self.Three.setFont(QFont("Arial",20,4))
        self.Four.setFont(QFont("Arial",20,4))
        self.Five.setFont(QFont("Arial",20,4))
        self.Six.setFont(QFont("Arial",20,4))
        self.Seven.setFont(QFont("Arial",20,4))
        self.Eight.setFont(QFont("Arial",20,4))
        self.Nine.setFont(QFont("Arial",20,4))
        self.point.setFont(QFont("Arial",20,4))
        
        self.equal.setShortcut("Return")
           
        v_box=QVBoxLayout()
        
        h_box=QHBoxLayout()
        
        h_box.addSpacing(20)
        h_box.addWidget(self.shift)
        h_box.addSpacing(20)
        h_box.addWidget(self.Rad)
        h_box.addSpacing(20)
        h_box.addWidget(self.Sqrt)
        h_box.addSpacing(20)
        h_box.addWidget(self.clear)
        h_box.addSpacing(20)
        h_box.addWidget(self.brackets)
        h_box.addSpacing(20)
        h_box.addWidget(self.mod)
        h_box.addSpacing(20)
        h_box.addWidget(self.div)
        
        h_box2=QHBoxLayout()
        
        h_box2.addSpacing(20)
        h_box2.addWidget(self.sin)
        h_box2.addSpacing(20)
        h_box2.addWidget(self.cos)
        h_box2.addSpacing(20)
        h_box2.addWidget(self.tan)
        h_box2.addSpacing(20)
        h_box2.addWidget(self.Seven)
        h_box2.addSpacing(20)
        h_box2.addWidget(self.Eight)
        h_box2.addSpacing(20)
        h_box2.addWidget(self.Nine)
        h_box2.addSpacing(20)
        h_box2.addWidget(self.mul)
        
        h_box3=QHBoxLayout()
        
        h_box3.addSpacing(20)
        h_box3.addWidget(self.In)
        h_box3.addSpacing(20)
        h_box3.addWidget(self.log)
        h_box3.addSpacing(20)
        h_box3.addWidget(self.measure)
        h_box3.addSpacing(20)
        h_box3.addWidget(self.Four)
        h_box3.addSpacing(20)
        h_box3.addWidget(self.Five)
        h_box3.addSpacing(20)
        h_box3.addWidget(self.Six)
        h_box3.addSpacing(20)
        h_box3.addWidget(self.minus)
        
        h_box4=QHBoxLayout()
        
        h_box4.addSpacing(20)
        h_box4.addWidget(self.e_power)
        h_box4.addSpacing(20)
        h_box4.addWidget(self.power2)
        h_box4.addSpacing(20)
        h_box4.addWidget(self.power)
        h_box4.addSpacing(20)
        h_box4.addWidget(self.One)
        h_box4.addSpacing(20)
        h_box4.addWidget(self.Two)
        h_box4.addSpacing(20)
        h_box4.addWidget(self.Three)
        h_box4.addSpacing(20)
        h_box4.addWidget(self.plus)
        
        h_box5=QHBoxLayout()
        
        h_box5.addSpacing(20)
        h_box5.addWidget(self.abs)
        h_box5.addSpacing(20)
        h_box5.addWidget(self.pi)
        h_box5.addSpacing(20)
        h_box5.addWidget(self.e)
        h_box5.addSpacing(20)
        h_box5.addWidget(self.plus_minus)
        h_box5.addSpacing(20)
        h_box5.addWidget(self.Zero)
        h_box5.addSpacing(20)
        h_box5.addWidget(self.point)
        h_box5.addSpacing(20)
        h_box5.addWidget(self.equal)
        
        h_box6=QHBoxLayout()
        h_box6.addWidget(self.text)
        h_box6.addSpacing(20)
        h_box6.addWidget(self.backspace)
        
        v_box.addLayout(h_box6)
        v_box.addSpacing(20)
        v_box.addLayout(h_box)
        v_box.addSpacing(20)
        v_box.addLayout(h_box2)
        v_box.addSpacing(20)
        v_box.addLayout(h_box3)
        v_box.addSpacing(20)
        v_box.addLayout(h_box4)
        v_box.addSpacing(20)
        v_box.addLayout(h_box5)
        v_box.addSpacing(20)
        
        self.windows.setLayout(v_box)
        
        self.Zero.clicked.connect(self.Print)
        self.point.clicked.connect(self.Print)
        self.shift.clicked.connect(self.Print)
        self.Rad.clicked.connect(self.Print)
        self.Sqrt.clicked.connect(self.Print)
        self.sin.clicked.connect(self.Print)
        self.cos.clicked.connect(self.Print)
        self.tan.clicked.connect(self.Print)
        self.In.clicked.connect(self.Print)
        self.log.clicked.connect(self.Print)
        self.measure.clicked.connect(self.Print)
        self.e_power.clicked.connect(self.Print)
        self.power.clicked.connect(self.Print)
        self.power2.clicked.connect(self.Print)
        self.abs.clicked.connect(self.Print)
        self.pi.clicked.connect(self.Print)
        self.e.clicked.connect(self.Print)
        
        self.clear.clicked.connect(self.Print)
        self.brackets.clicked.connect(self.Print)
        self.mod.clicked.connect(self.Print)
        self.div.clicked.connect(self.Print)
        self.mul.clicked.connect(self.Print)
        self.minus.clicked.connect(self.Print)
        self.plus.clicked.connect(self.Print)
        
        self.equal.clicked.connect(self.Print2)
        self.One.clicked.connect(self.Print)
        self.Two.clicked.connect(self.Print)
        self.Three.clicked.connect(self.Print)
        self.Four.clicked.connect(self.Print)
        self.Five.clicked.connect(self.Print)
        self.Six.clicked.connect(self.Print)
        self.Seven.clicked.connect(self.Print)
        self.Eight.clicked.connect(self.Print)
        self.Nine.clicked.connect(self.Print)
        self.backspace.clicked.connect(self.Print)
        self.plus_minus.clicked.connect(self.Print2)
        self.windows.show()
    
    def Print(self):
        sender=self.windows.sender()
        self.result=list()
        
        if sender.text()=="Shift":
            
            self.Shift_state +=1
            
            if (self.Shift_state%2!=0):
                self.Sqrt.setText("Cubic Root")
                self.sin.setText("Arcsin")
                self.cos.setText("Arccos")
                self.tan.setText("Arctan")
                self.In.setText("sinh")
                self.log.setText("cosh")
                self.measure.setText("tanh")
                self.e_power.setText("Arcsinh")
                self.power2.setText("Arccosh")
                self.power.setText("Arctanh")
                self.abs.setText("2^x")
                self.pi.setText("x^3")
                self.e.setText("x!")
            else:
                self.Sqrt.setText("Square Root")
                self.sin.setText("sin")
                self.cos.setText("cos")
                self.tan.setText("tan")
                self.In.setText("In")
                self.log.setText("Log")
                self.measure.setText("1/x")
                self.e_power.setText("e^x")
                self.power2.setText("x^2")
                self.power.setText("x^y")
                self.abs.setText("|x|")
                self.pi.setText("pi")
                self.e.setText("e")
        
        elif sender.text() =="Rad":
            self.expression=""
            self.expression +=sender.text()
            self.expression +='\t'
            self.Rad.setText("Deg")
            self.text.setText(self.expression)
            
        elif sender.text()=="Deg":
            self.expression=""
            self.expression +=sender.text()
            self.expression +='\t'
            self.Rad.setText("Rad")
            self.text.setText(self.expression)
            
        elif sender.text()=="1":
            self.expression +=sender.text()
            
        elif sender.text()=='2':
            self.expression +=sender.text()
            
        elif sender.text()=="3":
            self.expression +=sender.text()
            
        elif sender.text()=='4':
            self.expression +=sender.text()
            
        elif sender.text()=="5":
            self.expression +=sender.text()
            
        elif sender.text()=='6':
            self.expression +=sender.text()
            
        elif sender.text()=="7":
            self.expression +=sender.text()
            
        elif sender.text()=='8':
            self.expression +=sender.text() 
            
        elif sender.text()=="9":
            self.expression +=sender.text()
            
        elif sender.text()=='0':
            self.expression +=sender.text()
            
        elif sender.text()=='.':
            self.expression +=sender.text()
            
        elif sender.text()=='C':
            self.expression=" "*self.text.width()
            self.function_expression=""
        elif sender.text()=='()':
            self.brackets_state +=1
            if self.function_bracket:
               self.expression +=")"
               self.function_bracket=False
            elif (self.brackets_state%2!=0):
                self.expression +='('
            else:
                self.expression +=')'
        
        elif sender.text()=='%':
            self.expression +=sender.text()
            
        elif sender.text()=='-':
            self.expression +=sender.text()
            
        elif sender.text()=='+':
            self.expression +=sender.text()
            
        elif sender.text()=='x':
            self.expression +='*'
            
        elif sender.text()=='/':
            self.expression +=sender.text()
            
        elif sender.text()=='<':
            
            if (self.text.text() !=""):
              self.expression=list(self.text.text())
              self.expression.pop(len(self.expression)-1)
              self.expression2=""
              for i in self.expression:
                self.expression2 +=i                
              self.expression=self.expression2
              
        elif sender.text()=='Sin':
            self.Attention()
            self.expression +="np.sin("
            self.function_bracket=True
            
        elif sender.text()=="Cos":
            self.function_bracket=True
            self.expression +="np.cos("
            self.Attention()
            
            
        elif sender.text()=="Tan":
            self.function_bracket=True
            self.expression +="np.tan("
            self.Attention()
           
             
        elif sender.text()=="In":
            self.function_bracket=True
            self.expression +="np.log("            
               
        elif sender.text()=="x^y":
          self.expression +="**"
             
            
        elif sender.text()=="Square Root":
            self.function_bracket=True
            self.expression +="np.sqrt("
           
            
        elif sender.text()=="Log":
            self.function_bracket=True
            self.expression +="np.log10("
            
            
        elif sender.text()=="1/x":
            self.expression +="1/"
            
            
        elif sender.text()=="e^x":
            self.expression +="np.e**"
            
        elif sender.text()=="x^2":
            try:
              self.expression +="**2"
            except:
              pass
            
            
        elif sender.text()=="|x|":
            self.function_bracket=True
            self.expression +="abs("
            
        elif sender.text()=="pi":
           self.expression +="np.pi"
        elif sender.text()=="e":
            self.expression +="np.e"  
        
        elif sender.text()=='Arcsin':
            self.function_bracket=True
            self.expression +="np.arcsin("
            
          
            
        elif sender.text()=="Arccos":
            self.function_bracket=True
            self.expression +="np.arccos("
            
           
            
        elif sender.text()=="Arctan":
            self.function_bracket=True
            self.expression +="np.arctan("
            
           
             
        elif sender.text()=="sinh":
            self.function_bracket=True
            self.expression +="np.sinh("
            
            
               
            
             
            
        elif sender.text()=="Cubic Root":
            self.function_bracket=True
            self.expression +="np.cbrt("
            
            if self.text.text()=="":
              pass
            elif (float(self.text.text())>=0):
               self.expression +=(str(np.cbrt(float(self.text.text()))))
               self.result.append(str(np.cbrt(float(self.text.text()))))
            
        elif sender.text()=="cosh":
            self.function_bracket=True
            self.expression +="np.cosh("
            
            
            
        elif sender.text()=="tanh":
            self.function_bracket=True
            self.expression +="np.tanh("
            
            
        elif sender.text()=="Arcsinh":
            self.function_bracket=True
            self.expression +="np.arcsinh("
            
            
            
        elif sender.text()=="Arccosh":
            self.function_bracket=True
            self.expression +="np.arccosh("
            
            
            
        elif sender.text()=="Arctanh":
            self.function_bracket=True
            
            self.expression +="np.arctanh("
            
            
        elif sender.text()=="2^x":
          
           self.expression +="2**"
           
        elif sender.text()=="x^3":
          try:
            self.expression +="**3"
          except:
            pass
            
        elif sender.text()=="x!":
            self.function_bracket=True
            self.expression +="math.factorial("
        
        self.text.setText(self.expression)
        
            
        
    
    def Print2(self):
        sender=self.windows.sender()
        state=""
        if sender.text()=='=':               
           try:
            if "Rad" in self.text.text() or "Deg" in self.text.text():
             for i in self.text.text():
                if (ord(i)>64 and ord(i)<91) or (ord(i)>96 and ord(i)<123) or i=='.':
                     self.text.setText(self.text.text().replace(i,''))
                     state +=i
            self.expression=" "*self.text.width()
            
               
            if (state !=""):
              self.expression +=state
              self.expression +=('\t'+str(eval(self.text.text())))
          
            else:
                self.expression +=(str(eval(self.text.text())))
            self.text.setText(self.expression)
            self.expression=" "*self.text.width()
           except:
               pass
        elif sender.text()=="+/-":
            self.Attention()
            if self.text.text()=="":
              pass
                
            elif '+' in self.text.text() and self.text.text().count('+')>1:
                self_text_list=list(self.text.text())
                self_text_list[self.text.text().rfind("+")]="-"
                Text=""
                for i in self_text_list:
                    Text +=i
                self.text.setText(str(Text))
                
            elif '-' in self.text.text() and self.text.text().count('-')>1:
                self_text_list=list(self.text.text())
                self_text_list[self.text.text().rfind("-")]="+"
                Text=""
                for i in self_text_list:
                    Text +=i
                self.text.setText(str(Text))
            
            elif '+' in self.text.text() and self.text.text().count('+')==1:
                self.text.setText(self.text.text().replace('+', '-'))
            elif '-' in self.text.text() and self.text.text().count('-')==1:
                self.text.setText(self.text.text().replace('-', ''))
                
            else:
                self.text.setText(str(-1*float(self.text.text())))
                
            self.expression=self.text.text()
        
                
        
    
    def Attention(self):
        
        self.windows2=QWidget()
        self.windows2.setWindowTitle("Calculator")
        self.windows2.setStyleSheet("background: white")
        self.picture=QLabel()
        self.picture.setPixmap(QPixmap("C:\\Users\\asus\\Desktop\\Calculator\\Warning.png"))
        self.picture.setStyleSheet("background:white")
        self.Text=QLabel("You must write Your Value As type of Radian.")
        self.Text.setFont(QFont("Arial",20,4))
        self.Text.setStyleSheet("color:Red")
        
        h_box=QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.picture)
        h_box.addStretch()
        v_box=QVBoxLayout()
        v_box.addSpacing(30)
        v_box.addLayout(h_box)
        v_box.addSpacing(30)
        v_box.addWidget(self.Text)
        
        self.windows2.setLayout(v_box)
        self.windows2.show()
        
        
app=QApplication(sys.argv)
app.setWindowIcon(QIcon("C:\\Users\\asus\\Desktop\\Calculator\\calculator.png"))
calculator=Calculator()
sys.exit(app.exec())
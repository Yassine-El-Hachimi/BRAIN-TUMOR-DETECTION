from tkinter import *
import tkinter as tk
import tkinter
import tkinter as ttk
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter.messagebox import showinfo, showwarning
from tkinter.font import Font
import cv2
from PIL import ImageFilter
from scipy.misc import imread ,imresize
import os
import tensorflow as tf
import numpy as np
import keras
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
modelAdam = tf.keras.models.load_model('Brain_tumor.*.h5/Brain_tumorBAdam.h5')
modelRMS = tf.keras.models.load_model('Brain_tumor.*.h5/Brain_tumorBRMSpropV2.h5')
modelSGD = tf.keras.models.load_model('Brain_tumor.*.h5/Brain_tumorSGD.h5')

result = [""]*1
choix = [0]*3
window = Tk()
window.title("Tumoral Brain")
window.geometry("1080x650")
window.config(background='#f1f1f1')
frame = Frame(window,bg='#4065A4')
bar = Canvas(window,width =880,height=30 ,bg='#B20637')
bar.place(x=202,y=0)
title = tkinter.Label(window,text="Interface Of Tumor Detection Software",fg='#ffffff',bg='#B20637',bd=0,highlightthickness=0,font=("Helvetica",15))
title.place(x=450,y=5)
barleft = Canvas(window,width =215,height=650 ,bg='#1C1536')
barleft.place(x=0,y=0)

#fonction pour upload image
def importy():
    result[0] = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("jpg 				                    files", ".jpg"),("all files", ".*")))
    a=Image.open(result[0])
    res = a.resize((247,248))
    myImage = ImageTk.PhotoImage(res)
    labe.config(image = myImage)
    mainloop()
#fonction de thresholding   
def thre(a = 145):
    choix[1] = int(a)
    img = cv2.imread(result[0],cv2.IMREAD_GRAYSCALE)
    img3 = cv2.GaussianBlur(img,(15,15),cv2.BORDER_DEFAULT)
    retval,threshold = cv2.threshold(img3,int(a),255,cv2.THRESH_BINARY)
    choix[2] = threshold
    img = Image.fromarray(threshold)
    
    img = img.resize((247,248))
    myImage = ImageTk.PhotoImage(img)
    label.config(image = myImage)
    label.image = myImage

    
#fonctions pour l'effet sur les bouttons
def left1(event):
    
	if (choix[0] == 2):
		canvasRMSprop.config(fg = "#ffffff")
		canvasR.config(fg = "#B20637")
	elif (choix[0] == 3):
		canvasSGD.config(fg = "#ffffff")
		canvasS.config(fg = "#B20637")
	elif (choix[0] == 4):
		canvasAdagrad.config(fg = "#ffffff")
		canvasD.config(fg = "#B20637")
	elif (choix[0] == 5):
		canvasAdadelta.config(fg = "#ffffff")
		canvasT.config(fg = "#B20637")

	choix[0] = 1
	canvasAdam.config(fg = "#FAAE00")
	canvasA.config(fg = "#FAAE00")
   
def left2(event):

	if (choix[0] == 1):
		canvasAdam.config(fg = "#ffffff")
		canvasA.config(fg = "#B20637")
	elif (choix[0] == 3):
		canvasSGD.config(fg = "#ffffff")
		canvasS.config(fg = "#B20637")
	elif (choix[0] == 4):
		canvasAdagrad.config(fg = "#ffffff")
		canvasD.config(fg = "#B20637")
	elif (choix[0] == 5):
		canvasAdadelta.config(fg = "#ffffff")
		canvasT.config(fg = "#B20637")

	choix[0] = 2
	canvasRMSprop.config(fg = "#FAAE00")
	canvasR.config(fg = "#FAAE00")
     
def left3(event):

	if (choix[0] == 2):
		canvasRMSprop.config(fg = "#ffffff")
		canvasR.config(fg = "#B20637")
	elif (choix[0] == 1):
		canvasAdam.config(fg = "#ffffff")
		canvasA.config(fg = "#B20637")
	elif (choix[0] == 4):
		canvasAdagrad.config(fg = "#ffffff")
		canvasD.config(fg = "#B20637")
	elif (choix[0] == 5):
		canvasAdadelta.config(fg = "#ffffff")
		canvasT.config(fg = "#B20637")

	choix[0] = 3
	canvasSGD.config(fg = "#FAAE00")
	canvasS.config(fg = "#FAAE00")
   
def left4(event):

	if (choix[0] == 2):
		canvasRMSprop.config(fg = "#ffffff")
		canvasR.config(fg = "#B20637")
	elif (choix[0] == 3):
		canvasSGD.config(fg = "#ffffff")
		canvasS.config(fg = "#B20637")
	elif (choix[0] == 1):
		canvasAdam.config(fg = "#ffffff")
		canvasA.config(fg = "#B20637")
	elif (choix[0] == 5):
		canvasAdadelta.config(fg = "#ffffff")
		canvasT.config(fg = "#B20637")

	choix[0] = 4
	canvasAdagrad.config(fg = "#FAAE00")
	canvasD.config(fg = "#FAAE00")

   
    
def left5(event):

	if (choix[0] == 2):
		canvasRMSprop.config(fg = "#ffffff")
		canvasR.config(fg = "#B20637")
	elif (choix[0] == 3):
		canvasSGD.config(fg = "#ffffff")
		canvasS.config(fg = "#B20637")
	elif (choix[0] == 4):
		canvasAdagrad.config(fg = "#ffffff")
		canvasD.config(fg = "#B20637")
	elif (choix[0] == 1):
		canvasAdam.config(fg = "#ffffff")
		canvasA.config(fg = "#B20637")

	choix[0] = 5
	canvasAdadelta.config(fg = "#FAAE00")
	canvasT.config(fg = "#FAAE00")
"""bar left"""
def plot():
	img = cv2.imread(result[0],0) 

	histr = cv2.calcHist([img],[0],None,[256],[0,256]) 
	print(histr) 

	img = Image.fromarray(histr) # Transformation du tableau en image PIL
	if img.mode != 'RGB':
	    img = img.convert('RGB')
	#img = img.resize((247,248))
	myImage = ImageTk.PhotoImage(img)
	label3.config(image = myImage)
	label3.image = myImage


def delete():
	labe.config(image = "")
	label.config(image = "")
	label3.config(image = "")
#logo de l'application
image =PhotoImage(file="logo2.png").zoom(15).subsample(45)
canvas = tkinter.Canvas(window,width=190,height=200,bg='#1C1536',bd=0,highlightthickness=0)
canvas.create_image(90,70,image=image)
canvas.place(x=10,y=10)
#optimizer function
title_optimizer=tkinter.Label(window,text="OPtimizer Function",bg='#1C1536',fg='#FAAE00',font=("Helvetica",15))
title_optimizer.place(x = 20,y =150)
#ADAM
canvasAdam = tkinter.Label(window,text="Adam",width=8,height=2,fg='#ffffff',bg='#1C1536',bd=0,highlightthickness=0,font=("Helvetica",15))
canvasAdam.place(x=70,y=200)
canvasA = tkinter.Label(window,text="A",width=2,height=1,fg='#B20637',bg='#1C1536',bd=0,highlightthickness=0,font=("times",24,"italic"))
canvasA.place(x=30,y=200)
canvasAdam.bind("<Button-1>",left1)
#RMSprop
canvasRMSprop = tkinter.Label(window,text="RMSprop",width=8,height=2,fg='#ffffff',bg='#1C1536',bd=0,highlightthickness=0,font=("Helvetica",15))
canvasRMSprop.place(x=70,y=250)
canvasR = tkinter.Label(window,text="R",width=2,height=1,fg='#B20637',bg='#1C1536',bd=0,highlightthickness=0,font=("times",24,"italic"))
canvasR.place(x=30,y=251)
canvasRMSprop.bind("<Button-1>",left2)
#SGD
canvasSGD = tkinter.Label(window,text="SGD",width=8,height=2,fg='#ffffff',bg='#1C1536',bd=0,highlightthickness=0,font=("Helvetica",15))
canvasSGD.place(x=70,y=300)
canvasS = tkinter.Label(window,text="S",width=2,height=1,fg='#B20637',bg='#1C1536',bd=0,highlightthickness=0,font=("times",24,"italic"))
canvasS.place(x=30,y=301)
canvasSGD.bind("<Button-1>",left3)
#ADAGRAD
canvasAdagrad = tkinter.Label(window,text="Adagrad",width=8,height=2,fg='#ffffff',bg='#1C1536',bd=0,highlightthickness=0,font=("Helvetica",15))
canvasAdagrad.place(x=70,y=350)
canvasD = tkinter.Label(window,text="D",width=2,height=1,fg='#B20637',bg='#1C1536',bd=0,highlightthickness=0,font=("times",24,"italic"))
canvasD.place(x=30,y=351)
canvasAdagrad.bind("<Button-1>",left4)
#ADADELTA
canvasAdadelta= tkinter.Label(window,text="Adadelta",width=8,height=2,fg='#ffffff',bg='#1C1536',bd=0,highlightthickness=0,font=("Helvetica",15))
canvasAdadelta.place(x=70,y=400)
canvasT = tkinter.Label(window,text="T",width=2,height=1,fg='#B20637',bg='#1C1536',bd=0,highlightthickness=0,font=("times",24,"italic"))
canvasT.place(x=30,y=401)
canvasAdadelta.bind("<Button-1>",left5)
#nombre of epoche
title_optimizer=tkinter.Label(window,text="Number Of Epoches",bg='#1C1536',fg='#FAAE00',font=("Helvetica",15))
title_optimizer.place(x = 20,y =470)
title_optimizer=tkinter.Label(window,text="100",width = 7,height = 1,fg='black',font=("Helvetica",15))
title_optimizer.place(x = 60,y =520)
#BUTTON NEXT


def popup_showinfo():
	if (choix[0] == 0):

		showwarning("Window", "Essayer de bien choisir l'Optimizer !!!!!!") 

	elif (choix[0] == 1):

		
		out = modelAdam.predict(predict(result[0], choix[1]))
		Display_result(out)

	elif (choix[0] == 2):

		
		out = modelRMS.predict(predict(result[0], choix[1]))
		Display_result(out)
	elif (choix[0] == 3):

		
		out = modelSGD.predict(predict(result[0], choix[1]))
		Display_result(out)

	else:
		showwarning("Window", "Essayer de bien choisir l'Optimizer !!!!!!") 

def Display_result(out):
	if (round(out[0][0]) == 1.0):
		showinfo("Resultat ","Brain with tumor ")
	else:
		showinfo("Resultat ","Brain healthy ")

def crop_brain_contour(image,a):
  
    gray = cv2.GaussianBlur(image, (15, 15), 0)

    ret, thresh = cv2.threshold(gray, a, 255, cv2.THRESH_BINARY)
   
    return thresh
    

def predict(Img,a):
    x = cv2.imread(Img)
    x = crop_brain_contour(x,a)
   
    x = x / 255.
    x = imresize(x,(128,128))

    x = x.reshape(1,128,128,3)
    x = x.astype('float32')

    return x


#BUTTON upload  
photop = PhotoImage(file="upload.png")
btn = tkinter.Button(window,image = photop,command = importy,border = 0,bg="#f1f1f1",height = 65,width = 185)
btn.place( x = 290,y=100)
#BUTTON PRE6PROCESSING
photop2 = PhotoImage(file="prepro.png")
btn2 = tkinter.Button(window,image = photop2,command = thre,border = 0,bg="white",height = 65,width = 185)
btn2.place(x = 555,y=100)

#CLASSIFY
photop3 = PhotoImage(file="classify.png")
btn3 = tkinter.Button(window,image = photop3,command = popup_showinfo,border = 0,bg="white",height = 65,width = 185)
btn3.place( x = 840,y=100)

#PREVIOUS
photop4 = PhotoImage(file="previous.png")
btn4 = tkinter.Button(window,image = photop4,command = delete,border = 0,bg="white",height = 65,width = 185)
btn4.place( x = 290,y=500)

#PLOT graphe
photop5 = PhotoImage(file="plot.png")
btn5 = tkinter.Button(window,image = photop5,command = plot,border = 0,bg="white",height = 65,width = 185)
btn5.place( x = 840,y=500)

#CANVAS ADD IMAGE
# canvas pour importer l'image
canvas1 = Canvas(window,relief="ridge", width=250, height=250, bg='#ffffff')
labe= tkinter.Label(window,bg='#ffffff')
labe.place(x=253,y=212)
canvas1.place(x=250,y=210)

#CANVAS PREPROCESSING
#canvas pour pre-processing
canvas2 = Canvas(window,relief="ridge", width=250, height=250, bg='#ffffff')
label= tkinter.Label(window,bg='#ffffff')
label.place(x=525,y=210)
canvas2.place(x=525,y=210)

#CANVAS GRAPHE
canvas3 = Canvas(window,relief="ridge", width=250, height=250, bg='#ffffff')
label3= tkinter.Label(window,bg='#ffffff')
label3.place(x=800,y=210)
canvas3.place(x=800,y=210)
# le PAS se changement d'image
v = DoubleVar()
horizontal_pas = tkinter.Scale(window,variable = v, orient = HORIZONTAL, from_ = 0, to = 255, bd = 0, fg = '#B20837', bg="#f1f1f1",font = 'bolder',command = thre)
horizontal_pas.place(x = 600,y=510)
zero_label = tkinter.Label(window, text = "0", fg = '#F3B000',bg="#f1f1f1", font = 'bold')
zero_label.place(x = 575,y = 530)
pas_text = tkinter.Label(window, text = "Step", font = "bold",bg="#f1f1f1", fg = '#B20837')
pas_text.place(x = 630,y=550)
label_255 = tkinter.Label(window, text = "255", fg = '#F3B000',bg="#f1f1f1", font = 'bold')
label_255.place(x=715,y=530)
label_copy = tkinter.Label(window, text = "@All right reserved-ENSA SAFI",bg="#f1f1f1")
label_copy.place(x=555,y=620)

window.resizable(0,0)
window.mainloop()

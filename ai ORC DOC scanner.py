from tkinter import *
from PIL import ImageTk,Image
import pytesseract
import cv2
import playsound
from tkinter import filedialog

window=Tk()
window.geometry("1200x550")
window.title("my scanner")
window.configure(bg="turquoise")

#this revoes the maximixe button
window.resizable(0,0)

#load image
img=cv2.imread("background.jpg")

def displayImage(img):
    cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    img = img.resize((400, 400))
    dispImage = ImageTk.PhotoImage(img)
    panel.configure(image=dispImage)
    panel.image=dispImage


def OpenImg():
    global img
    imgName=filedialog.askopenfilename(title='open')
    if imgName:
        img = cv2.imread(imgName)
        displayImage(img)
        txt.delete("1.0",END)

def ScanImg():
    global img
    from playsound import playsound
    playsound('scanner.mp3')
    text = pytesseract.image_to_string(img, lang = 'eng')
    txt.insert(END, text)





def SaveTxt():
    #"""Save the current file as a new file."""
    filepath = filedialog.asksaveasfilename(defaultextension="txt")
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt.get("1.0",END)
        output_file.write(text)





#gui
panel=Label(window,bg="black")
panel.grid(row=0,rowspan=12,padx=40,pady=30)
displayImage(img)

button_open=Button(window,text="OPEN",width=25,command=OpenImg,bg="dodger blue",fg="white")
button_open.grid(row=13)

button_scan=Button(window,text="TEXT SCAN",width=25,command=ScanImg,bg="dodger blue",fg="white")
button_scan.grid(row=13,column=1)


button_save=Button(window,text="SAVE",width=25,command=SaveTxt,bg="dodger blue",fg="white")
button_save.grid(row=13,column=2)

txt=Text(window,bg="white")
txt.grid(row=0,column=1,columnspan=2,rowspan=12,padx=40,pady=30)

window.mainloop()















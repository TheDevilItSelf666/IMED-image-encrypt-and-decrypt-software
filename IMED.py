from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("520x400")
root.minsize(520,400)



root.title("IMED")
text1=Label(text="Enter the key before selecting the image and key should be +ve integer",background="orange",relief=SUNKEN,foreground="white",font=("comicsamsms",11,"bold"))
text1.pack()


photo=PhotoImage(file="im.png")
photo_label=Label(image=photo)
photo_label.pack()


def encrypt_image():
    file1 =filedialog.askopenfile(mode='r',filetypes=[('jpg file','*.jpg'),('png file','*.png')])
    if file1 is not None:
   
        file_name=file1.name
        print(file_name)
        key = entry1.get(1.0,END)
        print(file_name,key)
        fi=open(file_name,'rb')
        image = fi.read()
        fi.close()
        image=bytearray(image)
        for index,values in enumerate(image):
            image[index] = values^int(key)
        fi1=open(file_name,'wb')
        fi1.write(image)
        fi1.close()


def decrypt_image():
    file1 =filedialog.askopenfile(mode='r',filetypes=[('jpg file','*.jpg'),('png file','*.png')])
    if file1 is not None:
   
        file_name=file1.name
        print(file_name)
        key = entry1.get(1.0,END)
        print(file_name,key)
        fi=open(file_name,'rb')
        image = fi.read()
        fi.close()
        image=bytearray(image)
        for index,values in enumerate(image):
            image[index] = values^int(key)
        fi1=open(file_name,'wb')
        fi1.write(image)
        fi1.close()




b1=Button(root,text="Encrypt",background="orange",command=encrypt_image ,  height= 2 ,width=8)
b1.place(x =130,y=145)

b2=Button(root,text="Decrypt",background="orange",command=decrypt_image ,height= 2 ,width=8)
b2.place(x=335,y=145)

entry1=Text(root,background="grey",height=1,width=15)
entry1.place(x=210,y=290)

text2=Label(text="KEY :",background="orange",foreground="white",height=1)
text2.place(x=255,y=260)
root.mainloop()

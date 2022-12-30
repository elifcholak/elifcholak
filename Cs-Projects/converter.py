from sqlite3 import Row
from tkinter import *
from tkinter import ttk
import codecs
import binascii
import random
import customtkinter


mainroot = customtkinter.CTk()
mainroot.title("Computer Science Education System")
Label(mainroot, text="Data Management").place(x=200, y=50, height = 50, width = 150)
Label(mainroot, text="Click here to convert").place(x=60, y=160, width = 155, height= 40)
Label(mainroot, text="Click here For Binary calculations").place(x=310, y=160, width = 190, height= 40)
mainroot.geometry('600x600')



def openConvWindow():
    root = customtkinter.CTkToplevel(mainroot)
#root = customtkinter.CTk()
    root.title("ASCII Hex Denary Converter")
    root.geometry("600x600")

    RGRAY = '#10121f'
    new_c = "forestgreen"
    title_bar = Frame(root, bg="#10121f", relief='raised', bd=0,highlightthickness=0)

    customtkinter.set_appearance_mode("Dark") 
    #customtkinter.set_default_color_theme("darkblue") 

    def convertvar():
        
        
        #print(clicked_1.get(), clicked_2.get())
        if clicked_1.get() == "Hexadecimal" and clicked_2.get() == "Denary":
            denaryVal = int(inputEntry.get(),16)
            Label(root, text=str(inputEntry.get()) + " =" + str(denaryVal)).place(x=40, y=400)

        elif clicked_1.get() == "Denary" and clicked_2.get() == "Hexadecimal":
            denvar = int(inputEntry.get())
            denToHex = hex(denvar)
            denToHex = denToHex[2:]
            Label(root, text=str(inputEntry.get()) + " =" + str(denToHex)).place(x=40, y=420) 
        
        elif clicked_1.get() == "ASCII" and clicked_2.get() == "Denary":
            character = inputEntry.get()
            if len(character) > 1:
                win = Toplevel(root)
                win.geometry("500x150")

                for ch in character:
                    Label(win, text=ch + '=' + str(ord(ch))).pack(padx=0)
                    print(ch + '=' + str(ord(ch)))

            elif len(character) == 1:
                for ch in character:
                    Label(root, text=ch + '=' + str(ord(ch))).place(x=40, y=440)
                    print(ch + '=' + str(ord(ch)))
                


        elif clicked_1.get() == "Denary" and clicked_2.get() == "ASCII":
            denaryval = int(inputEntry.get())
            denaryval = chr(denaryval)
            Label(root, text=str(inputEntry.get()) + " =" + denaryval).place(x=40, y=460) 
        
        elif clicked_1.get() == "ASCII" and clicked_2.get() == "Hexadecimal":
            asciiVal = inputEntry.get().encode('UTF-8')
            asciiVal = asciiVal.hex()
            Label(root, text=str(inputEntry.get()) + " =" + str(asciiVal)).place(x=40, y=480) 

        elif clicked_1.get() == "Hexadecimal" and clicked_2.get() == "ASCII":
            
            hexvalue = inputEntry.get()
            print(hexvalue)
            byte_array = bytearray.fromhex(hexvalue)
            byte_array = byte_array.decode()
            Label(root, text=str(inputEntry.get()) + " =" + str(byte_array)).place(x=40, y=500) 

        elif clicked_1.get() == "ASCII" and clicked_2.get() == "Binary":
            Binary = binascii.a2b_uu(inputEntry.get())
            byte_array = inputEntry.get().encode()
            binary_int = int.from_bytes(byte_array, "big")
            binary_string = bin(binary_int)
            print(binary_string)
            binary_string = binary_string[2:]
            Label(root, text=str(inputEntry.get()) + " =" + str(binary_string)).place(x=40, y=520) 

        elif clicked_1.get() == "Binary" and clicked_2.get() == "ASCII":
            binary_int = int(inputEntry.get(), 2);
            byte_number = binary_int.bit_length() + 7 // 8
            binary_array = binary_int.to_bytes(byte_number, "big")
#############################################################

            decoded = str(binary_array.decode())
            Label(root, text= decoded).place(x =40, y = 520)
            print(decoded)
            def outputlabel():
                Label(root, text="binary to ascii = " + decoded).place(x=40, y=540) 
            outputlabel()
            #Label(root, text="binary to ascii = " + decoded).place(x=40, y=540) 
            

        else:
            newWindow = Toplevel(root)
            newWindow.geometry("500x100")
            customtkinter.set_appearance_mode("Dark") 
            firstOp = clicked_1.get()
            secondOp = clicked_2.get()
            Label(newWindow,text=str(firstOp) + " To " + str(secondOp) + " conversion isn't available").pack()




    wrapper = LabelFrame(root, text="Input Field",height=120, width=150,background="#222325", fg="white",font=20)
    wrapper.place(x=30,y=30, height=300, width=530)


    inputLabel = Label(wrapper, text="Your Input",background="#222325",fg="white",font=10).place(x=20,y=40)
    inputEntry = Entry(wrapper, textvariable="Inputentry")
    inputEntry.place(x=125,y=40, height=30)
    options_1 = [
        "Choose The Language",
        "ASCII",
        "Hexadecimal",
        "Denary",
        "Binary"
        
    ]

    clicked_1 = StringVar()
    clicked_1.set(options_1[0])

    drop_1 = OptionMenu(wrapper,clicked_1,*options_1)
    drop_1.config(bg="#222325")
    drop_1.config(fg="white")
    drop_1.place(x=150,y=120)
    optionLabel1 = Label(wrapper, text="Convert From",background="#222325",fg="white",font=10).place(x=20,y=125)

    options_2 = [
        "Choose The Language",
        "ASCII",
        "Hexadecimal",
        "Denary",
        "Binary"
    ]


    clicked_2 = StringVar()
    clicked_2.set(options_2[0])

    drop_2 = OptionMenu(wrapper,clicked_2,*options_2)
    drop_2.config(bg="#222325")
    drop_2.config(fg="white")


    drop_2.place(x=150,y=170)
    optionLabel2 = Label(wrapper, text="Convert To",background="#222325",fg="white",font=10).place(x=20,y=175)

    ConvertLabel = Label(wrapper, text="Press to Convert", background="#222325",fg="white",font=10).place(x=20,y = 215)
    ConvertButton = customtkinter.CTkButton(wrapper, text="Convert",command=convertvar,border_width=2, 
                                                border_color=new_c, 
                                                hover_color=new_c).place(x = 150, y = 170,width=120)

    wrapper2 = LabelFrame(root, text="Output Field",height=220, width=530,background="#222325", fg="white",font=20)
    wrapper2.place(x=30,y=350, )

    ##Label(root,text="Made by:Enes Ozdemir").place(x=40, y=580)
    Label(root,text="Base Converter", background="#222325", fg="white", font=24).place(x=240, y=10)

def openCalWindow():        

    root2 = customtkinter.CTkToplevel(mainroot)
    root2.geometry("600x600")
    inputLabel = Label(root2, text="Your Input",background="#222325",fg="white",font=10).place(x=20,y=40)
    a = Entry(root2, textvariable="a")
    a.place(x=125,y=40, height=30)

    b = Entry(root2, textvariable="b")
    b.place(x=125,y=100, height=30)

    
    #am = a.get()
    #bm = b.get()
    
    
    def openConvWindows():
        sum = bin(int(a.get(), 2) + int(b.get(), 2))
        Label(root2, text= sum[2:], background="#222325", fg="white", font=24).place(x=120, y=160)
        print(sum[2:])
        

    findmat = customtkinter.CTkButton(root2, text="Add the Data", command=openConvWindows,border_width=2, 
                                                border_color="forestgreen", 
                                                hover_color="forestgreen").place(x = 100, y = 170,width=160)
    
    
    ##a = input("enter Your set of Binary ")
    #b = input("enter Your set of Binary ") 
    
    
    
    #Label(root2, text= am, background="#222325", fg="white", font=24).place(x=240, y=10)
    # Calculating binary value using function
    
 
    # Printing result

    print(sum[2:])

ConversionButton = customtkinter.CTkButton(mainroot, text="Data conversion", command=openConvWindow,border_width=2, 
                                                border_color="forestgreen", 
                                                hover_color="forestgreen").place(x = 45, y = 170,width=160)

BinaryAddition = customtkinter.CTkButton(mainroot, text="Data calculation", command=openCalWindow,border_width=2, 
                                                border_color="forestgreen", 
                                                hover_color="forestgreen").place(x = 250, y = 170,width=160)
mainroot.mainloop()


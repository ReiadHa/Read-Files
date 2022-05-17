import yaml
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo
with open("C:/Users/Riad/OneDrive - Da Vinci College/A Mbo4/Git/Read-Files/settings.yml", "r") as file:
    data = yaml.safe_load(file)

val = [(f'{i}  :    {data[i]}') for i in data]

def Price(clik):
    global data
    if clik == True:
        showinfo(title="Prijzen",message= '\n'.join(val))
    elif clik == False:
        pass
    

def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()
      
def zakelijk():
    clear_frame()
    Liter = tk.Button(frame,text = f'1 Liter ijs :\n{data["liter"]}' ,font=30,bg='lightblue')
    Liter.place(rely = 0.5, relx= 0.5,anchor='center')
    
def particulier():
    global prijzenBut
    clear_frame()
    bakOfHorn()
    prijzenBut = tk.Button(window, text = 'Prijzen', font=('calibre',10, 'bold'),bg = 'black', fg = 'white',width=10)
    prijzenBut.place(rely=0.9,relx=0.10,anchor='center')
    prijzenBut.config(command=lambda: Price(True))

def bestellen():
    global antwoord1
    antwoord1 = tk.IntVar()
    vraag = tk.Label(frame,text = f'hoeveel bestellingen wilt u maken? ',bg='black' ,fg='white',width=30,height=2,font=15)
    vraag.place(rely = 0.5, relx= 0.5,anchor='center')
    antwoord = tk.Entry(frame,width=10,textvariable=antwoord1)
    antwoord.place(rely = 0.6, relx= 0.5,anchor='center')
    antButton = tk.Button(frame,text = 'submit',bg='lightblue',width=10,height=2,command=submit)
    antButton.place(rely = 0.67, relx= 0.5,anchor='center')
    
def submit():
    clear_frame()
    smaken()
    
def bakOfHorn():
    clear_frame()
    but1 = tk.Button(frame,text = f'Hoorntje',bg='lightblue',font=30,width=10,height=2,command=lambda: smaken(True))
    but1.place(rely = 0.3, relx= 0.5,anchor='center')
    
    but2 = tk.Button(frame,text = f'Bakje',bg='lightblue',font=30,width=10,height=2,command=lambda: smaken(False))
    but2.place(rely = 0.5, relx= 0.5,anchor='center')

def smaken(Wat) : 
    global smakenList, intaantal1,intaantal2,intaantal3,aantal2,aantal3,aantal1  
    clear_frame()
    smaken = ['choco','aardbei','banaan']
    TasteRely = 0.22
    taste = Label(frame,text = f'smaken',bg='black' ,fg='white',width=45,height=2,font=15)
    taste.place(rely = 0.1, relx= 0.1,anchor='nw')
    hoeveelBol = tk.Label(frame,text='Hoeveel bolletjes wilt u',bg='black' ,fg='white',width=45,height=2,font=15)
    hoeveelBol.place(rely = 0.2, relx= 0.1,anchor='nw')
    if Wat == True:
        aantaldef(True)
        but1 = tk.Button(frame,text = f'{smaken[0]}',bg='lightblue',font=30,width=10,height=2,command=lambda: smaakaantalHorn(smaken[0]))
        but1.place(rely = 0.3, relx= TasteRely,anchor='nw')
        
        but2 = tk.Button(frame,text = f'{smaken[1]}',bg='lightblue',font=30,width=10,height=2,command=lambda: smaakaantalHorn(smaken[1]))
        but2.place(rely = 0.3, relx= TasteRely+0.2,anchor='nw')
        
        but3 = tk.Button(frame,text = f'{smaken[2]}',bg='lightblue',font=30,width=10,height=2,command=lambda: smaakaantalHorn(smaken[2]))
        but3.place(rely = 0.3, relx= TasteRely+0.4,anchor='nw')
        
    elif Wat == False:
        aantaldef(False)
        but1 = tk.Button(frame,text = f'{smaken[0]}',bg='lightblue',font=30,width=10,height=2,command=lambda: smakenBakje(smaken[0]))
        but1.place(rely = 0.3, relx= TasteRely,anchor='nw')
        
        but2 = tk.Button(frame,text = f'{smaken[1]}',bg='lightblue',font=30,width=10,height=2,command=lambda: smakenBakje(smaken[1]))
        but2.place(rely = 0.3, relx= TasteRely+0.2,anchor='nw')
        
        but3 = tk.Button(frame,text = f'{smaken[2]}',bg='lightblue',font=30,width=10,height=2,command=lambda: smakenBakje(smaken[2]))
        but3.place(rely = 0.3, relx= TasteRely+0.4,anchor='nw')
        
def smakenBakje(soort):
    global intaantal1,intaantal2,intaantal3,aantal2,aantal3,aantal1
    alles= intaantal1+intaantal2+intaantal3
    if alles <10:
        if soort == 'choco':
            intaantal1 += 1
            aantal1.config(text=f'{intaantal1}')
            print(intaantal1,'test1')
        elif soort == 'aardbei':
            intaantal2 += 1
            print(intaantal2,'test2')
            aantal2.config(text=f'{intaantal2}')
            
        elif soort == 'banaan':
            intaantal3 += 1
            aantal3.config(text=f'{intaantal3}')
            print(intaantal3,'test3') 
    volgende()
def smaakaantalHorn(soort):
    global intaantal1,intaantal2,intaantal3,aantal2,aantal3,aantal1
    alles= intaantal1+intaantal2+intaantal3
    if alles < 5:
        if soort == 'choco':
            intaantal1 += 1
            aantal1.config(text=f'{intaantal1}')
            print(intaantal1,'test1')
            
        elif soort == 'aardbei':
            intaantal2 += 1
            print(intaantal2,'test2')
            aantal2.config(text=f'{intaantal2}')
            
        elif soort == 'banaan':
            intaantal3 += 1
            aantal3.config(text=f'{intaantal3}')
            print(intaantal3,'test3')   
    volgende()


    
def aantaldef(wat):
    global intaantal1,intaantal2,intaantal3,aantal2,aantal3,aantal1
    bak = 0
    horn = 0
    intaantal1 = 0
    intaantal3 = 0
    intaantal2 = 0
    if wat == True:
        print('test')
        horn += 1
        aantal1 = tk.Label(frame,text=f'{intaantal1}',bg='black' ,fg='white',width=10,height=2,font=15)
        aantal1.place(rely = 0.45, relx= 0.22,anchor='nw')

        aantal2 = tk.Label(frame,text=f'{intaantal2}',bg='black' ,fg='white',width=10,height=2,font=15)
        aantal2.place(rely = 0.45, relx= 0.42,anchor='nw')

        aantal3 = tk.Label(frame,text=f'{intaantal3}',bg='black' ,fg='white',width=10,height=2,font=15)
        aantal3.place(rely = 0.45, relx= 0.62,anchor='nw')
        
    elif wat == False:
        print('test')
        bak  += 1
        aantal1 = tk.Label(frame,text=f'{intaantal1}',bg='black' ,fg='white',width=10,height=2,font=15)
        aantal1.place(rely = 0.45, relx= 0.22,anchor='nw')

        
        aantal2 = tk.Label(frame,text=f'{intaantal2}',bg='black' ,fg='white',width=10,height=2,font=15)
        aantal2.place(rely = 0.45, relx= 0.42,anchor='nw')

        
        aantal3 = tk.Label(frame,text=f'{intaantal3}',bg='black' ,fg='white',width=10,height=2,font=15)
        aantal3.place(rely = 0.45, relx= 0.62,anchor='nw')
                
def volgende():
    but1 = tk.Button(frame,text = 'Volgende',bg='lightblue',font=30,width=10,height=2,command=lambda: rekenen())
    but1.place(rely = 0.9, relx= 0.9,anchor='center')

def rekenen():
    for i,v in enumerate(data):   
        print(i , v)
        
        
window = tk.Tk()
window.geometry('600x600')
window.title('Papigelati')



frame = Frame(window)
frame.config(bg='red')
frame.pack(side="top", expand=True, fill="both")

welkomLbl = tk.Label(window, text = 'Welkom bij PapiGelati', font=('calibre',20, 'bold'),bg = 'black', fg = 'white',width=50)
welkomLbl.place(rely=0.04,relx=0.5,anchor='center')

butZaklijk = tk.Button(frame, text = 'Zaklijk', font=('calibre',20, 'bold'),bg = 'lightblue', fg = 'black',width=15,height=5,command=zakelijk)
butZaklijk.place(rely=0.4,relx=0.25,anchor='center')

btuParticu = tk.Button(frame, text = 'Particulier', font=('calibre',20, 'bold'),bg = 'lightblue', fg = 'black',width=15,height=5,command=particulier)
btuParticu.place(rely=0.4,relx=0.75,anchor='center')

window.mainloop()








# aantal = tk.Label(frame,textvariable = aantalText,bg='black' ,fg='white',width=5,height=2,font=15)
# aantal.place(rely = 0.45, relx= TasteRely +0.04,anchor='nw')
# smakenList.append(aantal)
# smakenList[0].config(Command=smaakaantal('choco'))
# smakenList[1].config(Command=smaakaantal('aardbei'))
# smakenList[2].config(Command=smaakaantal('banaan'))


# for i in range(3):
#     smaak = tk.Button(frame,text = f'{smaken[i]}' ,font=30,bg='lightblue',width=10,height=4,command=smaakaantal(smaken[i]))
#     smaak.place(rely =0.3 , relx= TasteRely,anchor='nw')
#     TasteRely += 0.2
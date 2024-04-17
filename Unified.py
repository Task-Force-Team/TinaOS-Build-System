import os 
import sys
from tkinter import filedialog
import shutil


class menu:
    def __init__(self):
        self.dir = ''
        a = open(r"data/Maintainer.dat", "r")
        self.maintainer = a.read()
        if self.maintainer == 'Unknown':
            self.maintainer = 'Dont forget to set your name!'
        self.mods = 'TinaOS_Root'
        self.app_title = 'Welcome to TinaOS Auto Builder!'
        self.app_body = f'Choose one option {self.maintainer}'
        self.draw_mainmenu()
    def sel_name(self):
        print('Ok enter the name:')
        name = input("#: ")
        ag = open('data/Maintainer.dat', 'w')
        ag.write(name)
        print(f'Success! your name: {name}')
    def build(self):
        if self.maintainer == '\nDont forget to set your name!':
            print('looks like there is no name saved for maintainer name\nplease select one and try again')
            return
        else:
            #shutil.copy2(self.dir, 'super.img')
            #os.system(f'simg2img.exe super.img super.ext4.img')
            os.system(f'powershell ./lpunpack.py --slot=0 .\\super.img .\\partitions\\')
    def select_super(self):
        print("Passed")
        self.dir = filedialog.askopenfilename()
        if self.dir == '' or None:
            print('Error!: Please select a super.img, except i cant build!')
            return 1
        print(self.dir)
    def draw_mainmenu(self):
        while True:
            print('############################################')
            print(f'# -= {self.app_title}')
            print(f'# -= {self.app_body}')
            print('############################################')
            print('# -= Options:')
            print('# -= 1.Select a super.img')
            print('# -= 2.Enter a maintainer name')
            print('# -= 3.Build the TinaOS! (Requires ')
            print("# Selecting super.img of a hyperos)")
            print('# -= 4.Exit')
            print('############################################')            
            choice = input('Okey select a option!')
            a = self.goif(choice)
            if a == 'hes a dumbass, even dont selected correct option!':
                print("Invalid option.")
                return
            if choice == 4: break
    def goif(self, ch):
        ch = int(ch)
        if ch == 1:
            self.select_super()
        elif ch == 2:
            self.sel_name()
        elif ch == 3:
            self.build()
        elif ch == 4:
            pass
        else:
            return 'hes a dumbass, even dont selected correct option!'

if __name__=="__main__":
    JustSomeClass = menu()
    JustSomeClass.draw_mainmenu()
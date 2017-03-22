# -*- coding: utf-8 -*-

from Tkinter import *
import tkFileDialog

class Choise:
    def __init__(self, parent, label):
        self.label = label
        self.myParent = parent
#        self.topCont = Frame(parent)
#        self.topCont.pack()
        self.choiseCont = Toplevel(parent)
        self.choiseCont.title('Choise')
#        self.choiseCont.pack()

        button_width = 10

        button_padx = '2m'
        button_pady = '1m'

        buttons_frame_padx = '3m'
        buttons_frame_pady = '2m'
        buttons_frame_ipadx = '3m'
        buttons_frame_ipady = '1m'
#---------------container setting-----------
        self.controlCont1 = Frame(self.choiseCont)
        self.controlCont1.pack(
            side = TOP,
            ipadx = buttons_frame_ipadx,
            ipady = buttons_frame_ipady,
            padx = buttons_frame_padx,
            pady = buttons_frame_pady
            )

        self.controlCont2 = Frame(self.choiseCont)
        self.controlCont2.pack(
            side = TOP,
            ipadx = buttons_frame_ipadx,
            ipady = buttons_frame_ipady,
            padx = buttons_frame_padx,
            pady = buttons_frame_pady
            )
#--------------control container 1--------
        self.reportText = Text(self.controlCont1)
        self.reportText.configure(
            padx = button_padx,
            pady = button_pady,
            height = 16
            )

        self.reportText.pack(side = LEFT)
        self.reportText.insert(END, self.label)

#--------------control container 1--------
        self.oklButton = Button(self.controlCont2, command = self.ok)
        self.oklButton.configure(
            text = 'OK',
            width = button_width,
            padx = button_padx,
            pady = button_pady
            )
        self.oklButton.pack(side = LEFT)

        self.noButton = Button(self.controlCont2, command = self.no)
        self.noButton.configure(
            text = 'NO',
            width = button_width,
            padx = button_padx,
            pady = button_pady
            )
        self.noButton.pack(side = RIGHT)

        self.choise = None

    def ok(self):
        self.choise = True
        self.choiseCont.destroy()
    def no(self):
        self.choise = False
        self.choiseCont.destroy()

class InitialPar:
    def __init__(self, parent, filePath, settingFileList):
        self.filePath = filePath
        self.tempFilePath = filePath
        self.settFileList= settingFileList
        self.settingFile = settingFileList[0]
        self.savingFile = settingFileList[0][:2] + ' summary.txt'

#        self.filePath = r'D:\Processed_MicrarrayRawData'
#        self.tempFilePath = r'D:\Processed_MicrarrayRawData'
#        self.settingFile = 'All_DataSet.txt'
#        self.savingFile = 'All_DataSet summary.txt'

        self.myParent = parent
        self.initCont = Toplevel(parent)
        self.initCont.title ('Initialize')


        self.cont1 = Frame(self.initCont)
        self.cont1.pack(side = TOP, fill = X)
        self.cont2 = Frame(self.initCont)
        self.cont2.pack(side = TOP)
        self.cont3 = Frame(self.initCont)
        self.cont3.pack(side = TOP)
        self.cont4 = Frame(self.initCont)
        self.cont4.pack(side = TOP)
        self.cont5 = Frame(self.initCont)
        self.cont5.pack(side = TOP)

        self.packOpt = {'side':LEFT, 'padx':5, 'pady':5}

        Button(self.cont1, text = 'Dir', width = 6, command = self.openDir).pack(**self.packOpt)
        self.pathEntry = Entry(self.cont1)
        self.pathEntry.pack(side = RIGHT, padx = 5, pady = 5)
        self.pathEntry.insert(END, self.filePath)

        Label(self.cont2, text = 'SettingFile').pack(**self.packOpt)
        self.settingFileEntry = Entry(self.cont2)
        self.settingFileEntry.pack(**self.packOpt)
        self.settingFileEntry.insert(END, self.settingFile)

        Label(self.cont3, text = 'SettingFile\nPlease Double Click').pack(**self.packOpt)
        scrollBar = Scrollbar(self.cont3)
        scrollBar.pack(side=RIGHT, fill=Y)
        self.settingFileLB = Listbox(self.cont3, selectmode=SINGLE)
        self.settingFileLB.pack(**self.packOpt)
        scrollBar.config(command=self.settingFileLB.yview)
        self.settingFileLB.config(yscrollcommand=scrollBar.set)
        for item in self.settFileList:
            self.settingFileLB.insert(END, item)
        self.settingFileLB.bind('<Button-1>', self.createSavingFile)

        Label(self.cont4, text = 'SavingFile').pack(**self.packOpt)
        self.savingFileEntry = Entry(self.cont4)
        self.savingFileEntry.pack(**self.packOpt)
        self.savingFileEntry.insert(END, self.savingFile)

        Button(self.cont5, text = 'OK', width = 8, command = self.ok).pack(side = LEFT,  padx = 5, pady = 5)
        Button(self.cont5, text = 'NO', width = 8, command = self.no).pack(side = RIGHT, padx = 5, pady = 5)

    def openDir(self):
        self.filePath = tkFileDialog.askdirectory(initialdir = self.filePath, title = 'Choose the dir of the dataSet')
        self.pathEntry.delete(0, END)
        self.pathEntry.insert(END, self.filePath)

    def getSettingFile(self):
        self.settingFile = self.settingFileEntry.get().strip()
    def createSavingFile(self, event):
        try:
            secondIndex = self.settingFileLB.curselection()[0]
            self.savingFile = self.settFileList[int(secondIndex)]
        except IndexError:
            self.savingFile = self.settFileList[0]
        self.settingFileEntry.delete(0, END)
        self.settingFileEntry.insert(END, self.savingFile)
        self.savingFileEntry.delete(0, END)
        self.savingFileEntry.insert(END, self.savingFile[:2] + ' summary.txt')
    def getSavingFile(self):
        self.savingFile = self.savingFileEntry.get().strip()
    def ok(self):
        self.filePath = self.pathEntry.get().strip()
        self.getSettingFile()
        self.getSavingFile()
        self.initCont.destroy()
    def no(self):
        self.initCont.destroy()

class TipButton(Button):
    def __init__(self,parent=None,tip='',**kw):
        Button.__init__(self,parent,kw)
        self.bind('<Enter>',self._delayedshow)
        self.bind('<Button-1>',self._leave)
        self.bind('<Leave>',self._leave)

        self.frame = Toplevel(self,bd=1,bg="black")
        self.frame.withdraw()
        self.frame.overrideredirect(1)
        self.frame.transient()

        self.tipDelay = 800
        l=Label(self.frame,text=tip,bg="yellow",justify='left')
	l.update_idletasks()
        l.pack()
	l.update_idletasks()
        self.tipwidth = l.winfo_width()
        self.tipheight = l.winfo_height()

    def _delayedshow(self,event):
        self.focus_set()
        self.request=self.after(self.tipDelay,self._show)


    def _show(self):
        self.update_idletasks()
        FixX = self.winfo_rootx()+self.winfo_width()
        FixY = self.winfo_rooty()+self.winfo_height()
        if FixX + self.tipwidth > self.winfo_screenwidth():
            FixX = FixX-self.winfo_width()-self.tipwidth
        if FixY + self.tipheight > self.winfo_screenheight():
            FixY = FixY-self.winfo_height()-self.tipheight
        self.frame.geometry('+%d+%d'%(FixX,FixY))
        self.frame.deiconify()
#       print self.frame.geometry()
#	print self.winfo_screenwidth()


    def _leave(self,event):
        self.frame.withdraw()
        self.after_cancel(self.request)

class SingleInput:
    '''Type i:int, f:float, s:string
    '''
    def __init__(self, parent, initParameter, Type = 'i', info = 'Input'):
        self.initParameter = str(initParameter)
        self.parameter = initParameter
        self.info = info
        self.Type = Type

        self.myParent = parent
        self.initCont = Toplevel(parent)
        self.initCont.title ('Input parameter')

        self.cont1 = Frame(self.initCont)
        self.cont1.pack(side = TOP, fill = X)

        self.cont2 = Frame(self.initCont)
        self.cont2.pack(side = TOP)

        self.packOpt = {'side':LEFT, 'padx':5, 'pady':5}

        Label(self.cont1, text = self.info).pack(**self.packOpt)
        self.settingFileEntry = Entry(self.cont1)
        self.settingFileEntry.pack(**self.packOpt)
        self.settingFileEntry.insert(END, self.initParameter)

        Button(self.cont2, text = 'OK', width = 8, command = self.ok).pack(side = LEFT,  padx = 5, pady = 5)
        Button(self.cont2, text = 'NO', width = 8, command = self.no).pack(side = RIGHT, padx = 5, pady = 5)


    def getParameter(self):
        if self.Type == 'i':
            self.parameter = int(self.settingFileEntry.get().strip())
        elif self.Type == 'f':
            self.parameter = float(self.settingFileEntry.get().strip())
        else:
            self.parameter = self.settingFileEntry.get().strip()

    def ok(self):
        self.getParameter()
        self.initCont.destroy()
    def no(self):
        self.initCont.destroy()

class test:
    def __init__(self, parent):
        self.myParent = parent
        self.topCont = Frame(parent)
        self.topCont.pack()

        self.check = Checkbutton(self.topCont, command = self.ok)
        self.check['text'] = 'use'
        self.check.pack()

        optionList = ('a', 'b', 'c')
        self.v = StringVar()
        self.v.set(optionList[0])
        self.option = OptionMenu(self.topCont, self.v , *optionList)
        self.option['text'] = 'choose'
        self.option.pack()



    def ok(self):
        self.choise = True
        self.optionChoise = self.v.get()
        self.myParent.destroy()
if __name__ == '__main__':
    def testInitialPar(root):
        settingFileList = ['AFSet.txt', 'CSSet.txt', 'OTSet.txt', 'SGSet.txt', 'WSSet.txt', 'All_DataSet.txt']
        myChoise = InitialPar(root, r'D:\Processed_MicrarrayRawData', settingFileList)
        root.mainloop()
        print myChoise.filePath
        print myChoise.settingFile
        print myChoise.savingFile

    def testSingleInput(root):
        myChoise = SingleInput(root, 'input', 'hello', 's')
        root.mainloop()
        print myChoise.parameter



    root = Tk()

#    testInitialPar(root)
    testSingleInput(root)


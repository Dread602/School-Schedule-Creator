from Tkinter import *
import itertools
import urllib2
import linecache
from PIL import ImageGrab
#What's left:Put the save icon command
#Lower-Case function names and global variables
#Capitalize constants



class MainWindow():
    #Command functions
    def PrintName(self):
        global TheName
        TheName = UserName.get()
        Window1.destroy()
        self.PostLogIn()

    def ReturnToLogIn(self):
        Window2.destroy()
        self.PreLogIn()
    def UserNameStatus(self):
        print UserName.get()
    def Refresh(self):
        Window2.destroy()
        self.PostLogIn()
        
    
    #First interface function
    def PreLogIn(self):
        global Window1
        Window1 = Tk()
        Window1.wm_title('RSS School Schedules')
        Window1.resizable(False, False)
        Window1.iconbitmap(default='ProgramIcon.ico')
        global UserName
        UserName = Entry(Window1)
        LoginButton = Button(text = "Login", command = self.PrintName)
        UserName.grid(row = 0, column = 1)
        LoginButton.grid(row = 0, column = 2)
        UserNameLabel = Label(text = "Username")
        UserNameLabel.grid(row = 0, column = 0)
        Window1.mainloop()
        

    #Second interface function
    def PostLogIn(self):
    #MenuBar
        global Window2
        Window2 = Tk()
        Window2.wm_title('RSS School Schedules')
        Window2.resizable(False, False)
        Window2.geometry("938x590")
        Window2.iconbitmap(default='ProgramIcon.ico')
        MainMenu = Menu(Window2)
        Window2.config(menu = MainMenu)
        Menu1 = Menu(MainMenu, tearoff = False)
        MainMenu.add_cascade(label = "Account Actions", menu = Menu1)
        Menu1.add_command(label = "Change User", command = self.ReturnToLogIn)
        
    #Toolbar and its icons
        ToolbarFrame = Frame(Window2, bd = 1, relief = RAISED)
        SaveImage = PhotoImage(file = "Save.gif")
        SaveButton = Button(ToolbarFrame, image = SaveImage, command = ImageGrab.grab().save("%s's Schedule.png" %TheName, "PNG"))
        SaveButton.pack(side = LEFT)
        RefreshImage = PhotoImage(file = "Refresh.gif")
        RefreshButton = Button(ToolbarFrame, image = RefreshImage, command = self.Refresh)
        RefreshButton.pack(side = LEFT)
        ToolbarFrame.pack(side = TOP, fill = X)
        
    #Status bar
        StatusbarFrame = Frame(Window2, bd = 1, relief = SUNKEN)
        StatusbarFrame.pack(side = BOTTOM, fill = X)
        StatusbarLabel = Label(StatusbarFrame, text = "Logged in as: %s" %TheName)
        StatusbarLabel.pack(side = LEFT)
        
    #URL reading:
        ScheduleData = urllib2.urlopen("http://m.uploadedit.com/ba3n/1451094812124.txt")
        Result = ScheduleData.readlines()
        ResultFine = Result
        ResultFineString1 = ResultFine[0].split(",")

        ResultFineString2 = ResultFine[1].split(",")

        ResultFineString3 = ResultFine[2].split(",")

        ResultFineString4 = ResultFine[3].split(",")

        ResultFineString5 = ResultFine[4].split(",")
        
        ResultFineString6 = ResultFine[5].split(",")

        
        A1 = ResultFineString1[0]
        A2 = ResultFineString1[1] 
        A3 = ResultFineString1[2]
        A4 = ResultFineString1[3]
        A5 = ResultFineString1[4]
        A6 = ResultFineString1[5]
        A7 = ResultFineString1[6]
        A8 = ResultFineString1[7]
        B1 = ResultFineString2[0]
        B2 = ResultFineString2[1]
        B3 = ResultFineString2[2]
        B4 = ResultFineString2[3]
        B5 = ResultFineString2[4]
        B6 = ResultFineString2[5]
        B7 = ResultFineString2[6]
        B8 = ResultFineString2[7]
        C1 = ResultFineString3[0]
        C2 = ResultFineString3[1]
        C3 = ResultFineString3[2]
        C4 = ResultFineString3[3]
        C5 = ResultFineString3[4]
        C6 = ResultFineString3[5]
        C7 = ResultFineString3[6]
        C8 = ResultFineString3[7]
        D1 = ResultFineString4[0]
        D2 = ResultFineString4[1]
        D3 = ResultFineString4[2]
        D4 = ResultFineString4[3]
        D5 = ResultFineString4[4] 
        D6 = ResultFineString4[5]
        D7 = ResultFineString4[6] 
        D8 = ResultFineString4[7]
        E1 = ResultFineString5[0]
        E2 = ResultFineString5[1]
        E3 = ResultFineString5[2]
        E4 = ResultFineString5[3]
        E5 = ResultFineString5[4]
        E6 = ResultFineString5[5]
        E7 = ResultFineString5[6]
        E8 = ResultFineString5[7]
        Date = ResultFineString6[0]
    #Schedule:
        ScheduleFrame = Frame(Window2)
        Empty = Label(ScheduleFrame ,text = "--------------", bg = "White", height = 5, width = 14)
        Empty.grid(row = 0, column = 1)        
        

        TheClassNoList = ['FirstClass', 'SecondClass', 'ThirdClass', 'FourthClass', 'FifthClass', 'SixthClass', 'SeventhClass', 'EighthClass']
        TheList3 = [1, 1, 1, 1, 1, 1, 1, 1]
        TheList4 = [2, 3, 4, 5, 6, 7, 8, 9]

        for a, b, c, d in zip(TheClassNoList, TheClassNoList, TheList3, TheList4):
            a = Label(ScheduleFrame, text = b, bg = "White", height = 5, width = 14)
            a.grid(row = c-1, column = d)
        
       
    #Sunday:
        Sunday = Label(ScheduleFrame ,text ="Sunday", bg = "White", height = 5, width = 14)
        Sunday.grid(row = 1, column = 1)
        
        TheList1A = ['LabelA1', 'LabelA2', 'LabelA3', 'LabelA4', 'LabelA5', 'LabelA6', 'Label A7', 'Label A8']
        TheList2A = [A1, A2, A3, A4, A5, A6, A7, A8]

        for a, b, c, d in zip(TheList1A, TheList2A, TheList3, TheList4):
            a = Label(ScheduleFrame, text = b, bg = "White", height = 5, width = 14)
            a.grid(row = c, column = d)

       
    #Monday:
        Monday = Label(ScheduleFrame, text = "Monday", bg = "White", height = 5, width = 14)
        Monday.grid(row = 2, column = 1)
        
        TheList1B = ['LabelB1', 'LabelB2', 'LabelB3', 'LabelB4', 'LabelB5', 'LabelB6', 'Label B7', 'Label B8']
        TheList2B = [B1, B2, B3, B4, B5, B6, B7, B8]
        
        for a, b, c, d in zip(TheList1B, TheList2B, TheList3, TheList4):
            a = Label(ScheduleFrame, text = b, bg = "White", height = 5, width = 14)
            a.grid(row = c+1, column = d)

        
   #Tuesday:
        Tuesday = Label(ScheduleFrame, text = "Tuesday", bg = "White", height = 5, width = 14)
        Tuesday.grid(row = 3, column = 1)    

        TheList1C = ['LabelC1', 'LabelC2', 'LabelC3', 'LabelC4', 'LabelC5', 'LabelC6', 'Label C7', 'Label C8']
        TheList2C = [C1, C2, C3, C4, C5, C6, C7, C8]
        
        for a, b, c, d in zip(TheList1C, TheList2C, TheList3, TheList4):
            a = Label(ScheduleFrame, text = b, bg = "White", height = 5, width = 14)
            a.grid(row = c+2, column = d)        

        
    #Wednesday:
        Wednesday = Label(ScheduleFrame, text = "Wednesday", bg = "White", height = 5, width = 14)
        Wednesday.grid(row = 4, column = 1)        

        TheList1D = ['LabelD1', 'LabelD2', 'LabelD3', 'LabelD4', 'LabelD5', 'LabelD6', 'Label D7', 'Label D8']
        TheList2D = [D1, D2, D3, D4, D5, D6, D7, D8]
        
        for a, b, c, d in zip(TheList1D, TheList2D, TheList3, TheList4):
            a = Label(ScheduleFrame, text = b, bg = "White", height = 5, width = 14)
            a.grid(row = c+3, column = d)        


    #Thursday:
        Thursday = Label(ScheduleFrame, text = "Thursday", bg = "White", height = 5, width = 14)
        Thursday.grid(row = 5, column = 1)

        TheList1E = ['LabelE1', 'LabelE2', 'LabelE3', 'LabelE4', 'LabelE5', 'LabelE6', 'Label E7', 'Label E8']
        TheList2E = [E1, E2, E3, E4, E5, E6, E7, E8]
        
        for a, b, c, d in zip(TheList1E, TheList2E, TheList3, TheList4):
            a = Label(ScheduleFrame, text = b, bg = "White", height = 5, width = 14)
            a.grid(row = c+4, column = d)        

 
        
        DateFrame = Frame(Window2)
        DateLabel = Label(DateFrame, text = "Date: %s"%Date, bg = "white", height = 3, width = 133)
        
        
        
        DateLabel.pack()
        ScheduleFrame.pack()
        DateFrame.pack() 
        Window2.mainloop()




Start = MainWindow()
Start.PreLogIn()

from Tkinter import *
import urllib2
import linecache
'''What's left:
-Put the save icon command
-Lower-Case function names and global variables
-Capitalize constants'''




class MainWindow():
    #Command functions
    def PrintName(self):
        global TheName
        #print UserName.get()
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
        Window2.geometry("938x548")
        Window2.iconbitmap(default='ProgramIcon.ico')
        MainMenu = Menu(Window2)
        Window2.config(menu = MainMenu)
        Menu1 = Menu(MainMenu, tearoff = False)
        MainMenu.add_cascade(label = "Account Actions", menu = Menu1)
        Menu1.add_command(label = "Change User", command = self.ReturnToLogIn)
        
    #Toolbar and its icons
        ToolbarFrame = Frame(Window2, bd = 1, relief = RAISED)
        SaveImage = PhotoImage(file = "Save.gif")
        SaveButton = Button(ToolbarFrame, image = SaveImage)
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
        ScheduleData = urllib2.urlopen("http://m.uploadedit.com/ba3n/1451050673276.txt")
        Result = ScheduleData.readlines()
        ResultFine = Result
        ResultFineString1 = ResultFine[0].split(",")
        #print ResultFineString1[0]

        ResultFineString2 = ResultFine[1].split(",")
        #print ResultFineString2[0]

        ResultFineString3 = ResultFine[2].split(",")
        #print ResultFineString3[0]

        ResultFineString4 = ResultFine[3].split(",")
        #print ResultFineString4[0]

        ResultFineString5 = ResultFine[4].split(",")
        #print ResultFineString5[0]

        '''IGNORE:Result = [line.split(',') for line in ScheduleData.readlines()]
        RefinedResult = Result[0]
        print RefinedResult
        '''
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
      
        #Schedule:
        NewFrame = Frame(Window2)
        
        
        
        Empty = Label(NewFrame ,text = "--------------", bg = "White", height = 5, width = 14)
        Empty.grid(row = 0, column = 1)

        FirstClass = Label(NewFrame, text ="First class", bg = "White", height = 5, width = 14)
        FirstClass.grid(row = 0, column = 2)

        SecondClass = Label(NewFrame ,text ="Second class", bg = "White", height = 5, width = 14)
        SecondClass.grid(row = 0, column = 3)

        ThirdClass = Label(NewFrame, text ="Third class", bg = "White", height = 5, width = 14)
        ThirdClass.grid(row = 0, column = 4)

        FourthClass = Label(NewFrame ,text ="Fourth class", bg = "White", height = 5, width = 14)
        FourthClass.grid(row = 0, column = 5)

        FifthClass = Label(NewFrame, text ="Fifth class", bg = "White", height = 5, width = 14)
        FifthClass.grid(row = 0, column = 6)

        SixthClass = Label(NewFrame, text ="Sixth class", bg = "White", height = 5, width = 14)
        SixthClass.grid(row = 0, column = 7)

        SeventhClass = Label(NewFrame, text ="Seventh class", bg = "White", height = 5, width = 14)
        SeventhClass.grid(row = 0, column = 8)

        EighthClass = Label(NewFrame, text ="Eigth class", bg = "White", height = 5, width = 14)
        EighthClass.grid(row = 0, column = 9)
        #Sunday:
        Sunday = Label(NewFrame ,text ="Sunday", bg = "White", height = 5, width = 14)
        Sunday.grid(row = 1, column = 1)

        labelA1 = Label(NewFrame, text = A1, bg = "White", height = 5, width = 14)
        labelA1.grid(row = 1, column = 2)

        labelA2 = Label(NewFrame ,text = A2, bg = "White", height = 5, width = 14)
        labelA2.grid(row = 1, column = 3)

        labelA3 = Label(NewFrame, text = A3, bg = "White", height = 5, width = 14)
        labelA3.grid(row = 1, column = 4)

        labelA4 = Label(NewFrame ,text = A4, bg = "White", height = 5, width = 14)
        labelA4.grid(row = 1, column = 5)

        labelA5 = Label(NewFrame, text = A5, bg = "White", height = 5, width = 14)
        labelA5.grid(row = 1, column = 6)

        labelA6 = Label(NewFrame, text = A6, bg = "White", height = 5, width = 14)
        labelA6.grid(row = 1, column = 7)

        labelA7 = Label(NewFrame, text = A7, bg = "White", height = 5, width = 14)
        labelA7.grid(row = 1, column = 8)

        labelA8 = Label(NewFrame, text = A8, bg = "White", height = 5, width = 14)
        labelA8.grid(row = 1, column = 9)
        #Monday:
        Monday = Label(NewFrame, text = "Monday", bg = "White", height = 5, width = 14)
        Monday.grid(row = 2, column = 1)

        LabelB1 = Label(NewFrame, text = B1, bg = "White", height = 5, width = 14)
        LabelB1.grid(row = 2, column = 2)        

        LabelB2 = Label(NewFrame, text = B2, bg = "White", height = 5, width = 14)
        LabelB2.grid(row = 2, column = 3)        

        LabelB3 = Label(NewFrame, text = B3, bg = "White", height = 5, width = 14)
        LabelB3.grid(row = 2, column = 4)        

        LabelB4 = Label(NewFrame, text = B4, bg = "White", height = 5, width = 14)
        LabelB4.grid(row = 2, column = 5)        

        LabelB5 = Label(NewFrame, text = B5, bg = "White", height = 5, width = 14)
        LabelB5.grid(row = 2, column = 6)        

        LabelB6 = Label(NewFrame, text = B6, bg = "White", height = 5, width = 14)
        LabelB6.grid(row = 2, column = 7)

        LabelB7 = Label(NewFrame, text = B7, bg = "White", height = 5, width = 14)
        LabelB7.grid(row = 2, column = 8)

        LabelB8 = Label(NewFrame, text = B8, bg = "White", height = 5, width = 14)
        LabelB8.grid(row = 2, column = 9)        
        #Tuesday:
        Tuesday = Label(NewFrame, text = "Tuesday", bg = "White", height = 5, width = 14)
        Tuesday.grid(row = 3, column = 1)        

        LabelC1 = Label(NewFrame, text = C1, bg = "White", height = 5, width = 14)
        LabelC1.grid(row = 3, column = 2)        

        LabelC2 = Label(NewFrame, text = C2, bg = "White", height = 5, width = 14)
        LabelC2.grid(row = 3, column = 3)        

        LabelC3 = Label(NewFrame, text = C3, bg = "White", height = 5, width = 14)
        LabelC3.grid(row = 3, column = 4)        

        LabelC4 = Label(NewFrame, text = C4, bg = "White", height = 5, width = 14)
        LabelC4.grid(row = 3, column = 5)

        LabelC5 = Label(NewFrame, text = C5, bg = "White", height = 5, width = 14)
        LabelC5.grid(row = 3, column = 6)        

        LabelC6 = Label(NewFrame, text = C6, bg = "White", height = 5, width = 14)
        LabelC6.grid(row = 3, column = 7)        

        LabelC7 = Label(NewFrame, text = C7, bg = "White", height = 5, width = 14)
        LabelC7.grid(row = 3, column = 8)        

        LabelC8 = Label(NewFrame, text = C8, bg = "White", height = 5, width = 14)
        LabelC8.grid(row = 3, column = 9)
        #Wednesday:
        Wednesday = Label(NewFrame, text = "Wednesday", bg = "White", height = 5, width = 14)
        Wednesday.grid(row = 4, column = 1)        

        LabelD1 = Label(NewFrame, text = D1, bg = "White", height = 5, width = 14)
        LabelD1.grid(row = 4, column = 2)        

        LabelD2 = Label(NewFrame, text = D2, bg = "White", height = 5, width = 14)
        LabelD2.grid(row = 4, column = 3)        

        LabelD3 = Label(NewFrame, text = D3, bg = "White", height = 5, width = 14)
        LabelD3.grid(row = 4, column = 4)

        LabelD4 = Label(NewFrame, text = D4, bg = "White", height = 5, width = 14)
        LabelD4.grid(row = 4, column = 5)        

        LabelD5 = Label(NewFrame, text = D5, bg = "White", height = 5, width = 14)
        LabelD5.grid(row = 4, column = 6)        

        LabelD6 = Label(NewFrame, text = D6, bg = "White", height = 5, width = 14)
        LabelD6.grid(row = 4, column = 7)

        LabelD7 = Label(NewFrame, text = D7, bg = "White", height = 5, width = 14)
        LabelD7.grid(row = 4, column = 8)        

        LabelD8 = Label(NewFrame, text = D8, bg = "White", height = 5, width = 14)
        LabelD8.grid(row = 4, column = 9)        
        #Thursday:
        Thursday = Label(NewFrame, text = "Thursday", bg = "White", height = 5, width = 14)
        Thursday.grid(row = 5, column = 1)

        LabelE1 = Label(NewFrame, text = E1, bg = "White", height = 5, width = 14)
        LabelE1.grid(row = 5, column = 2)        

        LabelE2 = Label(NewFrame, text = E2, bg = "White", height = 5, width = 14)
        LabelE2.grid(row = 5, column = 3)        

        LabelE3 = Label(NewFrame, text = E3, bg = "White", height = 5, width = 14)
        LabelE3.grid(row = 5, column = 4)

        LabelE4 = Label(NewFrame, text = E4, bg = "White", height = 5, width = 14)
        LabelE4.grid(row = 5, column = 5)        

        LabelE5 = Label(NewFrame, text = E5, bg = "White", height = 5, width = 14)
        LabelE5.grid(row = 5, column = 6)        

        LabelE6 = Label(NewFrame, text = E6, bg = "White", height = 5, width = 14)
        LabelE6.grid(row = 5, column = 7)

        LabelE7 = Label(NewFrame, text = E7, bg = "White", height = 5, width = 14)
        LabelE7.grid(row = 5, column = 8)        

        LabelE8 = Label(NewFrame, text = E8, bg = "White", height = 5, width = 14)
        LabelE8.grid(row = 5, column = 9)   


        
        NewFrame.pack() 
        
        
        
       
        Window2.mainloop()




Start = MainWindow()
Start.PreLogIn()

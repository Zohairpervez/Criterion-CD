from tkinter import *
#from tkinter import filedialog
#from PIL import ImageTk,Image
#from datetime import datetime

#------- MY FUNCTIONS ------------

def schedule(day,numperiods,frame_xpos):
    #Getting global variable
    global elist
    #making frame
    f = Frame(frame,bg="blue",height=400,width=100)
    f.grid(row=1,column=frame_xpos)
    #Making Entry with adjustable placement for all of The schedule entries
    for i in range(numperiods):
       e = Entry(f)
       e.grid(row=i,column=0)
       # modifying by adding e into elist
       elist.append(e)
#for the button
def writeout():
    #makes file
    fo=open("Myschedule"+".csv","w")
    count = 0
     #writes to the file and adds commas
    for e in elist:
       if (count == 0):
          fo.write(e.get())
       else:
          fo.write("," + e.get())
       count = count + 1

    fo.close()
    print(str(count) + " records written to Myschedule.csv")
# to open file again after closing app
def readin():
    #opens the file
    fi = open("Myschedule.csv","r")
    #splits to turn into list
    skedlist = fi.readline().split(",")
    fi.close()
    #inserts in to the entries 
    count = 0
    for e in elist:
       e.insert(0,skedlist[count])
       count = count + 1

def test(event):
    print(event) 
    topframe = Frame(root,bg='yellow',height='20')
    topframe.grid(sticky="nsew")
    title = Label(topframe,text="Your Y9 Schedules!",fg="white",bg='#50d987')
    title.config(font=("Arial", 18))
    title.grid()

# ------- FIRST LINE OF CODE ------------ #

# Build GUI
root = Tk()
root.title("Stay Up To Date")
root.geometry("2000x500")
titleheight = 5
root.configure(bg='red')

test(event=None)

# Other GUI stuff
cenf= Frame(root, width=200,height=150)
cenf.grid()
cenf.configure(bg='#d9b186')
#another frame
frame = Frame(cenf,borderwidth = 1.5, relief=RAISED, width=100,height=150)
frame.grid(row=1, column=0, sticky=W+E)
#save button
testme = Button(root,text="SAVE",command=writeout)
testme.grid(row=10,column=0)
#day1 to 8 labels
b1=Label(frame, text="Day 1")
b2=Label(frame, text="Day 2")
b3=Label(frame, text="Day 3")
b4=Label(frame, text="Day 4")
b5=Label(frame, text="Day 5")
b6=Label(frame, text="Day 6")
b7=Label(frame, text="Day 7")
b8=Label(frame, text="Day 8")
#placing
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=0, column=3)
b5.grid(row=0, column=4)
b6.grid(row=0, column=5)
b7.grid(row=0, column=6)
b8.grid(row=0, column=7)
#reminder frame.File io unfinished
rf=Frame(root, width=600, height=200)
rf.grid(sticky=S+W)
remindtitle = Label(rf,text="Reminders")
remindtitle.grid()
r1=Entry(rf)
r2=Entry(rf)
r3=Entry(rf)
r1.grid(row=15,column=0)
r2.grid(row=16,column=0)
r3.grid(row=17,column=0)

# build 56 entries using a super cool all in one function
elist = [] # all in one entry widget list
day = 0
#entries
for i in range(8):
    schedule(day,7,day)
    day = day + 1

# read in existing data if it exists
readin()

root.mainloop()

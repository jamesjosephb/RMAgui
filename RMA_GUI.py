from tkinter import *
from tkinter.scrolledtext import ScrolledText
import RMA

class MPMGUI(Frame):
    def __init__(self, title, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.geometry("450x600")
        self.master.title(title)

        self.MPM = r'MPM012390529'
        self.issueCategory = 'Swiper'
        self.issueDescription = "This is a test"

        self.columnconfigure(0, minsize=220)
        self.promptForMPM = Label(self, text="Enter the MPM#: ", borderwidth=5)
        self.promptForMPM.grid(row=0, column=0, stick=E)

        self.MPMinput = Text(self, height=1, width=25)
        self.MPMinput.grid(row=0, column=1, stick=W)

        self.promptForCategory = Label(self, text="Choose the Category: ", borderwidth=5)
        self.promptForCategory.grid(row=1, column=0, stick=E)

        CatagoryVariable = StringVar(self)
        CatagoryVariable.set("Swiper")

        self.Categoryinput = OptionMenu(self, CatagoryVariable, "Swiper",
                                                                "Coordinator",
                                                                "ACW",
                                                                "Unitec",
                                                                "Vendor",
                                                                "Merchant Account",
                                                                "American Changer",
                                                                "Installation",
                                                                "Network Connection",
                                                                "Site Analytics",
                                                                "NR |")
        self.Categoryinput.grid(row=1, column=1, stick=W)




        self.promptForIssue = Label(self, text="Describe the issue below: ", borderwidth=5)
        self.promptForIssue.grid(row=2, column=0, columnspan=2)

        self.IssueInput = ScrolledText(self, width=70, font=("Helvetica", 8), borderwidth=5)
        self.IssueInput.grid(row=3, column=0, columnspan=2, stick=W)

        self.executeButton = Button(self, text='Create-RMA', command=lambda: self.retreiveSendRMAinfo())
        self. executeButton.grid(row=4, column=0, pady=5, ipadx=3, ipady=3, sticky=W+E)

        self.executeButton = Button(self, text='Send-Email')
        self. executeButton.grid(row=4, column=1, pady=5, ipadx=3, ipady=3, sticky=W+E)

        self.promptForEmail = Label(self, text="Enter outgoing email :", borderwidth=5)
        self.promptForEmail.grid(row=5, column=0, sticky=E)

        self.Emailinput = Text(self, height=1, width=25)
        self.Emailinput.grid(row=5, column=1, sticky=W)





    def retreiveSendRMAinfo(self):
        MPMnumber = self.MPMinput.get("1.0", "end-1c")
        #Catagory = self.getCatagory()

        Issue = self.IssueInput.get("1.0", "end-1c")
        createRMA(MPMnumber, Catagory, Issue)


if __name__ == '__main__':
    app = MPMGUI('RMA')
    app.mainloop()
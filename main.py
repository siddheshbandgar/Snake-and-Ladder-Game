from userInterface import *
        
def main():
    master = Tk()
    master.title("Snake and Ladder")
    master.geometry("")
    img = PhotoImage( file = "lenna1.gif")
    x = Display(master,img)
    master.mainloop()

main()

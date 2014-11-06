#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class
enemy1 = drawpad.create_rectangle(750,100,850,110,fill='orange')
enemy2 = drawpad.create_rectangle(400,400,430,420,fill='red')
enemy3 = drawpad.create_rectangle(500,300,560,260,fill='orange')
class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "white")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "maroon")
       	    self.down.grid(row=0,column=2)
       	    # Bind an event to the first button
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "white")
       	    self.left.grid(row=0,column=3)
       	    # Bind an event to the first button
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "maroon")
       	    self.right.grid(row=0,column=4)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    global enemy1, enemy2, enemy3
	    drawpad.move(enemy1,5,0)
	    drawpad.move(enemy2,-6,0)
	    drawpad.move(enemy3,8,0)
	    x1, y1, x2, y2 = drawpad.coords(enemy1)
            if x2 > drawpad.winfo_width(): 
                    drawpad.move(enemy1,-800,0)
            elif x1 < 0:
                    direction = 5
            x1, y1, x2, y2 = drawpad.coords(enemy2)
            if x1 < drawpad.winfo_width(): 
                    drawpad.move(enemy2,800,0)
            elif x2 > drawpad.winfo_width():
                     drawpad.move(enemy2,-800,0)
            x1, y1, x2, y2 = drawpad.coords(enemy3)
            if x1 < drawpad.winfo_width(): 
                    drawpad.move(enemy3,800,0)
            elif x2 > drawpad.winfo_width():
                     drawpad.move(enemy3,-800,0)
	    # Remember to include your "enemies" with "global"
	    
	    # Uncomment this when you're ready to test out your animation!
	    drawpad.after(10,self.animate)
	
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)	
	def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)	
	def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)	
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
	 
		

app = MyApp(root)
root.mainloop()
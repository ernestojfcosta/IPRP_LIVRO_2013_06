import tkinter as tk

pilAvailable = True
try:
    import Image
    import ImageTk
except:
    pilAvailable = False
    
    
_imroot = tk.Tk()
_imroot.withdraw()

def formatPixel(data):
    if type(data) == tuple:
        return '{#%02x%02x%02x}'%data
    elif isinstance(data,Pixel):
        return '{#%02x%02x%02x}'%data.getColorTuple()
    
class ImageWin(tk.Canvas):
    """
    ImageWin:  Make a frame to display one or more images.
    """
    def __init__(self,title,width,height):        
        """
        Create a window with a title, width and height.
        """
        master = tk.Toplevel(_imroot)
        master.protocol("WM_DELETE_WINDOW", self._close)
        #super(ImageWin, self).__init__(master, width=width, height=height)
        tk.Canvas.__init__(self, master, width=width, height=height)
        self.master.title(title)
        self.pack()
        master.resizable(0,0)
        self.foreground = "black"
        self.items = []
        self.mouseX = None
        self.mouseY = None
        self.bind("<Button-1>", self._onClick)
        self.height = height
        self.width = width
        self._mouseCallback = None
        self.trans = None # for coordinates transformation
        _imroot.update()
        
    def _close(self):
        """Close the window"""
        self.master.destroy()
        self.quit()
        _imroot.update()
        
        
    def getMouse(self):
            """Wait for mouse click and return a tuple with x,y position in screen coordinates after
            the click"""
            self.mouseX = None
            self.mouseY = None
            while self.mouseX == None or self.mouseY == None:
                self.update()
            return ((self.mouseX,self.mouseY))
    
    def setMouseHandler(self, func):
        self._mouseCallback = func

    def _onClick(self, e):
        self.mouseX = e.x
        self.mouseY = e.y
        if self._mouseCallback:
            self._mouseCallback(Point(e.x, e.y)) 
            
    def exitOnClick(self):
        """When the Mouse is clicked close the window and exit"""
        self.getMouse()
        self._close()
        
    def getWidth(self):
        """Window width."""
        return self.width
    
    def getHeight(self):
	""" Window height."""
	return self.height
	
	
    def setBackground(self, color):
	""" Set the background color of the window."""
	self.config(bg=color)

def toScreen(self,x,y):
    """ Coordinates expressed in screen coordinates."""
    trans = self.trans
    if trans:
	return self.trans.screen(x,y)
    else:
	return x,y
    
def toWorld(self,x,y):
    trans = self.trans
    if trans:
	return self.trans.world(x,y)
    else:
	return x,y
    
def setCoords(self, x1,y1,x2,y2):
    """Window coordinates from (x1,y1) lower-left to (x2,y2) up-right."""
    self.trans = Transform(self.width,self.height,x1,y1,x2,y2)
    


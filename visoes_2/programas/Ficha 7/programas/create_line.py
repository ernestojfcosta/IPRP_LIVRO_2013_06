# exploring module cImage (a Tkinter wrapper)
# from:
# http://www.cs.luther.edu/~pythonworks/PythonContext/cImage.py
 
import cImage
 
# this actually creates a canvas ready for drawing
#win = cImage.ImageWin("My Canvas", 500, 400)
 
# let's draw a red line on the canvas object
# from coordinate points x1=10, y1=100 to x2=400, y2=50
#win.create_line(10, 100, 400, 50, fill="red")

#win.create_oval( 50,50,200,100,fill='blue')

#win.create_rectangle(0,0,250,250,fill='green')

def triangulo(p1,p2,p3, win):
    win.create_line(p1[0], p1[1],p2[0],p2[1], fill="red")
    win.create_line(p2[0], p2[1],p3[0],p3[1], fill="red")
    win.create_line(p3[0], p3[1],p1[0],p1[1], fill="red")
def main():
    win=cImage.ImageWin('Janela',600,400)
    triangulo((20,30),(40,80), (30,50),win)
    win.exitOnClick()
# needed
#win.exitOnClick()

if __name__ =='__main__':
    main()
"""
image.py
Para manipular imagens bitmap não comprimidas em formato PPM.
Este módulo benificiou das ideias e de algum código de John Zelle (graphics.py) e Brad Miller (cImage.py).
"""

# tkinter para vizualizar imagens
import tkinter as tk

_imroot = tk.Tk()
_imroot.withdraw()

class ImageWin(tk.Canvas):
    """
    ImageWin:  Permite mostrar uma ou mais imagens
    """
    def __init__(self,title,width,height):        
        """
        Cria uma janela a partir do título e das dimensões
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
        self.bind("<Button-1>", self._on_click)
        self.height = height
        self.width = width
        self._mouseCallback = None
        self.trans = None # for coordinates transformation
        _imroot.update()
        
    def _close(self):
        """Fecha a janela"""
        self.master.destroy()
        self.quit()
        _imroot.update()
        
        
    def get_mouse(self):
            """Devolve a posição do rato quando o botão é accionado"""
            self.mouseX = None
            self.mouseY = None
            while self.mouseX == None or self.mouseY == None:
                self.update()
            return ((self.mouseX,self.mouseY))
    
    def set_mouse_handler(self, func):
        self._mouseCallback = func

    def _on_click(self, e):
        self.mouseX = e.x
        self.mouseY = e.y
        if self._mouseCallback:
            self._mouseCallback(Point(e.x, e.y)) 
            
    def get_width(self):
        return self.width
        
    def get_height(self):
        return self-height
            
    def exit_on_click(self):
        """Fecha a janela e termina quando rato accionado"""
        self.get_mouse()
        self._close()
        
# Pixel

class Pixel(object):
    """Para manipulação dos bvalores RGB."""
    def __init__(self, red, green, blue, max_=255):
        self._red = red
        self._green = green
        self._blue = blue
        self._max = max_
        
    def get_red(self):
        return self._red
    
    def get_green(self):
        return self._green
    
    def get_blue(self):
        return self._blue
    
    def get_colour_tuple(self):
        return (self._red, self._green, self._blue)
    
    def set_red(self,red):
        assert self._max >= red >= 0
        self._red = red
               
    def set_green(self,green):
        assert self._max >= green >= 0
        self._green = green
        
    def set_blue(self,blue):
        assert self._max >= blue >= 0
        self._blue = blue     
        
    def __getitem__(self,key):
        if key == 0:
            return self._red
        elif key == 1:
            return self._green
        elif key == 2:
            return self._blue
        else:
            raise ValueError('Erro: %d indice fora dos limites' % key)
        
    def set_range(self,val_max):
        if (val_max == 1.0) or (val_max == 255):
            self._max = val_max
        else:
            raise ValueError('Erro: os valores possíveis são 1.0 ou 255')
        
    def __str__(self):
        return str(self.get_colour_tuple())
    

# Images

class AbstractImage(object):
    
    image_cache = dict()
    image_id = 1
    
    def __init__(self, fname=None, data = [], imobj = None, height=0, width=0):
        super(AbstractImage,self).__init__()
        
        self.load_image = self._load_tk_image
        self.create_blank_image = self._create_blank_tk_image
        self.set_pixel = self._set_tk_pixel
        self.get_pixel = self._get_tk_pixel
        self.save = self._save_tk
        
        if fname:
            self.load_image(fname)
            self._im_file_name = fname
            
            
        elif data:
            pass
        elif height > 0 and width > 0:
            pass
        elif imobj:
            pass
        
        self.width = self.im.width()
        self.height = self.im.height()
        
        self.center_x = self.width//2 + 3
        self.center_y = self.height//2 + 3
        
        
        def _load_tk_image(self,fname):
            pass
        
    
    

    
if __name__ == '__main__':
    cor = (128,255,64)
    pix_1 = Pixel(cor[0],cor[1], cor[2])
    print(pix_1)
    """
    jan = ImageWin('toto', 400,200)
    img = tk.PhotoImage(file='/data/imagens/aima.gif',format='GIF')
    jan.create_image(0,0, image=img)
    _imroot.update()
    jan.exit_on_click()
    """
    

                  
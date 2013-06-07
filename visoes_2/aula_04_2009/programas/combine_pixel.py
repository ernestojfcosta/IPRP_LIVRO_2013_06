import cImage

def combine_pixel(pixel1, pixel2,function):
    """ Combina dois pixeis de acordo com a função."""
    r1 = pixel1.getRed()
    g1 = pixel1.getGreen()
    b1 = pixel1.getBlue()
    
    r2 = pixel2.getRed()
    g2 = pixel2.getGreen()
    b2 = pixel2.getBlue()
    
    r,g,b = function(r1,r2,g1,g2,b1,b2)
    return cImage.Pixel(r,g,b)

print combine_pixel(cImage.Pixel(128,255,45), cImage.Pixel(255,128,128), (lambda x1,x2,y1,y2,z1,z2: ((x1 + x2) /2, (y1+y2)/2, (z1+z2)/2)))

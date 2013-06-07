def RGBToHexaColor(rgb_tuple):
    """ convert an (R, G, B) tuple to #RRGGBB """
    hexcolor = '#%02x%02x%02x' % rgb_tuple
    return hexcolor

if __name__ == '__main__':
    print(RGBToHexaColor((255,0,0)))
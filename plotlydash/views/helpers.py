def determine_font_color(background_color):

    background_color = hex_to_rgb(background_color)
    
    r = background_color[0]
    g = background_color[1]
    b = background_color[2]

    font_color = '#000000' if (r*0.299 + g*0.587 + b*0.114) > 186 else '#ffffff'

    return font_color

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb
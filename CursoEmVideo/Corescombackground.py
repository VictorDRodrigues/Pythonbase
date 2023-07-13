styles = ['0', '1', '4', '7']
text_colors = ['30', '31', '32', '33', '34', '35', '36', '37']
bg_colors = ['40', '41', '42', '43', '44', '45', '46', '47']

for style in styles:
    for text_color in text_colors:
        for bg_color in bg_colors:
            code = '\033[{};{};{}m'.format(style, text_color, bg_color)
            print('{}Texto formatado{} estilo {} cor {} background {}'.format(code, '\033[m', style, text_color, bg_color))


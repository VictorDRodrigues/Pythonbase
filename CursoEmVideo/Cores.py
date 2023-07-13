
st = ['0', '1', '4', '7']

bscores = ['30', '31', '32', '33', '34', '35', '36', '37',
           '40', '41', '42', '43', '44', '45', '46', '47']

for style in st:
    for color in bscores:
        code = '\033[{};{}m'.format(style, color)
        print('{}Texto formatado{} estilo {} cor {}'.format(code, '\033[m', style, color))


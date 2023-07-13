
r = int(input('Digite um número e descubra seu fatorial: '))
s = 1
lo = r
ss = ''
while lo >= 1:
    s = s * lo
    if lo == r:
        ss = ss + str(lo)
    else:
        ss = ss + 'x' + str(lo)
    lo = lo - 1

print("{:.0f}! = {} = {}".format(r,ss,s))
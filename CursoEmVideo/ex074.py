import random
print('Cria Tuplas randomicas')
r = ''
x = 0
lr = {}

while x in range(0,5):
    le = str(random.randint(1,10))
    print(le)
    if x == 4:
        r = r + "'"+ str(le) +  "'"
        lr[x] = le
        #r = r + str(le) 
    else:
        r = r + "'"+ str(le) +  "', "
        #r = r + str(le) +  ", "
        lr[x] = le
    le = ()
    x = x + 1

r = r

le = lr

print(lr[0])
print(lr[2])
print(lr[3])
print(lr[4])
print(lr)
print(r)
print(le)
print(le[0])
print(le[2])
print(le[3])
print(le[4])

sec = int(input('Enter seccond: '))
h = ((sec // 3600)) % 24
m = (sec // 60) % 60
s = sec % 60
print('%02d:%02d:%02d'% (h, m, s))
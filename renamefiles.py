import os

exdir = 'C:\\Users\\sunnan\\Desktop\\JIANRENWU\\'
k = 1
for file in os.listdir(exdir):
    s = str(k)+'.png'
    os.rename(os.path.join(exdir, file), os.path.join(exdir, s))
    print file, 'ok'
    k += 1


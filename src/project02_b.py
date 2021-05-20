# project 02 b
# KAKEMBO ISMAIL ABDUL WADUDU 2020/BSE/115/PS
# MASIKA PEACE KEITH 2020/BSE/033/PS
# AKAMPURIRA GODSON 2020/BSE/005/PS
# NIYONSHUTI NOBERT 2020/BSE/056/PS
def open_file():
while True:
        fileName = input('Enter file name\n')
try:

    fileHandle = open(fileName)
    fileHandle = open('measles.txt')

break
except:
print('File not available. Try again with the correct file name!')
return fileName

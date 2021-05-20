  # the program reads from measles.txt
  # project 02 a
# KAKEMBO ISMAIL ABDUL WADUDU 2020/BSE/115/PS
# MASIKA PEACE KEITH 2020/BSE/033/PS
# AKAMPURIRA GODSON 2020/BSE/005/PS
# NIYONSHUTI NOBERT 2020/BSE/056/PS

try:
    fileHandle = open('measles.txt')
    print(fileHandle)
    lowest = None
    highest = None
    for line in fileHandle:
        year = line[-5:]
        year = year.strip()
        #print the year

        if (lowest is None) or (highest is None):
            lowest = year
            highest = year
        elif lowest > year:
            lowest = year
        elif highest < year:
            highest = year

    print(highest)
    print(lowest)
    # if the program is unable to open file from measles.txt
except:
    print('Unable to open specified file!!')
    quit()
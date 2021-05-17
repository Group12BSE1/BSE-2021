count = 0
total = 0
print('________________________________')
try:
    file1 = input('Enter file name: ') # Input file name to be worked on
    op_file = open(file1)#opening the file
    for line in op_file:
        line = op_file.readline() # reading each line in the file
        if line.startswith('X-DSPAM-Conference:'):
            x = line.find('')# starting point for extraction
            y = float(line[x:27])
            count = count + 1
            total = total + y
    print('count is:', count)
    print('total is:',total)
    Average = total/count
    print('Average spam confidence:', Average)
except:
    print('file',file1,'does not exist')
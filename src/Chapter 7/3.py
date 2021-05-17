from os import path
print('_________________________________')
check1 = 'na na boo boo'
file1 = input('Enter file name: ')
file1 = file1.lower()
if path.exists(file1):
    file2 = open(file1)
    for line in file2:
        line = file2.readlines()
        line = len(line)
    print('There are ',line,'lines in the file')
elif file1 == check1:
    print('NA NA BOO BOO - YOU HAVE BEEN PRANKED')
else:
    print("File doesn't exist")
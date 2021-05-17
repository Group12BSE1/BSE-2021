str1 = 'X-DSPAM-Confidence: 0.8475'
str2 = str1.find('')# obtaining the position of the first space
print("String is:",str1)
print("Length: ",len(str1))
x = str2 + 1
y = str1[x:len(str1)]
y = float(y)
print('Number is:',y)
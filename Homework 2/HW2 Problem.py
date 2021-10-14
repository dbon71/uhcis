#David Bonilla
#CIS2348 Ratner
#PSID:1913106
#PART A
#define months
v = 1
months =['January','February','March','April','May','June','July','August','September','October','November','December']
#loop for input date
while v == 1:
  try:
    string = input('Enter the month day, year:')
  except SyntaxError:
    continue
  if string == '-1':
    break
  try:
    arrange = string.split()
    digit = len(arrange)
    if digit != 3:
      continue
    m = arrange[0]
    day = arrange[1]
    y = arrange[2]
    d, comma = day.split(',')
#code for date format
    for x in range(12):
      if string.find(months[x]) >= 0:
        mns = str(x+1)
        ans = mns + '/' + d + '/' + y
        print(ans)
        break
  except ValueError:
    continue


#PART B
files = open ('inputDates.txt','r')
dates = files.readlines()

months =['January','February','March','April','May','June','July','August','September','October','November','December']

for string in dates:
  if string == '-1':
    break
  try:
    arrange = string.split()
    digit = len(arrange)
    if digit != 3:
      continue
    m = arrange[0]
    day = arrange[1]
    y = arrange[2]
    d, comma = day.split(',')

    for x in range(12):
      if string.find(months[x]) >= 0:
        mns = str(x+1)
        ans = mns + '/' + d + '/' + y
        print(ans)
        break
  except ValueError:
      continue
#PART C
files = open ('inputDates.txt','r')
dates = files.readlines()

months =['January','February','March','April','May','June','July','August','September','October','November','December']

count=0
for string in dates:
  count++
  if string == '-1':
    break
  try:
    arrange = string.split()
    digit = len(arrange)
    if digit != 3:
      continue
    m = arrange[0]
    day = arrange[1]
    y = arrange[2]
    d, comma = day.split(',')

    for x in range(12):
      if string.find(months[x]) >= 0:
        mns = str(x+1)
        ans = mns + '/' + d + '/' + y
        if count >0:
          files2 = open('parsedDates.txt','a')
          files2.write('ans \n')
          files2.close()
        else:
          files3 = open('parsedDates.txt','w')
          files3.write('ans \n')
          files3.close()
        break
  except ValueError:
    continue
files.close()

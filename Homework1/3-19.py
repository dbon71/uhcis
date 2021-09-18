#David Bonilla
#CIS2348 Ratner
#PSID:1913106
import math
height = int(input())
width = int(input())
area = height*width
need = area/350
print('Enter wall height (feet):')
print('Enter wall width (feet):')
print('Wall area:', area,'square feet' )
print('Paint needed:','{:.2f}'.format(need),'gallons')
print('Cans needed:', round(need),'can(s)')

print('Choose a color to paint the wall:')
print('Cost of purchasing',color,'paint:',price)
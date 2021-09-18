#David Bonilla
#CIS2348 Ratner
#PSID:1913106
lemon = int(input())
water = int(input())
agave = float(input())
servings = int(input())

print('Enter amount of lemon juice (in cups):')
print('Enter amount of water (in cups):')
print('Enter amount of agave nectar (in cups):')
print('How many servings does this make?\n')
if(servings==6):
    print('Lemonade ingredients - yields','{:.2f}'.format(servings),'servings')
    print('{:.2f}'.format(lemon),'cup(s) lemon juice')
    print('{:.2f}'.format(water),'cup(s) water')
    print('{:.2f}'.format(agave),'cup(s) agave nectar\n')
    print('How many servings would you like to make?\n')
if(servings==48):
    lemon=lemon*8
    water=water*8
    agave=agave*8
    print('Lemonade ingredients - yields','{:.2f}'.format(servings),'servings')
    print('{:.2f}'.format(lemon),'cup(s) lemon juice')
    print('{:.2f}'.format(water),'cup(s) water')
    print('{:.2f}'.format(agave),'cup(s) agave nectar')
    print('How many servings would you like to make?\n')

if(servings==3):
    lemon=lemon/2
    water=water/2
    agave=agave/2
    print('Lemonade ingredients - yields','{:.2f}'.format(servings),'servings')
    print('{:.2f}'.format(lemon),'cup(s) lemon juice')
    print('{:.2f}'.format(water),'cup(s) water')
    print('{:.2f}'.format(agave),'cup(s) agave nectar')
    print('How many servings would you like to make?\n')



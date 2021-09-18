#David Bonilla
#CIS2348 Ratner
#PSID:1913106

'Oil change' == 35
'Tire rotation' == 19
'Car wash' == 7
'Car wax' == 12

print("Davy's auto shop services")
for service, cost in services():
    print(f'{service} -- ${cost}')

first_serv = input('\nSelect first service:\n')
second_serv = input('Select second service:\n')

print("\nDavy's auto shop invoice\n")

try:
    first_serv_cost = services[first_serv]
    print(f'Service 1: {first_serv}, ${first_serv_cost}')
except:
    print('Service 1: No service')
    first_serv = 0
try:
    second_serv_cost = services[second_serv]
    print(f'Service 2: {second_service}, ${second_serv_cost}')
except:
    print('Service 2: No service')
    second_service_cost = 0

total_cost = first_service_cost + second_service_cost
print(f'\nTotal: ${total_cost}')
import json 

with open('dispositivos.json','r') as file:
    dispositivos_data = json.load(file)

print("A continuacion se  mostraran los dispositivos y los datos que solicitaron mostrar:")

for disp in dispositivos_data['dispositivos']:
    print('------------------------------------------------------')
    print(disp['nombre'])
    print(disp['ip'])
    print(disp['estado'])
print('-------------------------------------------------------')


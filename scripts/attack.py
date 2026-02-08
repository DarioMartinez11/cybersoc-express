import time
from datetime import datetime

print('Generando logs de ataque...')
for i in range(1, 6):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log = f'{timestamp} - SSH failed password from 10.0.0.{i}'
    print(log)
    with open('/logs/attack.log', 'a') as f:
        f.write(log + '\n')
    time.sleep(0.5)
print('Hecho. Ver Kibana: http://localhost:5601')

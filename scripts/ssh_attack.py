#!/usr/bin/env python3
import time
import sys

print('[+] SIMULANDO ATAQUE SSH BRUTE FORCE...')

for i in range(1, 11):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'{timestamp} - SSH failed password for root from 192.168.1.100 port 22 (attempt {i})'
    print(log_entry)
    # Escribir en un log que Filebeat recoja
    with open('/var/log/ssh_attack.log', 'a') as f:
        f.write(log_entry + '\n')
    time.sleep(1)

print('[+] ATAQUE COMPLETADO. Revisa Kibana -> Discover')

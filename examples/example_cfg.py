import socket

global config
config = {}
possible_main_servers = ['10.1.1.1', '10.1.1.2']

for srv in possible_main_servers:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((srv, 80))
    except:
        continue
    s.close()
    config['main_server'] = srv
    break

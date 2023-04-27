import os
import sys
from server import Server
from receiver import Receiver
from generator import Generator

def main():
    # Parse command line arguments
    if len(sys.argv) < 3:
        print("Usage: ./mrsync.py <source> <destination>")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    # Start the server and connect to the client via pipes
    server_read, client_write = os.pipe()
    client_read, server_write = os.pipe()

    pid = os.fork()

    if pid == 0: # Child process (server)
        # Redirect standard input and output to pipes
        os.close(sys.stdin.fileno())
        os.dup(server_read)
        os.close(sys.stdout.fileno())
        os.dup(client_write)

        # Close all other file descriptors
        os.close(server_read)
        os.close(client_read)
        os.close(server_write)
        os.close(client_write)

        # Launch the server
        server = Server()
        receiver = Receiver(destination)
        receiver.receive(server.receive())
        generator = Generator(source, destination)
        generator.compare(receiver.get_file_list())
        for request in generator.get_requests():
            server.send(request)
            receiver.receive(server.receive())
            generator.send(request, receiver)
        sys.exit(0)
    else: # Parent process (client)
        # Redirect standard input and output to pipes
        os.close(sys.stdin.fileno())
        os.dup(client_read)
        os.close(sys.stdout.fileno())
        os.dup(server_write)

        # Close all other file descriptors
        os.close(server_read)
        os.close(client_read)
        os.close(server_write)
        os.close(client_write)

        # Launch the client
        server = Server()
        server.send(destination)
        receiver = Receiver(destination)
        generator = Generator(source, destination)
        generator.compare(receiver.get_file_list())
        for request in receiver.get_requests():
            server.send(request)
            generator.receive(request, server)
        sys.exit(0)

if __name__ == "__main__":
    main()


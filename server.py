import os
import sys

from receiver import Receiver
from generator import Generator

def server():

    # Set up the pipes for communication with the client
    # configure les tubes pour communiquer avec le client
    in_pipe_r, in_pipe_w = os.pipe()
    out_pipe_r, out_pipe_w = os.pipe()

    # Fork the process to create the server and the client processes
    # fork le precessus pour cree le processus client et serveur
    pid = os.fork()

    if pid == 0:
        # Child process - this is the server process
        os.close(in_pipe_w)
        os.close(out_pipe_r)

        # Redirect standard input and output to the pipes
        # redirige l'entree et la sortie standard vers les tubes
        os.dup2(in_pipe_r, 0)
        os.dup2(out_pipe_w, 1)

        # Create a new Receiver instance and start it
        # cree un nouveau receveur et le lancer
        receiver = Receiver()
        receiver.start()

        # Wait for the receiver to finish
        # attendre que le receveur finisse
        receiver.join()

        # Exit the child process
        sys.exit(0)

    else:
        # Parent process - this is the client process
        os.close(in_pipe_r)
        os.close(out_pipe_w)

        # Redirect standard input and output to the pipes
        os.dup2(out_pipe_r, 0)
        os.dup2(in_pipe_w, 1)

        # Create a new Generator instance and start it
        generator = Generator()
        generator.start()

        # Wait for the generator to finish
        generator.join()

        # Exit the parent process
        sys.exit(0)

if __name__ == '__main__':
    server()


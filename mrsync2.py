import os
import sys
import argparse
import signal
import time
from pathlib import Path

from server import Server
from receiver import Receiver
from generator import Generator
from message import Message

def parse_args():
    parser = argparse.ArgumentParser(description='mrsync')
    parser.add_argument('src', help='Source directory')
    parser.add_argument('dst', help='Destination directory')
    parser.add_argument('-r', action='store_true', help='Recursive copy')
    parser.add_argument('-v', action='store_true', help='Verbose output')
    return parser.parse_args()

def send_files(src, dst, recursive=False, verbose=False):
    # Create a pipe for communication between the server and the client
    # cree un tube pour communiquer entre le serveur et le client
    pipe_r, pipe_w = os.pipe()

    # Fork the process to create the server and the receiver
    # fork le processus pour creer le serveur et le receveur
    pid = os.fork()

    if pid == 0:
        # This is the child process (server)
        # Close the write end of the pipe
        # fermer le cote ecriture du tube
        os.close(pipe_w)

        # Redirect the standard input and output to the pipe
        # redirige l'entree et la sortie standard vers le tube
        os.dup2(pipe_r, 0)
        os.dup2(pipe_r, 1)

        # Create the server and start it
        # cree le serveur et le lance
        server = Server()
        server.start()

    else:
        # This is the parent process (sender)
        # Close the read end of the pipe
        # fermer le cote lecture du tube
        os.close(pipe_r)

        # Create the receiver and start it
        # creer le receiver et le lancer
        receiver = Receiver(dst)
        receiver.start()

        # Calculate the list of files to send
        # calculer la liste de fichiers a envoyer
        src_path = Path(src)
        files_to_send = []
        if src_path.is_file():
            files_to_send.append(src_path)
        elif src_path.is_dir():
            if recursive:
                files_to_send = list(src_path.glob('**/*'))
            else:
                files_to_send = list(src_path.glob('*'))

        # Send the list of files to the receiver
        # envoie la liste de fichier au receiver
        receiver.send(Message('files', files_to_send))

        # Fork the process to create the generator
        # Fork le processus pour cree le generateur
        pid_generator = os.fork()

        if pid_generator == 0:
            # This is the child process (generator)
            generator = Generator(src_path, dst)
            generator.start()

        else:
            # This is the parent process (sender)
            # Wait for the generator to finish
            # on attend que le generateur finisse
            os.waitpid(pid_generator, 0)

            # Stop the receiver
            receiver.stop()

            # Wait for the server to finish
            # on attend que le server finisse
            os.waitpid(pid, 0)

def main():
    # Parse the command line arguments
    args = parse_args()

    # Call the send_files function
    # appel la fonction send_files 
    send_files(args.src, args.dst, args.r, args.v)

if __name__ == '__main__':
    main()


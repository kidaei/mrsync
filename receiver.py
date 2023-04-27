import os
import sys
import message

def receive_files(dest_dir):
    # Open a pipe to read messages from the server
    read_pipe, write_pipe = os.pipe()
    os.close(write_pipe)
    input_fd = read_pipe

    # Redirect input to the read end of the pipe
    # rediriger l'imput vers la lecture du tube
    sys.stdin = os.fdopen(input_fd)

    # Calculate the list of files in the destination directory
    # calcule la liste des fichiers dans le repertoire destination
    dest_files = set(os.listdir(dest_dir))

    # Wait for the list of files sent by the sender
    # attend la liste des fichiers envoyee par la source
    sender_list = message.receive_message(sys.stdin)
    sender_files = set(sender_list)

    # Fork the generator to compare the two lists and request missing or outdated files
    # Fork le generateur pour comparer les 2 listes et demande les fichiers manquants ou non mis a jour
    pid = os.fork()
    if pid == 0:  # child process (generator)
        generate_requests(sender_files, dest_files)
        os._exit(0)  # exit child process
    else:  # parent process (receiver)
        # Wait for the generator to finish and get the list of files to receive
        # attend que le generateur finisse et obtient la liste de fichiers a recevoir
        missing_files = message.receive_message(sys.stdin)

        # Receive each missing or outdated file from the sender and write it to the destination directory
        # recoit tous les fichiers manquants ou non-mis a jours de la source et les ecrits dans la destination
        for filename in missing_files:
            filedata = message.receive_file(sys.stdin)
            filepath = os.path.join(dest_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(filedata)

def generate_requests(sender_files, dest_files):
    # Find missing or outdated files and send a request for each one
    # trouve les fichiers manquants ou non mis a jour et envoi une requete a chaqun
    missing_files = sender_files - dest_files
    outdated_files = {filename for filename in sender_files if filename in dest_files and os.path.getmtime(filename) < os.path.getmtime(dest_dir)}
    missing_outdated_files = missing_files | outdated_files
    message.send_message(missing_outdated_files, sys.stdout)



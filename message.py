import pickle


def send_msg(fd, msg):
    """Send a message to a file descriptor.

    Args:
        fd (int): The file descriptor to send the message to.
        msg (object): The message to send.

    Raises:
        IOError: If an error occurs while sending the message.
    """
    try:
        msg_bytes = pickle.dumps(msg)
        msg_len = len(msg_bytes)
        header = f"{msg_len:<10}".encode()
        fd.write(header + msg_bytes)
        fd.flush()
    except pickle.PickleError as e:
        raise IOError(f"Error pickling message: {e}")
    except (BrokenPipeError, OSError) as e:
        raise IOError(f"Error sending message: {e}")


def recv_msg(fd):
    """Receive a message from a file descriptor.

    Args:
        fd (int): The file descriptor to receive the message from.

    Returns:
        object: The message received.

    Raises:
        IOError: If an error occurs while receiving the message.
    """
    try:
        header_bytes = fd.read(10)
        if not header_bytes:
            return None
        msg_len = int(header_bytes.strip())
        msg_bytes = fd.read(msg_len)
        msg = pickle.loads(msg_bytes)
        return msg
    except pickle.PickleError as e:
        raise IOError(f"Error unpickling message: {e}")
    except (BrokenPipeError, OSError) as e:
        raise IOError(f"Error receiving message: {e}")


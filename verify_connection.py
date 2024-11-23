import socket

def check_internet_connection():
  try:
    socket.create_connection(('8.8.8.8', 53), timeout = 5)
    return True
  except OSError:
    return False

if __name__ == '__main__':
  check_internet_connection()
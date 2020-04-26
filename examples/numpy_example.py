from DataSocket import SendSocket, ReceiveSocket, NUMPY
import time
from threading import Thread


number_of_messages = 2000  # number of sample messages to send
port = 4001  # TCP port to use


# define a function to send data across a TCP socket
def sending_function():
    send_socket = SendSocket(tcp_port=port, send_type=NUMPY)
    send_socket.start()

    for i in range(number_of_messages):
        send_socket.send_data(i*10)
        time.sleep(0.25)

    print("closing send socket.")
    send_socket.stop()


# define a function to recieve and print data from a TCP socket
def recieving_function():
    num_messages_recieved = [0]

    # function to run when a new piece of data is received
    def print_value(data):
        print("value recieved: ", data['data'])
        num_messages_recieved[0] = 1 + num_messages_recieved[0]

    rec_socket = ReceiveSocket(tcp_port=port, handler_function=print_value)
    rec_socket.start()

    while num_messages_recieved[0] < number_of_messages:
        # add delay so this loop does not unnecessarily tax the CPU
        time.sleep(0.25)

    print("closing receive socket.")
    rec_socket.stop()


if __name__ == '__main__':
    # define separate threads to run the sockets simultaneously
    send_thread = Thread(target=sending_function)
    rec_thread = Thread(target=recieving_function)

    send_thread.start()
    rec_thread.start()

    send_thread.join()
    rec_thread.join()

global send_socket
send_socket = TCPSendSocket(4343, '0.0.0.0');
rec_socket = TCPReceiveSocket(4242,'0.0.0.0',@echo_back);

send_socket.start()
rec_socket.start()

pause(10) % arbitrarily stay open for 10 seconds to receive the messages
          % from python

send_socket.stop();
rec_socket.stop();

function echo_back(data)
    global send_socket;
    send_socket.send_data(data);
end
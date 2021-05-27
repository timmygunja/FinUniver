import socket


class Client(object):
    sock = socket.socket()
    # sock.setblocking(1)
    server = None
    data = None

    def connect(self):
        self.sock.connect(self.server)
        print("Client: connecting")

    def input_msg(self):
        return input("Input a message: ")

    def send_msg(self, msg):
        self.sock.sendto(msg.encode(), self.server)
        print("Client: sending data to server")

    def accept_data(self):
        self.data = self.sock.recv(1024)
        print("Client: accepting data from server")
        print(f"Answer received: {self.data}")

    def close(self):
        self.sock.close()
        print("Client: closing connection")


if __name__ == "__main__":
    client = Client()

    while True:
        host = input("Input a host you want to connect to (or \"s\" to use standard host): ")
        port = input("Input a port you want to connect to (or \"s\" to use standard port): ")

        if host.lower() == "s":
            host = "localhost"

        if port.lower() == "s":
            port = 9091

        try:
            client.server = (host, int(port))
            client.connect()
            break
        except:
            print("Server: ERROR - INVALID HOST/PORT PAIR GIVEN!")



    while True:
        msg = client.input_msg()

        if msg.lower() == "exit":
            break

        client.send_msg(msg)
        client.accept_data()

    client.close()


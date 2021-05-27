import socket


class Server(object):
    sock = socket.socket()
    conn = None
    addr = None

    def start(self):
        while True:
            data = self.conn.recv(1024)
            print("Server: accepting data")

            if not data:
                print("Server: no data found")
                break

            self.conn.send(data.upper())
            print("Server: data received, echoed back")

        self.close()

    def close(self):
        self.conn.close()
        print("Server: closing connection")

    def listen(self, channels):
        server.sock.listen(channels)
        print(f"Server: listening to {channels} channels")

    def bind(self, client):
        self.sock.bind(client)
        print(f"Server: binding {client[0]} on port {client[1]}")

    def accept_clients(self):
        self.conn, self.addr = self.sock.accept()
        print("Server: accepting clients")


if __name__ == "__main__":
    print("Server: starting")
    server = Server()

    while True:
        port = input("Input a port you want to connect to (or \"s\" to use standard port): ")

        if port.lower() == "s":
            port = 9090

        try:
            client = ('localhost', int(port))
            break
        except:
            print("Server: ERROR - INVALID PORT!")

    server.bind(client)

    while True:
        server.listen(1)
        server.accept_clients()
        server.start()
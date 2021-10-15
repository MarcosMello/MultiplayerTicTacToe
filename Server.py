import socket, _thread, sys, random, tkinter

def threaded_client(conn, addr):
    while True:
        try:
            data = conn.recv(2084);
            reply = data.decode("utf-8");
            if not data:
                print("Client Disconnected!");
                break;
            else:
                print(F"Received: {reply}");
                print(F"Sending: {reply}");
            conn.sendall(str.encode(reply));
        except:
            print(F"Error!");
            break;

server = "192.168.15.6";
port = 5555; #Provavelmente precisarei mudar

sock = socket.socket();

try:
    sock.bind((server, port));
except socket.error as e:
    print(F"Error! {str(e)}");

sock.listen();
print("Sucess!");

while True:
    conn, addr = sock.accept();
    print(F"Connected to: {addr}");
    
    _thread.start_new_thread(threaded_client, (conn, addr));
from tkinter import *
from tkinter import simpledialog
import grpc
import bidirectional_pb2
import bidirectional_pb2_grpc

address = 'localhost'
port = 50051


class Welcome:

    def __init__(self, u: str, window):
        
        self.window = window
        self.username = u
        
        channel = grpc.insecure_channel(address + ':' + str(port))
        self.conn = bidirectional_pb2_grpc.BidirectionalServerStub(channel)
        self.__setup_ui()
        self.window.mainloop()
 

    def send_message(self, event):
        message = self.entry_message.get()  
        if message !=():
            n = bidirectional_pb2.Message()  
            n.name = self.username  
            n.message = message  
            print("S[{}] {}".format(n.name, n.message))  
            self.conn.BidirectionalStream(n)  

    def __setup_ui(self):
        self.bidirectional_pb2_grpc_list = Text()
        self.bidirectional_pb2_grpc_list.pack(side=TOP)
        self.lbl_username = Label(self.window, text=self.username)
        self.lbl_username.pack(side=LEFT)
        self.entry_message = Entry(self.window, bd=5)
        self.entry_message.bind('<Return>', self.send_message)
        self.entry_message.focus()
        self.entry_message.pack(side=BOTTOM)


if __name__ == '__main__':
    root = Tk()  
    frame = Frame(root, width=300, height=300)
    frame.pack()
    root.withdraw()
    username = None
    while username is None:
        
        username = simpledialog.askstring("Username", "Enter Username", parent=root)
    root.deiconify()  
    w = Welcome(username, frame)  
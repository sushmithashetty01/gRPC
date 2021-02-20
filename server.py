from concurrent import futures
import grpc
import time
import bidirectional_pb2
import bidirectional_pb2_grpc

class BidirectionalServer(bidirectional_pb2_grpc.BidirectionalServerServicer):  

    def __init__(self): 
        self.chats = []

    def BidirectionalStream(self, request_iterator, context):
        lastindex = 0     
        while True:  
            while len(self.chats) > lastindex:
                n = self.chats[lastindex]
                lastindex += 1
                yield n

if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bidirectional_pb2_grpc.add_BidirectionalServerServicer_to_server(BidirectionalServer(), server)
    print('Starting server...')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    
    
    
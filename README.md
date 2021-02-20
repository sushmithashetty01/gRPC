# gRPC

Prerequisites:
 - Python 3.5 or higher
 - pip version 9.0.1 or higher

Implementation:

1. Create a proto file -

    bidirectional.proto 

2. Install dependencies -

   virtualenv venv
   source venv/Scripts/activate
   pip install grpcio
   pip install grpcio-tools

3. Command to generate the stub -

   python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/bidirectional.proto
   
   file generated
   
       . bidirectional_pb2.py
       . bidirectional_pb2_grpc.py
       
4. Implementing server and client -
  
   Run --> python client.py
   output:
            . enter username: [your name]
            . enter message: [your message]
   
   
   Result will be displayed on terminal
   


   

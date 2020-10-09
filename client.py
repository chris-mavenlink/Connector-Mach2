import grpc

import connector_pb2 as pb2
import connector_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051', options=(('grpc.enable_http_proxy', 0),))
    #channel = grpc.insecure_channel('18.219.167.218:50051', options=(('grpc.enable_http_proxy', 0),))
    stub = connector_pb2_grpc.ConnectorStub(channel)

    print('This is your client calling')
    print(stub.actions(pb2.ActionsRequest(whatever='really, whatever')))
    print(stub.triggers(pb2.TriggersRequest()))
    """
    # say hello
    print('Calling SayHello...')
    print(stub.SayHello(pb2.HelloRequest(hello_from_earth='Hello!')))

    # get a message from Mars
    print('Calling GetMessageFromMars...')
    for msg in stub.GetMessageFromMars(pb2.MessageRequest(request='Requesting Mars message')):
        print(msg)

    # send message from Earth to Mars asynchronously
    print('Calling SendMessageFromEarth...')
    print(stub.SendMessageFromEarth(get_message_iterator()))

    # send and receive messages between Earth and Mars asynchronously
    print('Calling SendAndReceiveMessage...')
    for msg in stub.SendAndReceiveMessage(get_message_iterator()):
        print(msg)
       """

run()
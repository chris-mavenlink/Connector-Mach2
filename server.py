# You define all of the methods in the server.py and leave all of the pb2 stuff alone
import time

import grpc
from concurrent import futures

import connector_pb2 as pb2
import connector_pb2_grpc


class InterstellarServer(connector_pb2_grpc.ConnectorServicer):

    def __init__(self):
        self.earth_message_history = []

    def triggers(self, request, context):

    	return pb2.TriggersResponse()

    def actions(self, request, context):
        #request means the source object
        # create a field object
        # create a Trigger object that contains the field object
        # create a Trigger[triggers=array of Trigger objects]

        """
        Field field1 = new Field()
        field1.display_name=...
        ...
        field1.type="yay this will work"

        Field output = new Field()
        output.display_name="Hello World!""
        ...

        Action action1 = new Action()
        action1.display_name="action1"
        action1.description="some description of the action"
        action1.Inputs.Add(field1)
        action1.Outputs.Add(output)

        ActionResponse response = new ActionResponse()
        response.Actions.Add(action1)
        return response

        """
        field1 = pb2.Field()
        field1.display_name = "Please Work"
        field1.key = "full_name"
        field1.type = "anything"
        field1.description = "This is a test server code"

        output = pb2.Field()
        output.display_name = "This will return a name eventually"
        output.key = "full_name"
        output.type = "anything"
        output.description = "This is the output for the test server code"

        action1 = pb2.Action()
        action1.display_name = "Chris's Action"
        action1.description = "Chris Ackerman's first action"
        #person.id.extend([1, 32, 43432])
        action1.inputs.extend([field1])
        action1.outputs.extend([output])

        response = pb2.ActionsResponse()
        response.actions.extend([action1])

        return response
    


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    connector_pb2_grpc.add_ConnectorServicer_to_server(
        InterstellarServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('server started at port 50051')
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)

serve()
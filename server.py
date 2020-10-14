# You define all of the methods in the server.py and leave all of the pb2 stuff alone
import time

import grpc
from concurrent import futures

import connector_pb2 as pb2
import connector_pb2_grpc


class ConnectorServer(connector_pb2_grpc.ConnectorServicer):

    def triggers(self, request, context):

    	return pb2.TriggersResponse()


    def perform_trigger(self, request, context):
        #do something
        return pb2.TriggerResponse()

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
        #print('New Workspace from Mavenlink: ', request.whatever)
        field1 = pb2.Field()
        field1.display_name = "Input Project CF"
        field1.key = "id"
        field1.type = "text"
        field1.description = "This is the internal ID of the source project"

        output = pb2.Field()
        output.display_name = "New Project ID"
        output.key = "Project ID"
        output.type = "text"
        output.description = "This is the custom field value for Workflow Text 1"

        action1 = pb2.Action()
        action1.display_name = "New Project"
        action1.description = "Chris Ackerman's first action"
        # need to perform an action here, maybe make an API call. Would need the new workspace ID though
        action1.inputs.extend([field1])
        action1.outputs.extend([output])

        response = pb2.ActionsResponse()
        response.actions.extend([action1])

        return response
    
    def perform_action(self, request, context):
        #do something
        return pb2.ActionResponse()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    connector_pb2_grpc.add_ConnectorServicer_to_server(
        ConnectorServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('server started at port 50051')
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)

serve()
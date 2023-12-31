# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import user_service_pb2 as user__service__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/userservice.UserService/CreateUser',
                request_serializer=user__service__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=user__service__pb2.CreateUserResponse.FromString,
                )
        self.AuthenticateUser = channel.unary_unary(
                '/userservice.UserService/AuthenticateUser',
                request_serializer=user__service__pb2.LoginUserRequest.SerializeToString,
                response_deserializer=user__service__pb2.LoginUserResponse.FromString,
                )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AuthenticateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=user__service__pb2.CreateUserRequest.FromString,
                    response_serializer=user__service__pb2.CreateUserResponse.SerializeToString,
            ),
            'AuthenticateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.AuthenticateUser,
                    request_deserializer=user__service__pb2.LoginUserRequest.FromString,
                    response_serializer=user__service__pb2.LoginUserResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'userservice.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userservice.UserService/CreateUser',
            user__service__pb2.CreateUserRequest.SerializeToString,
            user__service__pb2.CreateUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AuthenticateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/userservice.UserService/AuthenticateUser',
            user__service__pb2.LoginUserRequest.SerializeToString,
            user__service__pb2.LoginUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

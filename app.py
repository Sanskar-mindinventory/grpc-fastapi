"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging
import grpc
import user_service_pb2, user_service_pb2_grpc
from src.api.v1.UserAuthentication.services.user_services import UserServices as user_services
from database.database import get_db


db = get_db()

class UserServices(user_service_pb2_grpc.UserServiceServicer):
    def CreateUser(self, request, context):
        user = user_services.register(request=request, db_session=db)
        return user_service_pb2.CreateUserResponse(user_id=str(user.get('data').user_id), username=user.get('data').username, email=user.get('data').email)

    def AuthenticateUser(self, request, context):
        user_token = user_services.login(request=request, db_session=db)
        return user_service_pb2.LoginUserResponse(access_token=user_token.get('access_token'), token_type=user_token.get('token_type'))


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServices(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
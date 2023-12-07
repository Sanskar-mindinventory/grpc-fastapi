from database.database import get_db
from src.api.v1.UserAuthentication.server_files import user_service_pb2, user_service_pb2_grpc
from src.api.v1.UserAuthentication.services.user_services import UserServices as us


db = get_db()

class UserServices(user_service_pb2_grpc.UserServiceServicer):
    def CreateUser(self, request, context):
        user = us.register(request=request, db_session=db)
        return user_service_pb2.CreateUserResponse(user_id=str(user.get('data').user_id), username=user.get('data').username, email=user.get('data').email)

    def AuthenticateUser(self, request, context):
        user_token = us.login(request=request, db_session=db)
        return user_service_pb2.LoginUserResponse(access_token=user_token.get('access_token'), token_type=user_token.get('token_type'))
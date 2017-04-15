from mongoengine import Q
from werkzeug import security

from flaskr.auth.model import User
from utils.services import ModelService


class UserService(ModelService):
    """
    用户的复用服务
    """

    def get_by_username(self, username):
        query = Q(username=username)
        return self.get_one(User.objects, query)

    def get_by_email(self, email):
        query = Q(email=email)
        return self.get_one(User.objects, query)

    def new_user(self, username, password, email, description=''):
        """
        创建用户
        :return: User
        """
        encrypted_password = security.generate_password_hash(password)
        user = User(username=username, password=encrypted_password, email=email, description=description)
        user.save()
        return user

    def authenticate(self, username, password):
        """
        验证用户名密码
        :return: User/None 验证通过的用户, 不通过则为None
        """
        user = self.get_by_username(username)
        if user and security.check_password_hash(user.password, password):
            return user
        else:
            return None


user_service = UserService()

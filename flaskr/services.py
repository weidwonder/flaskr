from flaskr.auth.model import User


class UserService(object):

    def get(self, id):
        return User.objects.filter(id=id).first()

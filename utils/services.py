class ModelService(object):
    """
    model的服务
    """

    def get_one(self, manager, query):
        return manager.filter(query).first()

    def get_multi(self, manager, query):
        return manager.filter(query)

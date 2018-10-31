from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import BaseModel


class DatabaseSession(object):

    engine = create_engine('sqlite:///:memory:', echo=True)

    def __init__(self):
        BaseModel.metadata.create_all(self.engine)
        self.session_maker = sessionmaker(bind=self.engine)
        self.session = self.session_maker()
    
    def add_models_to_db(self, models: list):
        self.session.add_all(models)
        return models
    
    def add_model(self, model):
        self.session.add(model)
        return model
    
    def delete_model(self, model):
        self.session.delete(model)
        return model
    
    def commit_changes(self):
        self.session.commit()

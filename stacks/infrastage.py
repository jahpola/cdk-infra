from aws_cdk import core

from .infra import InfraStack
from .database import DBStack

class InfraStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        #Infra = InfraStack(self, "Infra")
        DB = DBStack(self, "Database")

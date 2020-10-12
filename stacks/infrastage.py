from aws_cdk import core

from infra import InfraStack

class InfraStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        Infra = InfraStack(self, "Infra")

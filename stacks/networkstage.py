from aws_cdk import core

from vpc import VPCStack

class NetworkStage(core.Stage):
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        VPC = VPCStack(self, "VPC")


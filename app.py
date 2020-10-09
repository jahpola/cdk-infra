#!/usr/bin/env python3

from aws_cdk import core
from aws_cdk.core import Tags

#from stacks.infra import InfraStack
#from stacks.vpc import VPCStack
from stacks.pipeline import PipelineStack

app = core.App()

PipelineStack(app, 'PipelineStack')

#VPC = VPCStack(app, "VPC")
#Infra = InfraStack(app, "infra")

#Tags.of(VPC).add("CDK","True")
#Tags.of(Infra).add("CDK","True")

app.synth()

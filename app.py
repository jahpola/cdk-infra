#!/usr/bin/env python3

from aws_cdk import core as cdk

from stacks.pipeline import PipelineStack

env_EU = cdk.Environment(account="257750605947",region="eu-west-1")

app = cdk.App()

PipelineStack(app, 'PipelineStack', env=env_EU)

app.synth()

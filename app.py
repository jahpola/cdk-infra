#!/usr/bin/env python3

from aws_cdk import core

from stacks.pipeline import PipelineStack

env_EU = core.Environment(account="257750605947",region="eu-west-1")

app = core.App()

PipelineStack(app, 'PipelineStack', env=env_EU)

app.synth()

#!/usr/bin/env python3

from aws_cdk import core

from futucloud_jahp.futucloud_jahp_stack import FutucloudJahpStack


app = core.App()
FutucloudJahpStack(app, "futucloud-jahp")

app.synth()

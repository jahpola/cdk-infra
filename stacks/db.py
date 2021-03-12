from aws_cdk import core
from aws_cdk import aws_rds as rds
from aws_cdk import aws_ssm as ssm
from aws_cdk import aws_secretsmanager as secret

class DBStack(core.Stack):
  def __init__(self, scope: core.Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    ssm.StringParameter(self, "DB",
        parameter_name="foo",
        string_value="bar"
    )
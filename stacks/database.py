from aws_cdk import core
import aws_cdk.aws_dynamodb as dynamodb

class DBStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here

        testi = dynamodb.Table(self, "Testi",
            partition_key=Attribute(name="id", type=dynamodb.AttributeType.STRING)
        )
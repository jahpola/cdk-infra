from aws_cdk import core
import aws_cdk.aws_ecr as ecr

class InfraStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        
        repo = ecr.Repository(self, "Test",
            image_scan_on_push=True,
            repository_name="foori"
        )

        repo.add_lifecycle_rule(max_image_age=core.Duration.days(30))
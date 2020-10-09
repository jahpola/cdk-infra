from os import name
from aws_cdk import core
import aws_cdk.aws_ec2 as ec2
from aws_cdk.aws_ec2 import GatewayVpcEndpointOptions


class VPCStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        self.vpc = ec2.Vpc(self, "Playground",
            max_azs=3,
            nat_gateways=1,
            gateway_endpoints={
                "S3": GatewayVpcEndpointOptions(
                    service=ec2.GatewayVpcEndpointAwsService.S3
                ),
                "DynamoDB": GatewayVpcEndpointOptions(
                    service=ec2.GatewayVpcEndpointAwsService.DYNAMODB
                )
            },
            subnet_configuration=[ec2.SubnetConfiguration(
                subnet_type=ec2.SubnetType.PUBLIC,
                name="Public"
            ), ec2.SubnetConfiguration(
                subnet_type=ec2.SubnetType.PRIVATE,
                name="Private"
            ), ec2.SubnetConfiguration(
                subnet_type=ec2.SubnetType.ISOLATED,
                name="DB"
            )
            ]

        )

        core.CfnOutput(self, "Output",
            value=self.vpc.vpc_id
        )

        # core.CfnOutput(self, "private-subnets",
        #     value=self.vpc.private_subnets
        # )

        # core.CfnOutput(self, "public-subnets",
        #     value=self.vpc.public_subnets
        # )
    
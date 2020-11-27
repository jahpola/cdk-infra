from aws_cdk import core

import aws_cdk.aws_ecr as ecr
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_iam as iam
from aws_cdk.aws_ec2 import Subnet
from aws_cdk.aws_iam import ServicePrincipal
from aws_cdk.core import CfnOutput

class InfraStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        
        repo = ecr.Repository(self, "Test",
            image_scan_on_push=True,
            repository_name="multiarm"
        )

        repo.add_lifecycle_rule(max_image_age=core.Duration.days(30))

        vpc = ec2.Vpc.from_lookup(self, "VPC",
            vpc_id="vpc-0359f86f220141a6d" # https://github.com/aws/aws-cdk/issues/10095
        )

        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
            cpu_type=ec2.AmazonLinuxCpuType.ARM_64
        )

        # add role
        role = iam.Role(self, "InstanceSSM",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com")
        )

        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AmazonEC2RoleforSSM"))

        sg = ec2.SecurityGroup(self, "home",
            vpc=vpc,
            security_group_name="jahp-home"
        )

        sg.add_ingress_rule(ec2.Peer.ipv4('91.155.214.175/32'), ec2.Port.tcp(22), 'SSH from any')

        instance = ec2.Instance(self, "Testi1",
            instance_name="Testi",
            instance_type=ec2.InstanceType("t4g.micro"),
            machine_image=amzn_linux,
            vpc=vpc,
            role=role,
            security_group=sg,
            key_name="futucloud-jahp",
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC)
        )

        CfnOutput(self, "IP", value=instance.instance_public_ip)

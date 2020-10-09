from aws_cdk import core
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpactions
from aws_cdk import pipelines

from db import DBStack
from vpc import VPCStack

class PipelineStack(core.Stack):
  def __init__(self, scope: core.Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    source_artifact = codepipeline.Artifact()
    cloud_assembly_artifact = codepipeline.Artifact()

    pipeline = pipelines.CdkPipeline(self, "Pipeline",
        cloud_assembly_artifact=cloud_assembly_artifact,
        pipeline_name="Pipeline",

        source_action=cpactions.GitHubSourceAction(
            action_name="Github",
            output=source_artifact,
            oauth_token=core.SecretValue.secrets_manager('github-token'),
            owner="jahpola",
            repo="cdk-infra",
            trigger=cpactions.GitHubTrigger.WEBHOOK
        ),

        synth_action=pipelines.SimpleSynthAction(
            source_artifact=source_artifact,
            cloud_assembly_artifact=cloud_assembly_artifact,
            install_command='npm install -g aws-cdk && pip install -r requirements.txt',
            build_command='pytest unittests',
            synth_command='cdk synth'
        ))

    vpc_app =  VPCStack(self, "VPC")
    vpc_app_stage = pipeline.add_application_stage(vpc_app)




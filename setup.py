import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk infra",
    version="0.0.1",

    description="CDK infra",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Jyrki Ahpola",

    package_dir={"": "stacks"},
    packages=setuptools.find_packages(where="stacks"),

    install_requires=[
        "aws-cdk.core==1.93.0",
        "aws-cdk.aws-ec2==1.93.0",
        "aws-cdk.aws-rds==1.93.0",
        "aws-cdk.aws-ssm==1.93.0",
        "aws-cdk.aws_codepipeline==1.93.0",
        "aws-cdk.aws-codepipeline-actions==1.93.0",
        "aws-cdk.pipelines==1.93.0",
        "aws-cdk.aws-secretsmanager==1.93.0",
        "aws-cdk.aws-dynamodb==1.93.0",
        "aws-cdk.aws-route53==1.93.0"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)

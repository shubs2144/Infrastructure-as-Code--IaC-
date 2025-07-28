"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

ami = aws.ec2.get_ami(
    most_recent=True,
    owners=["amazon"],
    filters=[
        {
            "name": "name",
            "values": ["amzn2-ami-hvm-*-x86_64-gp2"]
        }
    ]
)

vpc = aws.ec2.get_vpc(
    default=True)

group = aws.ec2.SecurityGroup("web-secgrp",
    description="Enable HTTP access",
    vpc_id=vpc.id,
    ingress=[
        {
            "protopcol": "icmp",
            "from_port": -8,
            "to_port": 0,
            "cidr_blocks": ["0.0.0.0/0"]
        },
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"]
        }
    ],
)


serve = aws.ec2.Instance("web-server",
    ami=ami.id,
    instance_type="t2.micro",
    vpc_security_group_ids=[group.id],
    tags={
        "Name": "web-server"
    }
)

pulumi.export("instance_id", serve.id)
pulumi.export("instance_public_ip", serve.public_ip)
pulumi.export("hostname", serve.public_dns)
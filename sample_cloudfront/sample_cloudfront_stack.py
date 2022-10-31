from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_cloudfront as cf,
)


class SampleCloudfrontStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # my_distribution = cf.Distribution(self, "MyCfWebDistribution",
        #     default_behavior=cf.BehaviorOptions(
        #         ##origin=cf.IOrigin(origin_id="arn:aws:s3:::cloudfronttest-sample-bucket")
        #     )
        # )
        
        origin_property = cf.CfnDistribution.OriginProperty(
            domain_name=f"cloudfronttest-sample-bucket.s3.ap-northeast-1.amazonaws.com",
            id="myorigin1",
            # s3_origin_config=cf.CfnDistribution.S3OriginConfigProperty(
            #     origin_access_identity="originAccessIdentity"
            # ),
            custom_origin_config=cf.CfnDistribution.CustomOriginConfigProperty(
                origin_protocol_policy="https-only",
            ),
        )
        
        cfn_distribution = cf.CfnDistribution(self, "HogeDistribution",
            distribution_config=cf.CfnDistribution.DistributionConfigProperty(
                comment="this is hoge",
                enabled=True,
                default_cache_behavior=cf.CfnDistribution.DefaultCacheBehaviorProperty(
                    target_origin_id="myorigin1",
                    viewer_protocol_policy="https-only",
                    forwarded_values=cf.CfnDistribution.ForwardedValuesProperty(
                        query_string=False,
                    ),
                ),
                origins=[
                    origin_property
                ],
            )
        )

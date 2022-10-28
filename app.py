#!/usr/bin/env python3

import aws_cdk as cdk

from sample_cloudfront.sample_cloudfront_stack import SampleCloudfrontStack


app = cdk.App()
SampleCloudfrontStack(app, "sample-cloudfront")

app.synth()

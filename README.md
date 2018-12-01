# spare_the_air

Spare the Air is an Alexa Skill for querying the current wood burning status from www.sparetheair.org (applicable to SF Bay Area).

## Installation

Spare the Air is an AWS Lambda function. To install the Alexa Skill, follow [Amazon's instructions for hosting a custom skill as a lambda function](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html) and [install the AWS CLI tool](https://aws.amazon.com/cli/)

After your Alexa Skill configuration and AWS Lambda function is ready, run:

    $ make deploy

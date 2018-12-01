from spare_the_air import alexa


def lambda_handler(event, context):
    return alexa.respond(event)

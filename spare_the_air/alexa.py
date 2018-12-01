from spare_the_air.location import sf


def respond(event):
    request_type = event['request']['type']

    if request_type == 'CanFulfillIntentRequest':
        return CanFulfillIntentRequest(event)
    elif request_type == 'LaunchRequest':
        return respond_with_speech('Welcome to Spare the Air! ' + sf.get_burn_status())
    elif request_type == 'SessionEndedRequest':
        return respond_with_speech('Goodbye.')
    elif request_type == 'IntentRequest':
        intent = event['request']['intent']['name']

        if intent == 'GetBurnStatus':
            return respond_with_speech(sf.get_burn_status())
        elif intent == 'StopIntent':
            return respond_with_speech('Goodbye.')
        elif intent == 'CancelIntent':
            return respond_with_speech('Goodbye.')
        elif intent == 'HelpIntent':
            return respond_with_speech('I can tell you whether it\'s safe to burn wood today. Just ask!')
        else:
            return respond_with_speech(sf.get_burn_status())


def GetBurnStatus():
    return {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': sf.get_burn_status(),
            },
            'shouldEndSession': True,
        }
    }


def CanFulfillIntentRequest(event):
    intent_name = event['request']['intent']['name']

    if intent_name == 'GetBurnStatus':
        return respond_with_can_fulfill_intent({'canFulfill': 'YES'})
    else:
        return respond_with_can_fulfill_intent({'canFulfill': 'NO'})


def respond_with_speech(text):
    return {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': text,
            },
            'shouldEndSession': True,
        }
    }


def respond_with_can_fulfill_intent(can_fulfill_intent):
    return {
        'version': '1.0',
        'response': {
            'canFulfillIntent': can_fulfill_intent,
        },
    }

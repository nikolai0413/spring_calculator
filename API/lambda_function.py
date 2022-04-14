import json
import calculations as calc


class BadRequestError(Exception):
    """Cannot handle request"""
    pass


def lambda_handler(event, context=None):
    """AWS Lambda implemented function"""

    try:
        (httpReqType, calcFunction, body) = extractEventInfo(event)

        if httpReqType == "OPTIONS":
            return {"statusCode": 200}

        elif httpReqType == "POST":
            responseData = performCalculation(calcFunction, body)

            return {
                "statusCode": 200,
                "body": json.dumps(responseData),
            }

    except BadRequestError as err:
        return {"statusCode": 400, "ErrorMessage": repr(err)}

    except TypeError as err:
        return {"statusCode": 400, "ErrorMessage": repr(err)}


def extractEventInfo(event):
    """Exracts info needed for logic and to perform calculations"""
    httpReqContext = None
    calcFunction = None
    bodyJson = None
    body = None

    # Get HTTP method and calculation selection
    try:
        httpReqContext = event["requestContext"]["http"]["method"]
        calcFunction = event["queryStringParameters"]["CALCULATION"]
    except KeyError:
        raise BadRequestError("Event object missing fields")

    # Get body / payload
    try:
        bodyJson = event["body"]
    except KeyError:
        if httpReqContext == "POST":
            raise BadRequestError("POST must include body content")
        else:
            pass

    if httpReqContext == "POST":
        # encode json
        return (httpReqContext, calcFunction, json.loads(bodyJson))

    elif httpReqContext == "OPTIONS":
        # return empty body
        return (httpReqContext, calcFunction, body)

    else:
        raise BadRequestError("Unexpected HTTP Method: " + httpReqContext)


def performCalculation(calcFunction, bodyData):
    """Switch on calcFunction and call appropriate claculation, passing on data"""
    if calcFunction == "MAIN":
        return calc.main(**bodyData)
    elif calcFunction == "STATIC":
        return calc.static(**bodyData)
    elif calcFunction == "FATIGUE":
        return calc.fatigue(**bodyData)
    else:
        raise BadRequestError("Wrong calculation function specified")

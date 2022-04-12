import json

def lambda_handler(event, context):

    reqContext = event["requestContext"]["http"]["method"]

    if reqContext == "POST":
        calcSelection = event["queryStringParameters"]["CALCULATION"]
        print("calcSelection: " + calcSelection)

        calcData = json.loads(event["body"])
        print(calcData)

        responseData = {
            "p": 13,
            "nt": 25,
            "na": 1132,
            "k": 321,
            "F_ls": 3132,
            "n_ls": 123,
        }
        return {
            "statusCode": 200,
            "body": responseData
        }

    else:
        return {
            "statusCode": 200,
            "body": "Responding to HTTP " + reqContext,
        }

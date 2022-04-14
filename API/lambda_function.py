import json
from calculations import *

def lambda_handler(event, context):
    print("Full event JSON:")
    print(json.dumps(event))
    
    reqContext = event["requestContext"]["http"]["method"]
    print("ReqContext: " + reqContext)
    
    if reqContext == "POST":
        calcSelection = event["queryStringParameters"]["CALCULATION"]
        print("calcSelection: " + calcSelection)
        calcData = json.loads(event["body"])
        print(calcData)
        
        responseData = None
        
        if calcSelection == "MAIN":
            responseData = calculateMain(calcData)
        elif calcSelection == "STATIC":
            responseData = calculateStatic(calcData)
        elif calcSelection == "FATIGUE":
            responseData = calculateFatigue(calcData)
        else: 
            return {
                "statusCode": 400
            }
        
        return {
            "statusCode": 200,
            "body": json.dumps(responseData)
        }

    else:
        return {
            "statusCode": 200
        }

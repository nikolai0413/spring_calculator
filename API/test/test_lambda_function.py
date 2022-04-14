import json
import pytest
import sampleData
from lambda_function import extractEventInfo, BadRequestError, lambda_handler

def test_extractEventInfo():
	assert extractEventInfo(sampleData.main.options) == ("OPTIONS", "MAIN", None)
	assert extractEventInfo(sampleData.main.post) == ("POST", "MAIN", json.loads(sampleData.main.post["body"]))

	assert extractEventInfo(sampleData.static.options) == ("OPTIONS", "STATIC", None)
	assert extractEventInfo(sampleData.static.post) == ("POST", "STATIC", json.loads(sampleData.static.post["body"]))

	assert extractEventInfo(sampleData.fatigue.options) == ("OPTIONS", "FATIGUE", None)
	assert extractEventInfo(sampleData.fatigue.post) == ("POST", "FATIGUE", json.loads(sampleData.fatigue.post["body"]))

	with pytest.raises(BadRequestError):
		extractEventInfo({ 'hi': 'what up'})

	with pytest.raises(BadRequestError):
		extractEventInfo(sampleData.badReqs.badType);
	
	with pytest.raises(BadRequestError):
		extractEventInfo(sampleData.badReqs.postNoBody)

def test_lambda_handler():
	assert lambda_handler(sampleData.main.options) == { "statusCode": 200 }
	assert lambda_handler(sampleData.static.options) == { "statusCode": 200 }
	assert lambda_handler(sampleData.fatigue.options) == { "statusCode": 200 }

	testResponse = lambda_handler(sampleData.badReqs.badType)
	assert testResponse["statusCode"] == 400
	assert "ErrorMessage" in testResponse

	testResponse = lambda_handler(sampleData.badReqs.postNoBody)
	assert testResponse["statusCode"] == 400
	assert "ErrorMessage" in testResponse

	testResponse = lambda_handler(sampleData.main.post)
	assert testResponse["statusCode"] == 200
	assert "body" in testResponse

	testResponse = lambda_handler(sampleData.static.post)
	assert testResponse["statusCode"] == 200
	assert "body" in testResponse

	testResponse = lambda_handler(sampleData.fatigue.post)
	assert testResponse["statusCode"] == 200
	assert "body" in testResponse


	
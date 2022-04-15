rm ./API.zip
find . | grep -E "(__pycache__|\.pytest_cache|\.pyc|\.pyo$)" | xargs rm -rf
cd API
zip -r ../API.zip ./*
cd ..
aws lambda update-function-code --function-name springs_backend --zip-file fileb://./API.zip
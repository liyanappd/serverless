import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')


    aws lambda create-function --function-name student1014-lab2 --zip-file fileb://function.zip --handler main.lambda_handler --runtime python3.7 --role 


    :role/student1014


    aws lambda invoke --function-name student1014-lab2-1 --log-type Tail --cli-binary-format raw-in-base64-out --payload '{"key1":"value1", "key2":"value2", "key3":"value3"}' outputfile.txt

    echo U1RBUlQgUmVxdWVzdElkOiA0ZTUzNWFjNi0xZmI0LTRhODYtYTdjZC0wYTI3YzA5ZjliZjQgVmVyc2lvbjogJExBVEVTVAp2YWx1ZTEgPSB2YWx1ZTEKdmFsdWUyID0gdmFsdWUyCnZhbHVlMyA9IHZhbHVlMwpFTkQgUmVxdWVzdElkOiA0ZTUzNWFjNi0xZmI0LTRhODYtYTdjZC0wYTI3YzA5ZjliZjQKUkVQT1JUIFJlcXVlc3RJZDogNGU1MzVhYzYtMWZiNC00YTg2LWE3Y2QtMGEyN2MwOWY5YmY0CUR1cmF0aW9uOiAxLjUyIG1zCUJpbGxlZCBEdXJhdGlvbjogMiBtcwlNZW1vcnkgU2l6ZTogMTI4IE1CCU1heCBNZW1vcnkgVXNlZDogNDggTUIJSW5pdCBEdXJhdGlvbjogMTIxLjgzIG1zCQo= | base64 --decode


serverlesstraining
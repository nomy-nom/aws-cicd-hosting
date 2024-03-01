import os
import json
import http.client
import base64

def lambda_handler(event, context):
    http_method = event.get('httpMethod')
    if http_method and http_method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',  
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET,OPTIONS',
                'Content-Type': 'application/json'
            },
            'body': ''
        }

    username = "nomy-nom"
    repository = "aws-cicd-hosting"

    readme_url = f"/repos/{username}/{repository}/readme"

    github_token = os.environ.get('GITHUB_TOKEN')

    headers = {
        "Authorization": f"token {github_token}",
        "User-Agent": "Python"
    }

    try:
        connection = http.client.HTTPSConnection("api.github.com")

        connection.request("GET", readme_url, headers=headers)

        response = connection.getresponse()
        data = response.read().decode("utf-8")

      
        if response.status == 200:
            readme_content_encoded = json.loads(data).get("content", "")
            readme_content_decoded = base64.b64decode(readme_content_encoded).decode("utf-8")
        else:
            raise Exception(f"Failed to fetch README: {data}")

        connection.close()

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*' 
            },
            'body': json.dumps({
                'readme_content': readme_content_decoded
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*'  
            },
            'body': json.dumps({
                'error': str(e)
            })
        }

class claude():
    def submitMessage(self, message):
        bedrock = boto3.client(
            service_name="bedrock-runtime", region_name='us-east-1')

        body = json.dumps({
            "max_tokens": 256,
            "messages": [{"role": "user", "content": message}],
            "anthropic_version": "bedrock-2023-05-31"
        })

        response = bedrock.invoke_model(
            body=body, modelId="anthropic.claude-3-5-sonnet-20240620-v1:0")

        response_body = json.loads(response.get("body").read())
        return response_body.get("content")[0]["text"]

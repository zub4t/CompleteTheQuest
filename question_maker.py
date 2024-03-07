from flask import Flask, request, jsonify
from openai import OpenAI
import json
import random

import requests
app = Flask(__name__)
url = 'http://127.0.0.1:8083/make/answer'

@app.route('/make/question', methods=['POST'])
def make_question():
    data = request.get_json()
    prompt = data.get('prompt')
    random_number = random.randint(1, 99999)

    client = OpenAI(
        api_key='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'
    )
    model = "gpt-3.5-turbo"
    temperature = 0.3
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": f'{random_number} {prompt}'},
        ],
        temperature=temperature,
    )

    openai_response = response.choices[0].message.content
    print(openai_response)
    result_dict = {"question": openai_response}
    json_data = json.dumps(result_dict, ensure_ascii=False)
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json_data, headers=headers)
    return 'OK'



if __name__ == '__main__':
    app.run(port=8082)

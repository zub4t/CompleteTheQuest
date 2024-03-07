from flask import Flask, request, jsonify
from openai import OpenAI
import json

import requests
app = Flask(__name__)
url = 'http://127.0.0.1:8083/make/answer'

@app.route('/make/question', methods=['POST'])
def make_question():
    data = request.get_json()
    prompt = data.get('prompt')
    
    client = OpenAI(
        api_key='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'
    )
    model = "gpt-3.5-turbo"
    temperature = 0.3
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You're the best teacher in the world"},
            {"role": "user", "content": prompt},
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








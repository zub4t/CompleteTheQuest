from flask import Flask, request, jsonify
from openai import OpenAI
app = Flask(__name__)

@app.route('/make/answer', methods=['POST'])
def make_question():
    data = request.get_json()
    question = data.get('question')
    prompt = f'Answer the following question without adding anything else, just the strict answer: {question}'
    client = OpenAI(
        api_key='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'
    )
    model = "gpt-3.5-turbo"
    temperature = 0.3
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are the best students ever"},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
    )

    openai_response = response.choices[0].message.content
    print(openai_response)
    # Write the JSON string to a file
    string_to_save = f'''
    {{
        "question": "{question}",
        "answer": "{openai_response}"
    }}
    '''
    with open("daily_quest.json", "w") as file:
        file.write(string_to_save)
    return 'OK'



if __name__ == '__main__':
    app.run(port=8083)


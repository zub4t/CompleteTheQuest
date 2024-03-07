from flask import Flask
from openai import OpenAI
import json
import requests
import random

json_data = '''
{
    "topics": [
        "The Renaissance",
        "The Age of Exploration",
        "The French Revolution",
        "The Industrial Revolution in Europe",
        "World War I",
        "World War II",
        "The Cold War and its impact on Europe",
        "The formation and expansion of the European Union",
        "The fall of the Berlin Wall and the reunification of Germany",
        "The rise and fall of the Roman Empire",
        "The Byzantine Empire and its influence on Europe",
        "The Protestant Reformation",
        "The Spanish Inquisition",
        "The Hundred Years' War",
        "The Black Death and its impact on Europe",
        "The Age of Absolutism",
        "The Enlightenment",
        "The Napoleonic Wars",
        "The Balkan Wars",
        "The Irish Potato Famine"
    ]
}

'''

data = json.loads(json_data)

# Randomly choose a topic

app = Flask(__name__)
url = 'http://127.0.0.1:8082/make/question'

@app.route('/start/question/')
def question_topic():
    random_number = random.randint(1, 99999)
    random_topic = random.choice(data["topics"])

    client = OpenAI(
        api_key='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'
    )
    model = "gpt-3.5-turbo"
    temperature = 0.3

    prompt = f"I want you to replace the 'add here' part with the topic {random_topic} in the provided prompt, this subject will vary each time and you can not repeat, and then return the same prompt with this information added without any additional inserted text. Prompt: Imagine that you are an expert in 'add here', endowed with the highest technical and professional skills. One of your characteristics is that you love challenging people to guess a topic within your chosen school subject. The challenge format is more oriented towards the 'Guess What' game. Your response should focus only on posing the question, without introductory texts or anything similar."
    print(prompt)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
    )

    openai_response = response.choices[0].message.content
    print(openai_response)
    result_dict = {"prompt": openai_response}
    json_data = json.dumps(result_dict, ensure_ascii=False)
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json_data, headers=headers)
    return f'OK'

if __name__ == '__main__':
    app.run(port=8081)
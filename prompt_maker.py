from flask import Flask
from openai import OpenAI
import json
import requests
import random

json_data = '''
{
    "topics": [
        "Array",
        "String",
        "Hash Table",
        "Dynamic Programming",
        "Math",
        "Sorting",
        "Greedy",
        "Depth-First Search",
        "Database",
        "Binary Search",
        "Tree",
        "Breadth-First Search",
        "Matrix",
        "Bit Manipulation",
        "Two Pointers",
        "Binary Tree",
        "Heap (Priority Queue)",
        "Prefix Sum",
        "Stack",
        "Simulation",
        "Graph",
        "Design",
        "Counting",
        "Sliding Window",
        "Backtracking",
        "Union Find",
        "Linked List",
        "Enumeration",
        "Ordered Set",
        "Monotonic Stack",
        "Trie",
        "Number Theory",
        "Divide and Conquer",
        "Recursion",
        "Bitmask",
        "Queue",
        "Segment Tree",
        "Binary Search Tree",
        "Memoization",
        "Geometry",
        "Binary Indexed Tree",
        "Hash Function",
        "Topological Sort",
        "String Matching",
        "Combinatorics",
        "Rolling Hash",
        "Shortest Path",
        "Game Theory",
        "Interactive",
        "Data Stream",
        "Brainteaser",
        "Monotonic Queue",
        "Randomized",
        "Merge Sort",
        "Iterator",
        "Concurrency",
        "Doubly-Linked List",
        "Probability and Statistics",
        "Quickselect",
        "Bucket Sort",
        "Suffix Array",
        "Minimum Spanning Tree",
        "Counting Sort",
        "Shell",
        "Line Sweep",
        "Reservoir Sampling",
        "Strongly Connected Component",
        "Eulerian Circuit",
        "Radix Sort",
        "Rejection Sampling",
        "Biconnected Component"
    ]
}
'''

data = json.loads(json_data)

# Randomly choose a topic
random_topic = random.choice(data["topics"])

app = Flask(__name__)
url = 'http://127.0.0.1:8082/make/question'

@app.route('/start/question/')
def question_topic():
    client = OpenAI(
        api_key='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'
    )
    model = "gpt-3.5-turbo"
    temperature = 0.3

    prompt = f"I want you to replace the 'add here' part with {random_topic} in the provided prompt with a random school subject, this subject will vary each time and you can not repeat, and then return the same prompt with this information added without any additional inserted text. Prompt: Imagine that you are an expert in 'add here', endowed with the highest technical and professional skills. One of your characteristics is that you love challenging people to guess a topic within your chosen school subject. The challenge format is more oriented towards the 'Guess What' game. Your response should focus only on posing the question, without introductory texts or anything similar."
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

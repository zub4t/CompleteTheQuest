from flask import Flask, request, jsonify
from openai import OpenAI
import json
import ast

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


app = Flask(__name__)
url = 'http://127.0.0.1:8083/make/answer'

@app.route('/make/question', methods=['GET'])
def make_question():
    random_topic = random.choice(data["topics"])
    random_integer = random.randint(1, 1000)
    prompt = f'I {random_integer} want you to imagine that you are an expert in Computer Science, endowed with the highest technical and professional skills. One of your characteristics is that you love challenging people to guess a topic within your chosen subject, that is: {random_topic}. The challenge format is more oriented towards the "Guess What" game. Your response should focus only on providing a JSON with the question and the answer, without introductory texts or anything similar.'
    print(prompt)
    # Your API key and client configuration
    client = OpenAI(
        api_key='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'
    )
    model = "gpt-3.5-turbo"
    temperature = 0.5

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
    )

    # Get the response from OpenAI API
    openai_response = response.choices[0].message.content

    try:
        # Try to parse the response as JSON
        response_json = json.loads(openai_response)
        final_answer = response_json.get("answer", openai_response)
        question = response_json.get("question", "")
    except json.JSONDecodeError:
        # If parsing fails, assume the entire content is the answer

        # Check if the answer contains a formatted JSON string
        if "```json" in openai_response and "```" in openai_response:
            # Extract the JSON content from the formatted string
            formatted_json_str = openai_response.split("```json")[1].split("```")[0].strip()
            formatted_json = ast.literal_eval(formatted_json_str)
            final_answer = formatted_json.get("answer", formatted_json_str)
            question = formatted_json.get("question", "")
        else:
            final_answer = openai_response
            question = ""

    # Create a dictionary with the question and the answer
    result_dict = {
        "question": question,
        "answer": final_answer
    }

    # Print the formatted JSON
    formatted_json = json.dumps(result_dict, ensure_ascii=False, indent=2)
    print(formatted_json)

    # Write the JSON string to a file
    with open('daily_question.json', 'w', encoding='utf-8') as json_file:
        json_file.write(formatted_json)

    print(f'Successfully created JSON file: output.json')
    return 'OK'



if __name__ == '__main__':
    app.run(port=8082)








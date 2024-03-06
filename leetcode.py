import openai
import json
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




# Replace 'your_api_key_here' with your actual OpenAI API key
openai.api_key = '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'

import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=openai.api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Create a Guess what  question about {random_topic}. Limit it to 1 paragraphs. Write without any hint",
        }
    ],
    model="gpt-3.5-turbo",
)
question = chat_completion.choices[0].message.content
print(question)
string_to_save = f'''
{{
    "question": "{question}",
    "answer": "{random_topic}"
}}
'''
with open("daily_quest.json", "w") as file:
    file.write(string_to_save)
print("String saved to file.")


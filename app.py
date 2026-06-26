from ollama import chat
from time import perf_counter

question = input("Ask something: ")

start = perf_counter()

response = chat(
    model='qwen3:4b',
    messages=[
        {
            'role': 'user',
            'content': question
        }
    ]
)

end = perf_counter()

answer = response['message']['content']

print("\nResponse:\n")
print(answer)

print(f"\nTime taken: {end-start:.2f} seconds")
print(f"Words generated: {len(answer.split())}")
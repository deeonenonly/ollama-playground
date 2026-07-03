from ollama import chat
from time import perf_counter

MODEL="qwen3:4b"
LINE = "=" * 42
SEPARATOR = "-" * 42

def print_banner():
    print(LINE)
    print("      Local LLM Playground v1.2")
    print(LINE)
    print(f"Model  : {MODEL}")
    print("Status : Ready")
    print("Type 'exit' to quit.")
    print(LINE)
    print()

def main():
    print_banner()
    question = input("User: ") #get user input
    if question.lower() == "exit":
        print("\nGoodbye!\n")
        return
    start = perf_counter()

    response = chat(
        model=MODEL,
        messages=[
            {
                'role': 'user',
                'content': question
            }
        ]
    )

    end = perf_counter()

    answer = response["message"]["content"]

    print("\nAI:")  
    print(answer) #display model response

    print(SEPARATOR)
    print()

    print(f"\nTime taken    : {end-start:.2f} seconds")
    print(f"Words generated : {len(answer.split())}")
    print(f"Characters      : {len(answer)}")

    print()
    print(LINE)

if __name__ == "__main__":
    main()
    
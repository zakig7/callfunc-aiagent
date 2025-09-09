import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions, call_function
from config import MAX_ITERS


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    # Pass the api key locally in an .env file, and add .env to your .gitignore.
    # Do not commit the key, or any secrets 
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(arg)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    # Limit the loop to 20 iterations,
    # and stop at final text with no func calls
    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")


def parse_args(args):
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("prompt", nargs="+", help="Prompt the AI assistant")
    parser.add_argument("--verbose", action="store_true", help="Show API token usage details")
    parser.add_argument("--model", type=str, default="gemini-2.0-flash-001", help="Model version to use")
    args = parser.parse_args()
    return " ".join(args.prompt), args.verbose, args.model


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    # Add model replies to conversation
    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)

    # handle tool calls
    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("Empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("No function responses generated, exiting.")

    messages.append(types.Content(role="user", parts=function_responses))


if __name__ == "__main__":
    main()

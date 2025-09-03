import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions, call_function


def main():
    """CLI conversational Gemini tool with a few arguments"""
    load_dotenv()
    user_prompt, verbose, model = parse_args(sys.argv[1:])
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = fetch_api_response(client, messages, model)
    output_result(user_prompt, response, verbose, model)


def parse_args(args):
    """Add a few arguments"""
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    # Store Conversational value for context continuity 
    parser.add_argument("prompt", nargs="+", help="Prompt the AI assistant")
    parser.add_argument("--verbose", action="store_true", help="Show API token usage details")
    parser.add_argument("--model", type=str, default="gemini-2.0-flash-001", help="Model version to use")

    args = parser.parse_args()
    user_prompt = " ".join(args.prompt)

    return user_prompt, args.verbose, args.model



def fetch_api_response(client, messages, model):
    return client.models.generate_content(
        model=model,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )


def output_result(user_prompt, response, verbose, model):
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Model: {model}")

    if not response.function_calls:
        print("Response:")
        print(response.text)
        return
    
    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            # function_call_result is a types.Content. `parts` is its list of Parts
            # `parts[0]` is the Part containing the function_response
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("Empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])
    if not function_responses:
            raise RuntimeError("Missing tool's function call response")


if __name__ == "__main__":
    main()

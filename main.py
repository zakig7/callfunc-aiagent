import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    """CLI conversational Gemeni tool with a few arguments"""
    load_dotenv()
    user_prompt, verbose, model = parse_args(sys.argv[1:])

    api_key = os.environ.get("GEMINI_API_KEY")
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
    )


def output_result(user_prompt, response, verbose, model):
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Model: {model}")
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()

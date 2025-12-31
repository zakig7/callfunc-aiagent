# AI Coding Assistant

This project is a simplified version of AI-powered coding assistants like Cursor/Zed's Agentic Mode or Claude Code. It allows you to interact with an AI agent that can read, write, and execute code within a sandboxed environment.

**Warning:** This is a toy project and is not intended for production use. Even commercial AI coding assistants have security vulnerabilities, so exercise extreme caution when granting the agent access to your files and system.

## Features

![demo](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2g2dWk5NjYzMW5xdG9zY3h4NnprYnp4NXphdHp0YmdyenJxNGlmeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xE6o9wiKBonMHqq1Le/giphy.gif)

* **File System Access:** The AI agent can list files and directories within the project's working directory.
* **File Content Retrieval:** The agent can read the contents of text files.
* **Code Execution:** The agent can execute Python files and receive the output.
* **File Modification:** The agent can create and modify files.

## Security Considerations

This project is for educational and experimental purposes only. It is crucial to understand the security risks associated with AI agents that have access to your file system and code execution capabilities.

* **Sandboxing:** The agent operates within a sandboxed environment to limit its access to the broader system. However, sandboxes are not impenetrable.
* **Limited Scope:** The agent's capabilities are intentionally limited to prevent unintended consequences.
* **No Guarantees:** There are no guarantees of security or stability. Use at your own risk.

## Getting Started

1. Clone this repository.
2. Set up a virtual environment using `uv`.
3. Install the dependencies.
4. Run the `main.py` file to start chatting away, or modify `config.py` to point the agent to another repo or working directory.
It will answer the sme way Gemeni, Claude, or ChatGPT would. There's a demo app in the `calculator` directory to showcase the coding assistant functions.

### Usage

To run the `main.py` script, you need to set the `GEMINI_API_KEY` and `GEMINI_MODEL` environment variables. You can do this by creating a `.env` file in the project root directory with the following content:

```shell
GEMINI_API_KEY=<YOUR_API_KEY>
GEMINI_MODEL="gemini-2.5-flash"
```

Replace `YOUR_API_KEY` with your actual Gemini API key, and choose whatever model you wish. Make sure to add `.env` in your `.gitignore`

Then, you can run the script from the command line:

```shell
python main.py "your prompt here"
```

You can also use the following optional arguments:

* `--verbose`:  Show API token usage details.
* `--model`: Specify the model version to use (default: `gemini-2.0-flash-001`).

Examples:

```shell
python main.py "fix the bug in the calculator" --verbose --model gemini-2.0-pro-005
```

### Typical flow

* User: "Please fix the bug in the calculator"
* Model: "I want to call get_files_info..."
* Tool: "Here's the result of get_files_info..."
* Model: "I want to call get_file_content..."
* Tool: "Here's the result of get_file_content..."
* Model: "I want to call run_python_file..."
* Tool: "Here's the result of run_python_file..."
* Model: "I want to call write_file..."
* Tool: "Here's the result of write_file..."
* Model: "I want to call run_python_file..."
* Tool: "Here's the result of run_python_file..."
* Model: "I fixed the bug and then ran the calculator to ensure it's working."

## Disclaimer

The author of this project is not responsible for any damages or losses resulting from the use of this software. By using this project, you acknowledge and agree to these terms.
